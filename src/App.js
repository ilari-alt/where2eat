import React, {useState,useEffect} from 'react'
import groupService from './services/groupService'

const App = () =>{
  const [startPage, showStartPage] = useState(true)
  const [groupNamePage, showGroupNamePage] = useState(false)
  const [groupViewPage, showGroupViewPage] = useState(false)
  const [group, setGroup] = useState('')


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
    const groupObj = {
      groupID : `${group}`
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

    const handleSubmit = (event) => {
      event.preventDefault()
      console.log(event.target.value)
      setGroup(event.target.value)
    }

    if(!groupNamePage){
      return(
        null
      )
    }
    return(
      <div>
        <div>Enter group name</div>
        <form onSubmit = {joinToGroupPage}>
          <input onChange = {({target}) => setGroup(target.value)}></input>
          <button type = "submit">JOIN</button>
        </form>
      </div>
    )
  }

  return(
    <div>
      <h1> OPT2EAT </h1> 
      <StartPage></StartPage>
      <FindGroupPage></FindGroupPage>
      <GroupPage></GroupPage>
      <button onClick = {handleBackButton}>Back</button>
    </div>
  )
}

export default App
