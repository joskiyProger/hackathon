import React from "react";
import "./RatingBoard.css"
import { Star } from 'lucide-react';
function RatingBoard() {
  const listItems = [
    { id: 1, name: "Item 1" },
    { id: 2, name: "Item 2" },
    { id: 3, name: "Item 3" },
    { id: 4, name: "Item 4" },
    { id: 5, name: "Item 5" },
    { id: 6, name: "Item 6" },
    { id: 4, name: "Item 4" },
    { id: 5, name: "Item 5" },
    { id: 6, name: "Item 6" },
    { id: 4, name: "Item 4" },
    { id: 5, name: "Item 5" },
    { id: 6, name: "Item 6" },
  ];
  return (
    <div className="rating-comp">
      <div className="rating-board">
        {/* List */}
        <div className="rating-items">
          {listItems.map((item) => (
            <div
              key={item.id}
              className="rating-item"
            >
              {item.id <= 3 ? (
                <Star className="star"/>
              ) : (
                <span className="item-without-star">
                  {item.id}
                </span>
              )}
              <span className="user-name">{item.name}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default RatingBoard;
