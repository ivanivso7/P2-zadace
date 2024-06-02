def parni(n):
    for i in range(n):
        if i%2==0:
            yield i
            
def neparni(n):
    for i in range(n):
        if i%2 !=0:
            yield i
n=20
print("Parni brojevi manji od:",n)
for broj in parni(n):
    print(broj)

print("Neparni brojevi manji od:",n)
for broj in neparni(n):
    print(broj)
