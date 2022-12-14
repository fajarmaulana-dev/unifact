import re, string, json, os, uvicorn, argparse
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from tcn import TCN
from keras.models import load_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

##### Normalize Input #####
def txt_to_sets(txt, sets, sep):
    filename = open(f'content/{txt}', "r")
    file_read = filename.read()
    for i in file_read.split(sep=sep): sets.add(i)
    filename.close()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'(\S+|)(http|blogspot|@|mail|dot)(\S+|)', '', text)
    text = " ".join([w.replace(w, '') if ('.' and '/') in w else w for w in text.split()])
    text = re.sub('[.,-]', ' ', text)
    text = "".join([i for i in text if ord(i) < 128])
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('<.*?>+', '', text)
    text = " ".join([re.sub('[%s]' % re.escape(string.punctuation), ' ', w) if '#' not in w else w for w in text.split()])
    text = " ".join([w.replace(w, '') if w.isdigit() else w.replace(w, '') if (len(re.findall(r'\d+', w)) > 0 and len(re.findall(r'\d+', w)[0]) >= 7) else w for w in text.split()])
    return text.strip()

def splitHashTag(hashTag):
    new_words = []
    for wordSequence in re.findall('(?:' + wordOr + ')+', hashTag):
        for word in re.findall(wordOr, wordSequence):
            new_words.append(word)
    return ' '.join(new_words)

def normalize(text, alay, normal):
    n = text.split()
    for a in range(len(alay)):
        if alay[a] in n:
            n[n.index(alay[a])] = normal[a]
    
    text = " ".join(n)
    text = " ".join(w for w in text.split() if not any(c.isdigit() for c in w)) # remove word containing number
    text = " ".join(w for w in text.split() if w not in abnormal)
    text = clean_text(text)
    return text

def remove_stop(text):
    text = " ".join([w for w in text.split() if w not in stopword])
    return text

word_index = None
residu = None
alay = None
with open('content/word_dict.json') as json_file: word_index = json.load(json_file)
with open('content/residu.json') as json_file: residu = json.load(json_file)
with open('content/alay.json') as json_file: alay = json.load(json_file)

def tokenize(text):
    s = text.split()
    return [word_index[s[i]] if s[i] in word_index else 1 for i in range(len(s))]

max_len = 196
def pad_sequence(seq):
    return [0 if i < (max_len - len(seq)) else seq[i - (max_len - len(seq))] for i in range(max_len)]

def filters(obj):
    if obj['num'] == 0: return False
    return True

hashtag = set()
txt_to_sets('tags.txt', hashtag, ',')

wordList = list(dict.fromkeys(hashtag))
wordList.remove('')

wordOr = '|'.join(wordList)

abnormal = set()
txt_to_sets('stop.txt', abnormal, '\n')

stopword = set()
txt_to_sets('stopwordsID.txt', stopword, '\n')
stopword = set(dict.fromkeys(stopword))

##### Predict #####
model = load_model('content/model.h5', custom_objects={'TCN': TCN})

def predict(text):
    text = clean_text(text)
    text = ' '.join([splitHashTag(w) if '#' in w else w for w in text.split()])
    normal = normalize(text, alay['alay'], alay['normal'])
    nonstop = remove_stop(normal)
    seq = tokenize(nonstop)
    padded = np.array([pad_sequence(seq)])
    preds = model.predict(padded)
    proba = preds[0].tolist()
    classes = ['Fabricated Content/Imposter Content', 'Misleading Content/False Context/Manipulated Content', 'Valid']
    
    max_classes = []
    false_num = []
    imposter_num = []
    valid_num = []
    for i in nonstop.split():
        max_res = []

        if i in residu['imposter']:
            if {'word': i, 'num': residu['imposter'][i]} not in imposter_num:
                imposter_num.append({'word': i, 'num': residu['imposter'][i]})
            max_res.append(residu['imposter'][i])
        else:
            if {'word': i, 'num': 0} not in imposter_num:
                imposter_num.append({'word': i, 'num': 0})
            max_res.append(0)

        if i in residu['false']:
            if {'word': i, 'num': residu['false'][i]} not in false_num:
                false_num.append({'word': i, 'num': residu['false'][i]})
            max_res.append(residu['false'][i])
        else:
            if {'word': i, 'num': 0} not in false_num:
                false_num.append({'word': i, 'num': 0})
            max_res.append(0)

        if i in residu['valid']:
            if {'word': i, 'num': residu['valid'][i]} not in valid_num:
                valid_num.append({'word': i, 'num': residu['valid'][i]})
            max_res.append(residu['valid'][i])
        else:
            if {'word': i, 'num': 0} not in valid_num:
                valid_num.append({'word': i, 'num': 0})
            max_res.append(0)

        if max(max_res) != 0:
            max_classes.append(max_res.index(max(max_res)))
    
    imposter_count = max_classes.count(0)
    false_count = max_classes.count(1)
    valid_count = max_classes.count(2)
    
    prediction = classes[proba.index(max(preds[0]))]
    probs = [{'class': classes[i], 'probs': f'{round((proba[i]*100), 2)}%'} for i in range(len(classes))]
    record = {'false': false_num, 'imposter': imposter_num, 'valid': valid_num}
    domination = {'false': false_count, 'imposter': imposter_count, 'valid': valid_count}
    domi = list(domination.keys())[list(domination.values()).index(max(list(domination.values())))]
    dominate = ''
    if domi == 'imposter': dominate = classes[0]
    if domi == 'false': dominate = classes[1]
    if domi == 'valid': dominate = classes[2]

    existence = {'false': len(list(filter(filters, false_num))), 'imposter': len(list(filter(filters, imposter_num))), 'valid': len(list(filter(filters, valid_num)))}
    
    ico = ''
    if prediction == classes[0]: ico = 'fa-solid fa-masks-theater'
    if prediction == classes[1]: ico = 'fa-solid fa-skull-crossbones'
    if prediction == classes[2]: ico = 'fa-solid fa-circle-check'
    
    return normal, nonstop, prediction, probs, record, domination, dominate, existence, ico

##### Create Body Request Schema #####
class Naration(BaseModel):
    text: str

##### Create Routes #####
@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

@app.post("/predict", status_code=201)
async def get_predictions(naration: Naration):
    try:
      normal, nonstop, prediction, probability, record, domination, dominate, existence, ico = predict(naration.text)
      return {"normalNaration": normal, "withoutStopword": nonstop, "prediction": prediction, "probability": probability, "record": record, "domination": domination, "dominate": dominate, "existence": existence, "ico": ico}
    except:
      return {"prediction": "error"}

if __name__ == "__main__":
    port = os.getenv('PORT', default=5000)
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0", type=str)
    parser.add_argument("--port", default=port, type=int)
    opt = parser.parse_args()

    app_str = ("main:app")
    uvicorn.run(app_str, host=opt.host, port=opt.port, reload=True)