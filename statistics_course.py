# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:17:45 2023

@author: Sua
"""
from collections import Counter


sample_list = [5 ,10, 9, 10, 9, 8, 10, 5, 7, 6, 9, 7, 8, 8, 8, 7]
dictionary_list = {'arrow' : 1, 'sword': 2, 'shield' : 3}

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
    
def variance(sample_list):
    mean = sum(sample_list) / len(sample_list)
    squared_differences = [(x - mean)**2 for x in sample_list]
    variance = sum(squared_differences) / len(sample_list)
    return variance
    
def stdev(sample_list):
    mean = sum(sample_list) / len(sample_list)
    squared_differences = [(x - mean)**2 for x in sample_list]
    variance = sum(squared_differences) / len(sample_list)
    stdev = variance // 2
    return stdev
        
    
    
print(variance(sample_list))    
print(stdev(sample_list))