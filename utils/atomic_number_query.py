class query:
    def query_atomic_number( atomic_number = 0):
        atomic_query_range = range(1,119)
        if atomic_number not in atomic_query_range:
            print("Chem: Atomic number is not within the atomic query range!")
            exit(1)
            
            
