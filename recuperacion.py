#1

print "Primero:"
items =[[12,23,34,56],[10,23,34,33],[11,23,22,34,44],[11,23,34,66]]
print map(lambda x: [x[0],x[len(x)-1]],items)

#2

print "\nSegundo:"
lista=[2224,4321,6666,123]
print map(lambda k: k[1],filter(lambda o: o[0]==True,zip(map(lambda z: (z==[]),map(lambda x: filter(lambda x: x%2!=0,map(lambda x: int(x),(list(filter(lambda x: x!="[" or x!="]",str(x)))))),lista)),lista)))

#3

print "\nTercero:"
items =[[12,23,34,56],[10,23,34,33],[11,23,34,44],[11,23,34,66]]
print map(lambda x: max(x),items)

#4

print "\nCuarto:"
#print map(lambda k: map(lambda k: k[1],filter(lambda o: o[0]==True,zip(map(lambda z: (z==[]),map(lambda x: filter(lambda x: x%2!=0,map(lambda x: int(x),(list(filter(lambda x: x!="[" or x!="]",str(x)))))),k)),k))),items)
#z =map(lambda b: b,filter(lambda i: i!=[],map(lambda k: map(lambda k: k[1],filter(lambda o: o[0]==True,zip(map(lambda z: (z==[]),map(lambda x: filter(lambda x: x%2!=0,map(lambda x: int(x),(list(filter(lambda x: x!="[" or x!="]",str(x)))))),k)),k))),items)))
#print z
print "No"
#print map(lambda x: min(x),z)

#5

print "\nQuinto:"
lista5=[3,32,15,600,242,243,90,122,47]#3^5=243
print "numeros menores a",lista5[0]**5
print filter (lambda x: x<lista5[0]**5,lista5)

#6
print "\nSexto:"
        
class tupla:
    def __init__(self, valorx, valory):
        self.valorx = valorx
        self.valory = valory

tuplas=[tupla(6,3), tupla(15,5), tupla(234,7), tupla(21,6)]

print reduce(lambda x,y: x+y, map(lambda y: y.valorx,filter(lambda u: u.valorx==u.valory*(u.valory+1)/2,tuplas)))
