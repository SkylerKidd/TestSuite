from ipeds.models import InstitutionModel, TuitionModel, NonTuitionModel
from ipeds.stateabbvr import STATE_TO_ABBVR
from v2.transform import _compute_cost_of_attendance


def query_institutions(standard_institution_type, full_state_name, year):
    """
    -for "institution_type", 1=public , 2=private non-profit , 3=private for-profit
    -for "institution_type_and_level",
    1=public 4-year,
    2= private non-profit 4-year,
    3= private for-profit 4-year,
    4=public 2-to-4-year,
    5= private non-profit 2-to-4-year,
    6= private for-profit 2-to-4-year,
    7=public 2-year,
    8= private non-profit 2-year,
    9= private for-profit 2-year
    other codes in this column can be ignored

    -for "institutinon_level",
    1=4-year,
    2=2-to-4-year,
    3=2-year
    other codes in this column can be ignored


    -for "carnegie_classification"
    33,40=2-year institutions,
    21, 22, 31, 32=4-year institutions,
    15,16=research institutions
    other codes are special interest institutions that we will ignore
    :param standard_institution_type:
    :return:
    """
    institution_filter = None
    if standard_institution_type == 'Public Research':
        institution_filter = {
            'institution_type': 1,
            'institution_type_and_level': 1,
            'institution_level': 1,
            'carnegie_classification__in': [15, 16]
        }
    elif standard_institution_type == 'Public Regional':
        institution_filter = {
            'institution_type': 1,
            'institution_type_and_level': 1,
            'institution_level': 1,
            'carnegie_classification__in': [21, 22, 31, 32]
        }
    elif standard_institution_type == 'CTCS':
        institution_filter = {
            'institution_type': 1,
            'institution_type_and_level__in': [1, 4],
            'institution_level__in': [1, 2, 3],
            'carnegie_classification__in': [33, 40]
        }

    elif standard_institution_type == 'Private Nonprofit':
        institution_filter = {
            'institution_type': 2,
            'institution_type_and_level__in': [2],
            'institution_level': 1,
            'carnegie_classification__in': [15, 16, 21, 22, 31, 32, 40, 51, 52, 53, 55, 56, 57]
        }
    if institution_filter:
        institution_filter['state_abbreviation'] = STATE_TO_ABBVR.get(full_state_name)
        institution_filter['academic_year'] = year
        return InstitutionModel.objects.filter(**institution_filter)
    else:
        return None


def compute_cost_of_attendance(year, state, living_status, institution_type, tuition_cost_adjustment=0):
    institutions = query_institutions(institution_type, state, year)
    institution_ids = [i.institution_id for i in institutions]
    tuition_objects = TuitionModel.objects.filter(
        institution_id__in=institution_ids,
        academic_year=year)
    non_tuition_objects = NonTuitionModel.objects.filter(
        institution_id__in=institution_ids,
        academic_year=year)

    total_tuition = [t.published_in_state_tuition_and_fees for t in tuition_objects]

    if living_status == 'live_away':
        non_tuition = [n.total_on_campus() for n in non_tuition_objects]
    elif living_status == 'Indep_live_w_parent':
        non_tuition = [n.total_off_campus() for n in non_tuition_objects]
    else:
        non_tuition = [n.total_off_campus_with_family() for n in non_tuition_objects]

    return _compute_cost_of_attendance(total_tuition, non_tuition, tuition_cost_adjustment)
