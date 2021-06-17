import logging
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(filename='wwworldhappinessReport.log', level=logging.INFO,
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


def comperecontinents(dataframe, minplace = "", minreg = 1000000,maxplace = "", maxreg = 0, maxflag=True):
    """ gets the name and the ladder score of the happiest/least happiest continent.
    Args:
        dataframe:the dataframe
        minplace: the continent with the lower ladder score
        minreg: the min ladder score
        maxplace: the continent with the higher ladder score
        maxreg: the max ladder score
        maxflag: flag to check the comparisson 
    Returns:
        maxreg: the max ladder score
        maxplace: the name of the continent with the max ladder score
        minreg: the min ladder score
        minplace: the name of the continent with the min ladder score
    """
    index = dataframe["Regional indicator"].unique().tolist()
    for i in index:
        if maxflag and maxreg < dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean():
            maxreg = dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean()
            maxplace = str(i)
        elif not maxflag and minreg > dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean():
            minreg = dataframe.loc[dataframe["Regional indicator"]==str(i)]["Ladder score"].mean()
            minplace = str(i)
    return maxreg, maxplace, minreg, minplace


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
    maxscore, maxplace , minscore, minplace = comperecontinents(df, maxflag=True)
    maxscore, maxplace , minscore, minplace = comperecontinents(df,maxplace=maxplace, maxreg=maxscore, maxflag=False)
    addtoafile("\n Happiest Continent \n"+str([maxscore, maxplace]), "a+")
    addtoafile("\n Least Happiest Continent \n"+str([minscore, minplace]), "a+")
    logging.info("dailyreport.txt has been successfully created")
    os.system("pause")

if __name__ == '__main__':
    main()