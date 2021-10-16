from pandas import DataFrame, Series

def dtypes(df: DataFrame):
    return df.dtypes

def info(df: DataFrame, verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None):
    return df.info(verbose,buf,max_cols,memory_usage,show_counts,null_counts)

def select_dtypes(df: DataFrame, include=None, exclude=None):
    return df.select_dtypes(include,exclude)

def axes(df: DataFrame):
    return df.axes

def ndim(df: DataFrame):
    return df.ndim

def shape(df: DataFrame):
    return df.shape

def memory_usage(df: DataFrame, index=True, deep=False):
    return df.memory_usage(index, deep)

def is_empty(df: DataFrame):
    return df.empty