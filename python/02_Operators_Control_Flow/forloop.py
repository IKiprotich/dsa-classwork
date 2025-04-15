def get_data():
#using range
    for i in range (10):
        print(i)


get_data()

#using list
def get_data():
    my_list = [1, 2, 3, 4, 5]
    for i in my_list:
        print(i)
get_data()
#using tuple    
def get_data():
    my_tuple = (1, 2, 3, 4, 5)
    for i in my_tuple:
        print(i)
get_data()
#using set
def get_data():
    my_set = {1, 2, 3, 4, 5}
    for i in my_set:
        print(i)
get_data()
#using dictionary
def get_data():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key in my_dict:
        print(key, my_dict[key])
get_data()
#using string
def get_data():
    my_string = "Hello"
    for i in my_string:
        print(i)
get_data()