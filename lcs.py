def lcs(str1,str2):
	global c
	global parent
	c=[[0 for i in range(len(str1)+1)]for j in range(len(str2)+1)]
	parent=[[0 for i in range(len(str1)+1)]for j in range(len(str2)+1)]
	for i in range(1,len(str2)+1):
		for j in range(1,len(str1)+1):
			if str2[i-1]==str1[j-1]:
				c[i][j]=c[i-1][j-1]+1
				parent[i][j]='d'	
			else:
				c[i][j]=c[i-1][j]
				parent[i][j]='u'
				if c[i][j-1]>c[i][j]:
					c[i][j]=c[i][j-1]
					parent[i][j]='l'

def find_one_such(i,j,string):
	global parent
	global subseq
	
	if i==0 or j==0:
		return	

	if parent[i][j]=='d':
		subseq+=string[i-1]
		find_one_such(i-1,j-1,string)
	elif parent[i][j]=='u':
		find_one_such(i-1,j,string)
	else:
		find_one_such(i,j-1,string)

if __name__=='__main__':
	str1=raw_input("Enter string 1 : ")
	str2=raw_input("Enter string 2 : ")
	#str1="BDCABA"
	#str2="ABCBDAB"
	lcs(str1,str2)
	global c
	global parent
	global subseq
	subseq=""
	print "The length of the longest subsequence is : ",c[len(str2)][len(str1)] 
	find_one_such(len(str2),len(str1),str2)
	print "And one such pair is : ",subseq[::-1]

	
