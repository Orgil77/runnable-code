#CSCI3104
#Orgil Sugar
#Spring 2018

import random
#Defining a table object where I can 
#store the costs of the subproblems
class table(object):
	def __init__(self, x, y):
		#give a specific same value to every position
		#in order to know if it's solved or not afterwards.
		self.table = []
		i = 0
		j = 0
		while(i < x):
			j = 0
			row = []
			while(j < y):
				row.append(0)
				j+=1
			self.table.append(row)
			i+=1
	#Row size of the table
	def __rowSize__(self):
		return len(self.table[0]) 
	#Column size of the table
	def __colSize__(self):
		return len(self.table)
	#inserting a value to a table
	def __setv__(self,row,col,value):
		self.table[row][col] = value
	#getting a value from a table
	def __getv__(self,row,col):
		return self.table[row][col]

def optimal(s, i, j, x, y):
	#When the optimal is not sub then
	if((s.__getv__(i,j) - s.__getv__(i-1,j-1)) < 12):
		cheapests = []
		if(s.__getv__(i,j) == s.__getv__(i-1,j-1)):
			cheapest = min(s.__getv__(i-1,j) , s.__getv__(i,j-1) , s.__getv__(i,j))
			if(s.__getv__(i-1,j) == cheapest):
				cheapests.append("Delete " + x[i-1] + " from x")
			if(s.__getv__(i,j-1) == cheapest):
				cheapests.append("Insert " + y[j-1] + " into x" )
			if(s.__getv__(i-1,j-1) == cheapest):
				cheapests.append("no-op")
		else:
			cheapest = min(s.__getv__(i-1,j),s.__getv__(i,j-1))
			if(s.__getv__(i-1,j) == cheapest):
				cheapests.append("Delete " + x[i-1] + " from x")
			if(s.__getv__(i,j-1) == cheapest):
				cheapests.append("Insert " + y[j-1] + " into y")
		if(len(cheapests) == 0):
			return "no-op"
		else:
			randomindex = random.randint(0,len(cheapests)-1)
			return cheapests[randomindex]
    #otherwise doing sub
	else:
		return "Sub " + x[i-1] + " with " + y[j-1]

#aligning strings x and y
def alignStrings(x,y):
	s = table(len(x) + 1,len(y) + 1)
	#Initialize the first column and rows 
	#as base case
	i = 1
	while(i < s.__rowSize__()):
		s.__setv__(0,i,i)
		i+=1
	i = 1
	while (i < s.__colSize__()):
		s.__setv__(i,0,i)
		i+=1
	#Now we're going through all substrings 
	#using optimal to find the minimum cost 
	#to align the 2 master stringse
	i = 1
	j = 1
	while (i < s.__colSize__()):
		j=1
		while(j<s.__rowSize__()):
			if(x[i-1] == y[j-1]):
				#if the 2 characters doesn't require a operation
				#where they are same then set the value same as the minimum
				#of surrounding operations except swap which is always maximum
				s.__setv__(i,j,min(s.__getv__(i-1,j),s.__getv__(i,j-1),s.__getv__(i-1,j-1)))
			else:
				#somewhere where swap operation is possible consider
				#choosing swap 
				if(i>=2 and j>=2): 
					s.__setv__(i,j, min(s.__getv__(i-2,j-2) + 37, 
								    s.__getv__(i-1,j) + 1,
								    s.__getv__(i,j-1) + 1,
								    s.__getv__(i-1,j-1) + 12))
				#now for the positions where swap is not possible
				#where it'll throw a index error
				else:
					s.__setv__(i,j, min(s.__getv__(i-1,j) + 1,
								   s.__getv__(i,j-1) + 1,
								   s.__getv__(i-1,j-1)+12,))
			j+=1
		i+=1
	return s

def extractAlignments(s,x,y):
	a = []
	i = len(x)
	j = len(y)
	#using insert operation where we doesn't have to care about
	#the indexing of the optimal sequence.
	#insert will add next operation to the start of the sequence
	#we are starting from the back of the table
	while(i>0 or j>0):
		a.insert(0,optimal(s,i,j,x,y))
		#If the operation is insert then go back along with j
		if(a[0][:6] == "Insert"):
			j-=1
		#If the operation is delete then go back along with i
		elif(a[0][:6] == "Delete"):
			i-=1
		#If it's neither one of them then go back along with both
		#indexes. Where recursively you can get sub or swap.
		else:
			i -= 1
			j -= 1
	return a
def commonSubstrings(x, L, a):
	substrings = []
	substring  = ""
	i = 0
	for operation in a:
		#Compare that operation with some operation symbol except
		#no-op because we're trying to find the common substrings
		#using no-op.
		if(operation[:7] != "Insert "):
			#same character in both is common one
			if(operation == "no-op"):
				substring += x[i]
				i+=1
			else:
				if(len(substring) >= L):
					substrings.append(substring)
				substring=""
				i+=1
		else:
			if(len(substring) >= L):
				substrings.append(substring)
			substring = ""
	#Not trying to lose end points
	if(substring != ""):
		substrings.append(substring)
	return substrings

f1 = open("csci3104_PS7_data_string_x.txt", "r")
f2 = open("csci3104_PS7_data_string_y.txt", "r")
f1lines = f1.readlines()
f2lines = f2.readlines()
x = "".join(f1lines)
y = "".join(f2lines)
s = alignStrings(x,y)
a = extractAlignments(s,x,y)
c = commonSubstrings(x,9,a)
print c






	