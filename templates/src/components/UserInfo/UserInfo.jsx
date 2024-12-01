import React from "react";
import "./UserInfo.css";
function UserInfo() {
  const chartData = [
    { day: "пн", value: 60 },
    { day: "вт", value: 80 },
    { day: "ср", value: 50 },
    { day: "чт", value: 70 },
    { day: "пт", value: 40 },
    { day: "сб", value: 90 },
    { day: "вс", value: 30 },
  ];
  return (
    <div className="user-info">
      <div className="stats-card">
        <h2 className="">136</h2>
        <p className="">ОЧКОВ</p>
        <div className="stats-grid">
          <div className="stat-item">
            <h3 className="text-2xl font-bold">20</h3>
            <p className="text-xs text-gray-400">мой филиал</p>
          </div>
          <div className="stat-item">
            <h3 className="text-2xl font-bold">48</h3>
            <p className="text-xs text-gray-400">среди всех резидентов</p>
          </div>
          <div className="stat-item">
            <h3 className="text-2xl font-bold">3</h3>
            <p className="text-xs text-gray-400">место филиала</p>
          </div>
        </div>
      </div>
      <div className="chart-container">
        <div className="chart">
          {chartData.map((item, index) => (
            <div key={item.day} className="chart-bar">
              <div
                
                style={{ height: `${item.value}%` }}
              ></div>
              <span className="chart-label">{item.day}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default UserInfo;
