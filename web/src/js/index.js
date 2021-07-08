
firebase.database().ref('attendance-management-sy-59713-default-rtdb').on('value',(snap)=>{
    var res="";
    var recieveData =snap.val();
    console.log(recieveData);
    
    Object.values(recieveData).forEach((entry, index)=>{
        res+=Object.keys(recieveData)[cnt];
        res+="<table class='table table-bordered table-hover w-50  align-middle'>";
        res+="<thead class='table-primary table-dark'><tr class=''><td>Date</td><td>Enrollment Id</td><td>Name</td></tr></thead><tbody class='table-sm'>";
        Object.values(entry).forEach((data, index)=>{
                res+="<tr>";
                res+="<td>"+data["Date"]+"</td>";
                res+="<td>"+data["Enrollment"]+"</td>";
                res+="<td>"+data["Name"]+"</td>";
                res+="</tr>"
            })
        res+="</tbody></table>";
        res+="</div>";
        res+="</div>";
        res+="</div>";
        cnt++;

    })
    document.getElementById("accordion").innerHTML=res;
  });
