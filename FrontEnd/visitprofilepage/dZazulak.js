const userBirthDate = document.getElementById("userBirthdateInput");
const userAboutMe = document.getElementById("userAboutMeInput");
const modalMessageDiv = document.getElementById("ModalMsgProfile");
const followerSectionDiv = document.getElementById("followers-div");
const groupSectionDiv = document.getElementById("groups-div");
const profileUsername = document.getElementById("profileUsername");
const profileDOB = document.getElementById("profileDOB");
const profileEmail = document.getElementById("profileEmail");
visitedUserId = localStorage.getItem("visitUserIdPage");



async function getUserByUserId(){
    let url = "http://127.0.0.1:5000/user/" + visitedUserId;
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateUserProfileByUserId(body);
        let initialAboutMe = localStorage.getItem("AboutMe");
        // userAboutMe.innerText = initialAboutMe;
        populateAboutMeForVisitedUser();
    }
    else{
        alert("There seems to be some sort of issue going on with the database: Apologies!");
    }
}

function populateUserProfileByUserId(user){

    let text = user.user_birth_date.split(" ");
    let array = text[1] + " " + text[2] + " " + text[3];
    let BirthDateValue = "";
    profileUsername.innerText = `${user.username}`;
    profileDOB.innerText = `${array}`;
    profileEmail.innerText = `${user.email}`;

    /*
        Sets the aboutMe to the value by using getUserById, then setting it to the localStorage to use for the textarea
    */
    localStorage.setItem("AboutMe", user.user_about);

    /*
        Switch statement to format the Month to a format that the date input will like as the value
        Sets the attribute of the value afterwards using the getUserById
    */
    let month = "";
    switch(text[2]){
        case "Jan":
            month = "01";
            break;
        case "Feb":
            month = "02";
            break;
        case "Mar":
            month = "03";
            break;
        case "Apr":
            month = "04";
            break;
        case "May":
            month = "05";
            break;
        case "Jun":
            month = "06";
            break;
        case "Jul":
            month = "07";
            break;
        case "Aug":
            month = "08";
            break;
        case "Sep":
            month = "09";
            break;
        case "Oct":
            month = "10";
            break;
        case "Nov":
            month = "11";
            break;
        case "Dec":
            month = "12";
            break;

    }
    BirthDateValue = text[3] + "-" + month + "-" + text[1];
    // userBirthDate.setAttribute("value", BirthDateValue);
}

function populateAboutMeForVisitedUser(){
    visitUserAboutMe = document.getElementById("visitedUserPageAboutMe");
    visitUserAboutMePTag = document.createElement("p");
    visitUserAboutMe.innerHTML = '';
    visitUserAboutMePTag.innerText = localStorage.getItem("AboutMe");
    visitUserAboutMe.appendChild(visitUserAboutMePTag);
    
}

/*
    Grabs the user profile information from the update profile modal and sends it through the layers
*/
async function updateUserProfileData(){

    let url = "http://127.0.0.1:5000/user/profile/update/" + userId;
    
    let updateUserProfileJSON = JSON.stringify({"firstName": "Shouldn't change",
        "lastName": "Shouldn't change",
        "email": "Shouldn't change",
        "username": "Shouldn't change",
        "passcode": "Shouldn't change",
        "userAbout": userAboutMe.value,
        "userBirthDate": userBirthDate.value,
        "userImageFormat": "Shouldn't change"});

    let response = await fetch(url, {
        method: "PATCH",
        headers:{"Content-Type": 'application/json'},
        body:updateUserProfileJSON})

        if(response.status === 200){
            let body = await response.json();
            successMessageForProfileModal();
            getUserByUserId()
            localStorage.setItem("AboutMe", body.user_about);
            console.log(body);
        }
        else{
            errorMessageForProfileModal();
        }
}

/* 
    Reset the modal data when you close it
*/
function resetProfileModalData(){
    document.getElementById("updateUserProfileForm").reset()
    modalMessageDiv.innerHTML = '';
}

/*
    Function to print error message for update profile modal
*/
function errorMessageForProfileModal(){
    modalMessageDiv.innerHTML = '';
    let profileErrorMessage = document.createElement("p");
    profileErrorMessage.innerText = 'Birthdate may not be blank';
    profileErrorMessage.style.color = 'red';
    profileErrorMessage.setAttribute("id", "modalProfileErrorMessage");
    modalMessageDiv.append(profileErrorMessage);
}

/*
    Function to print success message for update profile modal
*/
function successMessageForProfileModal(){
    modalMessageDiv.innerHTML = '';
    let profileSuccessMessage = document.createElement("p");
    profileSuccessMessage.innerText = 'Saved';
    profileSuccessMessage.style.color = 'blue';
    profileSuccessMessage.setAttribute("id", "modalProfileSuccessMessage");
    modalMessageDiv.append(profileSuccessMessage);
}

/* 
    Grabs all the users followers from the database
*/
async function getUserFollowers(){
    let url = "http://127.0.0.1:5000/user/followers/" + visitedUserId;

    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        // console.log(body);
        populateUserFollowers(body);
        getFollowerImage(body);
    }
    else{
        alert("Error with followers");
    }
}

function populateUserFollowers(followerBody){
    for(let follower in followerBody){
        // Created div to hold the image and username div and set class name
        let followerDiv = document.createElement("div");
        followerDiv.setAttribute("class", "follower-in-list");

        // Create the image tag and set class name
        let followerImage = document.createElement("img");
        followerImage.setAttribute("class", "friend");
        followerImage.setAttribute("id", `${follower}-image`);
        followerImage.setAttribute("alt", "No Image");
        followerImage.setAttribute("src", "img/default-profile-picture.jpg");

        // Created the username div and set the class name and username
        let followerUsernameDiv = document.createElement("div");
        followerUsernameDiv.setAttribute("class", "name valign-text-middle poppins-bold-astronaut-22px");
        followerUsernameDiv.innerHTML = `<a onclick="localStorage.setItem('visitUserIdPage', ${followerBody[follower]})" class="name valign-text-middle poppins-bold-astronaut-22px" href="../visitprofilepage/visit-profile-page.html">${follower}</a>`;

        // Append the created elements to the page
        followerSectionDiv.appendChild(followerDiv);
        followerDiv.appendChild(followerImage);
        followerDiv.appendChild(followerUsernameDiv);

    }
}

async function getFollowerImage(followerBody){
    for(follower in followerBody){
        let image_Element = document.getElementById(`${follower}-image`);
        let url = `http://127.0.0.1:5000/user/image/${followerBody[follower]}`;
        console.log(url);
        let response = await fetch(url);
        if(response.status === 200){
            const image_text = await response.text();
            image_Element.src = image_text;
        }

}
}

async function getGroupsForUser(){
    let url = "http://127.0.0.1:5000/group/user/" + visitedUserId;

    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        // console.log(body);
        populateGroupsForUsers(body);
    }
    else{
        alert("Error with groups");
    }
}

function populateGroupsForUsers(groupBody){
    for (let group in groupBody){
        let groupsDiv = document.createElement("div");
        groupsDiv.setAttribute("class", "group-in-list");

        let groupImage = document.createElement("img");
        groupImage.setAttribute("class", "friend");
        groupImage.setAttribute("alt", "No Image");
        groupImage.setAttribute("src", "img/default-profile-picture.jpg");

        let groupNameDiv = document.createElement("div");
        groupNameDiv.setAttribute("class", "name valign-text-middle poppins-bold-astronaut-22px");
        groupNameDiv.innerHTML = `<a id="groupLink-${groupBody[group].groupId}" class="name valign-text-middle poppins-bold-astronaut-22px" onclick=goToGroupPage(${groupBody[group].groupId})>${groupBody[group].groupName}</a>`;
        groupSectionDiv.appendChild(groupsDiv);
        groupsDiv.appendChild(groupImage);
        groupsDiv.appendChild(groupNameDiv);


    }
}


function goToGroupPage(groupId){
    // let groupLink = getElementById("groupLink-" + groupId);
    // groupLink.setAttribute("href", "")
    localStorage.setItem("groupId",groupId);
    localStorage.getItem("groupId");
}

getUserFollowers();
getGroupsForUser();
getUserByUserId();