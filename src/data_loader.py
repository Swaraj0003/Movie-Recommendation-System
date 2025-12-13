import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['genres'] = df['genres'].apply(eval)  # Convert string list to actual list
    return df

