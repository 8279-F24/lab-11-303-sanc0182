# LAB 9.17
# Roberto Sanchez
# 041144901

contact_list = [str(i) for i in input().split()]
name = input()
for contact in contact_list:
    if name in contact:
        print(contact.split(',')[1])
