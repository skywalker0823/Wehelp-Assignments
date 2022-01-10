function burger_list(){
    var logo_list=document.getElementById("menu_outer");
    // if(logo_list.style.display=="none"){
    //     logo_list.style.display="block"
    // }else{logo_list.style.display="none"}
    logo_list.classList.toggle("hide")
    logo_list.classList.toggle("out")
};
let counter=1
function site_in(){
    fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
  .then(function(response) {
    return response.json();
  })
  .then(function(datas) {
    let data=datas.result.results
    for(site of data){
        //console.log(site.stitle,site.file.toLowerCase().split("jpg")[0]+"jpg")
        let site_pic=site.file.toLowerCase().split("jpg")[0]+"jpg";//圖片兒
        let pic_in=document.getElementById("pic_in");//圖片從這開始放
        
        let new_space=document.createElement("div");//產生新的div
        new_space.className="box";//調整classname
        new_space.id="box"+counter;
        
        let pic_here=document.createElement("img");
        let site_name_space=document.createElement("p");
        pic_here.src=site_pic;
        site_name_space.className="pic_text";
        let site_name=document.createTextNode(site.stitle);//地名
        
        pic_in.appendChild(new_space).appendChild(pic_here);
        pic_in.appendChild(new_space).appendChild(site_name_space).appendChild(site_name);

        counter+=1 ;
        if(counter>9){
            document.getElementById(new_space.id).style.display="none"
        };
        
    };
  });
};
function more(){
    for(let counter=9;counter<17;counter++){
    document.getElementById("box"+counter).style.display="flex"
    };
};

// 1. 使用者打開網頁時，立刻透過 JavaScript 連線以上網址，取得景點資料。
// 2. 將取得的景點資料，使用 JavaScript 程式動態的做出畫面，顯示景點的第一張圖片和
// 景點的名稱。務必使用 document.createElement() 與 appendChild() 這兩個方法和其
// 相關的技巧搭配完成，禁止使用 innerHTML。
// 3. 顯示前 8 個景點即可。
// 4. 畫面的 RWD 版面設計保持與第一週時相同
// let target=100;
// for(let i=0;i<data.length;i++){
//   let index=data.indexOf(100-data[i]);
// }


// 要求三：JavaScript 建立載入更多的按鈕 (Optional)
// 延續上一題，在景點下方建立一個載入更多的按鈕，點擊就可以顯示額外 8 個景點資訊。請參
// 考以下兩張螢幕截圖，點擊第一張圖中的 Load More 按鈕後，產生如第二張圖的畫面。
