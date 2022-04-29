
const allGroupSectionDiv = document.getElementById("groups-div");





async function getAllGroupsForUser(){
    let url = "http://127.0.0.1:5000/group"

    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateAllGroupsForUsers(body);
    }
    else{
        alert("Error with groups");
    }
}

function populateAllGroupsForUsers(allGroupBody){
    for (let groups in allGroupBody){
        let allGroupsDiv = document.createElement("div");
        allGroupsDiv.setAttribute("class", "group-in-list");

        let groupImage1 = document.createElement("img");
        groupImage1.setAttribute("class", "friend");


        let allGroupNameDiv = document.createElement("div");
        allGroupNameDiv.setAttribute("class", "name valign-text-middle poppins-bold-astronaut-22px");
        allGroupNameDiv.innerHTML = `<a onclick=goToGroupPage(${allGroupBody[groups].groupId}); id="groupLink-${allGroupBody[groups].groupId}" class="name valign-text-middle poppins-bold-astronaut-22px" href = individualgrouppage/individual-group-page.html >${allGroupBody[groups].groupName}</a>`;


        allGroupSectionDiv.appendChild(allGroupsDiv);
        allGroupsDiv.appendChild(groupImage1);
        allGroupsDiv.appendChild(allGroupNameDiv);


    }
   
}

function goToGroupPage(groupId){
    localStorage.setItem("groupId", groupId);
    console.log(localStorage.getItem("groupId"))
    
}
// async function getGroup() {
//     groupId = localStorage.getItem("groupId")

//     let response = await fetch(url + `/group/${groupId}`)

//     if(response.status === 200){
//         let body = await response.json()
//         console.log(body)
//         // groupdef = document.getElementById("groupName")
//         // groupdef.innerHTML = body

//     }
    
// }

getAllGroupsForUser();