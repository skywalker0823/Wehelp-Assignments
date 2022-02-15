check_name=()=>{
    let who_is=document.getElementById("who_is").value;
    let you_are=document.getElementById("you_are");
    fetch(
        "/api/members?username="+who_is
    ).then((response)=>{
            return response.json();
    }).then((json_data)=>{
        if(json_data.data==null){
            throw new Error()
        }
        let name=json_data.data.name;
        you_are.innerHTML=name+"("+who_is+")"
    }).catch((error)=>{
        you_are.innerHTML="查無此號"
    })
}

rename=()=>{
    let new_name=document.getElementById("i_am");
    let rename_result=document.getElementById("rename_result");
    let name_message=document.getElementById("name_message");
    const url='/api/member';
    fetch(url,{
        method: 'POST',
        headers :{
            'content-type':'application/json',
        },
        body: JSON.stringify({name:new_name.value})
    }).then((response)=>{
        return response.json()
    }).then((json_data)=>{
        rename_result.innerHTML="更新成功";
        name_message.innerHTML=new_name.value+" 恭喜您~成功登入系統:)";
        new_name.value="";
    }).catch((error)=>{
        rename_result.innerHTML="更新斯拜";
    });
}