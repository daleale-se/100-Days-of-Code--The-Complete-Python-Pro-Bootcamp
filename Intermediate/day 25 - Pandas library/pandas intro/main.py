# import csv

# def main():
#     with open("./weather_data.csv") as file:
#         data = csv.reader(file)
#         temperatures = []
#         for row in data:
#             print(row)
#             if row[1] != "temp":
#                 temperatures.append(int(row[1]))
#         print(temperatures)

import pandas


def main():

    # data = pandas.read_csv("./weather_data.csv")

    # print(data)             # Dataframe
    # print(data["temp"])     # Series
    #
    # data_dict = data.to_dict()
    # print(data_dict)
    #
    # data_list = data["temp"].to_list()
    # print(data_list)
    #
    # print(data["temp"].mean())
    # print(data["temp"].max())
    #
    # print(data.condition.to_list())
    # print(data.day.to_list())
    #
    # print(data[data.day == "Sunday"])
    # print(data[data.temp == data.temp.max()])

    # print(data[data.day == "Monday"].temp)
    # print(data.temp[0] * (9 / 5) + 32)

    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    data_d = pandas.DataFrame(data_dict)
    print(data_d)
    data_d.to_csv("here.csv")


main()
