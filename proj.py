import csv

with open("./images/train/images.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)