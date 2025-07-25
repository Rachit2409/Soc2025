
import random
import json
import pickle
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import SGD


import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import json

with open("intents.json", encoding='utf-8') as f:
    intents = json.load(f)
    words=[]
classes=[]
documents=[]
ignore =['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list=nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words=[lemmatizer.lemmatize(word) for word in words if word not in ignore ]
words = sorted(set(words))
classes=sorted(set(classes))

pickle.dump(words,open("words.pkl","wb"))
pickle.dump(classes,open("classes.pkl","wb"))

train_list=[]
otempty=[0]* len(classes)
for document in documents:
    bag=[]
    wordpatterns=document[0]
    wordpatterns=[lemmatizer.lemmatize(word.lower()) for word in wordpatterns]
    for word in words: bag.append(1) if word in wordpatterns else bag.append(0)
    otrow=list(otempty)
    otrow[classes.index(document[1])]=1
    train_list.append(bag + otrow)

random.shuffle(train_list)
train_list=np.array(train_list)

train_x=train_list[:, :len(words)]
train_y=train_list[:, len(words):]

model=Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd=SGD(learning_rate=0.01, decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
model.fit(np.array(train_x),np.array(train_y),epochs=200,batch_size=5,verbose=1)
model.save('chatbot_model.h5')
print("done")