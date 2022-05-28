
"""""
my_dict = {1: 'one', 2:'two', 3:'three'}

my_dict['d'] = "four"

print(my_dict[2])

print(my_dict.get(3))


country_captal = {"Estonia": "Tallinn", "Lithuania": "Vilnus", "Latvia": "Riga", "Belarus":"Minsk"}

print(country_captal)
print(country_captal["Estonia"])
"""
phonebook = {"Emergency": 112, "KFC": 9999, "SEB": 6209999, "SWEDBANK": 6999999, "Emotional helpline": 6558088, "Peeter": 54541010}

user_input = str(input("What service do you need? "))


#for key in phonebook:
#    print(key)

if user_input in phonebook:
    print(f'Dialing: {phonebook[user_input]}')
else:
    print(f"We dont offer service called: {user_input}")


"""
#print(list(phonebook.items()))
#print(list(phonebook.keys()))

x = set()
print(type(x))

y = {1, 2, 3, 4, 5}
"""

