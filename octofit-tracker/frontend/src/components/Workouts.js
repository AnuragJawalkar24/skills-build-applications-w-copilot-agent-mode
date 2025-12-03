import React, { useEffect, useState } from 'react';
const codespace = process.env.REACT_APP_CODESPACE_NAME;
const endpoint = codespace ? `https://${codespace}-8000.app.github.dev/api/workouts/` : 'http://localhost:8000/api/workouts/';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Workouts endpoint:', endpoint);
        console.log('Fetched data:', data);
        setWorkouts(data.results || data);
      });
  }, []);
  return (
    <div className="card p-4">
      <h2 className="card-title text-primary">Workouts</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="thead-dark">
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Description</th>
              <th>Suggested For</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, idx) => (
              <tr key={workout.id || idx}>
                <td>{idx + 1}</td>
                <td>{workout.name}</td>
                <td>{workout.description}</td>
                <td>{workout.suggested_for}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
export default Workouts;
