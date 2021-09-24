import chemispy.utils
import chemispy.elements
from chemispy.utils.atomic_number_query import atomic_number_query, query

atomic_number_query.elements.append("ATOMIC_11")

print(query.query_atomic_number(120))