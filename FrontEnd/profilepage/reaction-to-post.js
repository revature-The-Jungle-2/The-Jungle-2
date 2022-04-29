let likeButton = document.getElementById("trigger");
console.log("JS is connected to HTML");

likeButton.onclick = async function(e){
    e.preventDefault(); 

    let response = await fetch(`http://127.0.0.1:5000/postfeed`, {
        method : "POST",
        body : JSON.stringify({
        postId: 2 //need to be changed when integrated!
           
        })
        
    })

    let responseData = await response.json()
    console.log(responseData)
    document.getElementById("likedComment").innerHTML="Total Number Of Likes: "+responseData;
  
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