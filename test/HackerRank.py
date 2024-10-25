# def plusMinus(arr):
#     # Write your code here
#     pos = 0
#     neg = 0 
#     zero = 0
#     for i in range(n):
#         if n > 0:
#             pos+=1
#         elif n > 0:
#             neg+=1
#         else:
#             zero+=1
#     return (n/pos, n/neg, n/zero)

# n = int(input().strip())
# arr = list(map(int, input().strip().split()))
# result = diagonalDifference(arr)
# print(result)


arr= [1,2,3,4,5]
d=3
for i in range(len(arr)):
        if arr[d]==arr[i]:
            arr.insert(0,arr[d])
print(arr)