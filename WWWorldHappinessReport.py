import pandas as pd
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
    indexlist = dataframe["Regional indicator"].unique().tolist()
    for i in indexlist:
        dataframe[dataframe["Regional indicator"]==str(i)].plot(kind='barh', x="Country name", y="Ladder score", figsize=(10,15))
        plt.savefig("plots/Vaccinations of "+str(i)+".png")

def main():
    df = createdataframe(FILENAME)
    print(df)


if __name__ == '__main__':
    main()