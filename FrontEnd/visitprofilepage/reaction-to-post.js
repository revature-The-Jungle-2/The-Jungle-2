// let likeButton = document.getElementById("trigger");
// console.log("JS is connected to HTML");


const devUrlPython="http://ec2-204-236-138-16.us-west-1.compute.amazonaws.com:5000"


// likeButton.onclick = 
async function likePost(e){

    let fetchJson = JSON.stringify({"postId": e})

    let url = devUrlPython+"/postfeed"
    
    let theResponse = await fetch(url, {
        method:"POST",
        headers:{'Content-Type': 'application/json'}, 
        body:fetchJson}).then(response => {return response.json()});

    console.log(theResponse)
    let heart = document.getElementById("likedComment" + e);
    heart.innerHTML = theResponse;
  
}

/*
commentButton.onclick = async function(e){
    e.preventDefault();

 

    let response = await fetch(`http://127.0.0.1:5000/postfeed/comment`, {
        method : "POST",
        body : JSON.stringify({
            commentId: 2
           
        })
        
    })

    let responseData = await response.json()
    console.log(responseData)


}

*/