document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('follow').onsubmit = function()
    {
        const puser_id = document.querySelector('#puser_id').value;
        const followers = document.querySelector('#followers').value;

        fetch('/follow',{
            method:'POST',
            body: JSON.stringify({
                puser_id:puser_id,
                followers:followers
            })
        })
        .then(response => response.json())
        .then(result => {//1
            console.log("Result: ")
            console.log(result);
        fetch(`fval/${puser_id}`)
        .then(response=>response.text())
        .then(data=>{
            console.log(data)
            data = JSON.parse(data)
            console.log(data)

        const current_followers = document.querySelector("#nfollowers");
        current_followers.innerHTML = `${data.followers_count} Followers`;
        document.querySelector('#second').style.display = 'block';
        document.querySelector('#first').style.display = 'none';
    
        

       
        })
    });//1

        return false;
    }
     
    
    document.getElementById('unfollow').onsubmit = function()
    {
        console.log("hello")
        const puser_id = document.querySelector('#puser_id').value;
        const followers = document.querySelector('#followers').value;
        console.log(puser_id)
        console.log(followers)

        fetch('/unfollow',{
            method:'POST',
            body: JSON.stringify({
                puser_id:puser_id,
                followers:followers
            })
        })
        .then(response => response.json())
        .then(result => {//1
            console.log(result);
        
        console.log("id is: ")
        console.log(puser_id)
        fetch(`fval/${puser_id}`)
        .then(response=>response.text())
        .then(data=>{
            console.log("Namaskar")
            console.log(data)
            data = JSON.parse(data)
            console.log(data)
        const current_followers = document.querySelector("#nfollowers");
        current_followers.innerHTML = `${data.followers_count} Followers`;
        document.querySelector('#first').style.display = 'block';
        document.querySelector('#second').style.display = 'none';
    
        

        })
    });//1

        return false;
    }

   
    

});

