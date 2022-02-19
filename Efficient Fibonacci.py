d={}
def FAT(n:int):
    if (n==1 or n==0):
        return n
    elif n in d.keys():
        return d[n]
    return FAT(n-1)+FAT(n-2)
a=int(input())
for i in range(a+1):
	d[i]=FAT(i)
	print(d[i])
	