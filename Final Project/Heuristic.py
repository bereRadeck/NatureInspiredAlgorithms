import numpy as np
from abc import ABC, abstractmethod
from GA.ProblemDefinition import ProblemDefinition
from GA.Individual import Individual


class Heuristic:

    @classmethod
    @abstractmethod
    def calcHeuVal(cls,ind:Individual, probDef: ProblemDefinition):
        pass


class BeardwoodHeuristic(Heuristic):
    """
    'In 1959,´Beardwood et al. [1] derived an asymptotic expected tour length formula.
    T* ~ b(NA)½, for euclidean distances
    N = number of points
    A = Area
    b=0.75 has been approximated for large N'
    Since A only exists in euclidean problems it will be replaced by
    the average distance between all points
    the value of b is irrelevant since the heuristic only need to correlate with the actual value
    """
    @classmethod
    def calcHeuVal(cls,ind:Individual, probDef: ProblemDefinition):
        heuVals = np.empty(probDef.nrVehicles)
        #get nodes for each vehicle (graph)
        for vehicleInd in range(probDef.nrVehicles):
            distMatrix = ind.extractDistMatrix(vehicleInd)
            heuVals[vehicleInd] = np.mean(distMatrix) * distMatrix.shape[0] * probDef.transCost[vehicleInd]
        return -np.sum(heuVals)


class DaganzoHeuristic(Heuristic):
    """
    'In 1984, Daganzo [3] developed distance formulas for a vehicle routing problem (VRP). In
    particular, he derived a formula for determining the length of a tour through N points located in a
    subregion of A that does not include the depot. A vehicle can make at most C stops. Letting the
    density of points be given by 6 = N / A and the average straight-line distance from the points in the
    subregion to the depot be denoted by D, the optimal tour length (denoted by L*) is given by
    L* ,~ 2D(N/C) + 0.57(N6-½)
    This can be used to estimate the length of the optimal TSP tour through the N points. In
    this case, N = C and substituting 6 = N / A yields
    T* ~ 2D + 0.57(NA)½'

    """
    def calcHeuVal(cls,ind:Individual, probDef: ProblemDefinition):
        pass






