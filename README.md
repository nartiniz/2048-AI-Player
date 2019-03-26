# 2048-AI-Player
Designed an AI player in Python that solves 2048 using some heuristics.

GameManager_3.py . This is the driver program that loads your Computer AI and Player AI
and begins a game where they compete with each other. 

Grid_3.py : This module defines the Grid object, along with some useful operations:
move() , getAvailableCells() , insertTile() , and clone() . 

BaseAI_3.py . This is the base class for any AI component. All AIs inherit from this module,
and implement the getMove() function, which takes a Grid object as parameter and returns a move (there
are different "moves" for different AIs).

ComputerAI_3.py : This inherits from BaseAI. The getMove() function returns a computer
action that is a tuple (x, y) indicating the place you want to place a tile.

PlayerAI_3.py : The PlayerAI class inherit from BaseAI. The
getMove() function to implement must return a number that indicates the player’s action. In particular, 0
stands for "Up", 1 stands for "Down", 2 stands for "Left", and 3 stands for "Right" . This is where player-optimizing 
logic lives and is executed.

BaseDisplayer_3.py and Displayer_3.py : These print the grid

This was my homework assignment of Artificial Intelligence Course. 
