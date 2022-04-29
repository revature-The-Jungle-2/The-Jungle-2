let userId = JSON.parse(localStorage.getItem("userInfo")).userId;


// async function getPostImage(){// the postId and imageFormat will probably have to be passed as parameters
//   let url = "http://127.0.0.1:5000/post/image/" + postId;//post_id parameter
//   console.log(url);
//   let response = await fetch(url);
//   console.log(response);

//   if(response.status === 200){

//       const image_text = await response.text();
//       const image_Element = document.createElement('img');
//       image_Element.src = image_text;//image_parameter
//       document.getElementById("postImage").appendChild(image_Element);
//   }
// }




// A basic create post without images for users.
async function createPost(){
    let postText = document.getElementById("postText");
    let postJson = JSON.stringify({"user_id":userId, "post_text": postText.value, "image_format": "false"});
    let url = "http://127.0.0.1:5000/post"
    let thePost = await fetch(url, {
        method:"POST",
        headers:{'Content-Type': 'application/json'}, 
        body:postJson}).then(response => {return response.json()});
    
    add_post_first(thePost)
}



// A more complicated create post with images for users.
async function createPostWithImage() {
    let file    = document.getElementById('imageFile').files[0];
    let reader  = new FileReader();
    const postText = document.getElementById("postText").value;
    console.log(postText.value);
    let base64gif;
  
    reader.addEventListener("load", async function () {
      base64gif = reader.result;
      console.log(base64gif.slice(11, 14));


      if (base64gif.length < 1_000_000 && base64gif.startsWith("data:image/")){
        let postJson = JSON.stringify({"user_id":userId, "post_text": postText, "image_format": "true"});
        let url = "http://127.0.0.1:5000/post"
        
        //Inserts the post into the post table
        let thePost = await fetch(url, {
            method:"POST",
            headers:{'Content-Type': 'application/json'}, 
            body:postJson}).then(response => {return response.json()});

        //Inserts the image into the post_image_table
        let response = await fetch(
            "http://127.0.0.1:5000/post/image/" + thePost["post_id"], {
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: String(base64gif)
          });
          const imageText = await response.text();
        add_post_first(thePost)
      
      }
      else{
        document.getElementById("postErrorMessage").innerHTML = "Error creating the post."
      }
    }, false);
    
    if (file) {
      reader.readAsDataURL(file);
    }else if (document.getElementById("postText")){ // if there is no file put in, then the post is sent with the simpler method as long as there is text
      createPost()
    }else{
      alert("No Post entered.")//need to replace this alert method later
    }
    
    document.getElementById("createPostForm").reset();//because I don't know how to use PHP
  }


  async function getPost() {
    let response = await fetch("http://127.0.0.1:5000/user/post/" + userId, {
      method: "GET",
      mode: "cors",
    });
    if (response.status === 200) {
      let body = await response.json();
      populateData(body);
    }
  }
  getPost()
  
  async function populateData(responseBody) {
    const allpost = document.getElementById("post column");
    for (let post of responseBody) {
      let postBox = document.createElement('div');
      
      //add the poster image
      let url = "http://127.0.0.1:5000/user/image/" + post.user_id;
      let response = await fetch(url);
      let user_image_text;
      if(response.status === 200){
          user_image_text = await response.text();
        }
  
      //get the post image
      url = "http://127.0.0.1:5000/post/image/" + post.post_id;
      console.log(url);
      response = await fetch(url);
      console.log(response);
      let date_time = new Date(post.date_time_of_creation)
      let date = date_time.toDateString();
  
      if(response.status === 200){//if there is an image then this one, else the other one
        const image_text = await response.text();
        postBox.innerHTML = 
        `<div class = "post`+ post.post_id +`" id = "post`+ post.post_id + `">
        <div class="flex-row">
          <div class="overlap-group2">
            <div class="new-york-ny valign-text-middle">`+ date +`</div>
            <div class="username-1 valign-text-middle poppins-bold-cape-cod-20px">${post.user_name}</div>
            <img class="feed-avatar-1" src="`+ user_image_text + `" alt="img/ellipse-1@2x.png" />
          </div>
          <input type="image" class="three-dots-icon-1" src="img/bi-three-dots@2x.svg" id="deletePost${post.post_id}" onclick="deletePost(${post.post_id})"/>
        </div>
        <img class="feed-picture" src="`+ image_text +`" />
        <div class="icon-container">
        <input type="image" class="heart-icon" src="img/heart-icon@2x.svg" onclick="likePost(${post.post_id})"/>
        <p id ="likedComment${post.post_id}">` + post.likes + `</p>
          <input type="image" class="chat-bubble-icon" src="img/chat-bubble-icon@2x.svg"/>
          <img class="share-icon" src="img/share-icon@2x.svg" />
        </div>
        <div class="overlap-group-1">
          <div class="feed-text-2 valign-text-middle poppins-medium-black-18px">`+ post.post_text + `</div>
        </div>
      </div>`
      }else{
        postBox.innerHTML = 
      `<div class = "post`+ post.post_id +`" id = "post`+ post.post_id + `">
      <div class="flex-row">
        <div class="overlap-group2">
          <div class="new-york-ny valign-text-middle">`+ date +`</div>
          <div class="username-1 valign-text-middle poppins-bold-cape-cod-20px">${post.user_name}</div>
          <img class="feed-avatar-1" src="`+ user_image_text + `" alt="img/ellipse-1@2x.png" />
        </div>
        <input type="image" class="three-dots-icon-1" src="img/bi-three-dots@2x.svg" id="deletePost${post.post_id}" onclick="deletePost(${post.post_id})"/>
      </div>
      <div class="icon-container">
      <input type="image" class="heart-icon" src="img/heart-icon@2x.svg" onclick="likePost(${post.post_id})"/>
      <p id ="likedComment${post.post_id}">` + post.likes + `</p>
        <input type="image" class="chat-bubble-icon" src="img/chat-bubble-icon@2x.svg"/>
        <img class="share-icon" src="img/share-icon@2x.svg" />
      </div>
      <div class="overlap-group-1">
        <div class="feed-text-2 valign-text-middle poppins-medium-black-18px">`+ post.post_text + `</div>
      </div>
    </div>`
      }
  
      allpost.appendChild(postBox)
    }
  }

  async function deletePost(post_id) {
    let deleteResponse = await fetch("http://127.0.0.1:5000/group_post/" + post_id, {
      method: "DELETE"
    })
    console.log(deleteResponse)
    if (deleteResponse.status === 200) {
      document.getElementById("post" + post_id).remove();
    }
  }



  const logout = () => {
    // delete fake token from local storage
    localStorage.removeItem("pseudoToken");
    // delete fake token from local storage
  
    // redirect user back to home page
    // location.href = "home.html";

    // redirect user back to the login
    localStorage.removeItem("userInfo");
  };
  

  async function add_post_first(post){
    let postBox = document.createElement('div');
      
      //add the poster image
      let url = "http://127.0.0.1:5000/user/image/" + post.user_id;
      let response = await fetch(url);
      let user_image_text;
      if(response.status === 200){
          user_image_text = await response.text();
        }
  
      //get the post image
      url = "http://127.0.0.1:5000/post/image/" + post.post_id;
      console.log(url);
      response = await fetch(url);
      console.log(response);
      let date_time = new Date(post.date_time_of_creation)
      let date = date_time.toDateString();
  
      if(response.status === 200){//if there is an image then this one, else the other one
        const image_text = await response.text();
        postBox.innerHTML = 
        `<div class = "post`+ post.post_id +`" id = "post`+ post.post_id + `">
        <div class="flex-row">
          <div class="overlap-group2">
            <div class="new-york-ny valign-text-middle">`+ date +`</div>
            <div class="username-1 valign-text-middle poppins-bold-cape-cod-20px">${post.user_name}</div>
            <img class="feed-avatar-1" src="`+ user_image_text + `" alt="img/ellipse-1@2x.png" />
          </div>
          <input type="image" class="three-dots-icon-1" src="img/bi-three-dots@2x.svg" id="deletePost${post.post_id}" onclick="deletePost(${post.post_id})"/>
        </div>
        <img class="feed-picture" src="`+ image_text +`" />
        <div class="icon-container">
          <input type="image" class="heart-icon" src="img/heart-icon@2x.svg" onclick="likePost(${post.post_id})"/>
          <p id ="likedComment${post.post_id}">` + post.likes + `</p>
          <input type="image" class="chat-bubble-icon" src="img/chat-bubble-icon@2x.svg"/>
          <img class="share-icon" src="img/share-icon@2x.svg" />
        </div>
        <div class="overlap-group-1">
          <div class="feed-text-2 valign-text-middle poppins-medium-black-18px">`+ post.post_text + `</div>
        </div>
      </div>`
      }else{
        postBox.innerHTML = 
      `<div class = "post`+ post.post_id +`" id = "post`+ post.post_id + `">
      <div class="flex-row">
        <div class="overlap-group2">
          <div class="new-york-ny valign-text-middle">`+ date +`</div>
          <div class="username-1 valign-text-middle poppins-bold-cape-cod-20px">${post.user_name}</div>
          <img class="feed-avatar-1" src="`+ user_image_text + `" alt="img/ellipse-1@2x.png" />
        </div>
        <input type="image" class="three-dots-icon-1" src="img/bi-three-dots@2x.svg" id="deletePost${post.post_id}" onclick="deletePost(${post.post_id})"/>
      </div>
      <div class="icon-container">
        <input type="image" class="heart-icon" src="img/heart-icon@2x.svg" onclick="likePost(${post.post_id})"/>
        <p id ="likedComment${post.post_id}">` + post.likes + `</p>
        <input type="image" class="chat-bubble-icon" src="img/chat-bubble-icon@2x.svg"/>
        <img class="share-icon" src="img/share-icon@2x.svg" />
      </div>
      <div class="overlap-group-1">
        <div class="feed-text-2 valign-text-middle poppins-medium-black-18px">`+ post.post_text + `</div>
      </div>
    </div>`
      }
      const allpost = document.getElementById("post column");
      allpost.prepend(postBox)
  };
