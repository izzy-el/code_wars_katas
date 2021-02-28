# def sum_pairs(ints, s):
#     arr = []
#     arr.append(ints[0])

#     for i in range(1, len(ints)):
#         for i in range(1, len(ints)):
#             arr.append(ints[i])
#             for j in range(len(arr)):
#                 if(arr[j] + ints[i] == s and j != i):
#                     return ([arr[j], arr[i]])

# def sum_pairs(_list, _sum):
#     sorted_list = sorted(_list)
#     left = 0
#     right = len(_list) - 1

#     while left < right:
#         if sorted_list[left] + sorted_list[right] > _sum:
#             right -= 1
#         elif sorted_list[left] + sorted_list[right] < _sum:
#             left += 1
#         elif sorted_list[left] + sorted_list[right] == _sum:
#             if sorted_list[left] == sorted_list[right]:
#                 return [sorted_list[left], sorted_list[left]]
#             elif _list.index(sorted_list[left]) < _list.index(sorted_list[right]):
#                 return [sorted_list[left], sorted_list[right]]
#             else:
#                 return [sorted_list[right], sorted_list[left]]

#     return None

def sum_pairs(_list, _sum):
    s = set()

    for i in range(len(_list)):
        diff = _sum - _list[i]
        if diff in s:
            return [diff, _list[i]]

        s.add(_list[i])
    
    return None
        

# def testing(ints, s):
#     # arr = []
#     # arr.append(ints[0])
#     # print(arr)
#     value = []
#     for index in range(1, len(ints)):
#         arr.append(index)
#         value = [arr for i in range(1, len(ints)) for i in range(1, len(ints)) for j in range(len(arr)) if(arr[j] + arr[i] == s and j != i)]

    #return [[ints[i], ints[j]] for i in range(0, len(ints)) for i in range(0, len(ints)) for j in range(len(ints)) if(ints[j] + ints[i] == s and j != i)]

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs(l1, 8)) #== [1, 7], 
print(sum_pairs(l2, -6)) #== [0, -6]
print(sum_pairs(l3, -7)) #== None
print(sum_pairs(l4, 2)) #== [1, 1]
print(sum_pairs(l5, 10)) #== [3, 7]
print(sum_pairs(l6, 8)) #== [4, 4]
print(sum_pairs(l7, 0)) #== [0, 0]
print(sum_pairs(l8, 10)) #== [13, -3]
