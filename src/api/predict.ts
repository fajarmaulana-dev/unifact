import {reactive, ref} from '@vue/reactivity';
import Api from './api';

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
  const error = ref('');
  const prediction: any = ref<Prediction>();

  const predict = async (data: any) => {
    error.value = '';
    const res = await Api.post(`/predict`, data);
    if (res.data) prediction.value = res.data;
    if (res.status >= 300) {
      error.value = 'Jaringanmu kurang stabil.';
    }
  };

  return {
    error,
    prediction,
    predict,
  };
};
