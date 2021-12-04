# defaultdict.py
from collections import defaultdict

my_dict = {"a": ["apple"], "b": ["banana", "blueberry"], "c": ["cherry"]}

my_dict = defaultdict(list)

print(my_dict["d"])
