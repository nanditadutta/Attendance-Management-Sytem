
firebase.database().ref('attendance-management-sy-59713-default-rtdb').on('value',(snap)=>{
    var res="";
    var recieveData =snap.val();
    console.log(recieveData);
    cnt=0;
    // Object.values(recieveData).forEach((entry, index)=>{
    //     res+="<span class ='Subject fs-2 fw-bold'>"+Object.keys(recieveData)[cnt]+"</span> </br><table class='table  mx-5 mb-5 mt-2 table-bordered'>" 
    //     res+="<thead><tr class='table-primary'><td>Date</td><td>Enrollment Id</td><td>Name</td></tr></thead><tbody class='table table-dark table-hover'>"
    //     Object.values(entry).forEach((data, index)=>{
    //         res+="<tr>";
    //         res+="<td>"+data["Date"]+"</td>";
    //         res+="<td>"+data["Enrollment"]+"</td>";
    //         res+="<td>"+data["Name"]+"</td>";
    //         res+="</tr>"
    //     })
    //     res+="</tbody></table>"
    //     document.getElementById("main").innerHTML=res;
    //     cnt++;
    // })

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
