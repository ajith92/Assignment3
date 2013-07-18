import sys

def show(a):
	for i in range(1,a.__len__()-1):
		print a[i],"\n"

def matrix_chain_order(i,j):
	global kfrom
	if i==j:
		print "A%d" %i,
	else:
		print "(",
		matrix_chain_order(i,kfrom[i][j]),
		print ".",
		matrix_chain_order(kfrom[i][j]+1,j),
		print ")", 
		 
def matrix_chain_cost(dim):
	n=dim.__len__()
	global c,kfrom
	c=[[0 for j in range(n)] for i in range(n)]
	kfrom=[[0 for j in range(n)] for i in range(n)]
	for m in range(2,n):
		for i in range(1,n-m+1):
			j=i+m-1
			c[i][j]=999999999
			for k in range(i,j):
				val=c[i][k]+c[k+1][j]+dim[i-1]*dim[k]*dim[j]
				if val<c[i][j]:
					c[i][j]=val
					kfrom[i][j]=k
	#show(c)
	#show(kfrom)

if __name__=='__main__':
	#################### User input ###################
	n=int(raw_input("Enter a number of matrix : "))
	dim=[]
	for i in range(n):
		print "Enter the dimensions of matrix %d" %(i+1)
		if i==0:
			dim.append(int(raw_input()))
			dim.append(int(raw_input()))
		else:
			temp=int(raw_input())
			if temp==dim[dim.__len__()-1]:
				dim.append(int(raw_input()))	
			else:
				print "Incompatible dimension"
				print "Program Exits"
				sys.exit(0)
	global c,kfrom			
	matrix_chain_cost(dim)	
	print "Minimum Cost of this chain multiplication is :", c[1][n]
	print "And Such order is : "
	matrix_chain_order(1,n)	
