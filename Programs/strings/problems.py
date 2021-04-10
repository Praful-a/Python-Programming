# Calculate lenght of the string
# string = "Python"
# count = 0
# for i in string:
#     count += 1
# print(count)

# count the frequency of each character in string
# def count_freq(str):
#     dict = {}
#     for n in str:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(count_freq("geeksforgeeks"))

def count_freq(str):
    count = 0
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] != str[j]:
                count = 1
            else:
                count += 1
    print("{} : {}".format(str[i], count))
count_freq("geeksforgeeks")
