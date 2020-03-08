# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2020-03-09

import requests
import json
import argparse
import re
from functools import cmp_to_key



def get_all_question():
    print("⚓️ Start fetching~")
    request = requests.get(
        'https://leetcode.com/api/problems/all/')
    if request.status_code == 200:
        def fmt(item):
            return {
                "question_id": item["stat"]["question_id"],
                "frontend_question_id": item["stat"]["frontend_question_id"],
                "question__title": item["stat"]["question__title"],
                "question__title_slug": item["stat"]["question__title_slug"]
            }
        def cmp(x, y):
            return 0 if x["frontend_question_id"] > y["frontend_question_id"] else -1
        res = [fmt(i) for i in request.json()["stat_status_pairs"]]
        res.sort(key=cmp_to_key(cmp))
        res_str = json.dumps(res, sort_keys=True, indent=4, separators=(',', ':'))
        with open('./leco_db.json', 'wt') as f:
            f.write(res_str)
        print("🎉 Update all leetcode~")
        return res
    else:
        raise Exception("🙈 Can not fetch latest leecode data")


def get_short_name(frontend_question_id):
    if not frontend_question_id:
        return
    data = []
    with open('./leco_db.json', 'rt') as f:
        data = json.loads(f.read())
        if not data:
            data = get_all_question();
    if data:
        quest = data[frontend_question_id - 1]
        if quest["frontend_question_id"] == frontend_question_id:
            return quest["question__title_slug"]
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
        'https://leetcode.com/graphql',
        json={'query': query, 'variables': {"titleSlug": question__title_slug} })
    if request.status_code == 200:
        return request.json()["data"]["question"]
    raise Exception("🙈 Net broken~")

def fmt(quest):
    title = ".".join([quest["questionFrontendId"], quest["title"]])
    file_name = ".".join([quest["questionFrontendId"], quest["titleSlug"], "py"])
    res = "\"\"\"\n" + title + "\n\n"
    res += "Difficulty: " + quest["difficulty"] + "\n"
    content = re.sub(r'<.+?>', '', quest["content"])
    content = re.sub(r'(\-\&gt\;|\&rarr\;)', "→", content).replace("&hellip;","…")
    link = "https://leetcode.com/problems/" + quest["titleSlug"] + "/"
    res +=  content + "\n\nLink: " + link + "\n\"\"\""
    solutionName = "solution"
    solutionNameSlug = "solution"
    for code in quest["codeSnippets"]:
        if code["langSlug"] == "python3":
            # re def reorderList(
            m = re.search('def(\w+)\(', code["code"])
            solutionName = re.search('def\s+(.+)\(', "def reorderList(self, head: ListNode) -> None:").group(1)
            solutionNameSlug = re.sub(r'(?<!^)(?=[A-Z])', '_', solutionName).lower()
            res += "\n\nfrom typing import List\n\n" + code["code"] + "\n\n"
            break

    test = """

import unittest
        
class SolutionCase(unittest.TestCase):
    def test_%s(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.%s(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
    """ % (solutionNameSlug, solutionName)
    
    res += test
    with open(file_name, 'wt') as f:
        f.write(res)
    return file_name

def get_quest(frontend_question_id):
    print("⚓️ Start fetching~")
    name = get_short_name(frontend_question_id)
    file_name = fmt(get_quest_data(name))
    print("🎉 Download %s success, go leetcoding~" % (file_name))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Let\'s go leetcoding~ ')
    parser.add_argument('update', nargs='?', help='Update local leedcode data.')
    parser.add_argument('-q', '--quest', dest='id', type=int, help='Get leetcode by problem ID')
    args = parser.parse_args()
    if args.id:
        get_quest(args.id)
    elif args.update == 'update':
        get_all_question()
    else:
        print("🙈 Command refuse sir!")
