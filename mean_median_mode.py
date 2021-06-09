import csv
from collections import Counter

def find_mean(data):
    sum_of_data = 0

    for i in data:
        sum_of_data = sum_of_data + i

    mean = sum_of_data / len(data)
    print("Mean Of Data: " + str(mean))

def find_median(data):
    
    data.sort()
    data_length = len(data)
    if data_length % 2 == 0:
        first_num = float(data[data_length // 2])
        second_num = float(data[data_length // 2 - 1])
        
        median = (first_num + second_num) / 2
    else:
        median = float(data[data_length // 2])
    print("Median: " + str(median))

def find_mode(data):
    data.sort()
    count_data = Counter(data)
    mode_occurence = 0
    final_mode = 0
    mode_data_for_range = {
        "75-85": 0, 
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }

    for height, occurence in count_data.items():
        if  75 <= float(height) < 85:
            mode_data_for_range["75-85"] += occurence
        elif 85 <= float(height) < 95:
            mode_data_for_range["85-95"] += occurence
        elif 95 <= float(height) < 105:
            mode_data_for_range["95-105"] += occurence
        elif 105 <= float(height) < 115:
            mode_data_for_range["105-115"] += occurence
        elif 115 <= float(height) < 125:
            mode_data_for_range["115-125"] += occurence
        elif 125 <= float(height) < 135:
            mode_data_for_range["125-135"] += occurence
        elif 135 <= float(height) < 145:
            mode_data_for_range["135-145"] += occurence
        elif 145 <= float(height) < 155:
            mode_data_for_range["145-155"] += occurence
        elif 155 <= float(height) < 165:
            mode_data_for_range["155-165"] += occurence
        elif 165 <= float(height) <= 175:
            mode_data_for_range["165-175"] += occurence

    for eachRange, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range = [int(eachRange.split("-")[0]), int(eachRange.split("-")[1])]
            mode_occurence = occurence
            final_mode = float((mode_range[0] + mode_range[1]) / 2)

    print('Final Mode: ' + str(final_mode))

with open("./hwFiles/data/SOCR-HeightWeight-1.csv", newline="") as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in file_data:
    new_data.append(float(i[2]))
new_data.sort()

find_mean(new_data)
find_median(new_data)
find_mode(new_data)



