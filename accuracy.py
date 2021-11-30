
#this is the place where we measure acuray
import copy
import numpy as np
import math
import numpy as np

def leave_one_out_cross_validation(data, curr_set, feature_to_add):
    correct_class = 0
    temp_set = curr_set.copy()
    temp_set.add(feature_to_add)
    #print(temp_set)
    #print(len(data))
    count = 0
    for i in range(len(data)):
        object_to_classify = data[i][1:]
        label_object_to_classify = data[i][0]
        nn_dist = float('inf')
        nn_loc = float('inf')
        for j in range(len(data)):
            if j != i:
                sum = 0
                for k in temp_set:
                #    print("k = " , k)
                    sub_exp = (object_to_classify[k-1] - data[j][k])**2
                #    print("sub exp = ", sub_exp)
                    sum += sub_exp
                #    print(object_to_classify)
                #    print(object_to_classify[k])
                #    print("data ", data[j])
                #    print("data " , data[j][k+1])

                dist = math.sqrt(sum)
                #print("sum = ", sum)
                #print("dist = ", dist)
                #return 1
                if dist < nn_dist:
                #    print("dist = ",  dist)
                #    print("old dist = ",  nn_dist)
                    nn_dist = dist
                    nn_loc = j
                    nn_label = data[j][0]
                #print("\n\n\n\n\n")
        count +=1
        if label_object_to_classify == nn_label:
            correct_class += 1
    #print(count)
    return correct_class/len(data)
