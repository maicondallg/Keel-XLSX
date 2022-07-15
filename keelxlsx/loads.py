import pandas as pd
import os



dirname = os.path.dirname(__file__)
datasets = os.listdir(dirname+'/datasets/')
datasets_discretized = os.listdir(dirname+'/datasets_discretized/')


def available_datasets():
    print('Default datasets:', datasets)
    print('Discretized datasets:', datasets_discretized)


def load(dataset='iris', discretized=True):
    if dataset in datasets_discretized:
        if discretized:
            return [(pd.read_excel(dirname+f"/datasets_discretized/{dataset}/{dataset}-{i}-train.xlsx"),
                     pd.read_excel(dirname+f"/datasets_discretized/{dataset}/{dataset}-{i}-test.xlsx")) for i in range(1, 11)]

    return [(pd.read_excel(dirname+f'/datasets/{dataset}/{dataset}-{i}-train.xlsx'),
             pd.read_excel(dirname+f'/datasets/{dataset}/{dataset}-{i}-test.xlsx')) for i in range(1, 11)]

