function getData(){//這裡在主流程開始的時候 便會立即執行
    return new Promise(function(resolve,reject){
        let req=new XMLHttpRequest();
        req.open("get","data.txt");
        req.onload=function(){//連線完畢 並且丟出一個promise的檔案 然後丟回下方的then繼續執行
            resolve(this.responseText);//成功之後 此資料將從getdata()回傳 給15行的datapromise
        };
        req.onerror=function(){//若失敗則會執行
            reject("error")
        };
        req.send();
    })
};

//這裡是主流程
let datapromise=getData();
datapromise.then(function(result){//這裡的then會等待上方的結果都處理完之後，接續執行
    console.log(result);
},function(error){//失敗時執行
    console.log(error);
})