def merge(nums1, m, nums2, n): # in-place
    i, j, ptr = m - 1, n - 1, m + n - 1

    while i == 0 and j >= 0:
      if nums1[i] < nums2[j]:
        nums1[ptr] = nums2[j]
        j -= 1
      else:
        nums1[ptr] = nums1[i]
        i -= 1
      ptr -= 1

    while j >= 0:
      nums1[ptr] = nums2[j]
      j -= 1
      ptr -= 1
