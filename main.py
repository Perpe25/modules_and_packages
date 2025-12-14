import os
import pandas as pd

from analytics import Grouper, Merger, Filter, Dataloader, Cleaner, Plotter
from handler_package import Filehanding, CsvHandler, JsonHandler

def file_hander(folder: str):
    os.makedirs(folder, exist_ok=True)

    json_path = os.path.join(folder, "new.json")
    data1 = [{"id":1, "categorycl": "A", "value": 10},
             {"id":2, "category": "B", "value": 20},
             {"id":3, "category": "A", "value": 30}
             ]
    jh = JsonHandler(json_path)
    jh.write(data1)

    csv_path = os.path.join(folder, "new.csv")
    data2 = [
             {"id":1, "category": "A", "value": 10},
             {"id":2, "category": "B", "value": 20},
             {"id":3, "category": "A", "value": 30}
             ]
    jh = CsvHandler(csv_path)
    jh.write(data2)

    return json_path, csv_path

def process_data(json_path:str, csv_path:str):
    loader = Dataloader(json_path)
    df = loader.loader()
    print(df)

    loader2 = Dataloader(csv_path)
    df2 = loader2.loader()
    print(df2)

    grouping = Grouper(df)
    grouped = grouping.group_and_agg(by=["category"], agg={"value": "mean"})
    print(grouped)

    merger = Merger(df, df2)
    merged = merger.merge(on=["id"], how="left")
    print(merged)
    new_merged =merged.rename(columns={"category_x":"category",
                                       "value_x":"value"      
                                       }).drop(columns=["category_y", "value_y"])
    try: 
        plotter = Plotter(new_merged)
        plotter.plot(x="category", y="id", kind="bar", title="Category")
    except Exception as e:
        print("failed to plot", e)

if __name__ == "__main__":
    folder = os.path.join(os.getcwd(), "data_files") 
    json_path, csv_path = file_hander(folder)
    process_data(json_path, csv_path)

    # new branch added

    # Am in new branch 2 