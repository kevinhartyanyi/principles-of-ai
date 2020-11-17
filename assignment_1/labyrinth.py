import numpy as np

"""
Possible moves
0 -> wall
1 -> free
"""

labyrinth = np.asarray(
    [   [0,0,0,0,0,0,0,0,0],
        [0,"M", 0, "N",0,"O",1,"P",0],
        [0, 1,  0,  1, 0, 1, 0, 0, 0],
        [0,"I", 1, "J",0,"K",1,"L",0],
        [0, 0,  0,  1, 0, 0, 0, 1, 0],
        [0,"E", 0, "F",0,"G",1,"H",0],
        [0, 1,  0,  1, 0, 1, 0, 1, 0],
        [0,"A", 1, "B",1,"C",1,"D",0],
        [0,0,0,0,0,0,0,0,0]])

def backtrack(start=(1,7), goal=(7,7)):
    # preference: E, N, W, S
    step_count = 0
    backtrack_count = 0
    path = []
    def main(current=start):
        nonlocal step_count
        nonlocal backtrack_count
        nonlocal path
        if labyrinth[current] == labyrinth[goal]:
            print("Goal")
            path.append(labyrinth[current])
            print(f"Step Count: {step_count}\nBacktrack Count: {backtrack_count}\nPath: {path}")
            return True
        step_count += 1
        r,c = current
        path.append(labyrinth[current])
        print(f"Position: {labyrinth[current]}")
        print(f"Current Path: {path}")
        input()
        if c+2 < 9:
            print(f"Check Right {labyrinth[r,c+2]}")
        if labyrinth[r,c+1] == '1' and not labyrinth[r,c+2] in path:
            if main((r,c+2)):
                return True

        if r-2 >= 0:
            print(f"Check Up {labyrinth[r-2,c]}")
        if labyrinth[r-1,c] == '1' and not labyrinth[r-2,c] in path:
            if main((r-2,c)):
                return True

        if c-2 >= 0:
            print(f"Check Left {labyrinth[r,c-2]}")
        if labyrinth[r,c-1] == '1' and not labyrinth[r,c-2] in path:
            if main((r,c-2)):
                return True

        if r+2 < 9:
            print(f"Check Down {labyrinth[r+2,c]}")
        if labyrinth[r+1,c] == '1' and not labyrinth[r+2,c] in path:
            if main((r+2,c)):
                return True
        
        
        
        
        
        print("No Route backtrack")
        path = path[:-1]
        step_count -= 1
        backtrack_count += 1
        return False
    main(start)

print(labyrinth, labyrinth.shape)

backtrack()