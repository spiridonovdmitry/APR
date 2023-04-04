# def pairwise(arr, n):
#   ans = 0
#   dict1 = {}
#   for i in range(0, len(arr)):
#     x = n - arr[i]
#     print(x, arr[i], dict1.get(x))
#     if (dict1.get(x) and dict1.get(x) != -1):
#         dict1[x] = -1
#         ans += dict1.get(x) + i
#     else:
#         dict1[arr[i]] = i
#   return ans






def pairwise(arr, n):
  ans = 0 
  used = [0] * len(arr)
  for i in range(0, len(arr)):
    if(used[i] == 1):
        continue
    x = n - arr[i]
    for j in range(i + 1, len(arr)):
        if(arr[j] == x and used[j] == 0):
            used[j] = 1
            used[i] = 1
            ans += i + j
            break
  return ans

print(pairwise([5, 25, 9, 10, 23, 2, 2, 9, 7, 14, 6, 0, 17, 13, 12, 9, 24, 13, 9, 0, 3, 8],16))