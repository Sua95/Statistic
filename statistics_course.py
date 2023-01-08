# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:17:45 2023

@author: Sua
"""
from collections import Counter


#group_1 = [5 ,10, 9, 10, 9, 8]
#group_2 = [6, 9, 10, 10, 9, 7]

sqrft = [650, 785, 1200, 720, 975]
price = [772000, 998000, 1200000, 800000, 895000]

def mean(sample_list):
    mean = sum(sample_list) / len(sample_list)
    return mean
    

def median(sample_list):
    sorted_list = sorted(sample_list)
    len_sample = len(sorted_list)
    mid_number = len_sample // 2
    return sorted_list[mid_number]

def mode(sample_list):
    sorted_list = Counter(sorted(sample_list))
    mode = sorted_list.most_common(1)
    return mode

def sample_variance(sample_list):
    dp_minus_mean = []
    mean = sum(sample_list)/len(sample_list)
    for i in sample_list:
        dp_minus_mean.append((i-mean)**2)
    divided_num_samples = sum(dp_minus_mean)/(len(sample_list)-1)
    return divided_num_samples

def population_variance(sample_list):
    dp_minus_mean = []
    mean = sum(sample_list)/len(sample_list)
    for i in sample_list:
        dp_minus_mean.append((i-mean)**2)
    divided_num_samples = sum(dp_minus_mean)/len(sample_list)
    return divided_num_samples
    
def sample_stdev(sample_list):
    dp_minus_mean = []
    mean = sum(sample_list)/len(sample_list)
    for i in sample_list:
        dp_minus_mean.append((i-mean)**2)
    divided_num_samples = sum(dp_minus_mean)/(len(sample_list)-1)
    result_sqrt = divided_num_samples ** 0.5
    return result_sqrt

def population_stdev(sample_list):
    dp_minus_mean = []
    mean = sum(sample_list)/len(sample_list)
    for i in sample_list:
        dp_minus_mean.append((i-mean)**2)
    divided_num_samples = sum(dp_minus_mean)/len(sample_list)
    result_sqrt = divided_num_samples ** 0.5
    return result_sqrt

def sample_covariance(x, y):
    x_mean, y_mean = sum(x)/len(x), sum(y)/len(y)
    array_x = []
    array_y = []
    mult_array = []
    for i in x:
        array_x.append(i-x_mean)
    for i in y:
        array_y.append(i-y_mean)
    for i in range(len(array_x)):
        mult_array.append(array_x[i]*array_y[i]) 
    result = sum(mult_array) / (len(mult_array)-1)
    return result

def population_covariance(x, y):
    x_mean, y_mean = sum(x)/len(x), sum(y)/len(y)
    array_x = []
    array_y = []
    mult_array = []
    for i in x:
        array_x.append(i-x_mean)
    for i in y:
        array_y.append(i-y_mean)
    for i in range(len(array_x)):
        mult_array.append(array_x[i]*array_y[i]) 
    result = sum(mult_array) / len(mult_array)
    return result

def correlation_coefficient(covariance, stdev, data_1, data_2):
    cov = sample_covariance(data_1, data_2)
    stdev_x, stdev_y = sample_stdev(data_1), sample_stdev(data_2)
    result = cov / (stdev_x * stdev_y)
    return round(result, 3)
    

def z_score(data, mean, stdev):
    array_minus_mean = []
    zscore = []
    data_stdev = stdev(data)
    data_mean = mean(data)
    for i in data:
        array_minus_mean.append(i-data_mean)
    for i in array_minus_mean:
        zscore.append(i / data_stdev)
    return zscore
        
    
        
    
    
print(z_score(price, mean, sample_stdev))







    