/** -----------------------------------------------------Join Group------------------------------------------------------------ */
// let url = "http://127.0.0.1:5000";
// const groupId = 1;
// const userId = 10;

async function joinGroup() {
    let url = "http://127.0.0.1:5000";
    const groupId = 1;
    const userId = 10;


    // const groupId = localStorage.getItem("groupId").value;
    // const userId = localStorage.getItem("userId").value;


    let response = await fetch(url + "/group/join/" + groupId + "/" + userId);
    if (response.status === 200) {
        console.log(response);
        const groupJoined = document.getElementById("groupJoined");
        groupJoined.style.display = "block";
        setTimeout(fade_out, 5000);
        const hideJoinButton = document.getElementById("submitJoinGroup");
        hideJoinButton.style.display = "none";
    } else {
        console.log(response.status);
        const groupNotJoined = document.getElementById("groupNotJoined");
        groupNotJoined.style.display = "block";
    }
}

function fade_out() {
    document.getElementById("groupJoined").style.display = "none";
}