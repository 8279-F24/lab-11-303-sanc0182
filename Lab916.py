# LAB 9.16
# Roberto Sanchez
# 041144901

numbers = [int(i) for i in input().split()]
negative_numbers = sorted([i for i in numbers if (i < 0)], reverse=True)
for neg in negative_numbers:
    print(neg, end=' ')


