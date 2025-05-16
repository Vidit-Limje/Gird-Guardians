def preprocess_data(df):
    # Dummy preprocessing: assumes last column is target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    return X, y 