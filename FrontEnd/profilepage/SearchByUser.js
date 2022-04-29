const url = "http://localhost:8080";
const searchField = document.getElementById("searchInputBox");
const searchListResults = document.getElementById("searchList");
function referToProfile(userId) {
    localStorage.setItem("targetId", userId);
    location.href="profile-page.html";
}
const searchUserButton = document.getElementById("searchButton");


const searchByUsername = async() => {
    const username = searchField.value
    const response = await fetch(url + "/user/search/" + username,{
        method: "GET", 
        mode: "cors" 
    });
    console.log(response);
    console.log(username);
    document.getElementById("searchList").innerHTML = "";
    if (response.status === 200) {
        const body = await response.json();
        if (body.searchResult.length === 0) {
            searchListResults.style.display="block";
            document.getElementById("searchList").innerHTML += `<li class="list-group-item">No Results</li>`;
        } else {
            for (let user of body.searchResult) {
                searchListResults.style.display="block";
                document.getElementById("searchList").innerHTML += `<li class="list-group-item"><a onclick=referToProfile(${user.userId})>${user.username}</a></li>`;
            }
        }
    }
}
searchUserButton.addEventListener("click", searchByUsername);

