'use strict'

let file = "fetch_info.txt"
// let url = 'https://randomuser.me/api/?results=5&nat=gb'
let url = 'http://127.0.0.1:8000/star-wars/species/'
// 'http://worldtimeapi.org/api/timezone/Europe/London.txt

// Check that service workers are supported
if ('serviceWorker' in navigator) {
    // Use the window load event to keep the page load performant
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('service-worker.js');
    });
}

function fetchData() {
    fetch(url)
        .then(response => {
            // console.log(response);
            if (!response.ok) {
                throw error('ERROR');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            const html = data  //.results
                .map(user => {
                    return `
                    <div class="card">
                        <h1 class="card--title">${user.name}</h1>
                        <h1 class="card--title">${user.classification} </h1>
                        <a  class="card--link" href="#">${user.language}</a>
                    </div>
                    `;
                })
                .join("");
            // console.log(html);
            document
                .querySelector('.container')
                .insertAdjacentHTML("afterbegin", html);
        })
        .catch(error => {
            console.log(error);
        });
}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function postData() {
    fetch(url, {
        method: 'POST',
        body: JSON.stringify({
            name: 'John',
            classification: "Mammal",
            language: "Galatic Basic"
    }),
    headers: {
        "content-type": "application/json; charset=UTF-8"
    }
    })
        .then(response => response.json())
        .then(data => console.log(data));
}

function updateData() {
    fetch(url, {
        method: 'PUT',
        body: JSON.stringify({
            name: 'John',
            classification: "Mammal",
            language: "Galatic BasicS"
    }),
    headers: {
        "content-type": "application/json; charset=UTF-8"
    }
    })
        .then(response => response.json())
        .then(data => console.log(data));
}

function deleteData() {
    fetch(url, {
        method: 'DELETE',
        headers: {
            "content-type": "application/json; charset=UTF-8"
        }
    })
        .then(response => response.json())
        .then(data => console.log(data));
}


fetchData();
// postData();
// updateData(); //PUT NOT WORKING
