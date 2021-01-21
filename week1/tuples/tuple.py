from collections import defaultdict

# variableName = defaultdict(argument/aka=default_factory)

# This is a tuple of tuples. Change this into a dictionary of key values. The value will be an array of the values for the same key
#  expected output: {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]}


# Python program to demonstrate 
# defaultdict 
  
   
  
  
# Function to return a default 
# values for keys that is not 
# present 
# def def_value(): 
#     return "Not Present"
      
# # Defining the dict 
# d = defaultdict(def_value) 
# d["a"] = 1
# d["b"] = 2
  
# print(d["a"]) 
# print(d["b"]) 
# print(d["c"]) 


# Defining a dict 
# d = defaultdict(list) 
  
# for i in range(5): 
#     d[i].append(i) 
      
# print("Dictionary with values as list:") 
# print(d) 

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

d = defaultdict(list)

for a, b in classes:
    d[a].append(b)

print(d)