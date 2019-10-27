from FileLoader import FileLoader

class SpatioTemporalData :
    def __init__ (self, df):
        self.df = df

    def when(self, location):
        res = []
        df = self.df.loc[self.df['City'] == location]
        df = df['Year']
        for y in df:
            if y not in res:
                res.append (y)
        return res

    def where(self, date):
        df = self.df.loc[self.df['Year'] == date]
        df = df['City']
        return df.iloc[0]

if __name__ == "__main__":
    fl = FileLoader()
    df = fl.load("../data/athlete_events.csv")

    std = SpatioTemporalData(df)
    print(std.when('Tokyo'))
    print(std.where(2000))