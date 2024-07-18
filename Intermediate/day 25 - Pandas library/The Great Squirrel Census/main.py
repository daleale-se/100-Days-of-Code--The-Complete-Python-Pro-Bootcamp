import pandas


def main():

    # squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census.csv")
    # color_series = squirrel_data.pivot_table(index='Primary Fur Color', aggfunc='size')
    # color_dict = color_series.to_dict()
    # result_dict = {
    #     "Fur Color": [],
    #     "Count": []
    # }
    # for key in color_dict:
    #     result_dict["Fur Color"].append(key)
    #     result_dict["Count"].append(color_dict[key])
    # new_dataframe = pandas.DataFrame(result_dict)
    # new_dataframe.to_csv("squirrel_count.csv")

    data = pandas.read_csv("./2018_Central_Park_Squirrel_Census.csv")
    grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

    data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
    }

    print(pandas.DataFrame(data_dict))

main()