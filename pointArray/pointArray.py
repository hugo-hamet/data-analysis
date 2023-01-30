from random import choice


class Graph:
    def __init__(self, points) -> None:
        """
        Class constructor.
            > points (list) : Dataset of points. Format (x,y)
        
        Its instances will have the following variables :

            > nbPoints (int) : Number of original points there was in the dataset before the array is set.
            
            > pointsArray (list) : Dataset of the points after the array is set. Their format is (x, y).
                If the coordinates of the points are floats, they will be rounded up using the built-in round() function.
            
            > mX & mY (int) : Respective maximums of the X and Y axis of the dataset.
            
            > arrayGraph (list) : Table of values indicating if whether or not there is a point at an X and Y position.
        """
        self.nbPoints = len(points)

        self.pointsArray = []
        for point in points:
            self.pointsArray.append((int(round(point[0])),int(round(point[1]))))
        
        self.mX, self.mY = 0, 0
        for point in self.pointsArray:
            if point[0] > self.mX: self.mX = point[0]
            if point[1] > self.mY: self.mY = point[1]
        
        self.arrayGraph = [[0 for x in range(self.mX+2)] for y in range(self.mY+2)]
        for point in self.pointsArray:
            self.arrayGraph[point[1]][point[0]] = 1

    def __str__(self) -> str:
        """
        Special method. Returns the characters chain of the point array.
        The characters used to represent each point don't have any signification (for now).
        """
        res = ""
        for line in self.arrayGraph:
            for pos in line:
                if pos == 1: res += choice(["x", "o", ".", "*"])
                else: res += " "
            res += "\n"
        # with a separation before and after >> f'{"_"*(self.mX+1)}\n{res}{"_"*(self.mX+1)}'
        return res

    def __repr__(self) -> str:
        """
        Special method. Returns the __str__() method.
        """
        return self.__str__()

    def conservationPercentage(self, digitPrecision=1) -> float:
        """
        Usual method. Returns the percentage of data conservation between before and after the array is done.
        
        > digitPrecision (int) : Number of percentage's decimal (recommended 1)

        Remarks :
            - The result will always be a float, even if there's no decimals.
            - The return isn't accompanied by a '%', so you can use the value as you see fit.
        """
        assert isinstance(digitPrecision, int), "Called conservationPercentage() method using a non-integer digitPrecision."
        return round(((100*len(list(set(self.pointsArray))))/self.nbPoints), digitPrecision)

    def updateMaximums(self) -> None:
        """
        Usual method. Returns None. Updates the values of self.mX and self.mY.
        
        Remarks :
            - This function might be useful if you're adding points to the array using the addPoint() method.
        """
        self.mX, self.mY = 0, 0
        for point in self.pointsArray:
            if point[0] > self.mX: self.mX = point[0]
            if point[1] > self.mY: self.mY = point[1]

    def updateGraph(self) -> None:
        """
        Usual method. Returns None. Updates the values of self.mX and self.mY.
        
        Remarks :
            - This function might be useful if you're adding points to the array using the addPoint() method.
        """
        newGraph = [[0 for x in range(self.mX+2)] for y in range(self.mY+2)]
        for point in self.pointsArray:
            try : newGraph[point[1]][point[0]] = 1
            except : pass
        self.arrayGraph = newGraph

    def addPoint(self, point) -> None:
        """
        Usual method. Returns None. Adds a point to the array and updates the graph.
        If the coordinates of the points are floats, they will be rounded up using the built-in round() function.
        If there are twin points, the new will only be stocked in self.pointsArray without being drawn in the graph.

        > point ((int, float), (int, float)) : Coordinates (x, y) of a point.

        Remarks :
            - You might want to use the updateMaximums() and updateGraph() methods if you're adding point(s).
            If you don't, the points that are exterior to the graph when you add them will not be drawn, but
            they will still be stocked in self.pointsArray.
        """
        assert (type(point) in [list, tuple]), "Called addPoint() not using a sorted pair of values (should be list or tuple)"
        assert type(point[0] in [int, float]) and type(point[1] in [int, float]), "Called addPoint() not using a pair of numbers (should be int or float)"

        try : self.arrayGraph[int(round(point[1]))][int(round(point[0]))] = 1
        except : pass
        self.pointsArray.append(
            (
                int(round(point[0])),
                int(round(point[1]))
            )
        )