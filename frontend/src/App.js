import React from "react";
import './App.css';
import { BrowserRouter, Route } from "react-router-dom";
import SendLink from './pages/sendLink';
import ShowClips from './pages/showClips';
import ShowResult from './pages/showResult';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route exact path = "/" component = { SendLink }></Route>
        <Route exact path = "/clips" component = { ShowClips }></Route>
        <Route exact path = "/result" component = { ShowResult }></Route>
      </BrowserRouter>
    </div>
  );
}

export default App;
