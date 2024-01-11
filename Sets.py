# Sets Program in python . 
s1 = {1,2,3,4,2,3,4}
print(s1)

s2 = {'faiyan',324 ,False ,6.6,77,2}   # No garentee of Order .
print(s2)

Aman = set()
print(type(Aman))

# Set Methods in python .
set1 = {1,2,3,4,6,7,8,9}
set2 = {10,11,12,13,14,15,16,17,18,19}
print(set1.union(set2))

cities = {"Delhi","Rajasthan","Maharashtra"}
cities2 = {"Bihar","Uttarpradesh","chattisgarh"}
cities3 = cities.union(cities2)
print(cities3)

cities = {"Delhi","Rajasthan","Maharashtra"}
cities2 = {"Delhi","Uttarpradesh","chattisgarh"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Delhi","Rajasthan","Maharashtra"}
cities2 = {"Delhi","Uttarpradesh","chattisgarh"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Delhi","Rajasthan","Maharashtra"}
cities2 = {"Delhi","Uttarpradesh","chattisgarh"}
print(cities.isdisjoint(cities2))
