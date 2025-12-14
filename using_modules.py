
# csv, json,  math, random, re datetime, os, sys, typing 
import re
from datetime import datetime, date, time
import os
import sys
from typing import List, Dict, Tuple

text = "I am a python  programmer,  and am *@ "
search = re.findall(r"\d+", text)
# if search:
#     print("Positive")
# # print(datetime)
# os.chdir("sample_package1")
# print(os.removedirs())
# print(sys.modules)

def add(x: int) -> int:
       return x + 2 

print(add(2))