
#import matplotlib.pyplot as plt
#from collections import Counter


#text = "Con la banca móvil las instituciones financieras incorporaron el uso de la aplicación o app, y con ello ofrecer a sus clientes diversos tipos de operaciones bancarias, utilizando solo su teléfono inteligente, de acuerdo con la Condusef."


#raw_chars = {}
#just_chars = {}
'''
for char in text:
    raw_chars[char.lower()] =  raw_chars.get(char, 0) + 1
    if char.isalpha():
        just_chars[char.lower()] = just_chars.get(char, 0) + 1'''
        

#x, y = zip(*just_chars.items())

#plt.bar(x, y)
#plt.show()


#squares_to_ten = [x**2 for x in range(1,11)]

#raw_count = dict(Counter(text.lower()))

#clean_count = {k:v for k, v in raw_count.items() if k.isalpha()}

numerical_list = [2, 5, 3, 4, 7]

target = 10

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]

def two_sum_hash(nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            print(num_to_index)
            return [num_to_index[target - nums[i]], i]
        num_to_index[nums[i]] = i
    return [-1, -1]

#This solution ask in every iteration if the target minus the current loop i wich is the necesary amount to reach the target
#is on the dictionaty, and then return same index of target minus the curren index and the actual index













































