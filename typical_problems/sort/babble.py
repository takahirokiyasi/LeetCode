from typing import List
from random import sample


def babble_sort(n_list: List[int]):
    for i in range(len(n_list)):
        for j in reversed(range(i+1, len(n_list))):
            if n_list[j - 1] > n_list[j]:
                n_list[j - 1], n_list[j] = n_list[j], n_list[j - 1]
    return n_list


if __name__ == "__main__":
    arr = list(range(10))
    src = sample(arr, len(arr))

    print(src)
    # [7, 2, 5, 3, 1, 6, 9, 4, 8, 0]

    dst = babble_sort(src)
    print(dst)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
