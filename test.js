// function getData(){//這裡在主流程開始的時候 便會立即執行
//     return new Promise(function(resolve,reject){
//         let req=new XMLHttpRequest();
//         req.open("get","data.txt");
//         req.onload=function(){//連線完畢 並且丟出一個promise的檔案 然後丟回下方的then繼續執行
//             resolve(this.responseText);//成功之後 此資料將從getdata()回傳 給15行的datapromise
//         };
//         req.onerror=function(){//若失敗則會執行
//             reject("error")
//         };
//         req.send();
//     })
// };
// //這裡是主流程
// let datapromise=getData();
// datapromise.then(function(result){//這裡的then會等待上方的結果都處理完之後，接續執行
//     console.log(result);
// },function(error){//失敗時執行
//     console.log(error);
// })

// function getFirstInfo() {
// return new Promise((resolve, reject) => {
//     setTimeout(() => {
//     resolve('first data')
//     }, 1000);
// })}

// function getSecondInfo() {
// return new Promise((resolve, reject) => {
//     setTimeout(() => {
//     resolve('second data')
//     }, 2000);
// })}

// async function getGroupInfo() {
// console.log("1")
// // 代表等到第一筆資料回傳後，才印出結果和請求第二筆資料
// const firstInfo = await getFirstInfo()
// console.log(firstInfo)
// console.log("2")
// // 代表等到第二筆資料回傳後，才印出結果
// const secondInfo = await getSecondInfo()
// console.log(secondInfo)
// console.log("3")
// }

// getGroupInfo()

// function myDisplayer(some) {
//     setTimeout(()=>{
//         console.log(some)
//     },1000)
//   }
  
//   function myFirst() {
//     myDisplayer("Hello");
//   }
  
//   function mySecond() {
//     myDisplayer("Goodbye");
//   }
  
//   mySecond();
//   myFirst();
//   console.log("loha")

// myDisplayer=(some)=>{
//     console.log(some+"loha")
// }
  
// myCalculator=(num1, num2)=>{
//     let sum = num1 + num2;
//     myDisplayer(sum);
// }
  
// myCalculator(5, 5);

// function getFirstInfo() {
//     return new Promise((resolve, reject) => {
//       setTimeout(() => {
//         resolve('first data')
//       }, 5000);
//     })
//   }
  
//   function getSecondInfo() {
//     return new Promise((resolve, reject) => {
//       setTimeout(() => {
//         resolve('second data')
//       }, 2000);
//     })
//   }
  
//   async function getGroupInfo() {
//     // 代表等到第一筆資料回傳後，才印出結果和請求第二筆資料
//     const firstInfo = await getFirstInfo()
//     console.log(firstInfo)
//     console.log("hi")
//     // 代表等到第二筆資料回傳後，才印出結果
//     const secondInfo = await getSecondInfo()
//     console.log(secondInfo)
//   }
  
//   getGroupInfo()
// new Promise((resolve, reject) => {
//     console.log('Initial');

//     resolve();
// })
// .then(() => {
//     throw new Error('Something failed');

//     console.log('Do this');
// })
// .catch(() => {
//     console.log('Do thater');
// })
// .then(() => {
//     console.log('Do this whatever happened before');
// })
// .catch(() => {
//     console.log('Do Do');
// })
// .then(() => {
//     console.log('Do der');
// })

say=()=>
say()