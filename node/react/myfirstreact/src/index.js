import React from 'react';
// eslint-disable-next-line
import ReactDOM from 'react-dom';

// const myfirstelement = <h1>Hello steve to React!</h1>

// ReactDOM.render(myfirstelement, document.getElementById('root'));

// const myelement = (
//     <table>
//       <tr>
//         <th>Name</th>
//       </tr>
//       <tr>
//         <td>John</td>
//       </tr>
//       <tr>
//         <td>Elsa</td>
//       </tr>
//     </table>
//   );
  
//   ReactDOM.render(myelement, document.getElementById('root'));
//   ReactDOM.render(myelement, document.getElementById('foot'));

// class Car extends React.Component {
//     render() {
//       return <h2>I am a Car!</h2>;
//     }
//   }
  
//   class Garage extends React.Component {
//     render() {
//       return (
//         <div>
//         <h1>Who lives in my Garage?</h1>
//         <Car />
//         </div>
//       );
//     }
//   }
  
//   ReactDOM.render(<Garage />, document.getElementById('root'));

// import Car from './App.js';

// ReactDOM.render(<Car />, document.getElementById('root'));

// class Car extends React.Component {
//     render() {
//       return <h2>I am a {this.props.brand}!</h2>
//     }
//   }
  
//   const myelement = <Car brand="Ford" />;
  
//   ReactDOM.render(myelement, document.getElementById('root'));

// class Car extends React.Component {
//     render() {
//       return <h2>I am a {this.props.brand}!</h2>;
//     }
//   }
  
//   class Garage extends React.Component {
//     render() {
//       return (
//         <div>
//         <h1>Who lives in my garage?</h1>
//         <Car brand="Ford" />
//         </div>
//       );
//     }
//   }
  
//   ReactDOM.render(<Garage />, document.getElementById('root'));

// class Car extends React.Component {
//   render() {
//     return <h2>I am a {this.props.brand.model}!</h2>;
//   }
// }

// class Garage extends React.Component {
//   render() {
//     const carinfo = {name: "Ford", model: "Mustang"};
//     return (
//       <div>
//       <h1>Who lives in my garage?</h1>
//       <Car brand={carinfo} />
//       </div>
//     );
//   }
// }

// ReactDOM.render(<Garage />, document.getElementById('root'));

// class Car extends React.Component {
//     render() {
//       return <h2>I am a {this.props.brand.model}!</h2>;
//     }
//   }
  
//   class Garage extends React.Component {
//     render() {
//       const carinfo = {name: "Ford", model: "Mustang"};
//       return (
//         <div>
//         <h1>Who lives in my garage?</h1>
//         <Car brand={carinfo} />
//         </div>
//       );
//     }
//   }
  
//   ReactDOM.render(<Garage />, document.getElementById('root'));

// class Car extends React.Component {
//     constructor(props) {
//       super(props);
//       this.state = {
//         brand: "Ford",
//         model: "Mustang",
//         color: "red",
//         year: 1964
//       };
//     }
//     changeColor = () => {
//       this.setState({color: "blue"});
//     }
//     render() {
//       return (
//         <div>
//           <h1>My {this.state.brand}</h1>
//           <p>
//             It is a {this.state.color} {this.state.model} from {this.state.year}.
//           </p>
//           <button
//             type="button"
//             onClick={this.changeColor}
//           >Change color</button>
//         </div>
//       );
//     }
//   }
  
//   ReactDOM.render(<Car />, document.getElementById('root'));

// class MyForm extends React.Component {
//     constructor(props) {
//       super(props);
//       this.state = { username: '' };
//     }
//     myChangeHandler = (event) => {
//       this.setState({username: event.target.value});
//     }
//     render() {
//       return (
//         <form>
//         <h1>Hello {this.state.username}</h1>
//         <p>Enter your name:</p>
//         <input
//           type='text'
//           onChange={this.myChangeHandler}
//         />
//         </form>
//       );
//     }
//   }
  
//   ReactDOM.render(<MyForm />, document.getElementById('root'));
  

// class MyForm extends React.Component {
//     constructor(props) {
//       super(props);
//       this.state = {
//         username: '',
//         age: null,
//         errormessage: ''
//       };
//     }
//     myChangeHandler = (event) => {
//       let nam = event.target.name;
//       let val = event.target.value;
//       let err = '';
//       if (nam === "age") {
//         if (val !="" && !Number(val)) {
//           err = <strong>Your age must be a number</strong>;
//         }
//       }
//       this.setState({errormessage: err});
//       this.setState({[nam]: val});
//     }
//     render() {
//       return (
//         <form>
//         <h1>Hello {this.state.username} {this.state.age}</h1>
//         <p>Enter your name:</p>
//         <input
//           type='text'
//           name='username'
//           onChange={this.myChangeHandler}
//         />
//         <p>Enter your age:</p>
//         <input
//           type='text'
//           name='age'
//           onChange={this.myChangeHandler}
//         />
//         {this.state.errormessage}
//         </form>
//       );
//     }
//   }
  
//   ReactDOM.render(<MyForm />, document.getElementById('root'));

import './App.css';

class MyHeader extends React.Component {
  render() {
    return (
      <div>
      <h1>Hello Style!</h1>
      <p>Add a little style!.</p>
      </div>
    );
  }
}

ReactDOM.render(<MyHeader />, document.getElementById('root'));

/*
Notice that you now have three files in your project:
'index.js', 'index.html', and 'App.css'.
*/
