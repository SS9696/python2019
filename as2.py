import csv

with open('first_10.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        else:
            if float(row[9]) >= 100 and float(row[9]) <= 150:
                print(f'\t{row[0]} {row[1]} {row[9]}')
            line_count += 1
