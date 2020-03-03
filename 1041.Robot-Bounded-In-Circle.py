"""
1041. Robot Bounded In Circle
User Accepted:1620
User Tried:2130
Total Accepted:1665
Total Submissions:5152
Difficulty:Medium
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
    def robot_bounded_in_circle()->int:
    
class RobotBoundedInCircleCase(unittest.TestCase):
    def test_robot_bounded_in_circle(self):
        s = Solution()
        for i, o in []:
            self.assertEqual(s.robot_bounded_in_circle(i), o)


if __name__ == '__main__':
    s = Solution()
    unittest.main()

