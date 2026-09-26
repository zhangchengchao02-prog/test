import sys


def twoSum(nums, target):
    """返回和为 target 的两个数的下标（0-based），无解返回 []。时间 O(n)，空间 O(n)。"""
    seen = {}
    for i, v in enumerate(nums):
        need = target - v
        if need in seen:
            return [seen[need], i]
        seen[v] = i
    return []


def main():

    print("qhy")

if __name__ == '__main__':
    main()

