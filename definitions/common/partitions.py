from datetime import datetime


def get_year_partitions():
    current_year = datetime.now().year

    partitions = []
    for year in range(current_year, 1999, -1):
        partitions.append(str(year))
    return partitions
