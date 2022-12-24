import csv


dataset_1 = []
dataset_2 = []

with open("brightest_stars.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)


with open("brown_dwarf_stars.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

header_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

header_2 = dataset_2[0]
star_data_2 = dataset_2[1:]

stars_data = []
headers = header_1 + header_2

for index, sd in enumerate(star_data_2):
    stars_data.append(stars_data_1[index] + stars_data_2[index])
    with open("merge.csv", "a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)

