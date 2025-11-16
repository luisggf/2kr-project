import pandas as pd

def createBinaryCSV(df, feature, path):
    pd.DataFrame.to_csv(((df[feature] > 0).astype(int)), path)
    print('Dataframe created successfully in %{path}.')