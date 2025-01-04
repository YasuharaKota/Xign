import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

const Chart = () => {
    const { game_id, chart_id } = useParams();

    const [chartData, setChartData] = useState(null);
    const [oneLinerComment, setOneLinerComment] = useState('');
    const [detailedComment, setDetailedComment] = useState('');
    const [error, setError] = useState(null);

    // 譜面データ取得
    useEffect(() => {
        fetch(`/cms/charts/${chart_id}/`)
            .then(response => response.json())
            .then(data => {
                setChartData(data);
            })
            .catch(error => {
                console.error('Error fetching chart details:', error);
                setError('データ取得中にエラーが発生しました');
            });
    }, [chart_id]);

    // メモデータ取得
    useEffect(() => {
        fetch(`/cms/get_user_memo/${chart_id}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch memo data');
                }
                return response.json();
            })
            .then(data => {
                if (data && !data.error) {
                    setOneLinerComment(data.one_liner_comment || ""); // 修正: 適切なキーを使用
                    setDetailedComment(data.detailed_comment || "");  // 修正: 適切なキーを使用
                }
            })
            .catch(error => {
                console.error("Failed to fetch memo:", error);
                setError('メモの取得中にエラーが発生しました');
            });
    }, [chart_id]);

    const getCSRFToken = () => {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const [name, value] = cookies[i].trim().split('=');
            if (name === 'csrftoken') {
                return value;
            }
        }
        return null;
    };

    const handleSave = () => {
        const csrfToken = getCSRFToken();
        fetch(`/cms/upsert_user_memo/${chart_id}/`, {
            method: "POST",
            headers: { "Content-Type": "application/json", "X-CSRFToken": csrfToken },
            body: JSON.stringify({
                one_liner_comment: oneLinerComment,
                detailed_comment: detailedComment,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to update memo");
                }
                return response.json();
            })
            .then(data => {
                console.log(data.message);
            })
            .catch(error => {
                console.error("Failed to save memo:", error);
            });
    };

    if (error) {
        return <div>{error}</div>;
    }

    if (!chartData) {
        return <div>読み込み中...</div>;
    }

    return (
        <div className="container mt-5">
            <button className="btn btn-primary mb-4"
                onClick={() => window.location.href = `/${game_id}/charts`}>
                トップページに戻る
            </button>

            <h1>{chartData.music.title}</h1>
            <p>アーティスト: {chartData.music.artist_alias}</p>
            <p>BPM: {chartData.music.bpm_min}-{chartData.music.bpm_max}</p>
            <p>難易度: {chartData.difficulty.difficulty_name}</p>
            <p>Lv: {chartData.level.level_name}</p>
            <p>譜面定数: {chartData.chart_constant.constant_value}</p>
            <p>譜面制作者: {chartData.creator_alias.alias_name}</p>
            <hr />
            <h2>メモ</h2>
            <div className="mb-3">
                <p>ひとこと:</p>
                <textarea
                    className="form-control"
                    rows="3"
                    placeholder="ひとこと"
                    value={oneLinerComment}
                    maxLength={255}
                    onChange={(e) => setOneLinerComment(e.target.value)}
                />
            </div>
            <div className="mb-3">
                <p>メモ:</p>
                <textarea
                    className="form-control"
                    rows="6"
                    placeholder="メモ"
                    value={detailedComment}
                    onChange={(e) => setDetailedComment(e.target.value)}
                />
            </div>
            <button className="btn btn-primary" onClick={handleSave}>
                メモを保存
            </button>
        </div>
    );
};

export default Chart;