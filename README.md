<p align="center" >
    <img src="https://raw.githubusercontent.com/TechPenguineer/chem.py/main/public/logo.png" width="300px">
    <h1 align="center">Chemistry in python</h1>
</p>


# Resources Used
*The following items are not made by me! Click the words to go to the original source*<br><br>

**[Periodic Tab Json](https://github.com/Bowserinator/Periodic-Table-JSON/blob/master/PeriodicTableJSON.json)**  -> Used in -> **[periodic_table.json](periodic_table.json)**
# Installation
```bat
pip install chemispy
```

# Usage

```py
from chemispy import *
```

### Atomic Number Query

```python
query.query_atomic_number(1)
```
*Return's the name of the element corresponding to the atomic number*

### Elements List

```python
print(query.list_types())
```
*Returns a list of all elements (Used mostly for debugging)*

### Custom Elements
```python
from chemispy.utils.atomic_number_query import atomic_number_query

atomic_number_query.elements.append("ELEMENT_119")
```