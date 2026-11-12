def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False
print(first_last6([1,3,5,6,7]))


def same_first_last(nums):
    if len(nums) > 0 and nums[0] == nums[-1]:
        return True
    return False
print(same_first_last([1,2,5,1]))


def make_pi():
  return [3,1,4]
print(make_pi())


def common_end(a, b):
    return len(a) > 0 and len(b) > 0 and (a[0] == b[0] or a[-1] == b[-1])
print(common_end([1,2,3,4,5],[3,4,5,6]))



def sum3(nums):
  son = 0
  for x in nums:
    son = son + x
  return son
print(sum3([1,2,3,5]))


def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]
print(rotate_left3([4,6,8]))


def reverse3(nums):
  return [nums[2],nums[1],nums[0]]
print(reverse3([2,6,9]))


def max_end3(nums):
  katta = max(nums[0],nums[-1])
  return [katta,katta,katta]
print(max_end3([5,1,9]))


def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]
print(sum2([2,6,4,9]))



def middle_way(a, b):
  return [a[1],b[1]]
print(middle_way([2,3,8],[5,8,3]))



def make_ends(nums):
  return [nums[0],nums[-1]]
print(make_ends([5,8,4,6,3,1,9]))


def has23(nums):
    return 2 in nums or 3 in nums
print(has23([5,5]))