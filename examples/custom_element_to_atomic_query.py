from chemispy.utils.atomic_number_query import atomic_number_query, query  # <---- Essential Imports

atomic_number_query.elements.append("ATOMIC_11")   # <----  Appends to list of elements

print(query.query_atomic_number(119))   # <---- Prints the element based on its index in the list


############################
####        NOTE        ####
############################

# -> The elements are automatically listed index atomic numerical order
