import csv

rowheaders = []

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Assume the first column contains the row headers
        rowheaders.append(row[0])

print('CSV file successfully processed')
print('Row Headers:', rowheaders)
