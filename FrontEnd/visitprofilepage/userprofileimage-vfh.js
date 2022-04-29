
// let userId = 9000;

async function getUserImage(){
  let url = "http://127.0.0.1:5000/user/image/" + userId;
  console.log(url);
  let response = await fetch(url);
  console.log(response);

  if(response.status === 200){

      const image_text = await response.text();
      // const image_Element = document.createElement('img');
      // image_Element.src = image_text;
      // document.getElementById("userImage").appendChild(image_Element);
      let image_Element = document.getElementById("userImageFile");
      image_Element.src = image_text;
      
  }
}
getUserImage()

async function createUserWithImage() {
    let file    = document.getElementById('userImageFileInput').files[0];
    let reader  = new FileReader();
    let base64gif;
  
    reader.addEventListener("load", async function () {
      base64gif = reader.result;
      console.log(base64gif.slice(11, 14));


      if (base64gif.length < 1_000_000 && base64gif.startsWith("data:image/")){
        // let userText = document.getElementById("userText");
        // let userJson = JSON.stringify({"user_id":userId, "user_text": userText.value, "image_format": "true"});
        // let url = "http://127.0.0.1:5000/post"
        
        //ADJUSTING
        // console.log(theUser["user_id"]);
        let response = await fetch(
            //"http://127.0.0.1:5000/user/image/" + theUser["user_id"], 
            "http://127.0.0.1:5000/user/image/" + userId, { 
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: String(base64gif)
          });
          const imageText = await response.text();
          let image_Element = document.getElementById("userImageFile");
          image_Element.src = imageText;
      
      }
      else{
        alert("File Error")
      }
    }, false);
  
    if (file) {
      reader.readAsDataURL(file);
    }else{ 
      createUser()
    }
  }


  async function getUserInfoOnProfile(){
    let url = "http://127.0.0.1:5000/user/" + userId;
    let response = await fetch(url);
    console.log(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateUserInfoOnProfile(body);
    }
    else{
        alert("Error Trying To Obtain Database Information!");
    }
}

function populateUserInfoOnProfile(User){
    let text = User.user_birth_date.split(" ");
    let array = text[1] + " " + text[2] + " " + text[3];
    headerUsername.innerText = `${User.username}`;
    headerBirthday.innerText = `${array}`;
    headerEmail.innerText = `${User.email}`;
 
}

getUserInfoOnProfile();
