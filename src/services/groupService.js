import axios from "axios"

const baseUrl = 'placehold'


const getGroup = () => {
    const request = axios.get(baseUrl)
    return request.then(response => response.data)
}

export default {getGroup}