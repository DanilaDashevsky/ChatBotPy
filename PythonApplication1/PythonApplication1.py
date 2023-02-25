from bs4 import BeautifulSoup
import urllib.parse
from urllib.request import urlopen,Request
import random
import telebot
import emoji
import googletrans
import requests
import csv
from telebot import types
from transliterate import translit
from better_profanity import profanity
from deep_translator import GoogleTranslator

def repeat(message_from_user_id,text):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
     btn1 = types.KeyboardButton('Пиццы')
     btn2 = types.KeyboardButton('Роллы') 
     btn3 = types.KeyboardButton('Десерты и напитки')
     btn4 = types.KeyboardButton('Показать карзину')
     btn8 = types.KeyboardButton('Отчистить карзину')
     btn5 = types.KeyboardButton('Контакты')
     btn6 = types.KeyboardButton('Данные о доставке')
     btn7 = types.KeyboardButton('Играть')
     markup.add( btn1,btn2, btn3, btn4, btn5, btn6, btn7, btn8)
     bot.send_message(message_from_user_id, text, reply_markup=markup)


bot = telebot.TeleBot("YourToken")
counter_messager0 =0
counter_rolls0 =0
counter_rolls1 =0
summ=0
karsina=""
price=""
name=""

def get_text(url):
    r = requests.get(url)
    text=r.text 
    return text

def get_items_a(text,top_name,class_name):
   soup = BeautifulSoup(text, "lxml")
   items = soup.find_all("a", {'itemprop': "image"})
   dirty_link=[]
   for item in items:
       dirty_link.append(item.get("href"))
   return dirty_link

def get_items_img_roll(text,top_name,class_name,class_img):
   requester = {'User-Agent': 'Mozilla/5.0'}
   req=Request("https://yaponomaniya.com/rolly",headers=requester)
   u = urlopen(req)
   soup = BeautifulSoup(u.read(), features="lxml")
   items = soup.findAll('img',{'class': "product-img"})
   dirty_link=[]
   for item in items:
       dirty_link.append(item.get("alt"))
   return dirty_link

def get_items_img_picca(text,top_name,class_name,class_img):
   requester = {'User-Agent': 'Mozilla/5.0'}
   req=Request("https://yaponomaniya.com/pitstsy",headers=requester)
   u = urlopen(req)
   soup = BeautifulSoup(u.read(), features="lxml")
   items = soup.findAll('img',{'class': "product-img"})
   dirty_link=[]
   for item in items:
       dirty_link.append(item.get("alt"))
   return dirty_link

def get_items_img_disert(text,top_name,class_name,class_img):
   requester = {'User-Agent': 'Mozilla/5.0'}
   req=Request("https://yaponomaniya.com/deserty-i-napitki",headers=requester)
   u = urlopen(req)
   soup = BeautifulSoup(u.read(), features="lxml")
   items = soup.findAll('img',{'class': "product-img"})
   dirty_link=[]
   for item in items:
       dirty_link.append(item.get("alt"))
   return dirty_link

def get_items_img_sign(text): # здесь ищется изображение, которое ввёл пользователь 
   soup = BeautifulSoup(text, "lxml")
   items = soup.find('li',text)
   item0 = items.find('img')
   item1 = items.find('span', {"class":"price new h3"})
   item2 = items.find("div",{"class":"product-desc"} )
   dirty_link=[]
   for item in items:
       dirty_link.append(item.get("src"))
   return dirty_link


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global karsina
    global summ
    if message.text == "Привет":
        repeat(message.from_user.id,'Привет, чем я могу тебе помочь?')
    elif message.text == "Играть":
        bot.send_message(message.from_user.id, "Отлично, давай поиграем.😏 Напиши что-нибудь, а попробую найти картинку по твоему запросу")
        global counter_messager0
        counter_messager0 = counter_messager0 +1
    elif message.text == "/start":
            bot.send_message(message.from_user.id, "Здравствуй друг, рад приветствовать тебя ❤🙋‍♂️")
            bot.send_photo(message.from_user.id, "https://yt3.ggpht.com/a/AGF-l7875YxhMiA2466YQoQmRMMvf3rBtOPZ-D89fQ=s900-c-k-c0xffffffff-no-rj-mo")
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text='ЯПОНОмания', url='https://yaponomaniya.com/')
            markup.add(btn1)
            bot.send_message(message.from_user.id, "Вот наш официальный сайт. Ты можешь перейти на него или выбрать из меню, то что хочешь", reply_markup = markup)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
            repeat(message.from_user.id,'Вы снова в главном меню')
            #ответ бота
    elif message.text == "Роллы":
        url='https://yaponomaniya.com/rolly'
        text = get_text(url)
        top_name="product-item set"
        class_name ="item-link"
        class_img = "product-img"
        #y = get_items_a(text,top_name,class_name)
        y0 = get_items_img_roll(text,top_name,class_name,class_img)
        i = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        for h in y0:
           btn1 = types.KeyboardButton(h)
           markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отличный выбор!', reply_markup=markup)
        global counter_rolls1
        counter_rolls1 = counter_rolls1 +1
    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id, 'Контакты:\n'
                     +'🏪г. Киров, ул. Спасская, 17 / Ленина, 82\n'
                     +'🏪г. Киров, ул. Московская, 185а\n'
                     +'🏪г. Киров, Октябрьский пр-т, 19\n'
                     +'🏪г. Киров, Коминтерновская пл.1Б (ТЦ Клён, левое крыло)\n'
                     +'📞Телефон: +7 (8332) 735-166\n'
                     +'⌚️Прием заказов: 10:00 — 23:00\n\n'
                     +'🏪г. Кирово-Чепецк, ул.Фестивальная, 5\n'
                     +'🏪г. Кирово-Чепецк, ул. Володарского, 9\n'
                     +'🏪г. Кирово-Чепецк, пр-т России, 34 (ТЦ "Россия", 2 этаж)\n'
                     +'📞Телефон: +7 (8332) 735-166\n'
                     +'⌚️Прием заказов: 10:00 — 23:00\n\n'
                     +'📧Общая почта: marketing@yaponomaniya.com\n'
                     +'📧По вопросам рекламы: marketing@yaponomaniya.com\n'
                     +'📧Почта директора: director@yaponomaniya.com')
    elif message.text == 'Данные о доставке':
           bot.send_message(message.from_user.id, 'ВНИМАНИЕ!!! Изменения с 01.10.2022г.\n\n'
                     + '✅ г. Киров от 395 руб;\n\n'
                     +'Отдаленные районы:\n'
                     +'Коминтерн, Макарье от 395 р\n'
                     +'Лосево/Корчемкино/Нововятск/Радужный-900 р\n'
                     +'Катковы-900 р.\n'
                     +'Костино-900 р.\n'
                     +'Дороничи-900 р\n'
                     +'Сватково/ Никуленки-900 р.\n'
                     +'Головизненцы- 2000 р.\n'
                     +'Пасегово-2000 р.\n'
                     +'Макарье/Красный Химик/Дымково-395 р.\n'
                     +'Ганино/Порошино/Гнусино/ Б. Субботиха-600 р.\n'
                     +'Б./М. гора/ Малая Субботиха-900 р.\n'
                     +'Подгорена- 900 р.\n'
                     +'Бобино- 900 р.\n'
                     +'Шихово-900р\n\n'
                     +'*Среднее время доставки, 60 минут. В зависимости от дорожной обстановки, время может сокращаться и увеличиваться.\n\n'
                     +'Внимание!\n'
                     +'Заказы в дальние от центра районы принимаем до 22:00, а именно:\n'
                     +'Нововятск, Елки-Парк, Радужный, Дороничи, Головизненцы, Пасегово, Бобино, Мал. Субботиха, Мошкачи\n\n'
                     +'✅ г. Кирово-Чепецк от 395 руб.\n\n'
                     +'Отдаленные районы:\n'
                     +'ПМК-500 р.\n'
                     +'ТЭЦ-500 р.\n'
                     +'Просница-2000 р.\n'
                     +'Перекоп-1000 р.\n'
                     +'Ключи-500 р\n'
                     +'Квартал Деветьярово-500 р.\n'
                     +'Квартал Цепели-500 р.\n\n'
                     +'*Среднее время доставки 60 минут. В зависимости от дорожной обстановки, время может сокращаться и увеличиваться.\n\n'
                     +'Внимание!\n'
                     +'Заказы в дальние от центра районы принимаем до 22:00, а именно:\n'
                     +'В Просницу, Ильинское, Перекоп.\n\n'
                     +'Внимание!\n'
                     +'Мы стремимся к улучшению качества нашего сервиса, в том числе, скорости доставки. Поэтому с 18 ноября 2022 мы вынуждены отказаться от доставки - (за переезд) в Нововятск. Ждем вас за заказами на самовывоз.\n\n'
                     +'Подробную информацию вы можете узнать у операторов контакт-центра по единому телефону: ☎️ 735-166.')
    elif message.text == "Пиццы":
        url='https://yaponomaniya.com/pitstsy'
        text = get_text(url)
        top_name="product-item set"
        class_name ="item-link"
        class_img = "product-img"
        y0 = get_items_img_picca(text,top_name,class_name,class_img)
        i = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        for h in y0:
           btn1 = types.KeyboardButton(h)
           markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отличный выбор!', reply_markup=markup)
    elif message.text == 'Отчистить карзину':
        karsina=""
        summ=0
        bot.send_message(call.message.chat.id,"Карзина отчищена")
    elif "Пицц" in message.text:
        url='https://yaponomaniya.com/pitstsy'
        responce = requests.get(url)
        html = responce.text
        soup = BeautifulSoup(html, "html.parser")
        text=""
        item0 = soup.findAll('li',{'class': "product-item set"})
        for h in item0: # отвечает за отправку сообщения с описанием товара
                if message.text in h.find("img")["alt"] or h.find("img")["alt"] in message.text:
                    item1 = h.find("img")["src"]
                    #bot.send_message(message.from_user.id,"Ваш выбор: "+ message.text)
                    bot.send_photo(message.from_user.id, 'https://yaponomaniya.com'+item1)
                    item3 = h.find("div",{"class":"product-desc"} ).text
                    bot.send_message(message.from_user.id, item3)
                    item2 = h.find('span', {"class":"price new h3"}).text
                    #bot.send_message(message.from_user.id, "Цена: "+item2)
                    item0 = h.find('a',{"class":"item-link"})["href"]
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Больше описания товара на нашем сайте", url='https://yaponomaniya.com'+item0)
                    button2 = types.InlineKeyboardButton("Заказать", callback_data="Custom") #отвечает за оплату
                    button3 = types.InlineKeyboardButton("Добавить в карзину", callback_data="Add")
                    markup.add(button1,button2,button3)
                    bot.send_message(message.from_user.id, "Товар: "+ message.text + " Цена: "+item2, reply_markup=markup)
    elif message.text == "Десерты и напитки":
        url='https://yaponomaniya.com/deserty-i-napitki'
        text = get_text(url)
        top_name="product-item set"
        class_name ="item-link"
        class_img = "product-img"
        y0 = get_items_img_disert(text,top_name,class_name,class_img)
        i = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Назад"))
        for h in y0:
           btn1 = types.KeyboardButton(h)
           markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отличный выбор!', reply_markup=markup)
    elif "апиток" in message.text or "Морс" in message.text or "Чизкейк" in message.text or "Лимонад" in message.text or "Тутти" in message.text or "Шоколад" in message.text or "Клубнич" in message.text:
        url='https://yaponomaniya.com/deserty-i-napitki'
        responce = requests.get(url)
        html = responce.text
        soup = BeautifulSoup(html, "html.parser")
        text=""
        item0 = soup.findAll('li',{'class': "product-item set"})
        for h in item0: # отвечает за отправку сообщения с описанием товара
                if message.text in h.find("img")["alt"] or h.find("img")["alt"] in message.text:
                    item1 = h.find("img")["src"]
                    bot.send_message(message.from_user.id,"Ваш выбор: "+ message.text)
                    bot.send_photo(message.from_user.id, 'https://yaponomaniya.com'+item1)
                    item3 = h.find("div",{"class":"product-desc"} ).text
                    bot.send_message(message.from_user.id, item3)
                    item2 = h.find('span', {"class":"price new h3"}).text
                    bot.send_message(message.from_user.id, "Цена: "+item2)
                    item0 = h.find('a',{"class":"item-link"})["href"]
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Больше описания товара на нашем сайте", url='https://yaponomaniya.com'+item0)
                    button2 = types.InlineKeyboardButton("Заказать", callback_data="Custom") #отвечает за оплату
                    button3 = types.InlineKeyboardButton("Добавить в карзину", callback_data="Add")
                    markup.add(button1,button2,button3)
                    bot.send_message(message.from_user.id, "Товар: "+ message.text + " Цена: "+item2, reply_markup=markup)
    elif message.text == "Назад":
         counter_rolls1= counter_rolls1-1
         repeat(message.from_user.id,'Выберите из меню то, что вы хотите')
    elif message.text == "Показать карзину":
        bot.send_message(message.from_user.id,"Ваш выбор: "+ karsina + "Сумма заказа: "+str(summ) + '₽')
    elif "Ролл" in message.text:
        url='https://yaponomaniya.com/rolly'
        responce = requests.get(url)
        html = responce.text
        soup = BeautifulSoup(html, "html.parser")
        text=""
        item0 = soup.findAll('li',{'class': "product-item set"})
        for h in item0: # отвечает за отправку сообщения с описанием товара
                if message.text in h.find("img")["alt"] or h.find("img")["alt"] in message.text:
                    item1 = h.find("img")["src"]
                    bot.send_message(message.from_user.id,"Ваш выбор: "+ message.text)
                    bot.send_photo(message.from_user.id, 'https://yaponomaniya.com'+item1)
                    item3 = h.find("div",{"class":"product-desc"} ).text
                    bot.send_message(message.from_user.id, item3)
                    item2 = h.find('span', {"class":"price new h3"}).text
                    bot.send_message(message.from_user.id, "Цена: "+item2)
                    item0 = h.find('a',{"class":"item-link"})["href"]
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Больше описания товара на нашем сайте", url='https://yaponomaniya.com'+item0)
                    button2 = types.InlineKeyboardButton("Заказать", callback_data="Custom") #отвечает за оплату
                    button3 = types.InlineKeyboardButton("Добавить в карзину", callback_data="Add")
                    markup.add(button1,button2,button3)
                    bot.send_message(message.from_user.id, "Товар: "+ message.text + " Цена: "+item2, reply_markup=markup)
                    

    elif counter_messager0==1:
        counter_messager0 = counter_messager0 -1
        requester = {'User-Agent': 'Mozilla/5.0'}
        text = GoogleTranslator(source='auto', target='en').translate(message.text)
        censored = profanity.censor(text)
        x='*' in censored
        if x==True:
            bot.send_message(message.from_user.id, "Ну и запросы у тебя😳")
        req=Request("https://yandex.ru/images/search?text="+text.replace(" ", "%20"),headers=requester)
        u = urlopen(req)
        soup = BeautifulSoup(u.read(), features="lxml")

        img_url = []
        for h in soup.findAll('a', {'class': 'serp-item__link'}):
            img_url.append(h.get('href'))
        if img_url:
            imgurl ="https://yandex.ru" + random.choice(img_url)
            bot.send_photo(message.from_user.id, imgurl)
        else:
            bot.send_message(message.from_user.id, "*_*")
        bot.send_message(message.from_user.id, "Готово!")
        repeat(message.from_user.id,'Выберите из меню то, что вы хотите')
    else:
        repeat(message.from_user.id,'Извини, я не понимаю, чего ты хочешь')

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    global price
    global name
    global karsina
    global summ
    sign = 0
    x=0
    int_array = ['1','0','2','3','4','5','6','7','8','9']
    if call.data =="Custom":
        bot.send_message(call.message.chat.id,"Кнопка работает"+call.message.text)
    elif call.data =="Add":
        bot.send_message(call.message.chat.id,"Товар добавлен")
        for n in call.message.text:
            if n==':' and x==0:
                sign=sign+1
                x=x+1
            if n=="Ц":
                sign=0
            if sign==1 and n!=':':
               name = name+n
            if n in int_array:
                price =price+n
     
        y = int(price)
        print(price)
        summ = summ + y
        karsina =karsina+ name + ','
        print(karsina)
        price=""
        name=""

bot.polling(none_stop=True, interval=0)

