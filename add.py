# def add (a,b):
#     if type(a) in (int,float) and type(b) in (int,float):
#     # if type(a) in [int] and type(b) in [int]:
#         return a+b
# c=add('vinesh','kumar')
# # # a=add('vinesh',12)
# b=add(10,20)
# # # a=add(True,False)
# d=add(12,12.4)
# # print(add(12,12))
# print(d)
# print(c)
# print(b)
import csv
file_name = input()
to_csv = [
    {'name': 'bob', 'age': 25, 'weight': 200},
    {'name': 'jim', 'age': 31, 'weight': 180},
    {'name': 'vinesh', 'age': 25, 'weight': 60},
]

keys = to_csv[0].keys()

with open(file_name+'.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)