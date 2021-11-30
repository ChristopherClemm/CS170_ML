import sys
import pandas as pd
import accuracy
import math
small = "Ver_2_CS170_Fall_2021_LARGE_data__27.txt"
curr_set = set()
#print("hi")
data = []
with open(small) as myfile:
    for line in myfile:
        temp = line.split()
        map_obj = map(float, temp)
        temp2 = list(map_obj)
        data.append(temp2)
"""
acc = accuracy.leave_one_out_cross_validation(data, {26, 27},31)
print(acc)
"""

print(data[0])
data2 = {0,1,2,3,4}
best_overall = [0, set()]
print(len(data[0]))
for i in range(1, len(data[0])):
    print("on level ", i, " of the search tree")
    feature_to_add_this_level = 0
    best_acc_so_far = 0
    for j in range(1, len(data[0])):
        if j not in curr_set:
            print("considering adding ", j," feature" )
            acc = accuracy.leave_one_out_cross_validation(data, curr_set, j)
            if acc > best_acc_so_far:
                best_acc_so_far = acc
                feature_to_add_this_level = j
            #feature_to_add_this_level = j
    print("accuracy = ", best_acc_so_far)
    curr_set.add(feature_to_add_this_level)
    print(curr_set)
    if (best_overall[0] < best_acc_so_far):
        best_overall[1] = curr_set.copy()
        best_overall[0] = best_acc_so_far
    print("On level ", i , " i added feature ", feature_to_add_this_level, " to the current set")

print("\nThe best set found was " , best_overall[1], " with an accuracy of ", best_overall[0])
