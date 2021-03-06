from abc import ABC, abstractmethod
import numpy as np


class Mutator(ABC):

    @abstractmethod
    def mutate(self,toMutate):
        pass

    @abstractmethod
    def dynamicAdaptation(self, progress):
        pass


class RandomMutator(Mutator):

    def __init__(self, mutationRate=0.5, dynAdapt=False):
        self.mutationRate = mutationRate
        self.origMutationRate = mutationRate
        self.dynAdapt = dynAdapt

    def mutate(self, toMutate):
        """
        randomly mutate alleles
        :param toMutate:
        :return: mutated individual
        """
        mutPos = np.random.choice([True, False], size=toMutate.jobAssignments.size, p=[self.mutationRate, 1-self.mutationRate])
        toMutate.jobAssignments[mutPos] = np.random.randint(0, toMutate.jobAssignments.max(), toMutate.jobAssignments[mutPos].size)
        return toMutate

    def dynamicAdaptation(self, progress):
        if self.dynAdapt:
            self.mutationRate = self.origMutationRate*(1.2-progress)


class BoundaryMutator(Mutator):

    def mutate(self, toMutate):
        """
        Randomly sets individuals to the upper and lower boundary values of the array

        :param toMutate:
        :return: mutated individual
        """
        mask = np.random.randint(0,3,toMutate.jobAssignments.shape,np.int32)
        max = toMutate.jobAssignments.max()
        min = toMutate.jobAssignments.min()
        toMutate.jobAssignments[mask == 0] = min
        toMutate.jobAssignments[mask == 2] = max
        return toMutate

    def dynamicAdaptation(self, progress):
        pass


class SwapMutator(Mutator):

    def mutate(self, toMutate):
        """
        randomly swaps two adjacent alleles

        :param toMutate:
        :return: mutated individual
        """
        size = toMutate.jobAssignments.size
        mutPos = np.random.randint(size)
        toMutate.jobAssignments[mutPos], toMutate.jobAssignments[(mutPos+1) % size]\
            = toMutate.jobAssignments[(mutPos+1) % size], toMutate.jobAssignments[mutPos]
        return toMutate

    def dynamicAdaptation(self, progress):
        pass