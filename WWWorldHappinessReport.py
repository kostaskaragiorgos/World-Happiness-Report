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


def getvalueofcomparison(info, dataframe, comparison):
    index = list(dataframe)
    index.remove("Country name")
    index.remove("Regional indicator")
    for i in index:
        if comparison == "min":
            info.append(str(i) + str(dataframe.loc[dataframe[str(i)]==dataframe[str(i)].min()]["Country name"].to_string(index=False))+ str(dataframe.loc[dataframe[str(i)]==dataframe[str(i)].min()][i].to_string(index=False)))
        else:
            info.append(str(i) + str(dataframe.loc[dataframe[str(i)]==dataframe[str(i)].max()]["Country name"].to_string(index=False))+ str(dataframe.loc[dataframe[str(i)]==dataframe[str(i)].max()][i].to_string(index=False)))
    return info



def main():
    info = []
    df = createdataframe(FILENAME)
    ladderscoreofeverycontinent(df)
    info = getvalueofcomparison(info, df, "min")
    info = getvalueofcomparison(info, df, "max")
    print(info)

if __name__ == '__main__':
    main()