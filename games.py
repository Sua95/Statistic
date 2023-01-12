
import matplotlib.pyplot as plt
from collections import Counter


text = "Con la banca móvil las instituciones financieras incorporaron el uso de la aplicación o app, y con ello ofrecer a sus clientes diversos tipos de operaciones bancarias, utilizando solo su teléfono inteligente, de acuerdo con la Condusef."


raw_chars = {}
just_chars = {}
for char in text:
    raw_chars[char.lower()] =  raw_chars.get(char, 0) + 1
    if char.isalpha():
        just_chars[char.lower()] = just_chars.get(char, 0) + 1
        

x, y = zip(*just_chars.items())

#plt.bar(x, y)
#plt.show()


squares_to_ten = [x**2 for x in range(1,11)]

raw_count = dict(Counter(text.lower()))

clean_count = {k:v for k, v in raw_count.items() if k.isalpha()}


f = open("new_text.txt", "w")


f.write("New lines ")
f.write("New lines ")
f.write("New lines ")
f.write("New lines ")
f.close()


d = open("new_text.txt", "r")

print(d.read())
d.close()