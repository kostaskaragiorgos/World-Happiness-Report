import logging
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operator import le, ge

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

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
            dataframe[dataframe["Regional indicator"]==str(i)].plot(kind='barh', title=str(j) + " of " + str(i), x="Country name", y=str(j), figsize=(10,15))
            plt.savefig("plots/"+str(j) + " of "+str(i)+".png")


def getvalueofcomparison(info, dataframe, comparison):
    """
    Adds to a list the min or max value for every column name based on the value of comparison.
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


def findhappiestcontinent(dataframe):
    index = dataframe["Regional indicator"].unique().tolist()
    maxplace = ""
    maxreg = 0
    for i in index:
        if maxreg < dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean():
            maxreg = dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean()
            maxplace = str(i)
    return maxreg, maxplace


def findleasthappiestcontinent(dataframe):
    index = dataframe["Regional indicator"].unique().tolist()
    minplace = ""
    minreg = 10000000
    for i in index:
        if minreg > dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean():
            minreg = dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean()
            minplace = str(i)
    return minreg, minplace

def addtoafile(data, flag):
    """
    write data to a .txt file
    Args:
        data: data to the file save 
    """
    with open('dailyreport.txt', flag) as f:
        f.writelines(data)

def main():
    """ main function """
    info = []
    df = createdataframe(FILENAME)
    plotseofeverycontinent(df)
    logging.info("Plots for every continent have been successfully created")
    infomin = getvalueofcomparison(info, df, "min")
    addtoafile(infomin, "w")
    infomax = getvalueofcomparison(info, df, "max")
    addtoafile(infomax, "a+")
    maxscore, maxplace = findhappiestcontinent(df)
    minscore, minplace = findleasthappiestcontinent(df)
    addtoafile("\n Happiest Continent \n"+str([maxscore, maxplace]), "a+")
    addtoafile("\n Least Happiest Continent \n"+str([minscore, minplace]), "a+")
    logging.info("dailyreport.txt has been successfully created")
    os.system("pause")

if __name__ == '__main__':
    main()