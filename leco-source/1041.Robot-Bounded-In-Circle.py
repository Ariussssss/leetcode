"""
1041. Robot Bounded In Circle

Difficulty: Medium

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}



"""

import unittest


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        cur = [(0, 0), 0]

        for i in instructions:
            if i == "G":
                cur[0] = tuple([x + y for x, y in zip(cur[0], dirs[cur[1]])])
            elif i == "L":
                cur[1] = (cur[1] + 1) % len(dirs)
            else:
                cur[1] = (cur[1] + len(dirs) - 1) % len(dirs)
        return cur[0] == (0, 0) or cur[1] != 0


class RobotBoundedInCircleCase(unittest.TestCase):
    def test_robot_bounded_in_circle(self):
        s = Solution()
        for i, o in [
            ("GLRLLGLL", True),
            ("GLGLGGLGL", False),
            ("GGLLGG", True),
            ("GG", False),
            ("GL", True),
        ]:
            self.assertEqual(s.isRobotBounded(i), o)


if __name__ == "__main__":
    s = Solution()
    unittest.main()
