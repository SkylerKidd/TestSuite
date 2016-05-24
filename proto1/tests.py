import random

from django.test import TestCase

# Create your tests here.
from django.test.runner import DiscoverRunner

from proto1 import constants
from proto1.plots import common_utils
from proto1.plots.washington import InstitutionalAid


class TestInstitutionalAid(TestCase):
    def test_random_values_dont_crash_decide_averaging_path(self):
        for i in range(1, 201):
            result = InstitutionalAid.decide_averaging_path(
                percent_mfi=i,
                always_use_weighted_avg=bool(random.getrandbits(1)),
                sng_max_influence=InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT,
                sng_shown=bool(random.getrandbits(1)),
            )
            self.assertTrue(result in [InstitutionalAid.USE_CAMPUS_AID_N,
                                       InstitutionalAid.USE_CAMPUS_AID_Y,
                                       InstitutionalAid.USE_WEIGHTED_AVG])

    def test_weighted_avg_condition_decide_averaging_path(self):
        for i in range(1, 201):
            result = InstitutionalAid.decide_averaging_path(
                percent_mfi=i,
                always_use_weighted_avg=True,
                sng_max_influence=InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT,
                sng_shown=bool(random.getrandbits(1)),
            )
            self.assertEqual(result, InstitutionalAid.USE_WEIGHTED_AVG)

    def test_sng_y_condition_decide_averaging_path(self):
        for i in range(1, InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT):
            result = InstitutionalAid.decide_averaging_path(
                percent_mfi=i,
                always_use_weighted_avg=False,
                sng_max_influence=InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT,
                sng_shown=True,
            )
            self.assertEqual(result, InstitutionalAid.USE_CAMPUS_AID_Y)

    def test_sng_n_condition_decide_averaging_path(self):
        for i in range(InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT + 1, 201):
            result = InstitutionalAid.decide_averaging_path(
                percent_mfi=i,
                always_use_weighted_avg=False,
                sng_max_influence=InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT,
                sng_shown=True,
            )
            self.assertEqual(result, InstitutionalAid.USE_CAMPUS_AID_N)

        for i in range(1, 201):
            result = InstitutionalAid.decide_averaging_path(
                percent_mfi=i,
                always_use_weighted_avg=False,
                sng_max_influence=InstitutionalAid.SNG_INFLUENCE_MAX_MFI_PERCENT,
                sng_shown=False,
            )
            self.assertEqual(result, InstitutionalAid.USE_CAMPUS_AID_N)


class TestTimeToGraduate(TestCase):
    def test_time_to_graduate_not_available_in_scenario(self):
        tog = common_utils.compute_time_to_graduate({
            constants.INSTITUTION_TYPE: 'CTCS'
        })
        self.assertEqual(tog, 2.0)

    def test_tog_no_difference(self):
        tog = common_utils.compute_time_to_graduate({
            constants.INSTITUTION_TYPE: 'CTCS',
            constants.NOMINAL_TIME_TO_GRADUATE: 2,
            constants.TIME_TO_GRADUATE: 2
        })
        self.assertEqual(tog, 2)

    def test_tog_positive_difference(self):
        tog = common_utils.compute_time_to_graduate({
            constants.INSTITUTION_TYPE: 'CTCS',
            constants.NOMINAL_TIME_TO_GRADUATE: 4,
            constants.TIME_TO_GRADUATE: 5.3
        })
        self.assertEqual(tog, 3.3)

    def test_tog_negative_difference(self):
        tog = common_utils.compute_time_to_graduate({
            constants.INSTITUTION_TYPE: 'CTCS',
            constants.NOMINAL_TIME_TO_GRADUATE: 4,
            constants.TIME_TO_GRADUATE: 3.3
        })
        self.assertEqual(tog, 1.3)

    def test_tog_potentially_negative_difference(self):
        """
        The difference can potentially cause tog to be < 0
        :return:
        """
        tog = common_utils.compute_time_to_graduate({
            constants.INSTITUTION_TYPE: 'CTCS',
            constants.NOMINAL_TIME_TO_GRADUATE: 4,
            constants.TIME_TO_GRADUATE: 1
        })
        self.assertEqual(tog, 1)


class UseExistingDBDiscoverRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass
