//  main.js
url = "http://127.0.0.1:8000/users/"

function listUser() {
    //  GET request using fetch()
    fetch(url)
        // Converting received data to JSON
        .then(response => response.json())
        .then(json => {
            console.log(json);
            // Create a variable to store HTML
            let li = `<tr><th>Name</th><th>Email</th></tr>`;
            // Loop through each data and add a table row
            json.forEach(user => {
                li += `<tr>
                    <td>${user.username} </td>
                    <td>${user.email}</td>
                </tr>`;
            });
            // Display result
            document.getElementById("users").innerHTML = li;
        });
}

function addUserName(username) {
    // POST request using fetch()
    fetch(url, {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: JSON.stringify({
            username: username
        }),
        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        // Converting to JSON
        .then(response => response.json())
        // Displaying results to console
        .then(json => console.log(json));
    alert(username + " was submitted");
}

function menuFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

listUser();