document.addEventListener('DOMContentLoaded', function(){
    if (document.querySelector('#bio')!=undefined) {
        document.querySelector('#bio').onclick = function(){
            console.log('Clicked on edit bio');
            document.querySelector('.edit_bio_one').style.display = 'block';
            document.querySelector('.edit_bio_two').style.display = 'none';
            document.querySelector('#bio_text').style.display = 'none';
        }
    }
    
    document.getElementById('edit_bio_form').onsubmit = function(){
        console.log("Helllo")
        const bio_data = document.querySelector('#bio_data').value;
        console.log(bio_data);
        fetch('/edit_bio',{
            method:'POST',
            body: JSON.stringify({
                newbio:bio_data,
            })
        })
        .then(response => response.json())
        .then(result=>{
            console.log(result);

        })
        document.querySelector('.edit_bio_one').style.display = 'none';
        document.querySelector('.edit_bio_two').style.display = 'block';
        document.querySelector('#bio_text').style.display = 'block';
        document.querySelector('#bio_text').innerHTML = bio_data;
        
        return false;
    }
    if (document.getElementById('follow')!=undefined){
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
    }
    

   
    

});

