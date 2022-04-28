import pandas as pd
import datetime


RAW_DATA_DIR = "data/input-raw"
DATA_2017 = RAW_DATA_DIR + "/brand-registration-2017-4282022.csv"
DATA_2019 = RAW_DATA_DIR + "/brand-registration-2019-4282022.csv"
pd.options.display.max_columns = None
pd.options.display.max_rows = None


def load_data():
    df_2017 = pd.read_csv(DATA_2017, sep=";", header=1, encoding="ISO-8859-1",
                          names=["rank", "brand", "location", "registrations2017"])
    df_2019 = pd.read_csv(DATA_2019, sep=";", header=2, encoding="ISO-8859-1",
                          names=["rankB", "brand", "location", "registrations2019"])
    return df_2017, df_2019


def filter_data(_data_2017, _data_2019):
    return _data_2017.filter(["brand", "registrations2017"]), _data_2019.filter(["brand", "registrations2019"])


def get_aggregated_table(_data_2017, _data_2019):
    return pd.merge(_data_2017, _data_2019, on='brand')


def main():
    data_2017, data_2019 = load_data()
    data_2017, data_2019 = filter_data(data_2017, data_2019)
    aggr_table = get_aggregated_table(data_2017, data_2019)
    timestamp = datetime.datetime.now().strftime("%w%d%Y")
    aggr_table.to_csv("./data/output/brand-registrations-" + timestamp + ".csv")
    return aggr_table
