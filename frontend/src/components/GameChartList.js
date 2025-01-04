import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

const GameChartList = () => {
    const {game_id} = useParams();
    const [charts, setCharts] = useState([]);
    const [gameName, setGameName] = useState('');

    useEffect(() => {
        // APIから譜面一覧を取得する
        fetch(`/cms/charts/game/${game_id}`)
            .then(response => response.json())
            .then(data => {
                console.log("API Response:", data); // APIレスポンスを出力
                setCharts(data);
            })
            .catch(error => console.error('Error fetching games:', error));
    }, [game_id]);

    useEffect(() => {
        // game_idに対応するgame_nameを取得する
        fetch(`/cms/games/${game_id}/`)
            .then(response => response.json())
            .then(data => {
                console.log("Game Name API Response:", data);
                setGameName(data.game_name);
            })
            .catch(error => console.error('Error fetching game name:', error));
    }, [game_id]);

    return (
        <div className="container mt-5">
            {/* トップページリンク */}
            <button className="btn btn-primary mb-4"
                    onClick={() => window.location.href = '/games'}>トップページに戻る
            </button>

            <h1 className="text-center mb-4">{gameName} 譜面一覧</h1>

            {/* グリッドシステムを使ったカードレイアウト */}
            <div className="row">
                {charts.map((chart, index) => (
                    <div className="col-md-4 mb-4" key={index}>
                        <div className="card">
                            <div className="card-body">
                                {/* 曲名の表示 */}
                                <h5 className="card-title">{chart.music.title}</h5>

                                {/* 難易度の表示 */}
                                <p className="card-text">
                                    難易度: {chart.difficulty.difficulty_name}<br/>
                                    レベル: {chart.level.level_name}
                                </p>

                                {/* 詳細リンク */}
                                <a href={`/${game_id}/charts/${chart.chart_id}`} className="btn btn-outline-primary">詳細を見る</a>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default GameChartList;