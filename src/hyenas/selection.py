from typing import Dict, List
from pandas import DataFrame, Series

config: Dict = {
    "aggregation_default_first": False
}

def index(df: DataFrame) -> Series:
    return df.index.copy()

def columns(df: DataFrame) -> List:
    return df.columns

def group(df: DataFrame = None, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True):
    if df != None:
        df = df.copy()
        return df.groupby(by=by, axis=axis, level=level, as_index=as_index, sort=sort, group_keys=group_keys, observed=observed, dropna=dropna)
    else:
        return {'by':by, 'axis':axis, 'level':level, 'as_index':as_index, 'sort':sort, 'group_keys':group_keys, 'observed':observed, 'dropna':dropna}

def aggregate(df: DataFrame, func=None, axis=0, *args, **kwargs):
    df.aggregate(func=func, axis=axis, *args, **kwargs)

def __construct_aggregated_cols(cols):
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
    return aggregated_cols

def select(from_df: DataFrame, cols: List, group_by = []):
    from_df = from_df.copy()
    if isinstance(group_by,list):
        if len(group_by) > 0:
            aggregated_cols = __construct_aggregated_cols(cols)
            return from_df.groupby(by=group_by).agg(aggregated_cols)
        else:
            return from_df[list(cols)]
    elif isinstance(group_by,dict):
        group_by_args = group_by
        print(group_by_args)
        aggregated_cols = __construct_aggregated_cols(cols)
        return from_df.groupby(**group_by_args).agg(aggregated_cols)





# def alias(col, as_name: str = None):
     
def sum_agg(col_name: str):
    return {col_name:('sum')}

def mean_agg(col_name: str):
    return {col_name:('mean')}

def count_agg(col_name: str):
    return {col_name:('count')}

def first_agg(col_name: str):
    return {col_name:('first')}