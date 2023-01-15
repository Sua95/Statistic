
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


alphabet = {1: 'a', 2:'b', 3:'c'}
changes = 1
encript_alph = {}


list_alph = [k for k, v in alphabet.items()]
list_nums = [v for k, v in alphabet.items()]

encript_alph[1] = 'b'

print(encript_alph)