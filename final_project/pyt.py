import random
import json
import pickle
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json', encoding='utf-8').read())

words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))

model=load_model("chatbot_model.h5")
def clean_sentence(sentence):
    sentence_word=nltk.word_tokenize(sentence)
    sentence_word=[lemmatizer.lemmatize(word) for word in sentence_word]
    return sentence_word

def bag_words(sentence):
    sentence_words=clean_sentence(sentence)
    bag=[0]*len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word==w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow=bag_words(sentence)
    res=model.predict(np.array([bow]))[0]

    ERROR_THRESHOLD=0.25
    results=[[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x:x[1],reverse=True)
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    return return_list

"""def get_response(i_list,i_json):
    list_intents= i_json['intents']
    tag=i_list[0]['intent']
    for i in list_intents:
        if i['tag']==tag:
            result =random.choice(i["responses"])
            break
        return result"""
def get_response(ints, intents_json):
    tag = ints[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "Sorry, I didn't understand that."

    
print("chatbot is working")

while True:
    message=input("")
    ints=predict_class(message)
    res=get_response(ints,intents)
    print(res)
