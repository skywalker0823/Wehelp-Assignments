# WeHelp Bootcamp
# Assignment - Week 2

#Task 1
#迴圈計算min~max總合
def calculate(min,max):
    total=0
    for num in range(min,max+1):
        total+=num
    print(total)
calculate(1,3)
calculate(4,8)


# #Task 2
# #計算人員平均薪資並考慮可能異動狀況
def avg(data):
    emp=data["count"]
    total=0
    for salary in data["employees"]:
        total+=salary["salary"]
    result=total/emp
    print(result)
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})


# #Task 3 時間複雜度:O(n*n)
# #找到最大結果的相乘組合的數
def maxProduct(nums):
    init=nums[0]*nums[1]
    for neo in range(len(nums)-1):
        for neo2 in range(neo+1,len(nums)):
            if nums[neo]*nums[neo2]>init:
                init=nums[neo]*nums[neo2]
    print(init)
# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1,-2,0]) #得到 2


#Task 4
# 給予一組陣列，湊出兩個不同數字相加可以等於給予的目標數字，顯示其列表中位置
def twoSum(nums, target):
    for num in range(len(nums)-1):#長度4-1=3=0~3
        for num2 in range(num+1,len(nums)):#第一個~底(4)之前一個=1~3
            if nums[num]+nums[num2]==target:
                return [num,num2]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#Optional Task 5 時間複雜度:O(n)
# 找最長的0 並計算長度
def maxZeros(nums):
    record=0
    best=0
    for num in nums:
        if num==0:
            best+=1
            if best>record:
                record=best
        elif num==1:
            if best>record:
                record=best
                best=0
            else:
                best=0     
    print(record)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3