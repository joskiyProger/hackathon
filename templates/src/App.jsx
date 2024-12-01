import React from "react";
import Rating from "./components/Rating/Rating";
import Navbar from "./components/Navbar/Navbar";
import UserInfo from "./components/UserInfo/UserInfo";

const App = () => {
  return (
    <div>
      <Navbar />
      <div className="contain">
        <Rating />
        <UserInfo />
      </div>
    </div>
  );
};

export default App;
