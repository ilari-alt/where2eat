
import React, {useState} from 'react'
import groupService from '../services/groupService'



const FindGroupPage = () => {
    const [groupNamePage, showGroupNamePage] = useState(false)
    const [newGroup, setGroup] = useState('')
    const [newUserID, setNewUserID] = useState('')
    const [userID, setUser] = useState('')
    const [groupViewPage, showGroupViewPage] = useState(false)

    const loadGroupViewPage = () => {
        showGroupViewPage(!groupViewPage)
      }

    const handleUserID = (event) => {
        console.log(event.target.value)
        setNewUserID(event.target.value)
      }
    
    const loadShowGroupNamePage = () =>{
        showGroupNamePage(!groupNamePage)
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

export default FindGroupPage