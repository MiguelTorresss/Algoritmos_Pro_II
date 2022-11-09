

a= input("Ingrese el primer valor:") 
b= input("Ingrese el segundo valor:") 
c= input("Ingrese el tercer valor:")
d= input("Ingrese el cuarto valor:")

a= int (a)
b= int (b)
c= int (c)
d= int (d)


print (a+b)
print (b-c)
print (c*d)
print (b/a)

print ("Tabla de la verdad de AND") 
print (str(a==a) + " AND " + str (d==d) + " --> " + str (b==b))
print (str(b==b) + " AND " + str (a>a)  + " --> " + str (c==d))
print (str(c==a) + " AND " + str (c==c) + " --> " + str (b==a))
print (str(a>a)  + " AND " + str  (d>d) + " --> " + str (d==a))


print ("Tabla de la verdad de OR") 
print (str(a==a) + " OR " + str (c==c) + " --> " + str (b==b))
print (str(b==b) + " OR " + str (d>d)  + " --> " + str (b==b))
print (str(d==c) + " OR " + str (c==c) + " --> " + str (a==a))
print (str(a>a)  + " OR " + str  (c>c) + " --> " + str (c==d))


print ("Tabla de la verdad de THEN")
print (str(a==a) + " THEN " +  str (a==a)  +  " --> " + str (a==a))
print (str(b==b) + " THEN " +  str (b==c)  +  " --> " + str (b==c))
print (str(c<c)  + " THEN " +  str (c==c)  +  " --> " + str (d==d))
print (str(d==a) + " THEN " +  str (c==a)  +  " --> " + str (a==a))