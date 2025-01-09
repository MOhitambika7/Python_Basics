#Modifying lists.
#          ----> append()
#          ----> extend()
#          ----> insert()

Nums = [1, 2, 3]
Nums.append(5)
print(f"Added element is:- {Nums}")

Nums.extend([4, 8])
print(f"The extended elements:- {Nums}")

Nums.insert(1,2) #Index 1st ma 2 lai store garney.
print(Nums)