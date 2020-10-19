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

    dst = babble_sort(src)
    print(dst)
