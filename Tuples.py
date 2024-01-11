# Tuples programs in python .
tuple1 = (1,3,55,7,9)
print(type(tuple1))
print(tuple1[0])
print(tuple1[2])
print(tuple1[3])
print(tuple1[-4])

tuple2 = tuple1[0:4]
print(tuple2) 

# Operation on Tuple in python .
countries = ( "spain", "Italy", "India", "England", "Germany" )
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

countries = ("pakistan", "Afghanistan", "Bangladesh" ,"ShriLanka")
countries2 = ("Bhutan", "China", "Maldevis")
SouthAsia = countries + countries2
print(SouthAsia)

tuple1 = (0,1,2,3,4,5,0,1,2,3,4,5,1,2,3,4)
res =  tuple1.count(2)
print('count of 2 in tuples is:' , res)

