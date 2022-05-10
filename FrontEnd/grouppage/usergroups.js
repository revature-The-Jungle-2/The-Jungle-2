
const userGroupSectionDiv = document.getElementById("userGroups-div");
let user = JSON.parse(localStorage.getItem("userInfo"));
//let userId = user.userId;

async function getGroupsForUser(){
    let url = devUrlPython+"/group/user/"+user.userId;

    let response = await fetch(url, {mode: "cors"});

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
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

        let groupNameDiv = document.createElement("div");
        groupNameDiv.setAttribute("class", "name valign-text-middle poppins-bold-astronaut-22px");
        groupNameDiv.innerHTML = `<a onclick="goToGroupPages(${groupBody[group].groupId})" id="groupLink-${groupBody[group].groupId}" class="name valign-text-middle poppins-bold-astronaut-22px" href="../grouppage/individualgrouppage/individual-group-page.html">${groupBody[group].groupName}</a>`;

        userGroupSectionDiv.appendChild(groupsDiv);
        groupsDiv.appendChild(groupImage);
        groupsDiv.appendChild(groupNameDiv);


    }
    
}
function goToGroupPages(groupId){
    localStorage.setItem("groupId", groupId);
}

getGroupsForUser();