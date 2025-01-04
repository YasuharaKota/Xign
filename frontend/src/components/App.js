import React from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import GameList from './GameList';
import Home from "./Home";

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/games" element={<GameList/>}/>
            </Routes>
        </Router>
    );
};

export default App;