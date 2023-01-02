# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:17:45 2023

@author: Sua
"""

sample_list = [15, 5]

def mean(sample_list):
    sum_of_sample = 0
    len_sample = len(sample_list)
    for i in sample_list:
        sum_of_sample += i
    return sum_of_sample/len_sample
    


print(mean(sample_list))
        