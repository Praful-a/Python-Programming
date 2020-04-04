import csv
import os
os.chdir('/Users/Praful/Desktop/python/Python-CSV/')

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

# for line in csv_reader:
#     print(line)

# for line in csv_reader:
#     print(line[2])
# next(csv_reader)
#
# for line in csv_reader:
#     print(line[2])

# with open('new_names.csv', 'w') as new_file:
#     # csv_writer = csv.writer(new_file, delimiter='-')
#     csv_writer = csv.writer(new_file, delimiter='\t')
#
#     for line in csv_reader:
#         csv_writer.writerow(line)

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#
#     for line in csv_reader:
#         print(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    # for line in csv_reader:
    #     print(line['email'])

    with open('new_names2.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
