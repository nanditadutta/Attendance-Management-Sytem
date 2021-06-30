
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
        res+="<div class='card'>";
        res+="<div class='card-header' id='"+Object.keys(recieveData)[cnt]+"'>";
        res+="<h5 class='mb-0'>";
        res+=" <button class='btn ' data-toggle='collapse' data-target='#"+Object.keys(recieveData)[cnt]+"' aria-expanded='false' aria-controls='"+Object.keys(recieveData)[cnt]+"'>";
        res+=Object.keys(recieveData)[cnt];
        res+="    </button>";
        res+="  </h5>";
        res+=" </div>";
    
        res+="<div id='"+Object.keys(recieveData)[cnt]+"' class='collapse show' aria-labelledby='"+Object.keys(recieveData)[cnt]+"' data-parent='#accordion'>";
        res+="<div class='card-body'>";
        res+="<table class='table  mx-5 mb-5 mt-2 table-bordered w-75'>";
        res+="<thead><tr class='table-primary'><td>Date</td><td>Enrollment Id</td><td>Name</td></tr></thead><tbody class='table table-dark table-hover'>";
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
