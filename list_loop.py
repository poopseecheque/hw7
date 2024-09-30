prices = {'milk':80,'water':40, 'banana':90}
mylist = [1, "two", ["nested", 4, 5], prices, "five", "six"]
num_of_strings=0
for i in mylist:
    if type(i)==str:
        num_of_strings+=1
print(num_of_strings)