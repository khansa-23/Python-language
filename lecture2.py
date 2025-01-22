#in this we use the assigninig of multiple variables 
x,y,z="orange", "apple","cherry"
print(x)
print(y)
print(z)

#now we see how to output the variable in a single line or by using the comma separator and also by using the addition operator

x="Python"
y="is a "
z="good language"
print(x,y,z)

#mow we do the  same by using the addition   operator
x="Python"
y="is a "
z="good language"
print(x+y+z)

#now we perform our work by using the global variables
x="awesome"

def myfunc():
    print("Python is "+ x)

myfunc()

