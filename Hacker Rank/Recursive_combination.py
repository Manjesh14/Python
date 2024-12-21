
# RECURSIVE COMBINATION

def find_combinations(nums, target):
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        elif remaining < 0:
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path, remaining - nums[i])
            path.pop()

    nums.sort() 
    result = []
    backtrack(0, [], target)
    return result
size = int(input())
nums = list(map(int, input().split()))
target = int(input())
output = find_combinations(nums, target)
print(output)