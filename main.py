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
    # ACM 模式：一次性读入全部数据，避免 input() 在大数据下超时
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    target = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    res = twoSum(nums, target)
    # 若题目要求下标从 1 开始，改为 str(x + 1)
    sys.stdout.write(' '.join(map(str, res)))

if __name__ == '__main__':
    main()
