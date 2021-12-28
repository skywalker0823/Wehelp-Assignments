function burger_list(){





    var logo_list=document.getElementById("menu_outer");
    // if(logo_list.style.display=="none"){
    //     logo_list.style.display="block"
    // }else{logo_list.style.display="none"}

    logo_list.classList.toggle("hide")//這裡直接創立一個CSS並引用 屬於特殊方法
    logo_list.classList.toggle("out")
};
