import axios from "axios"

const baseUrl = 'placehold'


const getRestaurants = () => {
    const request = axios.get(baseUrl)
    return request.then(response => response.data)
}

export default {getRestaurants}