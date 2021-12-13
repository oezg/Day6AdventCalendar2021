from collections import Counter


def spawn(ctr):
    ctr_after = {}
    for i in range(9):
        if i == 6:
            ctr_after[i] = ctr.get(0, 0) + ctr.get(i + 1, 0)
        elif i == 8:
            ctr_after[i] = ctr.get(0, 0)
        else:
            ctr_after[i] = ctr.get(i + 1, 0)
    return ctr_after


with open("input_day6.txt") as inp:
    nums = inp.read()

nums = [int(num) for num in nums.strip().split(",")]
fish_counter = Counter(nums)
fish_counter = dict(fish_counter)
for _ in range(256):
    fish_counter = spawn(fish_counter)

print(sum(fish_counter.values()))