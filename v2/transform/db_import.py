from v2.transform.base import BaseTransform

__author__ = 'gautam'


class DBImportTransform(BaseTransform):
    def __init__(self, model, key):
        """
        :type model: django.db.models.Model
        :type key: str
        :param model:
        :param key: the key to store the result of the db transform
        :return:
        """
        super(DBImportTransform, self).__init__()
        self.model = model
        self.key = key
        self.query_set = self.model.objects.all()

    def filter(self, *args, **kwargs):
        self.query_set = self.query_set.filter(*args, **kwargs)
        return self

    def transform(self, scenario):
        """
        Evaluates the django queryset and stores the result in the scenario
        :type scenario: v2.scenario.Scenario
        :type query:
        :param scenario:
        :param query:
        :return:
        """
        super(DBImportTransform, self).transform(scenario)
        scenario[self.key] = list(self.query_set)
        return scenario
