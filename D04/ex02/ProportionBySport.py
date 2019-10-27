from FileLoader import FileLoader

def proportionBySport(df, olymp_year, sport, gender):
    #res = 0.0
    #div = 1.0
    #res = df.loc[(df['Year'] == olymp_year) & (df['Sport'] == sport) & (df['Sex'] == 'F')].sum()
    #for i in df.loc[(df['Year'] == olymp_year) & (df['Sport'] == sport) & (df['Sex'] == 'F')]:
    #    res += 1
    #i = 0
    #for i in df.loc[(df['Year'] == olymp_year) & (df['Sex'] == 'F')]:
    #for i in df.loc[(df['Sex'] == 'F')]:
    #   div += 1
    data = df.loc[(df['Year'] == olymp_year)]
    data = data.loc[(df['Sport'] == sport)]
    data = data.loc[(df['Sex'] == gender)]
    data = data.groupby(['ID']).size().reset_index(name='Count')
    numOfRows = data.shape[0]

    res = df.loc[(df['Year'] == olymp_year)]
    res = res.loc[(df['Sex'] == gender)]
    res = res.groupby(['ID']).size().reset_index(name='Count')
    numOfWomen = res.shape[0]
 
    print('Number of Rows in dataframe : ' , numOfRows)
    print('Number of fem : ' , numOfWomen)
    #print (data)
    #print (res)
    #print((res/div)/100)
    print(numOfRows/numOfWomen)

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    proportionBySport(data, 2004, 'Tennis', 'F')

    #Data.valuecount()