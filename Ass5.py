lists=[1,3,5,7,9,10,8,6,4,2]
print("sum is: ",sum(lists))
print("largest is: ",max(lists))
print("smallest is: ",min(lists))
lists.sort()
print("Ascending: ",lists)
lists.sort(reverse=True)
print("Descending is: ",lists)
t=tuple(lists)
print("Tuple: ",t)
del lists
print(lists)#not defined as lists is deleted