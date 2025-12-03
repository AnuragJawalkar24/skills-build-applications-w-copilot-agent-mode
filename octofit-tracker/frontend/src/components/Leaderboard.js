import React, { useEffect, useState } from 'react';
const codespace = process.env.REACT_APP_CODESPACE_NAME;
const endpoint = codespace ? `https://${codespace}-8000.app.github.dev/api/leaderboard/` : 'http://localhost:8000/api/leaderboard/';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard endpoint:', endpoint);
        console.log('Fetched data:', data);
        setLeaderboard(data.results || data);
      });
  }, []);
  return (
    <div className="card p-4">
      <h2 className="card-title text-primary">Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="thead-dark">
            <tr>
              <th>#</th>
              <th>Team</th>
              <th>Points</th>
              <th>Week</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry, idx) => (
              <tr key={entry.id || idx}>
                <td>{idx + 1}</td>
                <td>{entry.team?.name || 'Team'}</td>
                <td>{entry.points}</td>
                <td>{entry.week}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default Leaderboard;
