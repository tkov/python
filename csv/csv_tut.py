import csv

with open('./grades.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)    # skips header line/row

    for line in csv_reader:
        print(line)


"""
with open('new_grades.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimeter='\t') # separator is tab

    for line in csv_reader:
        csv_writer.writerow(line)

"""

with open('./grades.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_grades.csv', 'w') as new_csv_file:
        pass

