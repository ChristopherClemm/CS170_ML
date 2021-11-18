import csv

curr_set = set()

data = {0,1,2,3,4}

for i in range(len(data)):
    print("on level ", i, " of the search tree")
    feature_to_add_this_level = 0
    best_acc_so_far = 0
    for j in range(len(data)):
        if j not in curr_set:
            print("considering adding ", j," feature" )
            feature_to_add_this_level = j

    curr_set.add(feature_to_add_this_level)
    print(curr_set)
    print("On level ", i , " i added feature ", feature_to_add_this_level, " to the current set")
