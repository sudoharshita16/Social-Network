function edit(){
    document.querySelector('.view_one').forEach(view_one =>
        {
            view_one.style.display = 'none';
        })
}

function showFollow(){
    document.querySelector('#follow').follow.style.display = 'none';
    document.querySelector('#unfollow').follow.style.display = 'none';
    document.querySelector('#follow').follow.style.display = 'block';

}

function showUnfollow(){
    document.querySelector('#follow').follow.style.display = 'none';
    document.querySelector('#unfollow').follow.style.display = 'none';
    document.querySelector('#unfollow').follow.style.display = 'block';

}

<div id = "follow" ></div>
<div id = "unfollow"></div>
<script type="text/babel">
     
      
      class Follow extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                followers: 0,
                following: 0
            };
        }  

        render() {
            return(
                <div>
                    <h6>Followers:{{nfollowers}}</h6>
                    <h6>Following:{{nfollowing}}</h6>
                        <input type="submit" value="Follow" class="btn btn-primary btn-sm"></input>
                      
                 </div>
                );
        }
      }
      
      class Unfollow extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                followers: 0,
                following: 0
            };
        }  

        render() {
            return(
                <div>
                    <h6>Followers:{{nfollowers}}</h6>
                    <h6>Following:{{nfollowing}}</h6>
                        <input type="submit" value="Unfollow" class="btn btn-primary btn-sm"></input>
                      
                 </div>
                );
        }
      }
     

      ReactDOM.render(<Follow />,document.querySelector("#follow"));
      ReactDOM.render(<Unfollow />,document.querySelector("#unfollow"));

</script>

<script>
    document.addEventListener('DOMContentLoaded',{
        if (show_follow_button === 1){

        }
    });
</script>
