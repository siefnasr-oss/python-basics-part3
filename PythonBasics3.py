#--------------------------Continuation Of str Methods--------------------------
# 8-split() rsplit()

x = "I Love Python And C Programming Languages"
print(x.split())

t = "ILovePythonAndCProgrammingLanguages"
print(t.split())

y = "I-Love-Python-And-C-Programming-Languages"
print(y.split("-"))

z = "I-Love-Python-And-C-Programming-Languages"
print(z.split("-",2))

d = "I-Love-Python-And-C-Programming-Languages"
print(d.rsplit("-",2))


# 9-center()

a = "Sief"
print(a.center(9,"@"))


# 10-count()

f = "I Love Python And C Because C Is My First Lang I Learn"
print(f.count("C"))

g = "I Love Python And C Because C Is My First Lang I Learn"
print(g.count("C",0,24))


# 11-swapcase()

h = "I Love Python"
v = "i LOve PYThon"
print(h.swapcase())
print(v.swapcase())


# 12-startswith()

n = "I Love Python"
print(n.startswith("I"))
print(n.startswith("s"))
print(n.startswith("P",7,12))


# 13-endswith()

k = " I Love Python"
print(k.endswith("n"))
print(k.endswith("s"))
print(k.endswith("e",0,6))

# 14-index()

# x = "I Love Python"
# print(x.index("P"))

# y = "I Go To School By Bus"
# print(y.index("o",4,10))

# z = = "I Love Python"
# print(z.index("P",0,4))


# 15-find()

a = "I Love Python"
print(a.find("P"))

b = "I Go To School By Bus"
print(b.find("o",4,10))

q = "I Love Python"
print(q.find("P",0,4))


#16-rjust() , ljust()

k = "Sief"
print(k.rjust(10,"#"))

p = "Sief"
print(p.ljust(10,"#"))


# splitlines()

d = """Fisrt Line
Second Line
Third Line"""
print(d.splitlines())

o = "Fisrt Line \
Second Line \
Third Line"
print(d.splitlines())

l = "Fisrt Line\nSecond Line\nThird Line"
print(l.splitlines())


# 18-expandtabs()

f = "Hello\tWorld\tI\tLove\tPython"
print(f.expandtabs(10))


#-----------------------

one = "I Love Python And 3G"
print(one.istitle())

two = "I Love Python And 3g"
print(two.istitle())

three = " "
print(three.isspace())

four = ""
print(four.isspace())

five = "i love python"
print(five.islower())

six = "I Love Python"
print(six.islower())

seven = "Sief_Nasr"
eight = "SiefNasr100"
nine = "Sief--Nasr100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

w = "AaaaaaBbbbbb"
t = "AaaaaaBbbbbb111"
print(w.isalpha())
print(t.isalpha())

s = "AaaaaaBbbbbb"
j = "AaaaaaBbbbbb111"
print(s.isalnum())
print(j.isalnum())

#19-replace()

x = "Hello One Two Three Four One One One"
print(x.replace("One","1"))
print(x.replace("One","1",1))


#20-join()

y = ["Sief","Nasr","Mohamed"]
print(" ".join(y))
print("-".join(y))
print(type(" ".join(y)))

#------------------------------------------------------------------------------------------------
#-------------------------String Formating------------------------------------
#Old:
name = "Sief"
age = 20
grade = 3.73

print("My Name Is: " + name)
# print("My Name Is: " + name "And My Age Is: " + age) => Type Error

print("My Name Is: %s" %name)
print("My Name Is: %s" %"Sief")

print("Name: %s | Age: %d | Grade: %.2f" %(name,age,grade))

v = "Hello Python"
print("Message is %.5s" %v) # => truncate string



#-------New:
x = "Python"
print("I Love {}".format("Python"))
print("I Love {}".format(x))

name = "Sief"
age = 20
grade = 3.73

print("My Name Is {} , My Age {} Year And My Grade Is {}".format(name,age,grade))
print("Name: {:s} | Age: {:d} | Grade: {:.2f}".format(name,age,grade))

y = "My Fav Subject Is Math"
print("{:.7s}".format(y))

myMoney = 4330277189
print("{:,d}".format(myMoney))

a , b , c = "One" , "Two" , "Three"
print("Hello {1} {2} {0}".format(a,b,c))
print("Hello {} {} {}".format(b,c,a))

Myname = "Sief"
Myage = 20
print("Name: {Myname} | Age: {Myage}")
print(f"Name: {Myname} | Age: {Myage}")
#--------------------------------------------------------------------------------------------
#--------------------Numbers------------------------------------
x = 3+7j
y = 4+2j
print ( x + y )
print (f"Real Part Is: {x.real} | Imaginary Part Is: {x.imag}")

print (100)
print (float(100))
print (complex(100))

print (33.3)
print (int(33.3))
print (complex(33.3))

print(int(3+2j))
#-------------------------------------------------------------------------------------
#-------------------------------Lists---------------------------------------
myList = ["one" , "two" , "one" , 10 , 10.3 , True]
print(myList)
print(myList[0])
print(myList[-1])
print(myList[-3])
print(myList[1:4])
print(myList[::2])

print(myList)
myList[1] = 2
myList[-1] = False
print(myList)

# myList[1:4] = []
print(myList)

myList[0:3] = ["A"]
print(myList)

#----------------Lists Methods-----------------

# 1-append()

myList = ["one" , "two" , "three" , 1 , 2 , 3 , True]
myList.append(False)
print(myList)

myList2 = ["four" , "five"]
myList.append(myList2)
print(myList)

print(myList[8])
print(myList[8][0])

# 2-extend()

a = [1,2,3,4]
b = ["one" , "two" , "three" , "four"]

a.extend(b)
print(a)

# 3-remove()

x = [10,20,30,30,30]
x.remove(30)
print(x)

# 4-sort()

y = [10,3,-2,333,42,321,0,1000]
y.sort()
print(y)
y.sort(reverse=True)
print(y)

n = ["C" , "A" , "B"]
n.sort()
print(n)

# 5-reverse()

c = ["sief" , 10 , 20 ,-10 , 4]
c.reverse()
print(c)

# 6-clear 

u = [1,2,3,4]
u.clear()
print(u)

# 7-copy()

z = [1,2,3,4]
v = z.copy()

print(z)
print(v)

z.append(7)

print(z)
print(v)

# 8-count()

p = [1,2,3,9,8,1,4,11,1]
print(p.count(1))

# 9-index()

o = ["W","A","K","Q","A"]
print(o.index("A"))

# 10-insert()

i = ["A",1,4,2,"S",9]
i.insert(1,"B")
print(i)
i.insert(-1,8)
print(i)

# 11-pop()

k = ["Q","W","E","R"]
print(k.pop(1))
#---------------------------------------------------------------------------------------
