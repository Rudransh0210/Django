import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import React from 'react';
import LoginPage from "./pages/Login";
import HomePage from './pages/Home';
const App = () => {
    return (
    <Router>
      <Routes>
        <Route path="" element={<LoginPage/>}/>
        <Route path = '/main' element={<HomePage/>}/>
      </Routes>
    </Router>
  );
}

export default App;
