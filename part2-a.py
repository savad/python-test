import pandas as pd

def get_max_sepal_length_by_species(max):
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    df = df[df['sepal_length'] <= float(max)]
    df = df.groupby('species').size()
    return df.to_dict()
    
print(get_max_sepal_length_by_species("6.5"))
# sample output: {'setosa': 50, 'versicolor': 42, 'virginica': 28}


