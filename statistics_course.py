# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:17:45 2023

@author: Sua
"""
from collections import Counter


sample_list = [15, 10, 5, 45, 30, 30, 75]

def mean(sample_list):
    sum_of_sample = 0
    len_sample = len(sample_list)
    for i in sample_list:
        sum_of_sample += i
    return sum_of_sample/len_sample
    

def median(sample_list):
    sorted_list = sorted(sample_list)
    len_sample = len(sorted_list)
    mid_number = len_sample // 2
    return sorted_list[mid_number]

def mode(sample_list):
    sorted_list = Counter(sorted(sample_list))
    mode = sorted_list.most_common(1)
    return mode