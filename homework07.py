immutable_var = 7, 9, True,  "string"
print(immutable_var)
#immutable_var [0] = [9]
#print(immutable_var) как мы знаем кортеж нельзя изменит.
mutable_list = ([9,5, True , 'string',])
mutable_list[3] = 'Healer'
print(mutable_list)