import csv
import pandas as pd

dataset_1 = []
dataset_2 = []

with open("brightest_stars.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)


with open("merge.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

header_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

header_2 = dataset_2[0]
star_data_2 = dataset_2[1:]

for index, sd in enumerate(star_data_2):
    star_data_2[index]

final_star = []

for sd in star_data_1:
    final_star.append(sd)

for sd in star_data_2:
    final_star.append(sd)




df = pd.DataFrame(final_star, columns = ["name", "distance", "mass", "radius"])
df.to_csv("merge.csv")
