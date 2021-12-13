import numpy as np


def spawn(school):
    hatchlings = np.full_like(np.where(school == 0), 8)
    school[school == 0] = 7
    school -= 1
    return np.append(school, hatchlings)


with open("input_day6.txt") as inp:
    nums = inp.read()
nums = [int(num) for num in nums.strip().split(",")]
nums = np.array(nums)

part1 = 80
part2= 256 # too slow with this algorithm

for _ in range(part1):
    nums = spawn(nums)
    
print(len(nums))