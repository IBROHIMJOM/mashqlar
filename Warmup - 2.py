def string_times(str, n):
  return str * n
print(string_times("hi",5))


def front_times(str, n):
  front = str[:3]
  return front * n
print(front_times("hello", 10))


def string_bits(str):
  return str[::2]
print(string_bits("assalom"))


def string_splosion(str):
  s = ""
  for i in range(len(str)):
    s = s + str[:i+1]
  return s  
print(string_splosion("ibrohim"))

def last2(str):
    oxirgi = str[-2:]
    return sum(1 for i in range(len(str) - 2) if str[i:i+2] == oxirgi)
print(last2("salom"))


def array_count9(nums):
  son = 0
  for x in nums:
    if x == 9:
      son = son + 1
  return son
print(array_count9([10, 9, 34, 9, 125]))


def array_front9(nums):
  for x in nums[:4]:
    if x == 9:
     return True
  return False
print(array_front9([1, 2, 9, 3, 4]))


def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
     return True
  return False 
print(array123([1, 1, 2, 4, 1]))


def string_match(a, b):
  son = 0
  kichik = min(len(a),len(b))
  for i in range(kichik - 1):
    if a[i:i+2] == b[i:i+2]:
      son = son + 1
  return son    
print(string_match('xxcaazz', 'xxbaaz'))


