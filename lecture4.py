#now here we introduce the how to show the strings  in  python 
#we represent the strings by using  either the single quotes or the double quotes

#strings with single quotes
x="I am the  student of  Fast university"
print(x)

#strings with double quotes
x='I am  the student of AI'
print(x)

#now we see how to slice  the string
x="I am the student of Fastt university"
print(x[2:10])

#now we modify the string
x="Hello , world"  #now the string is convert into the upper case
print(x.upper())


z="Hello ,, world"
print(z.lower()) #in this we shift all the letters  towards the lower letters

y="  Hello, world  "
print(y.strip()) #in this we remove the  whitespaces  from the  start and from the end

#now we  study the string formating
age=23
txt=f"My name is john,I  am {age}"
print(txt)




