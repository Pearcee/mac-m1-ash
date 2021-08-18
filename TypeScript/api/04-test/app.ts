const container = document.querySelector(".container")
const app = document.getElementById("app");
const p = document.createElement("p");
const q = document.createElement("q");
p.innerHTML = "Hello, Steve!";
app?.appendChild(p);

const coffees = [
  { name: "Perspiciatis", image: "images/coffee1.jpg" },
  { name: "Voluptatem", image: "images/coffee2.jpg" },
  { name: "Explicabo", image: "images/coffee3.jpg" },
  { name: "Rchitecto", image: "images/coffee4.jpg" },
  { name: "Beatae", image: "images/coffee5.jpg" },
  { name: "Vitae", image: "images/coffee6.jpg" },
  { name: "Inventore", image: "images/coffee7.jpg" },
  { name: "Veritatis", image: "images/coffee8.jpg" },
  { name: "Accusantium", image: "images/coffee9.jpg" },
]

const showCoffees = () => {
    let output = '<h1>Title</h1>'
    coffees.forEach(
      ({ name, image }) =>
        (output += `
                <div class="card">
                  <img alt="Coffee" class="card--avatar" src=${image} />
                  <h1 class="card--title">${name}</h1>
                  <a class="card--link" href="#">Taste</a>
                </div>
                `)
    )
    p.innerHTML= output;
    app?.appendChild(p);
  }
  
  showCoffees();  

if ("serviceWorker" in navigator) {
    window.addEventListener("load", function() {
      navigator.serviceWorker
        .register("serviceWorker.js")
        .then(res => console.log("service worker registered"))
        .catch(err => console.log("service worker not registered", err));
    });
  }
  