import hashlib

import pickle

__author__ = 'gautam'


class BasePlot(object):
    def __hash__(self):
        return hashlib.md5(pickle.dumps(self)).hexdigest()

    def __init__(self, scenario):
        super(BasePlot, self).__init__()
        self.scenario = scenario

    def query_db(self):
        pass

    def pre_compute(self):
        pass

    def post_compute(self):
        pass

    def compute(self):
        pass

    def set_up(self, scenario):
        pass

    def execute(self):
        self.query_db()
        self.pre_compute()
        result = self.compute()
        self.post_compute()
        return result
