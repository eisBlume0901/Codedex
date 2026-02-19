import csv

data = [
    ["Item", "Quantity"],
    ["Umbrella", 1],
    ["Pair of Victorian Boots", 1],
    ["Pair of Statement Earrings", 2],
    ["Pair of High-Knee Socks", 5],
    ["Ribbon Clip" , 4]
]
try:
    with open("packing_list.csv", "r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print("Packing list file not found. Creating a new one")
    with open("packing_list.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)

        writer.writerows(data)