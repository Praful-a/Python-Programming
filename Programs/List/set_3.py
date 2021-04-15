"""Get the frequency of the elements in a list."""
"""First Method"""
# def get_freq(li):
#     freq = {}
#     count = 0
#     for i in li:
#         if i not in freq:
#             freq[i] = 1
#         else:
#             freq[i] += 1
#     return freq
#
# lst = [10, 1, 1, 2, 3, 100, 200, 200]
# print(get_freq(lst))
"""Second Method"""
# def countFreq(arr, n):
#     # Mark all array elements as not visited
#     visited = [False for i in range(n)]
#     # Traverse through array elements
#     # and count frequencies
#     for i in range(n):
#         # Skip this element if already
#         # processed
#         if (visited[i] == True):
#             continue
#         # Count frequency
#         count = 1
#         for j in range(i + 1, n, 1):
#             if (arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)
#
# # Driver Code
# if __name__ == '__main__':
#     arr = [10, 1, 1, 2, 3, 100, 200, 200]
#     n = len(arr)
#     countFreq(arr, n)

visited = [False for i in range(5)]
print(visited)
