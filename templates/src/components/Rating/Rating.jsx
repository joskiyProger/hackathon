import React, { useState } from 'react'
import "./Rating.css"
import RatingBoard from '../RatingBoard/RatingBoard'
function Rating() {
    const [active,setActive] = useState("All")
  return (
    <div className='rating'>
        <ul className='rating-menu'>
            <li className={active==="all"?"active":""}>Мой Филиал</li>
            <li className={active==="my-college"?"active":""}>Все филиалы</li>
            <li className={active==="all-branches"?"active":""}>все резиденты</li>
        </ul>
        <RatingBoard />
    </div>
  )
}

export default Rating