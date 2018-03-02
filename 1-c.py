def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start][0]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left][0] <= pivot:
            left = left + 1
        while myList[right][0] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def scanning(l):
  low = l[0][0]
  up = l[0][1]
  add=[]
  i = 1
  
  while(i<len(l)):
    if(l[i][0] > low and l[i][1] < up):

      if(l[i][0] > low):
        low = l[i][0]
      if(l[i][1] < up):
        up = l[i][1]
    elif(l[i][0] > up):
      add.append(up)
      low = l[i][0]
      up = l[i][1]

    i+=1
  add.append(up)
  return add
l=[[3,51],[6,60],[6,99],[105,155],[121,178],[86,186]]
l=quicksort(l,0,len(l)-1)
print "Displaying ad in these moments: "
print scanning(l)



  




	