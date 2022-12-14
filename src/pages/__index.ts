import {ref} from 'vue';
import {PredictService} from '@/components/api';

type Prediction = {
  normalNaration: string;
  withoutStopword: string;
  prediction: string;
  probability: object;
  record: object;
  domination: object;
  existence: object;
  dominate: string;
  ico: string;
};

export const usePredict = () => {
  const service = new PredictService();
  const loading = ref(false);
  const prediction: any = ref<Prediction[]>([]);

  const predict = async (data: any) => {
    try {
      loading.value = true;
      const res = await service.predict(data);
      prediction.value = res.data;
      loading.value = false;
      return res;
    } catch (err) {
      console.log(err);
    }
  };

  return {loading, predict, prediction};
};
