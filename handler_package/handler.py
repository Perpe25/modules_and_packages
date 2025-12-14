from abc import ABC, abstractmethod
import json
import csv
from typing import Any, Dict, List
import os


class Filehanding(ABC):
    def __init__(self, file_path: str):
        self._file_path = file_path

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, newfilepath: str) -> None:
        self._file_path = newfilepath

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class JsonHandler(Filehanding):

    def read(self) -> Any:
        if not os.path.exists(self._file_path):
            raise FileNotFoundError(f"File not found: {self._file_path}")

        with open(self._file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def write(self, data: Any) -> None:
        try:
            with open(self._file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except TypeError as e:
            raise TypeError(f"Was not able to write JSON data: {e}")


class CsvHandler(Filehanding):

    def read(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self._file_path):
            raise FileNotFoundError(f"File not found: {self._file_path}")

        with open(self._file_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def write(self, data: List[Dict[str, Any]]) -> None:
        if not isinstance(data, list):
            raise TypeError("CsvHandler expects a list of dictionaries")

        if len(data) == 0:
            raise ValueError("You passed an empty list")

        with open(self._file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()

            for row in data:
                if not isinstance(row, dict):
                    raise TypeError("Each row must be a dictionary")
                writer.writerow(row)  # ✅ FIXED
