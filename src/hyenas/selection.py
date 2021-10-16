from typing import Dict, List
from pandas import DataFrame, Series

config: Dict = {
    "aggregation_default_first": False
}

def index(df: DataFrame) -> Series:
    return df.index.copy()

def columns(df: DataFrame) -> List:
    return df.columns

def select(from_df: DataFrame, cols: List, group_by: List = []):
    if len(group_by) > 0:
        aggregated_cols: Dict = {}
        for col in cols:
            if isinstance(col, str):
                if not config['aggregation_default_first']:
                    raise Exception(
                        '''You need to provide an explicit (first_agg "{}") if a group_by is given.
                        \nTo disable this functionality set "aggregation_default_first" to True in selection config
                        '''.format(col))
                else:
                    aggregated_cols.update({col:('first')})
            else:
                aggregated_cols.update(col)
        return from_df.groupby(by=group_by).agg(aggregated_cols)
    else:
        return from_df[list(cols)].copy()


# def alias(col, as_name: str = None):
     
def sum_agg(col_name: str):
    return {col_name:('sum')}

def mean_agg(col_name: str):
    return {col_name:('mean')}

def count_agg(col_name: str):
    return {col_name:('count')}

def first_agg(col_name: str):
    return {col_name:('first')}

def group_by(df: DataFrame, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, dropna=True):
    df.groupby(by=by, axis=axis, level=level, as_index=as_index, sort=sort, group_keys=group_keys, squeeze=squeeze, observed=observed, dropna=dropna)

def aggregate(df: DataFrame, func=None, axis=0, *args, **kwargs):
    df.aggregate(func=func, axis=axis, *args, **kwargs)