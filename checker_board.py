import random

def display(grid):
	print
	for i in range(grid.__len__()):
		for j in range(grid.__len__()):
			print "\t",grid[i][j],
		print 
	print

def random_grid():
	global grid 
	for i in range(grid.__len__()):
		for j in range(grid.__len__()):
			grid[i][j]=random.randrange(-30,31)
	

def user_grid():	
	global grid
	print "Please Enter the value row by row"
	for i in range(grid.__len__()):
		for j in range(grid.__len__()):
			grid[i][j]=int(raw_input("Please insert : "))
		print "%dth row is done" %(i+1)

def cost_grid():
	global grid
	global cgrid
	global pgrid

	i=0
	for j in range(grid.__len__()):
		cgrid[i][j]=grid[i][j]	
	
	for i in range(1,grid.__len__()):
		for j in range(grid.__len__()):	
			ul,u,ur=j-1,j,j+1		#taking a loop will not help us				
			if ul>=0:
				val=grid[i][j]+cgrid[i-1][ul]
				if val>cgrid[i][j]:
					cgrid[i][j]=val
					pgrid[i][j]='ul'
			
			val=grid[i][j]+cgrid[i-1][u]
			if val>cgrid[i][j]:
				cgrid[i][j]=val
				pgrid[i][j]='u'
			
			if ur<grid.__len__():	
				val=grid[i][j]+cgrid[i-1][ur]
				if val>cgrid[i][j]:
					cgrid[i][j]=val
					pgrid[i][j]='ur'
			
def find_path(i,j):
	global grid,pgrid
	if pgrid[i][j] == 'X':
		print "%d" %grid[i][j]
		return
	else:
		print "%d" %grid[i][j], " >>",
		if pgrid[i][j]=='ul':
			find_path(i-1,j-1)
		elif pgrid[i][j]=='u':
			find_path(i-1,j)
		elif pgrid[i][j]=='ur':
			find_path(i-1,j+1)
		
				
	
if __name__=='__main__':
	
	n=int(raw_input("Enter the grid size : "))
	global grid,cgrid,pgrid
	#grid=[[5,1,8,7],[8,6,2,3],[4,3,9,1],[4,8,2,6]]
	#grid=[[30,-14,-21,-27],[-2,1,8,-17],[27,-19,1,3],[29,-2,-27,-22]]
	#grid=[[8,120,6,5,3],[10,7,60,4,2],[5,11,1,20,6],[1,2,7,100,3],[8,81,80,4,9]]
	grid=[[0 for i in range(n)]for j in range(n)]
	cgrid=[[-99999 for i in range(n)]for j in range(n)]
	pgrid=[['X' for i in range(n)]for j in range(n)]

	dec=raw_input("Do you want to create the grid with random number (Y/N) : ")
	if dec=="Y" or dec=="y":
		random_grid()
	else:
		user_grid()
	
	display(grid)

	cost_grid()
	
	display(cgrid)

	display(pgrid)
	print "Maximum cost you can get is :", max(cgrid[cgrid.__len__()-1])
	print "And one such path is : "
	index=cgrid[cgrid.__len__()-1].index(max(cgrid[cgrid.__len__()-1]))
	find_path(cgrid.__len__()-1,index)
