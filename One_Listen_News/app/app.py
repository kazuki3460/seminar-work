from flask import Flask, render_template
from newsapi import NewsApiClient
import requests
import json
import pygame.mixer
import time
import pyaudio
import subprocess
import wave
import shutil
import os

#バックエンド
newsapi = NewsApiClient(api_key='9f8a5d984cd240cf9def042a85a45dc4')


url = 'https://api.apigw.smt.docomo.ne.jp/gooLanguageAnalysis/v1/entity?APIKEY=6d783338306e685073744b546b304d6f56346f302f5642416975706f6f3554764c37766944493578374d38'

url2 = 'https://api.apigw.smt.docomo.ne.jp/crayon/v1/textToSpeech?APIKEY=6d783338306e685073744b546b304d6f56346f302f5642416975706f6f3554764c37766944493578374d38'


headers = {'Content-Type': 'application/json'}

#ビジネスニュース記事３つ取得
b_headlines = newsapi.get_top_headlines(category='business', country='jp')

b_wd0 = b_headlines['articles'][0]['description']
b_wd1 = b_headlines['articles'][1]['description']
b_wd2 = b_headlines['articles'][2]['description']

b_info0 = {"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":b_wd0}

b_info1 ={"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":b_wd1}

b_info2 ={"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":b_wd2}

#ビジネス記事のキーワード定義
b_r0 = requests.post(url,
                  data= json.dumps(b_info0),
                  headers=headers)

b_r1 = requests.post(url,
                  data= json.dumps(b_info1),
                  headers=headers)

b_r2 = requests.post(url,
                  data= json.dumps(b_info2),
                  headers=headers)

b_kw0 = b_r0.json()
b_kw1 = b_r1.json()
b_kw2 = b_r2.json()

##音声取得
#ビジネス　記事１　音声合成
b_news_sentence0 = b_headlines['articles'][0]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":b_news_sentence0}

b_audio_r0 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = b_audio_r0.content
with open( "b_input" + str(0) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " b_input" + str(0) + ".wav" + " b_output" + str(0) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "b_output" + str(0) + ".wav"

try:
    shutil.move('b_output0.wav','app/static/images')
    os.remove('b_input0.wav')

except shutil.Error:
    os.remove('app/static/images/b_output0.wav')
    os.remove('b_input0.wav')
    shutil.move('b_output0.wav','app/static/images')

#ビジネス　記事２　音声合成
b_news_sentence1 = b_headlines['articles'][1]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":b_news_sentence1}

b_audio_r1 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = b_audio_r1.content
with open( "b_input" + str(1) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " b_input" + str(1) + ".wav" + " b_output" + str(1) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "b_output" + str(1) + ".wav"

try:
    shutil.move('b_output1.wav','app/static/images')
    os.remove('b_input1.wav')

except shutil.Error:
    os.remove('app/static/images/b_output1.wav')
    os.remove('b_input1.wav')
    shutil.move('b_output1.wav','app/static/images')

#ビジネス　記事３　音声合成
b_news_sentence2 = b_headlines['articles'][2]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":b_news_sentence2}

b_audio_r2 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = b_audio_r2.content
with open( "b_input" + str(2) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " b_input" + str(2) + ".wav" + " b_output" + str(2) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "b_output" + str(2) + ".wav"

try:
    shutil.move('b_output2.wav','app/static/images')
    os.remove('b_input2.wav')

except shutil.Error:
    os.remove('app/static/images/b_output2.wav')
    os.remove('b_input2.wav')
    shutil.move('b_output2.wav','app/static/images')

#エンタメニュース記事３つ取得
e_headlines = newsapi.get_top_headlines(category='entertainment', country='jp')

e_wd0 = e_headlines['articles'][0]['description']
e_wd1 = e_headlines['articles'][1]['description']
e_wd2 = e_headlines['articles'][2]['description']

e_info0 = {"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":e_wd0}

e_info1 ={"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":e_wd1}

e_info2 ={"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":e_wd2}

#エンタメ記事のキーワード定義
e_r0 = requests.post(url,
                  data= json.dumps(e_info0),
                  headers=headers)

e_r1 = requests.post(url,
                  data= json.dumps(e_info1),
                  headers=headers)

e_r2 = requests.post(url,
                  data= json.dumps(e_info2),
                  headers=headers)

e_kw0 = e_r0.json()
e_kw1 = e_r1.json()
e_kw2 = e_r2.json()

##音声取得
#エンタメ　記事１　音声合成
e_news_sentence0 = e_headlines['articles'][0]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":e_news_sentence0}

e_audio_r0 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = e_audio_r0.content
with open( "e_input" + str(0) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " e_input" + str(0) + ".wav" + " e_output" + str(0) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "e_output" + str(0) + ".wav"

try:
    shutil.move('e_output0.wav','app/static/images')
    os.remove('e_input0.wav')

except shutil.Error:
    os.remove('app/static/images/e_output0.wav')
    os.remove('e_input0.wav')
    shutil.move('e_output0.wav','app/static/images')

#エンタメ　記事２　音声合成
e_news_sentence1 = e_headlines['articles'][1]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":e_news_sentence1}

e_audio_r1 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = e_audio_r1.content
with open( "e_input" + str(1) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " e_input" + str(1) + ".wav" + " e_output" + str(1) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "e_output" + str(1) + ".wav"

try:
    shutil.move('e_output1.wav','app/static/images')
    os.remove('e_input1.wav')

except shutil.Error:
    os.remove('app/static/images/e_output1.wav')
    os.remove('e_input1.wav')
    shutil.move('e_output1.wav','app/static/images')

#エンタメ　記事３　音声合成
e_news_sentence2 = e_headlines['articles'][2]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":e_news_sentence2}

e_audio_r2 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = e_audio_r2.content
with open( "e_input" + str(2) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " e_input" + str(2) + ".wav" + " e_output" + str(2) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "e_output" + str(2) + ".wav"

try:
    shutil.move('e_output2.wav','app/static/images')
    os.remove('e_input2.wav')

except shutil.Error:
    os.remove('app/static/images/e_output2.wav')
    os.remove('e_input2.wav')
    shutil.move('e_output2.wav','app/static/images')

#健康ニュース記事３つ取得
h_headlines = newsapi.get_top_headlines(category='health', country='jp')

h_wd0 = h_headlines['articles'][0]['description']
h_wd1 = h_headlines['articles'][1]['description']
h_wd2 = h_headlines['articles'][2]['description']

h_info0 = {"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":h_wd0}

h_info1 ={"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":h_wd1}

h_info2 ={"request_id":"record001",
        "class_filter":"ART|ORG|PSN|LOC",
        "sentence":h_wd2}

#健康記事のキーワード定義
h_r0 = requests.post(url,
                  data= json.dumps(h_info0),
                  headers=headers)

h_r1 = requests.post(url,
                  data= json.dumps(h_info1),
                  headers=headers)

h_r2 = requests.post(url,
                  data= json.dumps(h_info2),
                  headers=headers)

h_kw0 = h_r0.json()
h_kw1 = h_r1.json()
h_kw2 = h_r2.json()

##音声取得
#健康　記事１　音声合成
h_news_sentence0 = h_headlines['articles'][0]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":h_news_sentence0}

h_audio_r0 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = h_audio_r0.content
with open( "h_input" + str(0) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " h_input" + str(0) + ".wav" + " h_output" + str(0) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "h_output" + str(0) + ".wav"

try:
    shutil.move('h_output0.wav','app/static/images')
    os.remove('h_input0.wav')

except shutil.Error:
    os.remove('app/static/images/h_output0.wav')
    os.remove('h_input0.wav')
    shutil.move('h_output0.wav','app/static/images')

#健康　記事２　音声合成
h_news_sentence1 = h_headlines['articles'][1]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":h_news_sentence1}

h_audio_r1 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = h_audio_r1.content
with open( "h_input" + str(1) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " h_input" + str(1) + ".wav" + " h_output" + str(1) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "h_output" + str(1) + ".wav"

try:
    shutil.move('h_output1.wav','app/static/images')
    os.remove('h_input1.wav')

except shutil.Error:
    os.remove('app/static/images/h_output1.wav')
    os.remove('h_input1.wav')
    shutil.move('h_output1.wav','app/static/images')

#健康　記事３　音声合成
h_news_sentence2 = h_headlines['articles'][2]['description']
body = {"Command":"AP_Synth",
  "SpeakerID":"1",
  "StyleID":"1",
  "SpeechRate":"1.15",
  "AudioFileFormat":"0",
  "TextData":h_news_sentence2}

h_audio_r2 = requests.post(url2,
                  data=json.dumps(body),
                  headers=headers)

wav = h_audio_r2.content
with open( "h_input" + str(2) +".wav","wb") as fout:
    fout.write(wav)
cmd ="ffmpeg -i" + " h_input" + str(2) + ".wav" + " h_output" + str(2) +  ".wav"
runcmd = subprocess.call(cmd.split())
wavfile = "h_output" + str(2) + ".wav"

try:
    shutil.move('h_output2.wav','app/static/images')
    os.remove('h_input2.wav')

except shutil.Error:
    os.remove('app/static/images/h_output2.wav')
    os.remove('h_input2.wav')
    shutil.move('h_output2.wav','app/static/images')

app = Flask(__name__)

user_name="One Lessen News"

# メニューを表示
@app.route("/")
def menu():
    return render_template("index.html", user_name = user_name)

# ビジネス　#ブラウザに表示
@app.route("/business")
def walk():
    b_menu_name = "ビジネス"
    b_title = b_headlines['articles'][0]['title']
    b_title2 = b_headlines['articles'][1]['title']
    b_title3 = b_headlines['articles'][2]['title']

#ビジネスの記事１　キーワード
    try:
        b_key1 = "#" + b_kw0["ne_list"][0][0]
    except IndexError:
        b_key1 = ""

    try:
        b_key2= "#" + b_kw0["ne_list"][1][0]
    except IndexError:
        b_key2 = ""
    
    try:
        b_key3 = "#" + b_kw0["ne_list"][2][0]
    except IndexError:
        b_key3 = ""

    try:
        b_key4= "#" + b_kw0["ne_list"][3][0]
    except IndexError:
        b_key4 = ""

#ビジネスの記事２　キーワード
    try:
        b_key5 = "#" + b_kw1["ne_list"][0][0]
    except IndexError:
        b_key5 = ""

    try:
        b_key6= "#" + b_kw1["ne_list"][1][0]
    except IndexError:
        b_key6 = ""
    
    try:
        b_key7 = "#" + b_kw1["ne_list"][2][0]
    except IndexError:
        b_key7 = ""

    try:
        b_key8= "#" + b_kw1["ne_list"][3][0]
    except IndexError:
        b_key8 = ""
    
    #ビジネスの記事３　キーワード
    try:
        b_key9 = "#" + b_kw2["ne_list"][0][0]
    except IndexError:
        b_key9 = ""

    try:
        b_key10= "#" + b_kw2["ne_list"][1][0]
    except IndexError:
        b_key10 = ""
    
    try:
        b_key11 = "#" + b_kw2["ne_list"][2][0]
    except IndexError:
        b_key11 = ""

    try:
        b_key12= "#" + b_kw2["ne_list"][3][0]
    except IndexError:
        b_key12 = ""

    return render_template("b_screen_tran.html", b_menu_name = b_menu_name, b_title=b_title, b_title2=b_title2,b_title3=b_title3, b_key1=b_key1, b_key2=b_key2,b_key3=b_key3,b_key4=b_key4,b_key5=b_key5, b_key6=b_key6,b_key7=b_key7,b_key8=b_key8,b_key9=b_key9, b_key10=b_key10,b_key11=b_key11,b_key12=b_key12)
# エンタメ
@app.route("/entertain")
def attack():
    e_menu_name = "エンタメ"
    e_title = e_headlines['articles'][0]['title']
    e_title2 = e_headlines['articles'][1]['title']
    e_title3 = e_headlines['articles'][2]['title']
    
#エンタメの記事１　キーワード
    try:
        e_key1 = "#" + e_kw0["ne_list"][0][0]
    except IndexError:
        e_key1 = ""

    try:
        e_key2= "#" + e_kw0["ne_list"][1][0]
    except IndexError:
        e_key2 = ""
    
    try:
        e_key3 = "#" + e_kw0["ne_list"][2][0]
    except IndexError:
        e_key3 = ""

    try:
        e_key4= "#" + e_kw0["ne_list"][3][0]
    except IndexError:
        e_key4 = ""

#エンタメの記事２　キーワード
    try:
        e_key5 = "#" + e_kw1["ne_list"][0][0]
    except IndexError:
        e_key5 = ""

    try:
        e_key6= "#" + e_kw1["ne_list"][1][0]
    except IndexError:
        e_key6 = ""
    
    try:
        e_key7 = "#" + e_kw1["ne_list"][2][0]
    except IndexError:
        e_key7 = ""

    try:
        e_key8= "#" + e_kw1["ne_list"][3][0]
    except IndexError:
        e_key8 = ""
    
    #ビジネスの記事３　キーワード
    try:
        e_key9 = "#" + e_kw2["ne_list"][0][0]
    except IndexError:
        e_key5 = ""

    try:
        e_key10= "#" + e_kw2["ne_list"][1][0]
    except IndexError:
        e_key10 = ""
    
    try:
        e_key11 = "#" + e_kw2["ne_list"][2][0]
    except IndexError:
        e_key11 = ""

    try:
        e_key12= "#" + e_kw2["ne_list"][3][0]
    except IndexError:
        e_key12 = ""

    return render_template("e_screen_tran.html", e_menu_name = e_menu_name, e_title=e_title, e_title2=e_title2,e_title3=e_title3, e_key1=e_key1, e_key2=e_key2,e_key3=e_key3,e_key4=e_key4,e_key5=e_key5, e_key6=e_key6,e_key7=e_key7,e_key8=e_key8,e_key9=e_key9, e_key10=e_key10,e_key11=e_key11,e_key12=e_key12)


# 健康
@app.route("/health")
def healthy():
    h_menu_name = "健康"
    h_title = h_headlines['articles'][0]['title']
    h_title2 = h_headlines['articles'][1]['title']
    h_title3 = h_headlines['articles'][2]['title']

#健康の記事１　キーワード
    try:
        h_key1 = "#" + h_kw0["ne_list"][0][0]
    except IndexError:
        h_key1 = ""

    try:
        h_key2= "#" + h_kw0["ne_list"][1][0]
    except IndexError:
        h_key2 = ""
    
    try:
        h_key3 = "#" + h_kw0["ne_list"][2][0]
    except IndexError:
        h_key3 = ""

    try:
        h_key4= "#" + h_kw0["ne_list"][3][0]
    except IndexError:
        h_key4 = ""

#ビジネスの記事２　キーワード
    try:
        h_key5 = "#" + h_kw1["ne_list"][0][0]
    except IndexError:
        h_key5 = ""

    try:
        h_key6= "#" + h_kw1["ne_list"][1][0]
    except IndexError:
        h_key6 = ""
    
    try:
        h_key7 = "#" + h_kw1["ne_list"][2][0]
    except IndexError:
        h_key7 = ""

    try:
        h_key8= "#" + h_kw1["ne_list"][3][0]
    except IndexError:
        h_key8 = ""
    
    #健康の記事３　キーワード
    try:
        h_key9 = "#" + h_kw2["ne_list"][0][0]
    except IndexError:
        h_key9 = ""

    try:
        h_key10= "#" + h_kw2["ne_list"][1][0]
    except IndexError:
        h_key10 = ""
    
    try:
        h_key11 = "#" + h_kw2["ne_list"][2][0]
    except IndexError:
        h_key11 = ""

    try:
        h_key12= "#" + h_kw2["ne_list"][3][0]
    except IndexError:
        h_key12 = ""

    return render_template("h_screen_tran.html", h_menu_name = h_menu_name, h_title=h_title, h_title2=h_title2,h_title3=h_title3, h_key1=h_key1, h_key2=h_key2,h_key3=h_key3,h_key4=h_key4,h_key5=h_key5, h_key6=h_key6,h_key7=h_key7,h_key8=h_key8,h_key9=h_key9, h_key10=h_key10,h_key11=h_key11,h_key12=h_key12)

# music
@app.route("/business/b_music1")
def music1():
    bm_title = b_headlines['articles'][0]['title']
    bm_description = b_headlines['articles'][0]['description']
    bm_url = b_headlines['articles'][0]['url']

    return render_template("b_music1.html", bm_title = bm_title, bm_description = bm_description, bm_url = bm_url)

@app.route("/business/b_music2")
def music2():
    bm_title2 = b_headlines['articles'][1]['title']
    bm_description2 = b_headlines['articles'][1]['description']
    bm_url2 = b_headlines['articles'][1]['url']

    return render_template("b_music2.html", bm_title2=bm_title2, bm_description2=bm_description2,bm_url2 = bm_url2)

@app.route("/business/b_music3")
def music3():
    bm_title3 = b_headlines['articles'][2]['title']
    bm_description3 = b_headlines['articles'][2]['description']
    bm_url3 = b_headlines['articles'][2]['url']

    return render_template("b_music3.html", bm_title3=bm_title3, bm_description3=bm_description3,bm_url3 = bm_url3)

@app.route("/entertain/e_music1")
def music4():
    em_title = e_headlines['articles'][0]['title']
    em_description = e_headlines['articles'][0]['description']
    em_url = e_headlines['articles'][0]['url']

    return render_template("e_music1.html", em_title = em_title, em_description = em_description, em_url = em_url)

@app.route("/entertain/e_music2")
def music5():
    em_title2 = e_headlines['articles'][1]['title']
    em_description2 = e_headlines['articles'][1]['description']
    em_url2 = e_headlines['articles'][1]['url']

    return render_template("e_music2.html", em_title2=em_title2, em_description2=em_description2,em_url2 = em_url2)

@app.route("/entertain/e_music3")
def music6():
    em_title3 = e_headlines['articles'][2]['title']
    em_description3 = e_headlines['articles'][2]['description']
    em_url3 = e_headlines['articles'][2]['url']

    return render_template("e_music3.html", em_title3=em_title3, em_description3=em_description3,em_url3 = em_url3)

@app.route("/health/h_music1")
def music7():
    hm_title = h_headlines['articles'][0]['title']
    hm_description = h_headlines['articles'][0]['description']
    hm_url = h_headlines['articles'][0]['url']

    return render_template("h_music1.html", hm_title = hm_title, hm_description = hm_description, hm_url = hm_url)

@app.route("/health/h_music2")
def music8():
    hm_title2 = h_headlines['articles'][1]['title']
    hm_description2 = h_headlines['articles'][1]['description']
    hm_url2 = h_headlines['articles'][1]['url']

    return render_template("h_music2.html", hm_title2=hm_title2, hm_description2=hm_description2,hm_url2 = hm_url2)

@app.route("/health/h_music3")
def music9():
    hm_title3 = h_headlines['articles'][2]['title']
    hm_description3 = h_headlines['articles'][2]['description']
    hm_url3 = h_headlines['articles'][2]['url']

    return render_template("h_music3.html", hm_title3=hm_title3, hm_description3=hm_description3,hm_url3 = hm_url3)
