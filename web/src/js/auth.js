function validate(){
    var username = document.login.Username.value;
    var password = document.login.Password.value;
    //data recieve
    firebase.database().ref('teacherinfo').on('value',(snap)=>{
        var flag = true;
        var recieveData =snap.val();
        console.log(recieveData);
    

        Object.keys(recieveData).forEach((item, index)=>{
            if(username ===item && password === recieveData[item]) {
               flag=false;
               window.location.replace("home.html");
                //window.location ="home.html";
            } 
            
        });   
        
        
        
   
    });
}