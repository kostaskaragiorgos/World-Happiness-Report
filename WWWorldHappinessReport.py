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

def plotseofeverycontinent(dataframe):
    """
    Every plot for every continent.
    Args:
        dataframe: a dataframe
    """
    indexlist = dataframe["Regional indicator"].unique().tolist()
    index = list(dataframe)
    index.remove("Country name")
    index.remove("Regional indicator")
    for i in indexlist:
        for j in index:
            dataframe[dataframe["Regional indicator"]==str(i)].plot(kind='barh', x="Country name", y=str(j), figsize=(10,15))
            plt.savefig("plots/"+str(j) + "of "+str(i)+".png")


def getvalueofcomparison(info, dataframe, comparison):
    """
    Args:
        info: a list of info
        dataframe: the dataframe
        comparison: min or max
    Return:
        info: a list
    """
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
    plotseofeverycontinent(df)
    info = getvalueofcomparison(info, df, "min")
    info = getvalueofcomparison(info, df, "max")

if __name__ == '__main__':
    main()