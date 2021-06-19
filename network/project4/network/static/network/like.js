document.addEventListener('DOMContentLoaded',function(){
    var ar = document.querySelector('h3');
    var array = ar.innerHTML;
    var arr = JSON.parse(array);
    
    //document.getElementById("one").innerHTML = str.split("");
    //console.log(arr);
    //console.log(arr.value);
    document.querySelectorAll('.likeunlike').forEach(function(form){
        form.onsubmit = function(){
            const entry_id = form.elements[1].value;
            fetch('/like_unlike',{
                method:'POST',
                body: JSON.stringify({
                    entry_id:form.elements[1].value,
                    val:form.elements["liked"].value,
                })
            })
            
            .then(response => response.json())
            .then(result => {
                //console.log(result);
                fetch(`lval/${entry_id}`)  
                .then(response => response.text())
                .then(data=>{
                    //console.log(data)
                    data = JSON.parse(data)
                    //console.log(data)
                    const likes = document.getElementById(`${form.elements[1].value}`);
                    var count = 0;
                    var one;
                    var two;
                    document.querySelectorAll('.one').forEach(function(value){
                        console.log(arr[count]);
                        console.log(entry_id);
                        if (arr[count] == entry_id){
                            //console.log("true")
                            one = value;
                        }
                        count++;
                        //console.log(count);
                    });
                    //console.log(one);
                    count = 0;
                    document.querySelectorAll('.two').forEach(function(value){
                        console.log(count);
                        console.log(entry_id)
                        if (arr[count] == entry_id){
                            //console.log("true")
                            two = value;
                        } 
                        count++;   
                        //console.log(count);
                    });
                    count = 0;
                    //console.log(two);
                    likes.innerHTML = data.likes;
                    if (form.elements["liked"].value === "yes"){
                        form.elements["liked"].value = "no";
                        one.style.display = 'none';
                        two.style.display = 'block';
                    
                    }
                    else if (form.elements["liked"].value === "no"){
                        form.elements["liked"].value = "yes";
                        one.style.display = 'block';
                        two.style.display = 'none';
                    }    

                })

               

            })
        return false;
        }
       
    
    });


    document.querySelectorAll('.EDIT').forEach(function(form){
        form.onsubmit = function(){
            const entry_id = form.elements[1].value;
            var count = 0;
            var one;
            var two;
            //console.log(entry_id)
            document.querySelectorAll('.view_one').forEach(function(value){
                //console.log(count);
                //console.log(entry_id);
                if (arr[count] == entry_id){
                    //print("true")
                    one = value;
                }
                count++;
            });
            //console.log(one);
            count = 0;
            document.querySelectorAll('.view_two').forEach(function(value){
                //console.log(count);
                //console.log(value.elements[1].value);
                //console.log(entry_id);
                if (arr[count] == entry_id){
                    
                    two = value;
                } 
                count++;   
            });
            //console.log(two);
            count = 0
            one.style.display = 'none';
            two.style.display = 'block';

            return false;
        }
        });


      document.querySelectorAll('.edit').forEach(function(form){
          form.onsubmit = function(){
            const entry_id = form.elements[1].value;
            const data = form.elements[2].value;
            //console.log(entry_id)
            //console.log(data)
            fetch('/edit',{
                method:'POST',
                body: JSON.stringify({
                  entry_id:entry_id,
                  text:data
  
                })
            })
            .then(response=>response.json())
            .then(result => {
                //console.log(result);
                fetch(`eval/${entry_id}`)
                .then(response=>response.text())
                .then(data=>{
                    //console.log(data)
                    data = JSON.parse(data)
                    //console.log(data)
                    var count = 0;
                    document.querySelectorAll('.view_one').forEach(function(value){
                        
                        if (arr[count] == entry_id){
                            one = value;
                        }
                        count++;
                    });
                    count = 0;
                    document.querySelectorAll('.view_two').forEach(function(value){
                        //console.log(value.elements[1].value);

                        if (arr[count] == entry_id){
                            two = value;
                        } 
                        count++;   
                    });
                    
                    count = 0;
                    document.querySelectorAll('.para').forEach(function(value){
                        if (arr[count] == entry_id){
                            value.innerHTML = data.text;
                        } 
                        count++;   
                    });
                    
                    count = 0;
                    //console.log(val.p);
                    //one.p = data.text;
                    two.style.display = 'none';
                    one.style.display = 'block';

                })
                

            });
            return false;
          }

          


      });

});

