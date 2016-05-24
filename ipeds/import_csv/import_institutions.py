import django
from tablib import Dataset

from ipeds.models import InstitutionModel

PATH_HD = '/tmp/mergedipedswithreadableheaders/Institutions_HD_merged_header_names.csv'
PATH_IC = '/tmp/mergedipedswithreadableheaders/Institutions_IC_merged_header_names.csv'


def main():
    django.setup()
    model_dicts = {}
    models = []
    csv_hd = Dataset().load(open(PATH_HD).read())
    csv_id = Dataset().load(open(PATH_IC).read())
    integer_list = [
        'institution_id',
        'institution_type',
        'institution_type_and_level',
        'institution_level',
        'carnegie_classification',
        'land_grant_institution',
        'historically_black_colleges_and_universities',
        'tribal',
        'institutional_control_or_affiliation',
        'academic_year']

    for r_hd in csv_hd.dict:
        data_dict = {k: r_hd.get(k) for k in InstitutionModel._meta.get_all_field_names()}
        for k in integer_list:
            try:
                data_dict[k] = int(data_dict[k])
            except ValueError as e:
                print e
                data_dict[k] = None
            except TypeError as e:
                print e
                data_dict[k] = None

        model = InstitutionModel(**data_dict)
        models.append(model)
        key = (int(data_dict['academic_year']), int(data_dict['institution_id']))
        model_dicts[key] = model

    for r_id in csv_id.dict:
        academic_year = int(r_id['academic_year'])
        institution_id = int(r_id['institution_id'])
        institutional_control_or_affiliation = r_id['institutional_control_or_affiliation']
        model = model_dicts[(academic_year, institution_id)]
        model.institutional_control_or_affiliation = institutional_control_or_affiliation

    InstitutionModel.objects.bulk_create(models)


if __name__ == '__main__':
    main()
