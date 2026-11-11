# print("Hello world")


# n = int(input("Son kiriting: "))
# natija = 1
# for i in range(1, n + 1):
#     natija = natija * i
# print(f"{n}! = {natija}")



# parol = input("Parol kiriting: ")

# xatolar = []

# if len(parol) < 8:
#     xatolar.append("kamida 8 belgi bo'lishi kerak")

# raqam_bor = False
# katta_bor = False

# for belgi in parol:
#     if belgi.isdigit():
#         raqam_bor = True
#     if belgi.isupper():
#         katta_bor = True

# if not raqam_bor:
#     xatolar.append("kamida 1 ta raqam bo'lishi kerak")
# if not katta_bor:
#     xatolar.append("kamida 1 ta katta harf bo'lishi kerak")

# if len(xatolar) == 0:
#     print("Parol yaxshi!")
# else:
#     print("Parol zaif. Sabablari:")
#     for xato in xatolar:
#         print("-", xato)





# sonlar = [1, 2, 9, 3]
# print(sonlar[0])        # 1  (birinchi element)
# print(len(sonlar))      # 4  (nechta element)
# for s in sonlar:        # har bir elementni aylanish
#     print(s)

# def string_times(str, n):
#     return str * n

# print(string_times("Ha", 10500000))


# def kvadrat(n):
#     return n * n
# print(kvadrat(6))

# def yosh_hisobla(tugilgan_yil):
#     return 2026 - tugilgan_yil
# print(yosh_hisobla(1998))

# def juftmi(n):
#     if n % 2 == 0:
#       return True
#     else: return False
# print(juftmi(288))


def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+ 1] == 2 and nums[i + 2] == 3 :
            return True
    return False