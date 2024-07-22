# def add(a):
#     return a+10
# print(add(100))

#lambda arguments:expression

# add=lambda a:a+10
# print(add(100))

# x = lambda a, b : a * b
# print(x(5, 6))


# list1=[10,20,30,40,50,60,70,80,90,100]
# sq=list(map(lambda x:x**2, list1))
# fil=list(filter(lambda x:x>900, sq))
# print(fil)


from functools import reduce
list1=[10,20,30,40]
sum=reduce(lambda x,y:x+y,list1)
print(sum)