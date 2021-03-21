# -*- coding: utf-8 -*-
#
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2020-03-09

import requests
import json
import argparse
import re
from functools import cmp_to_key
import os.path
import webbrowser
import subprocess
import random

base_path = "./leco-source/"


def copy2clip(txt):
    cmd = "echo " + txt.strip() + "|  tr -d '\n' | pbcopy"
    return subprocess.check_call(cmd, shell=True)


def create_file_name(quest):
    return ".".join(
        [
            str(quest["frontend_question_id"]),
            quest["question__title_slug"],
            "py",
        ]
    )


def get_all_question():
    request = requests.get("https://leetcode.com/api/problems/all/")
    if request.status_code == 200:

        def fmt(item):
            return {
                "question_id": item["stat"]["question_id"],
                "frontend_question_id": item["stat"]["frontend_question_id"],
                "question__title": item["stat"]["question__title"],
                "question__title_slug": item["stat"]["question__title_slug"],
            }

        def cmp(x, y):
            return (
                0
                if x["frontend_question_id"] > y["frontend_question_id"]
                else -1
            )

        res = [fmt(i) for i in request.json()["stat_status_pairs"]]
        res.sort(key=cmp_to_key(cmp))
        res_str = json.dumps(
            res, sort_keys=True, indent=4, separators=(",", ":")
        )
        with open("./leco_db.json", "wt") as f:
            f.write(res_str)
            print("🎉 Update all leetcode~")
        return res
    else:
        raise Exception("🙈 Can not fetch latest leecode data")


def get_short_name(frontend_question_id):
    if not frontend_question_id:
        return
    data = []
    if not os.path.isfile("./leco_db.json"):
        data = get_all_question()
    else:
        with open("./leco_db.json", "rt") as f:
            data = json.loads(f.read())
            if not data:
                data = get_all_question()
    if data:
        quest = data[frontend_question_id - 1]
        if quest["frontend_question_id"] == frontend_question_id:
            file_name = create_file_name(quest)
            return quest["question__title_slug"], file_name
    raise Exception("🙈 No data found")


def get_quest_data(question__title_slug):
    query = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    content
    difficulty
    codeSnippets {
      lang
      langSlug
      code
      __typename
    }
  }
}
    """
    request = requests.post(
        "https://leetcode.com/graphql",
        json={
            "query": query,
            "variables": {"titleSlug": question__title_slug},
        },
    )
    if request.status_code == 200:
        return request.json()["data"]["question"]
    raise Exception("🙈 Net broken~")


def fmt(quest, file_name):
    title = ".".join([quest["questionFrontendId"], quest["title"]])
    res = '"""\n' + title + "\n\n"
    res += "Difficulty: " + quest["difficulty"] + "\n"
    content = re.sub(r"(<.+?>|\r)", "", quest["content"])
    content = re.sub(r"(\-\&gt\;|\&rarr\;)", "→", content).replace(
        "&hellip;", "…"
    )
    link = "https://leetcode.com/problems/" + quest["titleSlug"] + "/"
    res += content + "\n\nLink: " + link + '\n"""'
    solution_name = "solution"
    solution_name_slug = "solution"
    for code in quest["codeSnippets"]:
        if code["langSlug"] == "python3":
            # re def reorderList(
            solution_name = re.findall("def\\s+(.+)\\(", code["code"])[-1]
            solution_name_slug = re.sub(
                r"(?<!^)(?=[A-Z])", "_", solution_name
            ).lower()
            res += (
                "\n\nfrom typing import List\nimport unittest\n\n"
                + code["code"]
                + "\n\n"
            )
            break

    test = """
class SolutionCase(unittest.TestCase):
    def test_%s(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.%s(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    """ % (
        solution_name_slug,
        solution_name,
    )

    res += test
    with open(file_name, "x") as f:
        f.write(res)
    return file_name


class Commander:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Let's go leetcoding~ "
        )
        self.parser.add_argument(
            "random", nargs="?", help="Random quest."
        )
        self.parser.add_argument(
            "update", nargs="?", help="Update local leedcode data."
        )
        self.parser.add_argument(
            "-o",
            "--open",
            dest="oid",
            type=int,
            help="Location quest website by ID.",
        )
        self.parser.add_argument(
            "-s",
            "--solution",
            dest="sid",
            type=int,
            help="Location quest solution website by ID.",
        )
        self.parser.add_argument(
            "-q",
            "--quest",
            dest="qid",
            type=int,
            help="Get leetcode by problem ID.",
        )

    def get_quest(self, qid):
        print("⚓️ Start fetching~")
        name, file_name = get_short_name(qid)
        output_source = base_path + file_name
        if os.path.isfile(output_source):
            raise Exception("🙊 File existed!")
        fmt(get_quest_data(name), output_source)
        # copy2clip(output_source)
        print(
            "🎉 Download %s successed and file name in clipboard, \
            go leetcoding~"
            % (file_name)
        )

    def open_link(self, oid):
        name, _ = get_short_name(oid)
        webbrowser.open("https://leetcode.com/problems/%s/" % (name))
        print("💫️ Quest positioning complete!")

    def open_solution_link(self, oid):
        name, _ = get_short_name(oid)
        webbrowser.open(
            "https://leetcode.com/problems/%s/discuss/?currentPage=1&orderBy=hot\
            &query=&tag=python"
            % (name)
        )
        print("🐽️ Quest solution for noobs!")

    def update(self):
        print("⚓️ Start fetching~")
        get_all_question()

    def random(self):
        print("🐙 Random quest fetching~")
        done = False
        qid = random.randint(1, 1803)
        while not done:
            try:
                self.get_quest(qid)
                done = True
            except:
                qid = random.randint(1, 1803)

    def run(self):
        args = self.parser.parse_args()
        if args.qid:
            self.get_quest(args.qid)
        elif args.oid:
            self.open_link(args.oid)
        elif args.sid:
            self.open_solution_link(args.sid)
        elif args.update == "update":
            self.update()
        elif args.random:
            self.random()
        else:
            print(args)
            print("🙈 Command refuse sir!")
            self.parser.print_help()


if __name__ == "__main__":
    cmd = Commander()
    cmd.run()
