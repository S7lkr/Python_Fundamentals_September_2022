# strings = input()
# total_sum = 0
# string1, string2 = strings.split(" ")
# if len(string1) < len(string2):
#     shorter = string1
#     longer = string2
# else:
#     shorter = string2
#     longer = string1
# for index in range(len(shorter)):
#     total_sum += ord(shorter[index]) * ord(longer[index])
#
# diff = len(longer) - len(shorter)
# if diff > 0:
#     for ch in longer[-diff:]:
#            total_sum += ord(ch)
# print(total_sum)
