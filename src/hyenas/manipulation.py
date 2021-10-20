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
    df.insert(loc=loc, column=col_name, value=values)
    return df

def set_flags(df: DataFrame, allows_duplicate_labels=None):
    return df.set_flags(copy=True, allows_duplicate_labels=allows_duplicate_labels)

def as_type(df: DataFrame, dtype, errors='raise'):
    return df.astype(dtype, copy=True,  errors=errors)

def convert_dtypes(df: DataFrame, infer_objects=True, convert_string=True, convert_integer=True, convert_boolean=True, convert_floating=True):
    df = df.copy()
    df.convert_dtypes(infer_objects=infer_objects, convert_string=convert_string)

def infer_objects(df: DataFrame):
    df = df.copy()
    return df.infer_objects()

def copy_df(df: DataFrame, deep=True):
    return df.copy(deep=True)