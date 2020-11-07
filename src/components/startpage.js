import React, { useState } from 'react'

const StartPage = () =>{
    const [startPageVisible, setStartPageVisible] = useState(true)

    const loadJoinPage = () =>{
        setStartPageVisible(!startPageVisible)
      }
    
    if(!startPageVisible){
      return(
        null
      )
    }
    return(
        <div>
            <div>
                Create a group or join an existing one
            </div>
            <button>CREATE</button>
            <button onClick = {loadJoinPage}>JOIN</button>
        </div>
    )
  }

export default StartPage