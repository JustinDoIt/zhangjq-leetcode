
def removeDuplicates(nums): # return `ptr` / index / (int)
        ptr = 1

        for index in range(1, len(nums)):
            if nums[index] != nums[ptr - 1]:
                nums[ptr] = nums[index]
                ptr += 1
        return ptr
