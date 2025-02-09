import React from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import GameList from './GameList';
import Home from "./Home";
import GameChartList from "./GameChartList";
import 'bootstrap/dist/css/bootstrap.min.css';
import Chart from "./Chart";

const App = () => {

    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/games" element={<GameList/>}/>
                <Route path="/:game_id/charts" element={<GameChartList/>}/>
                <Route path="/:game_id/charts/:chart_id" element={<Chart/>}/>
            </Routes>
        </Router>
    );
};

export default App;