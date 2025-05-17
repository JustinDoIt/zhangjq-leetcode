def twoSum(nums, tgt):
  seen = dict()

  for index, num in enumerate(nums):
    diff = tgt - num # why not `num - tgt`
    if diff in seen:
      return [seen[diff], index]
    # 3, Update `seen`
    seen[num] = index
  return []
