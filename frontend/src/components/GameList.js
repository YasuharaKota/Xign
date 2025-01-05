import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const GameList = () => {
    const [games, setGames] = useState([]);

    useEffect(() => {
        // APIからゲームのデータを取得する
        fetch('/cms/games/')
            .then(response => response.json())
            .then(data => setGames(data))
            .catch(error => console.error('Error fetching games:', error));
    }, []);

    return (
        <div>
            <h1>ゲーム一覧</h1>
            <ul>
                {games.map((game, index) => (
                    <li key={index}>
                        <a href={`/${game.game_id}/charts`}>{game.game_name}</a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default GameList;