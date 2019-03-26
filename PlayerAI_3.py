import random
from BaseAI_3 import BaseAI
import math
from collections import deque
from Grid_3 import Grid

search_depth = 3
weights = [1,1]
p_inf = float("inf")
n_inf = float("-inf")

def heuristics1(grid):
    sum=0
    for i in range(4):
        for j in range(4):
            if (i + j == 2):
                sum = sum + grid.map[i][j]
            if (i + j == 3):
                sum = sum + 3*grid.map[i][j]
            if (i + j == 4):
                sum = sum + 5*grid.map[i][j]
            if (i + j == 5):
                sum = sum + 15*grid.map[i][j]
            if (i + j == 6):
                sum = sum + 30*grid.map[i][j]
    return sum

def heuristics2(grid):
    penalty=0
    for i in range(4):
        for j in range(4):
            if(grid.crossBound((i-1,j))):
                penalty=penalty+abs(grid.map[i][j]-grid.map[i-1][j])
            if (grid.crossBound((i +1, j))):
                penalty = penalty + abs(grid.map[i][j] - grid.map[i + 1][j])
            if (grid.crossBound((i , j-1))):
                penalty = penalty + abs(grid.map[i][j] - grid.map[i][j-1])
            if (grid.crossBound((i, j+1))):
                penalty = penalty + abs(grid.map[i][j] - grid.map[i][j+1])
    return -penalty


def heuristics(grid):
    return weights[0]*heuristics1(grid)+weights[1]*heuristics2(grid)


def maximize(state):

    if (state[2] == search_depth):
        return [None, heuristics(state[1])]
    else:
        max_child = Grid()
        max_utility=n_inf
        for child in state[1].getAvailableMoves():
            if(chance(["C",child[1],state[2]+1,state[3],state[4]])[1]>max_utility):
                max_child.map = child[1].map
                max_utility=chance(["C",child[1],state[2]+1,state[3],state[4]])[1]
            if(max_utility>=state[4]):
                break
            if(max_utility>state[3]):
                state[3]=max_utility
        return [max_child,max_utility]

def minimize(state):

    if(state[2]==search_depth):
        return [None,heuristics(state[1])]
    else:
        min_child = Grid(state[1].size)
        min_utility = p_inf
        for new_value in (2,4):
            for free_cell in state[1].getAvailableCells():
                new_child = state[1].clone()
                new_child.setCellValue(free_cell,new_value)
                if(maximize(["P",new_child,state[2]+1,state[3],state[4]])[1]<min_utility):
                    min_child.map = new_child.map
                    min_utility = maximize(["P",new_child,state[2]+1,state[3],state[4]])[1]
                if (min_utility<=state[3]):
                    break
                if(min_utility<state[4]):
                    state[4]=min_utility
        return [min_child,min_utility]

def chance(state):

    if(state[2]==search_depth):
        return [None,heuristics(state[1])]
    else:
        min_child = Grid(state[1].size)
        utility=0
        min_utility = p_inf
        for new_value in (2,4):
            for free_cell in state[1].getAvailableCells():
                new_child = state[1].clone()
                new_child.setCellValue(free_cell,new_value)
                if(new_value==2):
                    utility = utility + (9/10)*(1/len(state[1].getAvailableCells()))*maximize(["P",new_child,state[2]+1,state[3],state[4]])[1]
                if(new_value==4):
                    utility = utility + (1 / 10) * (1 / len(state[1].getAvailableCells())) * maximize(["P", new_child, state[2] + 1, state[3], state[4]])[1]
        if(utility<state[4]):
            state[4]=utility

        return [None,utility]


class PlayerAI(BaseAI):
    def getMove(self, grid):
        # Selects a random move and returns it
        currentGrid = ["P",grid,0,n_inf,p_inf]
        decision_child=maximize(currentGrid)[0]
        move=0
        moveset = grid.getAvailableMoves()

        for z in moveset:
            if(z[1].map==decision_child.map):
                move=z[0]

        return move if moveset else None