#!/usr/bin/python3
 
# https://po.kattis.com/problems/fargrobot
 
import sys
 
# Generator function that returns an iterator of all the colors
def gen_colors():
    colors = list(sys.stdin.readline().strip())
    for c in colors:
        yield c
 
def main():
    """
    The robot will stop moving once it has passed each color once, so we need
    to keep track of which colors the robot has passed.
    
    Example:
    RRBBBGG -> G 
 
    The robot first passes R and B, so when it gets to G it stops. If the robot
    should move more than once, this is where the next move starts.
    """
    moves = int(sys.stdin.readline())
    colors = gen_colors()
    it = gen_colors()
 
    for move in range(moves):
        passed_colors = []
        """
        The robot needs to move at least three times each move, so that it can pass
        each color once.
        """
        while len(passed_colors) is not 3:
            current_color = next(it) 
            
            if current_color not in passed_colors:
                passed_colors.append(current_color)
            else:
                continue
 
        print(current_color, end='')
    print()
if __name__ == '__main__':
    main()
