
#this is the place where we measure acuray
import copy
import numpy as np
import math
import numpy as np
import time

def leave_one_out_cross_validation(data, curr_set, feature_to_add):
    correct_class = 0
    temp_set = curr_set.copy()
    temp_set.add(feature_to_add)
    tempNP = np.array(data)
    #print("shape of old = ", tempNP.shape)
    temp_list = []
    temp_list.append(tempNP[:,0])
    #print("temp list = ", temp_list)
    s = time.time()
    for i in temp_set:
        temp_list.append(tempNP[:,i])
    dataNP = np.array(temp_list)
    e = time.time()
    #print("AAAAAAAAA = ", e - s)
    #print(dataNP.shape)
    #time.sleep(1)
    #print(dataNP)
    #print(type(dataNP))
    count = 0
    #print(dataNP.shape[1])
    start1 = time.time()
    """for i in range(1, dataNP.shape[1]):
        #print(i)
        if i not in temp_set :
            dataNP[:,i] = 0
    """
    #print(dataNP)
    for i in range(dataNP.shape[1]):
        label_object_to_classify = dataNP[0,i]
        object_to_classify = dataNP[1:,i]
        #print("label = ",label_object_to_classify)
        #time.sleep(1)
        #print(i)
        nn_dist = float('inf')
        nn_loc = float('inf')
        for j in range(dataNP.shape[1]):
            if j != i:
                #print("object_to_classify = ", object_to_classify)
                #print("dataNP = ", dataNP[1:,j], " shape = ",dataNP[1:,j].shape)
                #time.sleep(1)
                #distance = math.sqrt(np.sum(np.power((np.subtract(object_to_classify, dataNP[1:,j])),2)))
                #print("i = ", i, " j = " , j, " dist = ", distance)
                #distance = (np.subtract(object_to_classify, dataNP[1:,j]))
                #print(distance.shape)
                #time.sleep(100)
                distance = 1
                sum = 0
                #for i in distance:
                    #sum += i
                #print("distance = ",distance)
                if distance < nn_dist:
                    nn_dist = distance
                    nn_loc = j
                    nn_label = dataNP[0,j]
        if label_object_to_classify == nn_label:
            correct_class +=1
    end1 = time.time()
    print("The run time was: ", end1-start1)
    return correct_class/dataNP.shape[1]
    #print("her2")
    """
    start2 = time.time()
    for i in range(len(data)):
        object_to_classify = data[i][1:]
        label_object_to_classify = data[i][0]
        nn_dist = float('inf')
        nn_loc = float('inf')
        for j in range(len(data)):
            count += 1
            if j != i:
                sum = 0
                for k in temp_set:
                    count +=1
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
    #print("here")
    end2 = time.time()
    print("The run time was: ", end2-start2)

    return correct_class/len(data)

    return 0
    """
