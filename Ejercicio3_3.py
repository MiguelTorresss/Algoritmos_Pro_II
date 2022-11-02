
Arreglo1 = ((1,1)(1,2)(1,3)(1,4))
print ("El resultado del arreglo seria" , Arreglo1)

Arreglo2 = ((2,1)(2,2)(2,3)(2,4))
SumatoriaA = (Arreglo1,Arreglo2)

Arreglo3 = ((3,1)(3,2)(3,3)(3,4), SumatoriaA)
SumatoriaB = (SumatoriaA,Arreglo3)

Arreglo4 = ((4,1)(4,2)(4,3)(4,4))
SumatoriaC = (SumatoriaB,Arreglo4)
print ("El resultado de Arreglos es", SumatoriaC)