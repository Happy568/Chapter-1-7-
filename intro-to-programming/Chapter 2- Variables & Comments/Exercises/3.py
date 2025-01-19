# Stripping Names

name = "\tMohammed Osman\n"

print("Unmodified:")
print(repr(name))  

print("\nUsing lstrip():")
print(repr(name.lstrip()))  

print("\nUsing rstrip():")
print(repr(name.rstrip())) 
print("\nUsing strip():")
print(repr(name.strip())) 