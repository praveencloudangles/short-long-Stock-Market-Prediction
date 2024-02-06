from data_extraction import data_load

def data_analy():
    data = data_load()
    print(list(data.columns))
    print("null values---------", data.isnull().sum())
    print("duplicate values-------", data.duplicated().sum())
    print("shape of data--------", data.describe())
    print("unique values------------", data.nunique())
    return data
data_analy()