import random  #######################################
                                 # МЕТОДЫ!!!!

#9.141
# someString = 'hello4wor5ld6'
# string = someString.isdigit()
# num = ''
#
# for c in someString:
#     if c.isdigit():
#         num += c
#
# print('цифры в строке: ' + num)




#161
# someString = 'сколько дней в году'
# x = someString.lower().split()
#
# result = []
# for a in x:
#     for c in a:
#         if someString.count(c) == a.count(a):
#             result.append(c)
#
# print(result)

#9.166
# someString = 'я шел по дороге'.split()
# someString[0], someString[-1] = someString[-1], someString[0]
#
# print(someString)



# 9.113

# someString = 'hellco wocrlcd'.replace('c', '')
# print(someString)

#9.82

# someString = input('')
# result = someString[: someString.index(' ')].count('o')
# print(result)

#9.62

# someString = input('')
# result = someString.count('a') / len(someString) - someString.count(' ') * 100
# print(result)


# 9.72

# someString = input()
# result = someString.count(' ') + 1 > 3
# print(result)

#9.75
#
# someString = input()
# result = someString[: someString.index(',')]
# print(result)

# анаграмма
#
# someString1 = input()
# someString2 = input()
#
# result = len(someString2) == len(someString1)
#
# if result:
#     len1 = len(someString1)
#     index = 0
#     while index < len1:
#         if someString1.count(someString1[index]) != someString2.count(someString1[index]):
#             result = False
#             print(result)
#             break
#         index += 1
#
#     print(result)
#
# else:
#     print(result)


#############

someString = '123456787'
number = 9

summa = 7