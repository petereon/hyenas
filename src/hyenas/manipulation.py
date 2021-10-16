from pandas import DataFrame

def cast_as(df: DataFrame, dtype, errors='raise'):
    return df.astype(dtype, True, errors)

def with_column(df: DataFrame, col_name: str, values) -> DataFrame:
    df = df.copy()
    df[col_name] = values
    return df

def with_index(df: DataFrame, col_name: str, values) -> DataFrame:
    df = df.copy()
    df.index = values
    return df

def insert_column(df: DataFrame, col_name: str, values, loc: int = 0):
    df = df.copy()
    df.insert(loc, col_name, values)
    return df