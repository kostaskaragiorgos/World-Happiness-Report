import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILENAME = "world-happiness-report-2021.csv"

def createdataframe(filename):
    """
    creates a dataframe.
    Args:
        filename: a csv file
    Returns:
        a dataframe
    """
    return pd.read_csv(filename)

def ladderscoreofeverycontinent(dataframe):
    """
    Ladder score of every continent.
    Args:
        dataframe: a dataframe
    """
    indexlist = dataframe["Regional indicator"].unique().tolist()
    for i in indexlist:
        dataframe[dataframe["Regional indicator"]==str(i)].plot(kind='barh', x="Country name", y="Ladder score", figsize=(10,15))
        plt.savefig("plots/Happiness of "+str(i)+".png")


def getmax(dataframe):
    maxinfos = []
    index = list(dataframe)
    index.remove("Country name")
    index.remove("Regional indicator")
    for i in index:
        maxinfos.append(str(dataframe.loc[dataframe[str(i)]==dataframe[str(i)].max()]["Country name"]))
    return maxinfos


def main():
    df = createdataframe(FILENAME)
    ladderscoreofeverycontinent(df)
    infos = getmax(df)
    print(infos)

if __name__ == '__main__':
    main()