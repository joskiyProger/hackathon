import React from "react";
import { assets } from "../../assets/assets.js";
import "./Navbar.css";
function Navbar() {
  return (
    <div className="navbar">
      <p>Привет, no name</p>
      <img className="ava" src={assets.ava} alt="" />
    </div>
  );
}

export default Navbar;
