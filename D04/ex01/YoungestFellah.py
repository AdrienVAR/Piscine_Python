from FileLoader import FileLoader
import pandas as pd

def youngestFellah(df, value):
    youngestGuy = {}
    #youngestGuy = df.set_index("Sex").T.to_dict("Age")
    #youngestGuy = df.set_index('Sex')['Age'].to_dict(youngestGuy)
    #df.loc['Sex']
    fe = df.loc[(df['Year'] == value) & (df['Sex'] == 'F')].min()
    me = df.loc[(df['Year'] == value) & (df['Sex'] == 'M')].min()
    youngestGuy['f'] = fe['Age']
    youngestGuy['m'] = me['Age']
    print(youngestGuy)
#
#if __name__ == "__main__":
#    loader = FileLoader()
#    data = loader.load('../data/athlete_events.csv')
#    youngestFellah(data, 2004)
#
#    #df.loc() Access a group of rows and columns by label(s) or a boolean array.

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("good.csv")
    youngestFellah(data, 2004)