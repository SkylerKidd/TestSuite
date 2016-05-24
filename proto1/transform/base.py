from abc import abstractmethod
import abc

from proto1.scenario import Scenario

__author__ = 'gautam'


class BaseTransform:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def transform(self, scenario):
        """
        Transform a scenario object
        :type scenario: Scenario
        :param scenario: the scenario object to transform
        :return:
        """
        return scenario
