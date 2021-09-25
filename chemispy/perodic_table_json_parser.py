import json
from pathlib import *

table_file=open("chemispy\periodic_table.json", "r", encoding='utf-8')
table_contents=table_file.read()
print(table_contents)