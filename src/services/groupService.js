import axios from "axios"

const baseUrl = 'http://127.0.0.1:5000/groups/1'

const getGroup = () => {
    const request = axios.get(baseUrl)
    return request.then(response => response.data)
}

const addUser = () => {
    const user = {
        userID : 'U1100'
    }
    const request = axios.post(baseUrl, user)
    return request.then(response => response.data)
}

export default {getGroup, addUser}