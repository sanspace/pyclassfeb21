numbers = []

for num in range(1,5):
    tmp_list = []
    for anum in range(num):
        tmp_list.append(anum)
    numbers.append(tmp_list)

print(numbers)


nums = [[anum for anum in range(num)] for num in range(1,5)]
print(nums)