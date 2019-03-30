"""
Merge Names
"""

def unique_names(names1, names2):
    
    unique_names = list(set().union(names1, names2))
    # YOUR CODE GOES HERE
# A python set is a dictionary that contains only keys (and no values). And dictionary keys are, by definition, 
# unique. Hence, duplicate items are weeded out automatically. 
# Once you have the set, you can easily convert it back into a list. As easy as that!

    return unique_names

names1 = ["Ava", "Emma", "Olivia"]

names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))

# should print Ava, Emma, Olivia, Sophia