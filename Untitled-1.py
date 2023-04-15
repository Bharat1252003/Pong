for i in range(10):
	globals()[f"x{i}"] = i


print( globals().values() )
print(x1)
print(x2)

dict1 = {}

for i in range(10):
	key = str("x" + str(i))
	dict1[key] = i+10
print(dict1)

for key,value in dict1.items():
	exec(f'{key} = {value}')

print(x1)
print(x2)