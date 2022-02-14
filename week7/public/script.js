check_name=()=>{
    let who_is=document.getElementById("who_is").value;
    let you_are=document.getElementById("you_are");
    //我們要傳回她的name
    fetch("/api/members?username="+who_is)
    .then((response)=>{
        return response.json()
    }).then((json_data)=>{
        let name=json_data.data.name;
        you_are.innerHTML=name+"("+who_is+")"
    }).catch((error)=>{
        you_are.innerHTML="查無此人"
    })
}

rename=()=>{
    let new_name=document.getElementById("i_am").value;
    console.log(new_name)
    let rename_result=document.getElementById("rename_result");
    let name_message=document.getElementById("name_message")
    const url='/api/member';
    fetch(url,{
        method: 'POST',
        headers :{
            'content-type':'application/json',
        },
        body: JSON.stringify({name:new_name})
    }).then((response)=>{
        return response.json()
    }).then((json_data)=>{
        new_n=json_data.newname
        rename_result.innerHTML="更新成功"
        name_message.innerHTML=new_n+" 恭喜您~成功登入系統:)"
    }).catch((error)=>{
        rename_result.innerHTML="更新斯拜"
    });
    // (async()=>{
    //     const response = await fetch(url,{
    //         method: 'POST',
    //         headers: {
    //             'content-type':'application/json',
    //         },
    //         body: JSON.stringify({myname:name})
    //     });
    //     const data = await response.json();
    //     console.log(data)
    // })();
}