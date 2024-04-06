class Maze:
    def __init__(self, grid):
        self._nodesVisited = 0
        self._solutionPathLength = 0
        self._executionTime = 0
        self._isGoalReached = True
        self._solutionMaze = []
        self._grid = grid

    @property
    def nodesVisited(self):
        return self._nodesVisited

    @nodesVisited.setter
    def nodesVisited(self, newNodesVisited):
        self._nodesVisited = newNodesVisited

    @property
    def solutionPathLength(self):
        return self._solutionPathLength

    @solutionPathLength.setter
    def solutionPathLength(self, newSolutionPathLength):
        self._solutionPathLength = newSolutionPathLength

    @property
    def executionTime(self):
        return self._executionTime

    @executionTime.setter
    def executionTime(self, newExecutionTime):
        self._executionTime = newExecutionTime

    @property
    def isGoalReached(self):
        return self._isGoalReached

    @isGoalReached.setter
    def isGoalReached(self, newIsGoalReached):
        self._isGoalReached = newIsGoalReached

    @property
    def solutionMaze(self):
        return self._solutionMaze

    @solutionMaze.setter
    def solutionMaze(self, newSolutionMaze):
        self._solutionMaze = newSolutionMaze

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, newGrid):
        self._grid = newGrid
