import json
from pathlib import *

with open("chemispy\periodic_table.json", "r", encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)
        jsonData = data
        def return_element_order() -> list:
            order_of_elements=[]
            for x in jsonData["order"]:
                order_of_elements.append(x)
            return order_of_elements