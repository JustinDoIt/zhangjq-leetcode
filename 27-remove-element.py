def removeElement(nums, val):
  ptr = 0

  for index in range(len(nums)):
    if nums[index] != val:
      nums[ptr] = nums[index]
      ptr += 1
  return ptr
