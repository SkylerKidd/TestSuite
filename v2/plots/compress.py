from collections import OrderedDict

from scipy.stats import stats

__author__ = 'gautam'


class Compression(object):
    def compress(self, *args, **kwargs):
        pass


class CompressLines(Compression):
    def compress(self, data_list):
        zeros = [x for x in data_list if x == 0]
        non_zero = [x for x in data_list if x > 0]
        x1 = len(zeros) - 1
        x2 = x1 + len(non_zero)
        y1 = non_zero[0]
        y2 = non_zero[-1]
        return [
            [0, 0, x1 - 1, 0],
            [x1, y1, x2, y2]
        ]


class StepCompress(Compression):
    @staticmethod
    def first_index(item, data_list):
        return data_list.index(item)

    @staticmethod
    def last_index(item, data_list):
        return len(data_list) - data_list[::-1].index(item) - 1

    def compress(self, data_list):
        uniques = set()
        points = []
        for point in data_list:
            if point in uniques:
                continue
            x0 = self.first_index(point, data_list)
            x1 = self.last_index(point, data_list)
            y0 = point
            y1 = point
            points.append([
                x0, y0, x1, y1
            ])
            uniques.add(point)
        return points


class Smoothen(Compression):
    @staticmethod
    def build_index(data_list):
        indices = OrderedDict()
        for index, val in enumerate(data_list):
            index_array = indices.get(val)
            if not index_array:
                indices[val] = index_array = []
            index_array.append(index)
        return indices

    def compress(self, data_list):
        SMOOT_FACTOR = 5
        non_zero = filter(lambda x: not x == 0, data_list)
        zeros = filter(lambda x: x == 0, data_list)
        indexed_non_zero = self.build_index(non_zero)
        unique_elements = indexed_non_zero.keys()
        last_index_of_first = int(indexed_non_zero[unique_elements[0]][-1 * SMOOT_FACTOR])
        last_index_of_last = int(indexed_non_zero[unique_elements[-1]][-1])
        valid_indices = range(last_index_of_first, last_index_of_last + 1)
        slope, intercept, r_value, p_value, std_err = stats.linregress(valid_indices,
                                                                       non_zero[
                                                                       last_index_of_first:last_index_of_last + SMOOT_FACTOR])

        y_points = []
        for i in valid_indices:
            y = i * slope + intercept
            y_points.append(y)

        return filter(lambda x: x == non_zero[0], non_zero) + y_points + zeros[5:]
