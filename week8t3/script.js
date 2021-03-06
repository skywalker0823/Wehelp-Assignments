// check=()=>{
//     fetch("https://www.google.com/")
//     .then((response)=>{
//             return response.json()
//     }).then((data)=>{
//             console.log(data)
//             return data
//     }).catch((error)=>{
//             console.log("error")
//     })
// };
// const resp = await fetch(url,{
//     method:,
//     headers{},
// })

async function check(){
  try{
      const response = await fetch('http://127.0.0.1:3000/api/members?username=123', {method: 'get'});
      const result = await response.json();
      console.log({response,result});
}catch(err){
      console.log(err);
}
};

// 如果是簡單方法，伺服器必須打開對應方法如get/post的Access-Control-Allow-Origin
// 切勿設定成＊ 
//如果是非簡單方法如delete or put 伺服器必須在Option設定，Access-Control-Allow-Methods
//如果攜帶cookie 前端先聲明credentials: 'include' 或是 withCredentials
//後端要加上 Access-Control-Allow-Credentials header，而且 Access-Control-Allow-Origin header 不能用 *
async function check2(){
  const settings={
        method: 'POST',
        credentials: 'include',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            xhrFields: {
        withCredentials: true
        },
        },
        body: JSON.stringify({"name":"123"})
  }
  try{
      const response = await fetch('http://127.0.0.1:3000/api/tester', settings);
      const result = await response.json();
      console.log({response,result});
}catch(err){
      console.log(err);
}
};

async function signin(){
  const settings={
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({"account":"123","password":"123"})
    }
  try{
      const response = await fetch('http://127.0.0.1:3000/signin', settings);
      const result = await response.json();
      console.log({response,result});
}catch(err){
      console.log(err);
}
};
