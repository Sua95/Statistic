
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


w = 'camera'
number = 123
number_float = 12.5
a_list = [1, 2, 3]
mix_list = [1, 'a', 12.5]
a_dictionary = {"a": 1, 'b':2, 'c':3}
a_tuple = (1,2,3)
