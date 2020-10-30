l=[['Graguation', 'Jntu', 'Hyderabad'], ['Inter', 'Srigayathri', 'Kurnool'],['Mirafra', 'softeare','Bang']]
l1=[]
l2=[]
l3=[]
for x,y,z in l:
    l1.append(x)
    l2.append(y)
    l3.append(z)
print(l1)
print(l2)
print(l3)  

l1=[x for x,y,z in l]
print(l1)

l2=[x for x in range(50)]
print(l2)

l3=[x for x in range(50) if x%2==0]
print(l3)

l4=[15 if x%5==0 else x for x in range(50)]
print(l4)

l5=[x for x in range(1,20) if x%2==0 if x%5==0]
print(l5)

l6=[(x,y) for x in range(1,5) for y in range(1,7)]
print(l6)

l7=[x*x for x in range(1,5)]
print(l7)

l8=[2*x for x in range(1,5)]
print(l8)

l9=[[1,2,3],[4,5,6],[7,8,9]]
op=[x for x,y,z in l9]
print(op)







