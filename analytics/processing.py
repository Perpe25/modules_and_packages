import pandas as pd
from typing import Callable, Optional

class Dataloader:
    def __init__(self, source:str):
        self._source = source

    @property
    def source(self) -> str:
        return self._source
    
    def loader(self) -> pd.DataFrame:
        if self._source.lower().endswith(".csv"):
            return pd.read_csv(self._source)
        elif self._source.lower().endswith(".json"):
            return pd.read_json(self._source)
        else:
            raise ValueError("Unsupported file format")

class Filter:
    def __init__(self, fn: Callable[[pd.DataFrame], pd.Series]):
        self._fn = fn

    def apply(self, df:pd.DataFrame) -> pd.DataFrame:
        mask = self._fn(df)
        return df[mask]
    
class Cleaner:
    def __init__(self, df: Optional[pd.DataFrame] = None):
        self._df = df
    
    def set_df(self,df:pd.DataFrame) -> 'Cleaner':
        self._df = df
        return self
    
    def drop_null_rows(Self) -> 'Cleaner':
        Self._df = Self._df.dropna()
        return Self
    
    def fill_null(self, value) -> 'Cleaner':
        self._df = self._df.fillna(value)
        return self
    
    def convert_types (self, dtypes: dict) -> 'Cleaner':
        self._df = self._df.astype(dtypes)
        return self
    
    def get_df(self) -> 'Cleaner':
        return self._df


