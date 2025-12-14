from typing import List, Optional
import pandas as pd
import matplotlib.pyplot as plt

class Grouper:
    def __init__(self, df: pd.DataFrame):
        self._df = df

    
    def group_and_agg(self, by:List[str], agg:dict) -> pd.DataFrame:
        return self._df.groupby(by).agg(agg).reset_index()
    
class Merger:
    def __init__(self, left:pd.DataFrame, right:pd.DataFrame):
        self._left = left
        self._right = right
    
    def merge(self, on:List[str], how: str = 'inner') -> pd.DataFrame:
        return pd.merge(self._left, self._right, on=on, how=how)
    
class Plotter:
    def __init__(self, df:pd.DataFrame):
        self._df = df
    
    def plot(self, x:str, y:str, kind: str = 'line', title: Optional[str] = None) -> None:
        ax = self._df.plot( x=x, y=y, kind=kind)
        if title:
            ax.set_title(title)
        plt.show()