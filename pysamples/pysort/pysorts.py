#!/usr/bin/env python3


def selectSort(items):
    """
     O(n²)
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。
    """
    for i in range(len(items)-1):
        for j in range(i+1, len(items)):
            if items[j] < items[i]:
                items[i], items[j] = items[j], items[i]
    return items


if __name__ == "__main__":
    print(selectSort([3, 2, 5, 7, 1]))
