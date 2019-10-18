import time
import sys
sys.path.append('../binary_search_tree')
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Original method is O(n²). for each name in the first list of 10,000 names, the loop will run max 10,000 times
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

names_2_bst = BinarySearchTree(names_2[0])
for num, name in enumerate(names_2, start=1):
    if num > 0:
        names_2_bst.insert(name)

for name in names_1:
    if names_2_bst.contains(name):
        duplicates.append(name)

# this version is  O(n) complexity. will increase constantly with the size of the list of names
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# print(duplicates)
# print(names_2_bst.in_order_print())