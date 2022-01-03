// WeHelp Bootcamp
// Assignment - Week 2

//Task 1
//迴圈計算min~max總合
function calculate(min, max){
    let total=0
    for(num=min;num<=max;num++){
        total+=num
    }
    console.log(total)
};
calculate(1,3);
calculate(4,8);


//Task 2
//計算人員平均薪資並考慮可能異動狀況
function avg(data){
    let emp=data["count"]
    let total=0
    persons=data["employees"]
    for(person in persons){
        salary=(persons[person].salary)
        total+=salary
    }
    let result=total/emp
    console.log(result)
}
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
});


//Task 3
//最大兩數之相乘
function maxProduct(nums){
    let neo=nums[0];
    for(number of nums){
        if(number>neo){
            neo=number
        }
    }
    let index=nums.indexOf(neo)
    nums.splice(index,index+1)
    let neo2=nums[0]
    for(number2 of nums){
        if(number2>neo2){
            neo2=number2
        }
    }
    console.log(neo*neo2)

    }
    maxProduct([5, 20, 2, 6]) // 得到 120
    maxProduct([10, -20, 0, 3]) // 得到 30
    maxProduct([-1, 2]) // 得到 -2
    maxProduct([-1, 0, 2]) // 得到 0
    maxProduct([-1,-2,0]) //得到 0


//Task 4
//給予一組陣列，湊出兩個不同數字相加可以等於給予的目標數字，顯示其列表中位置
function twoSum(nums, target){
    for(num=0;num<nums.length-1;num++){
        for(num2=num+1;num2<nums.length;num2++){
            if(nums[num]+nums[num2]==target){
                return [num,num2]
            }
        }
    }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


//Optional Task 5
//找最長的0 並計算長度
function maxZeros(nums){
    let record=0
    let best=0
    for(num of nums){
        if(num==0){
            best+=1
            if(best>record){
                record=best
            }
        }
        else if(num==1){
            if(best>record){
                record=best
                best=0
            }
            else{best=0}
        }
    }
    console.log(record)
}
    maxZeros([0, 1, 0, 0]); // 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
    maxZeros([1, 1, 1, 1, 1]); // 得到 0
    maxZeros([0, 0, 0, 1, 1]) // 得到 3