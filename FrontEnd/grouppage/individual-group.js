/** -----------------------------------------------------Join Group------------------------------------------------------------ */
const devUrlPython="http://ec2-204-236-138-16.us-west-1.compute.amazonaws.com:5000"

async function joinGroup() {
    // const groupId = localStorage.getItem("groupId").value;
    // const userId = localStorage.getItem("userId").value;
    const groupId = 7;
    const userId = 9000;

    let response = await fetch(devUrlPython + `/group/join/${groupId}/${userId}`, {method: "POST", mode: "cors",
        headers: {"Content-Type": "application/json"}});
    
    await response.json();   


    if (response.status === 200) {
        const groupJoined = document.getElementById("groupJoined");
        groupJoined.style.display = "block";
        setTimeout(fade_out, 5000);
        const hideJoinButton = document.getElementById("submitJoinGroup");
        hideJoinButton.style.display = "none";
    }
    else {

        const groupNotJoined = document.getElementById("groupNotJoined");
        groupNotJoined.style.display = "block";
    }
}

function fade_out() {
    document.getElementById("groupJoined").style.display = "none";
}

const submitJoinGroup = document.getElementById("submitJoinGroup");
submitJoinGroup.addEventListener("click", joinGroup);