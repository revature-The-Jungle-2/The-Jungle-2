// small helper function for selecting element by id
let id = (id) => document.getElementById(id);


storage = JSON.parse(localStorage.getItem("userInfo"));

let ws;
function createChatConnection(groupId) {

    id("chat").innerHTML = "";
    ws = new WebSocket(
      "ws://" +
        "localhost" +
        ":" +
        "8080" +
        "/chat/" +
        groupId +
        "/" +
        storage.username
    );

    ws.onmessage = (msg) => updateChat(msg, ws);
    ws.onclose = () => alert("Connecting to new chat");
  
}

function sendAndClear(message) {
  if (message !== "") {
    let msg = {
      userId: "" + storage.userId,
      userName: storage.username,
      chatContent: id("message").value,
    };
    ws.send(JSON.stringify(msg));
    id("message").value = "";
  }
}

function updateChat(msg) {
  let data = JSON.parse(msg.data);

  //Resets the file input
  document.getElementById("imgInput").value = null;

  if (data.userList === undefined) {
    //if data is a string then it's Base64 code for an image
    if (typeof data.imgContent === "string") {
      var chatImg = new Image();
      chatImg.src = "data:image/png;base64," + data.imgContent;

      //if its a message from current user then make right side chat bubble
      if (data.userName === storage.username) {
        id("chat").insertAdjacentHTML(
          "beforeend",
          "<div class='overlap-group5'>" +
            "<div class='check-the-documentation valign-text-middle poppins-medium-white-18px'>" +
            "<img src=" +
            chatImg.src +
            " style='width: auto; height: 93px;'>" +
            "</div>"
        );
      } //else its an incoming message
      else {
        id("chat").insertAdjacentHTML(
          "beforeend",
          "<div class='received-message-1'>" +
            "<img class='ellipse-1' src='img/ellipse-1@2x.png' />" +
            "<div class='overlap-group6'>" +
            "<div class='where-are-the-user-stories valign-text-middle poppins-medium-black-18px'>" +
            "<img src=" +
            chatImg.src +
            " style='width: auto; height: 93px;'>" +
            "</div>" +
            "</div>" +
            "</div>"
        );
      }
    }
    //Else it's a normal message object
    else {
      //if its a message from current user then make right side chat bubble
      if (data.userName === storage.username) {
        id("chat").insertAdjacentHTML(
          "beforeend",
          "<div class='overlap-group5'>" +
            "<div class='check-the-documentation valign-text-middle poppins-medium-white-18px'>" +
            data.chatContent +
            "</div>"
        );
      } else {
        id("chat").insertAdjacentHTML(
          "beforeend",
          "<div class='received-message-1'>" +
            "<a>" +
            data.userName +
            "</a>" +
            "<div class='overlap-group6'>" +
            "<div class='where-are-the-user-stories valign-text-middle poppins-medium-black-18px'>" +
            data.chatContent +
            "</div>" +
            "</div>" +
            "</div>"
        );
      }
    }
  } else {
    updateUserList(data.userList);
  }
}

function updateUserList(userList) {
  id("chatList").innerHTML = "";
  const unique = [...new Set(userList)];
  for (let a of unique) {
    id(
      "chatList"
    ).innerHTML += `<li class="list-group-item" style="margin-right: 0.2em;"><img src="img/online.png" style="width:0.5em;height:0.5em;"> <span style="color:#20316ee8"> ${a}</span></li>`;
  }
}

//inputing file img type
window.addEventListener("load", function () {
  if (this.files === undefined) {
    id("send").addEventListener("click", () =>
      sendAndClear(id("message").value)
    );
    id("message").addEventListener("keypress", function (e) {
      if (e.keyCode === 13) {
        // Send message if enter is pressed in input field
        sendAndClear(e.target.value);
      }
    });
  }
  document
    .querySelector('input[type="file"]')
    .addEventListener("change", function () {
      if (this.files && this.files[0]) {
        var img = document.querySelector("img");

        if (this.files[0].size >= 65536) {
          //Resets the file input
          document.getElementById("imgInput").value = null;
          alert("File is too big to send");
        } else
          id("send").addEventListener("click", () => ws.send(this.files[0]));
      }
    });
});

const chatGroupDiv = document.getElementById("chatGroupName");
chatGroupDiv.setAttribute(
  "style",
  "margin-top:5em;max-height:350px;overflow-y:auto;"
);

//Displaying the Group Names by grabbing the userId's to display the names on the top right...
async function getAllGroupByUserId() {
  let url = "http://localhost:8080/user/groupNames/" + storage.userId;
  let response = await fetch(url);
  if (response.status === 200) {
    let body = await response.json();
    populateGroupNameByUserId(body);
  } else {
    alert("There was a problem trying to display the group data: apologies!");
  }
}

//This is to populate the Group Names from grabbing the UserId's...
function populateGroupNameByUserId(groupName) {
  for (let groupId in groupName) {
    let chatDivGroupNames = document.createElement("div");
    chatDivGroupNames.setAttribute("class", "chat-in-list");

    let chatDivImage = document.createElement("img");
    chatDivImage.setAttribute("class", "friend");

    let chatDiv = document.createElement("div");
    chatDiv.setAttribute("id", groupId);
    chatDiv.setAttribute(
      "class",
      "name valign-text-middle poppins-bold-astronaut-22px"
    );
    chatDiv.innerText = groupName[groupId];
    chatGroupDiv.appendChild(chatDivGroupNames);
    chatDivGroupNames.appendChild(chatDivImage);
    chatDivGroupNames.appendChild(chatDiv);

    chatDiv.addEventListener("click", function (e) {
      if (e.target && e.target.id === groupId) {
        if (ws.readyState === WebSocket.OPEN) {
            ws.close();
         }
      
        createChatConnection(e.target.id);
      }
    });
  }
}
getAllGroupByUserId();
