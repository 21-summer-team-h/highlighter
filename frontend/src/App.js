import React from "react";
import './App.css';
import { BrowserRouter, Route } from "react-router-dom";
import SendLink from './Components/Views/sendLink';
import Result from './Components/Views/showResult';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route exact path = "/" component = { SendLink }></Route>
        <Route exact path = "/result" component = { Result }></Route>
      </BrowserRouter>
    </div>
  );
}

export default App;
