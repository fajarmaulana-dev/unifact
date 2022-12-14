import axios from 'axios';
const base = import.meta.env.VITE_BASE_URL;

export class PredictService {
  predict(data: any) {
    return axios.post(`${base}/predict`, data);
  }
}
