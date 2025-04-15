a = 12
b = 10
GREATER_MESSAGE = "a is greater than b"
LESSER_MESSAGE = "a is less than b"

if a > b:
    print(GREATER_MESSAGE)
    
if (a > b):
    print(GREATER_MESSAGE)
else:
    print(LESSER_MESSAGE)

if a > b:
    print(GREATER_MESSAGE)
elif a == b:
    print("a is equal to b")
else:
    print(LESSER_MESSAGE)
