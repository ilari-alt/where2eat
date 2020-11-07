import React, {useState,useEffect} from 'react'
import groupService from './services/groupService'

const App = (props) =>{
  const [startPage, showStartPage] = useState(true)
  const [groupNamePage, showGroupNamePage] = useState(false)
  const [groupViewPage, showGroupViewPage] = useState(false)

  const [newGroup, setGroup] = useState('')

  const [newUserID, setNewUserID] = useState('')
  const [userID, setUser] = useState('')


  const loadJoinPage = () =>{
    showStartPage(!startPage)
  }

  const loadShowGroupNamePage = () =>{
    showGroupNamePage(!groupNamePage)
  }

  const loadGroupViewPage = () => {
    showGroupViewPage(!groupViewPage)
  }

  const startToJoinPage = () =>{
    loadJoinPage()
    loadShowGroupNamePage()
  }

  const joinToGroupPage = (event) =>{
    event.preventDefault()
    console.log(event.target)
    const groupObj = {
      userID : 'U1234'
    }
    setGroup(groupService.addUser(groupObj))
    loadShowGroupNamePage()
    loadGroupViewPage()
  }
  
  const handleBackButton = () => {
    showStartPage(true)
    showGroupNamePage(false)
    showGroupViewPage(false)
  }

  const handleUserID = (event) => {
    console.log(event.target.value)
    setNewUserID(event.target.value)
  }

  const StartPage = () =>{
    if(!startPage){
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
            <button onClick = {startToJoinPage}>JOIN</button>
        </div>
    )
  }

  const GroupPage = () =>{
    const people = ["Heikki", "Teemu", "Matti"]
    if(!groupViewPage){
      return null
    }
    return(
      <div>
        <div>Your group:</div>
        {people.map(p => 
          <li key = {p}>{p}</li>
        )}
      </div>
    )
  }

  const FindGroupPage = () => {

    if(!groupNamePage){
      return(
        null
      )
    }
    return(
      <div>
        <form onSubmit = {joinToGroupPage}>
          <div>Enter user id</div>
          <input 
            type = "text"
            value = {newUserID}
            onChange = {handleUserID}
          />
          <div>Enter group name</div>
          <input></input>
          <button type = "submit">JOIN</button>
        </form>
      </div>
    )
  }

  return(
    <div>

      <h1> OPT2EAT </h1> 
      <h2> Join a group:</h2>
      <div>
        <form onSubmit = {joinToGroupPage}>
          <div>Enter your user id</div>
          <input 
            type = "text"
            value = {newUserID}
            onChange = {handleUserID}
          />
          <div>Enter group id you want to join</div>
          <input></input>
          <button type = "submit">JOIN</button>
        </form>
      </div>
      <GroupPage></GroupPage>
    </div>
  )
}
//<button onClick = {handleBackButton}>Back</button>
//      <StartPage></StartPage>
//<FindGroupPage></FindGroupPage>
export default App
