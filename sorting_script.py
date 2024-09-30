a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

#flow to output sorted values
if a>b:
    x=a
    a=b
    b=x #we sorted for be to be before a
if a>c:
    n=a
    a=c
    c=n
if b>c:
    m=b
    b=c
    c=m
print(a,' ',b,' ', c)