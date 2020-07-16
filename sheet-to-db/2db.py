import csv

tsv_file = open("16-07-2020.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")

for row in read_tsv:
  print(row)