import hashlib

import pickle

__author__ = 'gautam'


class BasePlot(object):
    def __hash__(self):
        return hashlib.md5(pickle.dumps(self)).hexdigest()

    def compute(self, scenario):
        """
        :type scenario: Scenario
        :param scenario:
        :return:
        """

    def set_up(self, scenario):
        pass
