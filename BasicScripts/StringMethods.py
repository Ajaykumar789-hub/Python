name="ajay"
name1=name.upper()
print(name1)
print(name1.index('A')) #to get index of char
print(name1.index('A',2)) # we can pass start and end position in index
print(name1.replace('A','j')) #to replace a with j
name2="    Ajay,kumar"
print(name2.split(',')) #it will split string into parts and retun as list
print(name2.strip()) #it will trim strings
print(name2.lstrip())