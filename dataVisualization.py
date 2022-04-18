import numpy as np
import matplotlib.pyplot as plt


def create_bar_plot(_data_merged):
    height = [_data_merged["registrations2017"].sum(), _data_merged["registrations2019"].sum()]
    bars = ('2017', '2019')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.title("Registration of brands from Germany's most active companies")
    plt.savefig("./data/output/brand-registrations-bar-plot.png")
