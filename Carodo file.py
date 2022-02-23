a = input('Enter number: ')
a = int(a)
if type(a) != int:
    print("Error")
else:
    a = float(a)
b = input('Enter second number')
b = int(b)
if type(b) != int:
    print('Error')
else:
    b = float(b)
print(a + b)
