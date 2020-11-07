import axios from "axios"

const baseUrl = 'http://127.0.0.1:5000/groups/1'

const getGroup = () => {
    const request = axios.get(baseUrl)
    return request.then(response => response.data)
}

const addUser = async newObj => {
    console.log(newObj)
    const request = axios.post(baseUrl, newObj)
    return request.then(response => response.data)
}

export default {getGroup, addUser}