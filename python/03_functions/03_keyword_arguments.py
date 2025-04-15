def print_details(**kwargs):
    """
    This function takes any number of keyword arguments and prints them.
    """
    print(kwargs)

print_details(course="ICS", year=2.1, unit="DSA")  

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
