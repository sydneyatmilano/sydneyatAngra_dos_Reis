import axion from "axios";

const apiClient = axios.create({
    baseURL: "http://Localhost:8000/api",
    headers: {
        "Content-Type": "application/json",
    },
});

export default apiClient;