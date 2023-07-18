import requests
from bs4 import BeautifulSoup
import telebot

dollar_rub = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=AB5stBj7ab75ekkVVLeKFINMEW6KIsPa9w%3A1689610847030&ei=X2q1ZOPCAdLNwPAPxIKL0AU&ved=0ahUKEwij7uHykpaAAxXSJhAIHUTBAloQ4dUDCA8&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiGtC00L7Qu9C70LDRgCDQuiDRgNGD0LHQu9GOMgsQABiABBixAxiDATIKEAAYgAQYFBiHAjIFEAAYgAQyChAAGIAEGBQYhwIyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI9CdQ3gxYmyNwAXgBkAEAmAFToAG6B6oBAjE0uAEDyAEA-AEBqAIUwgIHECMY6gIYJ8ICEBAAGIoFGOoCGLQCGEPYAQHCAgcQIxiKBRgnwgIQEAAYgAQYFBiHAhixAxiDAcICERAuGIAEGLEDGIMBGMcBGNEDwgILEC4YigUYsQMYgwHCAggQABiABBixA8ICExAAGIAEGBQYhwIYsQMYgwEYyQPCAggQABiKBRiSA8ICCxAAGIoFGLEDGIMBwgIIEAAYgAQYkgPiAwQYACBBiAYBugYGCAEQARgB&sclient=gws-wiz-serp'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

full_page = requests.get(dollar_rub, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})

d_r = convert[0].text
d_r = d_r.replace(',', '.')
d_r = float(d_r)

rub_dollar = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sxsrf=AB5stBhQzpyXyARGDMWW3gBSZZ2GVebuyg%3A1689664532341&ei=FDy2ZJi1FOiawPAP4_acoAs&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+&gs_lp=Egxnd3Mtd2l6LXNlcnAiDtGA0YPQsdC70Ywg0LogKgIIADINEAAYigUYsQMYgwEYQzINEAAYigUYsQMYgwEYQzIKEAAYgAQYFBiHAjINEAAYigUYsQMYgwEYQzINEAAYigUYsQMYgwEYQzINEAAYigUYsQMYgwEYQzINEAAYigUYsQMYgwEYQzIKEAAYigUYsQMYQzINEAAYigUYsQMYgwEYQzINEAAYigUYsQMYgwEYQ0iGPFDRCli_LXACeAGQAQCYAWWgAdkFqgEDOC4xuAEByAEA-AEBqAIUwgIHECMY6gIYJ8ICEBAAGIoFGOoCGLQCGEPYAQHCAgcQIxiKBRgnwgIREC4YgwEYxwEYsQMY0QMYgATCAgsQABiABBixAxiDAcICCxAuGIAEGMcBGNEDwgIIEC4YgAQYsQPCAggQABiABBixA8ICBRAAGIAEwgIEECMYJ8ICBxAAGIoFGEPCAhEQLhiABBixAxiDARjHARjRA-IDBBgAIEGIBgG6BgYIARABGAE&sclient=gws-wiz-serp'

full_page_2 = requests.get(rub_dollar, headers=headers)

soup_2 = BeautifulSoup(full_page_2.content, 'html.parser')

convert_2 = soup_2.findAll("span", {"class": "DFlfde SwHCTb"})

r_d = convert_2[0].text
r_d = r_d.replace(',', '.')
r_d = float(r_d)


euro_rub = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome..69i57j0i512l9.2758j0j7&sourceid=chrome&ie=UTF-8'

full_page_3 = requests.get(euro_rub, headers=headers)

soup_3 = BeautifulSoup(full_page_3.content, 'html.parser')

convert_3 = soup_3.findAll("span", {"class": "DFlfde SwHCTb"})

e_r = convert_3[0].text
e_r = e_r.replace(',', '.')
e_r = float(e_r)


rub_euro = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%B2+%D0%B5%D0%B2%D1%80%D0%BE&oq=he%2Ckm+d+tdhj&aqs=chrome.1.69i57j0i10i433i512j0i10i512l5j0i10i22i30i625j0i10i22i30j0i10i22i30i625.5812j1j7&sourceid=chrome&ie=UTF-8'

full_page_4 = requests.get(rub_euro, headers=headers)

soup_4 = BeautifulSoup(full_page_4.content, 'html.parser')

convert_4 = soup_4.findAll("span", {"class": "DFlfde SwHCTb"})

r_e = convert_4[0].text
r_e = r_e.replace(',', '.')
r_e = float(r_e)


dollar_euro = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome..69i57j0i20i263i512j0i512l4j69i60j69i61.4347j0j7&sourceid=chrome&ie=UTF-8'

full_page_5 = requests.get(dollar_euro, headers=headers)

soup_5 = BeautifulSoup(full_page_5.content, 'html.parser')

convert_5 = soup_5.findAll("span", {"class": "DFlfde SwHCTb"})

d_e = convert_5[0].text
d_e = d_e.replace(',', '.')
d_e = float(d_e)


euro_dollar = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sxsrf=AB5stBiXO8pN1Quf1U_XGcq9B6VPo_Y1JA%3A1689666991509&ei=r0W2ZPHYHvW4wPAPnMaEkAk&ved=0ahUKEwix7MSG5JeAAxV1HBAIHRwjAZIQ4dUDCA8&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&gs_lp=Egxnd3Mtd2l6LXNlcnAiGtC10LLRgNC-INC6INC00L7Qu9C70LDRgNGDMgwQIxiKBRgnGEYYggIyBxAAGIoFGEMyBRAAGIAEMgcQABiKBRhDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESNEOUPAEWOsIcAF4AZABAJgBX6ABqgGqAQEyuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICBxAjGLECGCfCAgsQABgHGB4Y8QQYCsICBxAAGIAEGAriAwQYACBBiAYBkAYI&sclient=gws-wiz-serp'

full_page_6 = requests.get(euro_dollar, headers=headers)

soup_6 = BeautifulSoup(full_page_6.content, 'html.parser')

convert_6 = soup_6.findAll("span", {"class": "DFlfde SwHCTb"})

e_d = convert_6[0].text
e_d = e_d.replace(',', '.')
e_d = float(e_d)


TOKEN = '5839474123:AAE_ZxHJrOZjx5fWL4GaeiFkTyUra9jxgLA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])

def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте. В этом боте мы сможете конвертировать валюту. Чтобы ознакомиться с инструкцией, напишите команду /values')

@bot.message_handler(commands=['values'])

def instr(message):
    bot.send_message(message.chat.id, 'Инструкция\nВалюты:\nевро\nдоллар\nрубль\nТо есть вы должны сначала написать валюту, которую хотите конвертировать, а потом ту валюту, в которую вы хотите ковертировать. После этого нужно написать сумму для конвертации\nПример:\nдоллар рубль 100\nЭто значит, что вы хотите конвертировать 100 долларов в рубли\nНадеюсь, вы поняли. Поэтому пишите')

@bot.message_handler(content_types=['text'])

def text(message):
    txt = message.text.split()
    if txt[0].lower() == 'доллар' and txt[1].lower() == 'рубль':
        amount = int(txt[2])
        answer = d_r * amount
        bot.send_message(message.chat.id, f'Ответ: {answer}')
    elif txt[0].lower() == 'рубль' and txt[1].lower() == 'доллар':
        amount = int(txt[2])
        answer = r_d * amount
        bot.send_message(message.chat.id, f'Ответ: {answer}')
    elif txt[0].lower() == 'евро' and txt[1].lower() == 'рубль':
        amount = int(txt[2])
        answer = e_r * amount
        bot.send_message(message.chat.id, f'Ответ: {answer}')
    elif txt[0].lower() == 'рубль' and txt[1].lower() == 'евро':
        amount = int(txt[2])
        answer = r_e * amount
        bot.send_message(message.chat.id, f'Ответ: {answer}')
    elif txt[0].lower() == 'доллар' and txt[1].lower() == 'евро':
        amount = int(txt[2])
        answer = d_e * amount
        bot.send_message(message.chat.id, f'Ответ: {answer}')
    elif txt[0].lower() == 'евро' and txt[1].lower() == 'доллар':
        amount = int(txt[2])
        answer = e_d * amount
        bot.send_message(message.chat.id, f'Ответ: {answer}')
    else:
        bot.send_message(message.chat.id, 'Вы некорректно написали сообщение!')




bot.polling()



