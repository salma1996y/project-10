import requests


import pickle

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)
database_service =  requests.get("http://127.0.0.1:3000" +"/get_data" , params={'sort_order': "DESC" , 'count': 10})


import re

def clean_text(text):
    text = text.lower()
    text = re.sub("@[a-z0-9_]+", ' ', text)
    text = re.sub("[^ ]+\.[^ ]+", ' ', text)
    text = re.sub("[^ ]+@[^ ]+\.[^ ]", ' ', text)
    text = re.sub("[^a-z\' ]", ' ', text)
    text = re.sub(' +', ' ', text)

    return text
database_service = database_service.json()
for file in database_service:
    try:
        text = file.read()  # نقرأ النص
        text = clean_text(text)  # نستخدم دالة التنظيف لتنظيف و تبسيط النص
        if text == "":
            continue  # تجاهل النصوص التي تصبح فارغة بعد تنظيفها
        print(text)
        texts = []
        texts.append(text)  # نضيفه للقائمة
        print("-" * 10)
    except UnicodeDecodeError:  # قد نحصل على هذا الخطأ بسبب الملفات التالفة
        continue 

cleaned_test = clean_text(text)

test_vector = vectorizer.transform([cleaned_test])
result = model.predict(testـvector)

print("Sentence classification:", text)

print(result[1000])

from sklearn.metrics import accuracy_score
accuracy_score(result)
print(result[1000])

database_service =  request.get("http://127.0.0.1:3000" +"/get_data_count" , params={'label_name': 0 , 'count': 10})

database_service = database_service.json()

print("Sentence classification:", database_service)

print(result[1000])

