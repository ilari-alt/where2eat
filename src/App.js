import './App.css'
import React, {useState,useEffect} from 'react'
import ReactDOM from 'react-dom'


const App = () =>{
  const [city, setCity] = useState('')
  const [country, setCountry] = useState('')

  const handleSearchInfo = async (event) =>{
    event.preventDefault()
    console.log(city)
    console.log(country)
  }

  const handleSetCountry = (event) => {
    event.preventDefault()
    setCountry(event.target.value)
  }

  const handleSetCity = (event) => {
    event.preventDefault()
    setCity(event.target.value)
  }

  return(
    <div>
      hello
      <form onSubmit={handleSearchInfo}>
        <input type="text" value = {country} onChange={handleSetCountry}/>
        <input type = "text" value = {city} onChange = {handleSetCity} />
        <button type = "submit">GO!</button>
      </form>
    </div>

  )
}

export default App;
