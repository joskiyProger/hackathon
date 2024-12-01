import React from "react";
import { useState, useEffect } from "react";
import { assets } from "../../assets/assets.js";
import "./Navbar.css";
function Navbar() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        console.log(response.json());

        return response.json();
      })
      .then((user) => setData(user.employees)) // Assuming your JSON structure
      .catch((error) => setError(error.message));
  }, []);

  return (
    <div className="navbar">
      <p>Привет, </p>
      <img className="ava" src={assets.ava} alt="" />
    </div>
  );
}

export default Navbar;
