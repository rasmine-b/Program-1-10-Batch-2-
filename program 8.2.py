# Create a program that print all the odd numbers starting from 0 to 100

odd_num_list = []
for i in range (0,101):
    if i % 2 != 0:
        odd_num_list.append(i)
print(odd_num_list)