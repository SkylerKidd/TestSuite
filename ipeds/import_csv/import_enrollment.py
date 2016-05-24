import django
from tablib import Dataset

from ipeds.models import EnrollmentModel

CSV_PATH = '/tmp/mergedipedswithreadableheaders/Enrollment_merged_header_names.csv'

MODEL = EnrollmentModel

ERROR_COUNT = 0


def integer_or_nothing(value):
    global ERROR_COUNT
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        ERROR_COUNT += 1
        return None


def main():
    django.setup()
    csv = Dataset().load(open(CSV_PATH).read())
    models = []
    row_count = 0
    for row in csv.dict:
        data_dict = {k: integer_or_nothing(row.get(k)) for k in MODEL._meta.get_all_field_names()}
        models.append(MODEL(**data_dict))
        row_count += 1

    MODEL.objects.bulk_create(models)
    print "{} rows processed with {} errors".format(row_count, ERROR_COUNT)


if __name__ == '__main__':
    main()
