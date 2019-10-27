from FileLoader import FileLoader

def howManyMedals(df, name):
    ret = {}
    df = df.loc[(df["Name"] == name)]
    bronze = df.loc[(df["Medal"]) == "Bronze"]
    silver = df.loc[(df["Medal"]) == "Silver"]
    gold = df.loc[(df["Medal"]) == "Gold"]
    bronze = bronze["Year"]
    silver = silver["Year"]
    gold = gold["Year"]
    #res = res.loc["Year"]
    for elem in bronze:
        ret[elem] = {'G':0, 'S':0, 'B':0}
    for elem in silver:
        ret[elem] = {'G':0, 'S':0, 'B':0}
    for elem in gold:
        ret[elem] = {'G':0, 'S':0, 'B':0}
    for elem in bronze:
        ret[elem]['B'] += 1
    for elem in silver:
        ret[elem]['S'] += 1
    for elem in gold:
        ret[elem]['G'] += 1
    #print (bronze)
    print(silver)
    #print(gold)
    print (ret)

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    howManyMedals(data, 'Kjetil Andr Aamodt')

    #Data.valuecount()




























    #bronze = df.loc[df['Medal'] == "Bronze"]
    #silver = df.loc[df['Medal'] == "Silver"]
    #gold = df.loc[df['Medal'] == "Gold"]
    #bronze = bronze["Year"]
    #silver = silver["Year"]
    #gold = gold["Year"]
    #for elem in bronze:
    #    ret[elem] = {'G':0, 'S':0, 'B':0}
    #for elem in silver:
    #    ret[elem] = {'G':0, 'S':0, 'B':0}
    #for elem in gold:
    #    ret[elem] = {'G':0, 'S':0, 'B':0}
    #for elem in gold:
    #        ret[elem]['G'] += 1
    #for elem in silver:
    #        ret[elem]['S'] += 1
    #for elem in bronze:
    #        ret[elem]['B'] += 1
#
    #return (ret)