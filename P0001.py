#method 1, programical
sum=0
count=0
n=100
for i  in range(1,n):
	if (i % 3)==0 or (i% 5)==0:
		count=count+1
		sum=sum+i
		print (i)
	
print("sum: %d",sum)
print("count: %d", count)

# method 2: mathmatical
# sum of  nth number
def subsum(n,m):
	cnt=(int)((n-1)/m)
	sum=m*(cnt*(cnt+1))/2
	return sum
	
print (n, subsum(n,3)+subsum(n,5)-subsum(n,15))
