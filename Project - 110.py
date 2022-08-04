import random 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
import csv
df = pd.read_csv("data.csv")
data = df['temp'].tolist()
# fig = ff.create_distplot([data], ['temp'], show_hist = False)
# fig.show()
# population_mean = statistics.mean(data)
# std_deviation = statistics.stdev(data)
# print('Population mean is', population_mean)
# print('THe Standard Deviation is', std_deviation)
# fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0, 1], mode = 'lines', name = 'mean'))
#code to find mean and standard deviation of 100 data points
dataset = []
# for i in range(0, 100):
#     random_index = random.randint(0, len(data))
#     value = data[random_index]
#     dataset.append(value)
# mean = statistics.mean(dataset)
# std_deviation = statistics.stdev(dataset)
# print(mean)
# print(std_deviation)
#code to find mean of 100 datapoints 1000 times
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ['temp'], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'mean'))
    fig.show()
def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print('The mean of sampling distribution is', mean)
    print(std_deviation)
setup()