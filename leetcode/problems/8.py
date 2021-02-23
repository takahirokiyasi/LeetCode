class Solution:
    def myAtoi(self, string):
        list1 = []
        hasSpace = False
        for _ in range(0, len(string)):
            if hasSpace and string[_].isdigit() == False:
                break
            elif string[_] != ' ' or string[_] == '-' or string[_] == '+' or string[_].isdigit():
                hasSpace = True
                list1.append(string[_])
        try:
            if int(''.join(list1)) > (2 ** 31) - 1 or int(''.join(list1)) < (2 ** 31) * -1:
                if list1[0] == '-':
                    return (2 ** 31) * -1
                else:
                    return (2 ** 31) - 1
        except ValueError:
            return 0
        return int(''.join(list1))
