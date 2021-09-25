from chemispy.perodic_table_json_parser import *
elements = return_element_order()
class query:
    def list_types():
        return elements
    def query_atomic_number( atomic_number = 1):
        if not 1 < atomic_number < elements +1:
                print("Chem: Atomic number is not within the atomic query range!")
        else:
            return elements[atomic_number-1]
            
            
