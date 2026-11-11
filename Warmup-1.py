# def sleep_in(weekday, vacation):
#     if not weekday or vacation:
#         return True
#     else:
#         return False



def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False




def sum_double(a, b):
  if (a == b):
   return (a + b) * 2
  return (a + b)



def diff21(n):
 if n <= 21:
  return 21 - n
 else:
  return (n - 21) * 2




def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    return False





def makes10(a, b):
  if (a==10 or b==10 or a + b==10):
    return True
  return False




def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200 - n) <= 10




def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)



def not_string(str):
  if len(str) >= 3 and str[:3] == 'not':
    return str
  return 'not ' + str  




def missing_char(str, n):
  return str[:n] + str[n+1:]




def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1] + str[1:-1] +str[0]  




def front3(str):
  front = str[:3]
  return front * 3