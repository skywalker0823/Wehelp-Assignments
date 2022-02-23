# # WeHelp Bootcamp
# # Assignment - Week 2 - 更多解法

from cerberus import Validator
from flask import jsonify
# #Task 1
# #迴圈計算min~max總合
# def calculate(min,max):
#     total=0
#     for num in range(min,max+1):
#         total+=num
#     print(total)
# calculate(1,3)
# calculate(4,8)


# # #Task 2
# # #計算人員平均薪資並考慮可能異動狀況
# def avg(data):
#     emp=data["count"]
#     total=0
#     for salary in data["employees"]:
#         total+=salary["salary"]
#     result=total/emp
#     print(result)
# avg({
#     "count":3,
#     "employees":[
#         {
#             "name":"John",
#             "salary":30000
#         },
#         {
#             "name":"Bob",
#             "salary":60000
#         },
#         {
#             "name":"Jenny",
#             "salary":50000
#         }
#     ]
# })


# # #Task 3
# # #最大兩數之相乘 
# def maxProduct(nums):
#     neo=nums[0]
#     for number in nums:
#         if number>neo:
#             neo=number
#     nums.remove(neo)
#     neo2=nums[0]
#     for number2 in nums:
#         if number2>neo2:
#             neo2=number2
#     print(neo*neo2)
# # 請用你的程式補完這個函式的區塊
# maxProduct([5, 20, 2, 6]) # 得到 120
# maxProduct([10, -20, 0, 3]) # 得到 30
# maxProduct([-1, 2]) # 得到 -2
# maxProduct([-1, 0, 2]) # 得到 0
# maxProduct([-1,-2,0]) #得到 2(錯誤)

# def maxProduct(nums):
#     init=nums[0]*nums[1]
#     for neo in range(len(nums)-1):
#         for neo2 in range(neo+1,len(nums)):
#             if nums[neo]*nums[neo2]>init:
#                 init=nums[neo]*nums[neo2]
#     print(init)
# # 請用你的程式補完這個函式的區塊
# maxProduct([5, 20, 2, 6]) # 得到 120
# maxProduct([10, -20, 0, 3]) # 得到 30
# maxProduct([-1, 2]) # 得到 -2
# maxProduct([-1, 0, 2]) # 得到 0
# maxProduct([-1,-2,0]) #得到 2


# #Task 4
# # 給予一組陣列，湊出兩個不同數字相加可以等於給予的目標數字，顯示其列表中位置
# def twoSum(nums, target):
#     for num in range(len(nums)-1):#長度4-1=3=0~3
#         for num2 in range(num+1,len(nums)):#第一個~底(4)之前一個=1~3
#             if nums[num]+nums[num2]==target:
#                 return [num,num2]
# result=twoSum([2, 11, 7, 15], 9)
# print(result) # show [0, 2] because nums[0]+nums[2] is 9


# #Optional Task 5
# # 找最長的0 並計算長度
# def maxZeros(nums):
#     record=0
#     best=0
#     for num in nums:
#         if num==0:
#             best+=1
#             if best>record:
#                 record=best
#         elif num==1:
#             if best>record:
#                 record=best
#                 best=0
#             else:
#                 best=0     
#     print(record)

# maxZeros([0, 1, 0, 0]) # 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
# maxZeros([1, 1, 1, 1, 1]) # 得到 0
# maxZeros([0, 0, 0, 1, 1]) # 得到 3

# print("test")
# def maxProduct(nums):
#     # 請用你的程式補完這個函式的區塊
#     temp = nums[0]*nums[1]
#     # data=nums[1]-nums[0]
#     for i in range(len(nums)):
        
#         # print("M[i]:",M[i])
#         for j in range(i+1,len(nums)):
#             # print("j:",j)
#             sum=nums[i]*nums[j]
#             if sum>=temp:
#                 temp=sum
#     print("MAX:",max(temp,sum))
        
# maxProduct([5, 20, 2, 6]) # 得到 120
# maxProduct([10, -20, 0, 3]) # 得到 30
# maxProduct([-1, 2]) # 得到 -2
# def yes(a):
#     if a==1:
#         return "yes"
#     return "no"

# print(yes(1))        

# schemaa={"name":{'type':'string'}}
# v=Validator(schemaa)
# data=jsonify({"name":"XD"})

# checker=v.validate(data)

# print(checker)
import requests
url = 'https://www.google.com/'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
print(response.text)