import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('moving_items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    with open('moving_items.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

