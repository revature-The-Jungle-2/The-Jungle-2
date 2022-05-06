const allGroupSectionDiv = document.getElementById("groups-div");
const userGroupSectionDiv = document.getElementById("userGroups-div");
const url = "http://127.0.0.1:5000/";
const userId = 10;

async function getAllGroupsForUser() {
    let response = await fetch(url + "group");

    if (response.status === 200) {
        let body = await response.json();
        console.log(body);
        populateAllGroupsForUsers(body);
    } else {
        // alert("Error with groups");
    }
}

function populateAllGroupsForUsers(allGroupBody) {
    for (let groups in allGroupBody) {
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


async function getGroupsForUser() {
    let url = "http://127.0.0.1:5000/group/user/" + userId;

    let response = await fetch(url);

    if (response.status === 200) {
        let body = await response.json();
        console.log(body);
        populateGroupsForUsers(body);
    } else {
        // alert("Error with groups");
    }
}

function populateGroupsForUsers(groupBody) {
    for (let group in groupBody) {
        let groupsDiv = document.createElement("div");
        groupsDiv.setAttribute("class", "group-in-list");

        let groupImage = document.createElement("img");
        groupImage.setAttribute("class", "friend");

        let groupNameDiv = document.createElement("div");
        groupNameDiv.setAttribute("class", "name valign-text-middle poppins-bold-astronaut-22px");
        groupNameDiv.innerHTML = `<a onclick="goToGroupPages(${groupBody[group].groupId})" id="groupLink-${groupBody[group].groupId}" class="name valign-text-middle poppins-bold-astronaut-22px" href="../grouppage/individualgrouppage/individual-group-page.html">${groupBody[group].groupName}</a>`;
        localStorage.setItem("element", groupBody[group].groupId);

        userGroupSectionDiv.appendChild(groupsDiv);
        groupsDiv.appendChild(groupImage);
        groupsDiv.appendChild(groupNameDiv);

    }
}

function goToGroupPages(groupId) {
    localStorage.setItem("groupId", groupId);
}


/** -----------------------------------------------------Create Group------------------------------------------------------------ */
async function createGroup() {
    // const userId = localStorage.getItem("userId").value;
    const groupName = document.getElementById("groupName").value.trim();
    const groupAbout = document.getElementById("groupAbout").value.trim();
    let groupCreated = { "groupId": 0, "userId": userId, "groupName": groupName, "groupAbout": groupAbout, "imageFormat": "imageFormat" };

    let response = await fetch(url + "group/create", {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(groupCreated)
    });

    let groupObject = await response.json();

    if (groupObject.message) {
        let groupNameException = document.getElementById("duplicateGroupNameMessage");
        groupNameException.textContent = groupObject.message;
        duplicateGroupNameMessage.style.display = "block";

    } else {
        let messageGroupCreated = document.getElementById("messageGroupCreated");
        messageGroupCreated.style.display = "block";
        location.reload();
        getGroupsForUser();
        getAllGroupsForUser();
    }
}

getGroupsForUser();
getAllGroupsForUser();