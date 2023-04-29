
# with open("./weather_data.csv") as data_file:
#     weather_data_text = data_file.readlines()
#     print(weather_data_text)

####################################################


####################################################

import pandas as pd

data = pd.read_csv("weather_data.csv")# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# temp_list = data["temp"].to_list()
#
# average_temp = round(sum(temp_list) / len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"])
# print(data["temp"].max())

# Get data in Columns

# print(data.condition)

# Get data in Row

# print(data)
# print("---------------------------------------")
# print(data[data.day == "Monday"])
# print(data[data.temp.max() == data.temp])

# monday = data[data.day == "Monday"]
# c_temp = int(monday.temp)
# f_temp = round((9/5) * c_temp + 32)
# print(f_temp)