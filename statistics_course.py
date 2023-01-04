# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:17:45 2023

@author: Sua
"""
from collections import Counter
import statistics
import inspect


sample_list = [5 ,10, 9, 10, 9, 8]

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
    variance = statistics.variance(sample_list)
    return variance

def stdev(sample_list):
    stdev = statistics.stdev(sample_list)
    return stdev

print(stdev(sample_list))
print(variance(sample_list))