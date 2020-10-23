num = int(input())
ans = ''
nums_list = [1000, 500, 100, 50, 10, 5, 1]
symbol_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
target_nums = []
index = 1
while num > 0:
    target_nums.append((num % 10)*(10 ** (index - 1)))
    num = num // 10
    index += 1


def add_roman(target: int):
    roman_str = ''
    if target == 9:
        return 'IX'
    elif target == 90:
        return 'XC'
    elif target == 900:
        return 'CM'

    for index, num in enumerate(nums_list):
        add_str = ''
        count = 0

        while (target - num) >= 0:
            add_str = add_str + symbol_dict[num]
            target -= num
            count += 1

        if count == 4:
            add_str = ''
            add_str = symbol_dict[num] + symbol_dict[nums_list[index - 1]]

        roman_str += add_str
    return roman_str


for target in reversed(target_nums):
    print(target)
    ans += add_roman(target)


print(ans)
