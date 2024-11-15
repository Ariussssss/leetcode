import subprocess
import re
from os import walk


def get_difficulty(name):

    fs = open("./leco-source/" + name, "r")

    pattern = re.compile("Difficulty: ([^\n]*)\n")

    found = False
    difficulty = "unknown"
    for i, line in enumerate(fs):
        for match in re.finditer(pattern, line):
            difficulty = match.group(1)
            found = True
        if found:
            break
    return difficulty


def line(name, difficulty, code):
    return "\n  - [%s] %s %s" % (
        ("X" if code == 0 else " "),
        difficulty.rjust(8, " "),
        name,
    )


def main():
    f = []
    for (dirpath, dirnames, filenames) in walk("./leco-source"):
        f.extend(x for x in filenames if re.match(r"^\d.*\.py$", x))

    f.sort(key=lambda x: int(re.match(r"^(\d*).", x).group(1)))

    outputStr = ""
    counter = 0
    difficulty_map = {}

    for t in f:
        difficulty = get_difficulty(t)
        if difficulty not in difficulty_map:
            difficulty_map[difficulty] = [0, 1]
        else:
            difficulty_map[difficulty][1] += 1
        try:
            return_code = subprocess.run(
                "python3 ./leco-source/" + t,
                shell=True,
                timeout=2,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            outputStr += line(t, difficulty, return_code)
            if return_code == 0:
                difficulty_map[difficulty][0] += 1
                counter += 1
        except Exception:
            outputStr += line(t, difficulty, 1)
    outputStr = (
        """#+STARTUP: showall
* Leetcode Solutions

** Usage
#+begin_src bash
  python -m leco -h
  python -m leco -q 3249
#+end_src
** 🌟 Schedule [%s%%] %s


** 🪐 Total
  - %s Total: %s Done: %s"""
    ) % (
        int(counter * 100 / len(f)),
        outputStr,
        "All".rjust(8, " "),
        str(len(f)).rjust(4, " "),
        str(counter).rjust(4, " "),
    )

    for key, (d, a) in difficulty_map.items():
        outputStr += "\n  - %s Total: %s Done: %s" % (
            key.rjust(8, " "),
            str(a).rjust(4, " "),
            str(d).rjust(4, " "),
        )

    with open("./README.org", "w") as output:
        output.write(outputStr)

    print(outputStr)


if __name__ == "__main__":
    main()
