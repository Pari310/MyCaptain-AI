# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Perform set operations
union_set = E.union(N)
intersection_set = E.intersection(N)
difference_set = E.difference(N)
symmetric_difference_set = E.symmetric_difference(N)

# Print the results
print(f"Union of E and N is {union_set}")
print(f"Intersection of E and N is {intersection_set}")
print(f"Difference of E and N is {difference_set}")
print(f"Symmetric difference of E and N is {symmetric_difference_set}")
