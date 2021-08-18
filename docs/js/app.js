'use strict'

let file = "fetch_info.txt"
let url = 'https://randomuser.me/api/?results=5&nat=gb'
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
            const html = data.results
                .map(user => {
                    return `
                    <div class="card">
                        <img alt=${user.first_name} class="card--avatar" src="${user.picture.medium}" />
                        <h1 class="card--title">${user.email}</h1>
                        <h1 class="card--title">Phone:${user.phone} </h1>
                        <h1 class="card--title">Cell:${user.cell}</h1>
                        <a  class="card--link" href="#">${user.name.first} ${user.name.last}</a>
                        
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

fetchData();