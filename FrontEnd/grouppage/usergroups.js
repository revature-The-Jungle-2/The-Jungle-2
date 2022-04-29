
const userGroupSectionDiv = document.getElementById("userGroups-div");



async function getGroupsForUser(){
    let url = "http://127.0.0.1:5000/group/user/10"

    let response = await fetch(url);

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