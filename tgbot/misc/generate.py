from locale import currency
from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from aiogram.dispatcher.filters.content_types import ContentTypesFilter

from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

from tgbot.misc.texts import mess, make_mess
from tgbot.misc.states import makeImg

from PIL import Image, ImageDraw, ImageFont


async def generate(user_data):

    x = user_data['lavarage'].replace("x", "")
    x = user_data['lavarage'].replace("X", "")
    if float(x) >= 100:
        im = Image.open('tgbot/img/start2.png')
        w = True
    else:
        im = Image.open('tgbot/img/start1.png')
        w = False

    if user_data['way'].lower() == 'long':
        way_color = '#24be82'
        way = 'Long'
    else:
        way_color = '#d55169'
        way = 'Short'

    lav = 0
    for i in user_data['lavarage']:
        lav = lav + 1

    if w == False:
        lav_dist = 387
    else:
        lav_dist = 406

    currency = user_data['currency'].upper() + ' ' + 'Perpetual'

    font = ImageFont.truetype('tgbot/img/SFUIDisplay-Regular.ttf', size=42)
    draw_way = ImageDraw.Draw(im)
    draw_way.text(
        (181, 255),
        way,
        font=font,
        fill=way_color)

    font = ImageFont.truetype(
        'tgbot/img/Fontspring-DEMO-neuevektor-b-medium.otf', size=42)
    draw_lev = ImageDraw.Draw(im)
    draw_lev.text(
        (lav_dist, 252),
        user_data['lavarage'].lower(),
        font=font,
        fill='#f8f4f3')

    font = ImageFont.truetype('tgbot/img/SFUIText-Semibold.ttf', size=42)
    draw_cur = ImageDraw.Draw(im)
    if w == True:
        draw_cur.text(
            (600, 255),
            currency,
            font=font,
            fill='#f8f4f3')
    else:
        draw_cur.text(
            (555, 255),
            currency,
            font=font,
            fill='#f8f4f3')

    Gplus = Image.open('tgbot/img/plus.png')
    Gcom = Image.open('tgbot/img/gcom.png')
    Gper = Image.open('tgbot/img/per.png')
    G0 = Image.open('tgbot/img/0.png')
    G1 = Image.open('tgbot/img/1.png')
    G2 = Image.open('tgbot/img/2.png')
    G3 = Image.open('tgbot/img/3.png')
    G4 = Image.open('tgbot/img/4.png')
    G5 = Image.open('tgbot/img/5.png')
    G6 = Image.open('tgbot/img/6.png')
    G7 = Image.open('tgbot/img/7.png')
    G8 = Image.open('tgbot/img/8.png')
    G9 = Image.open('tgbot/img/9.png')

    # if w == True:
    Gper = Gper.resize((142, 129))
    Gcom = Gcom.resize((145, 131))
    Gplus = Gplus.resize((145, 137))
    G0 = G0.resize((145, 132))
    G1 = G1.resize((145, 130))
    G2 = G2.resize((145, 133))
    G3 = G3.resize((145, 130))
    G4 = G4.resize((145, 131))
    G5 = G5.resize((145, 131))
    G6 = G6.resize((145, 130))
    G7 = G7.resize((145, 130))
    G8 = G8.resize((145, 130))
    G9 = G9.resize((145, 131))
    # else:
    #     Gper = Gper.resize((150, 130))
    #     Gcom = Gcom.resize((150, 130))
    #     Gplus = Gplus.resize((150, 130))
    #     G0 = G0.resize((150, 130))
    #     G1 = G1.resize((150, 130))
    #     G2 = G2.resize((150, 130))
    #     G3 = G3.resize((150, 130))
    #     G4 = G4.resize((150, 130))
    #     G5 = G5.resize((150, 130))
    #     G6 = G6.resize((150, 130))
    #     G7 = G7.resize((150, 130))
    #     G8 = G8.resize((150, 130))
    #     G9 = G9.resize((150, 130))

    Yc = Image.open('tgbot/img/com.png')
    Y0 = Image.open('tgbot/img/00.png')
    Y1 = Image.open('tgbot/img/11.png')
    Y2 = Image.open('tgbot/img/22.png')
    Y3 = Image.open('tgbot/img/33.png')
    Y4 = Image.open('tgbot/img/44.png')
    Y5 = Image.open('tgbot/img/55.png')
    Y6 = Image.open('tgbot/img/66.png')
    Y7 = Image.open('tgbot/img/77.png')
    Y8 = Image.open('tgbot/img/88.png')
    Y9 = Image.open('tgbot/img/99.png')
    Yc = Yc.resize((46, 42))
    Y0 = Y0.resize((46, 42))
    Y1 = Y1.resize((46, 42))
    Y2 = Y2.resize((46, 42))
    Y3 = Y3.resize((46, 42))
    Y4 = Y4.resize((46, 42))
    Y5 = Y5.resize((46, 42))
    Y6 = Y6.resize((46, 42))
    Y7 = Y7.resize((46, 42))
    Y8 = Y8.resize((46, 42))
    Y9 = Y9.resize((46, 42))

    im.paste(Gplus, (120, 331), Gplus)
    profit_dist = 179
    for item in user_data['profit']:
        if item == '0':
            im.paste(G0, (profit_dist, 330), G0)
            profit_dist += 69
        elif item == '1':
            im.paste(G1, (profit_dist, 331), G1)
            profit_dist += 69
        elif item == '2':
            im.paste(G2, (profit_dist, 331), G2)
            profit_dist += 69
        elif item == '3':
            im.paste(G3, (profit_dist, 336), G3)
            profit_dist += 69
        elif item == '4':
            im.paste(G4, (profit_dist, 331), G4)
            profit_dist += 69
        elif item == '5':
            im.paste(G5, (profit_dist, 331), G5)
            profit_dist += 69
        elif item == '6':
            im.paste(G6, (profit_dist, 331), G6)
            profit_dist += 69
        elif item == '7':
            im.paste(G7, (profit_dist, 331), G7)
            profit_dist += 69
        elif item == '8':
            im.paste(G8, (profit_dist, 331), G8)
            profit_dist += 69
        elif item == '9':
            im.paste(G9, (profit_dist, 331), G9)
            profit_dist += 69
        elif item == ',':
            im.paste(Gcom, (profit_dist-15, 376), Gcom)
            profit_dist += 42
        elif item == ' ':
            profit_dist += 32

    im.paste(Gper, (profit_dist + 17, 333), Gper)

    if w == True:
        price_dist = 537
    else:
        price_dist = 555
    for item in user_data['fprice']:
        if item == '0':
            im.paste(Y0, (price_dist, 475), Y0)
            price_dist += 22
        elif item == '1':
            im.paste(Y1, (price_dist, 475), Y1)
            price_dist += 22
        elif item == '2':
            im.paste(Y2, (price_dist, 475), Y2)
            price_dist += 22
        elif item == '3':
            im.paste(Y3, (price_dist, 475), Y3)
            price_dist += 22
        elif item == '4':
            im.paste(Y4, (price_dist, 475), Y4)
            price_dist += 22
        elif item == '5':
            im.paste(Y5, (price_dist, 475), Y5)
            price_dist += 22
        elif item == '6':
            im.paste(Y6, (price_dist, 475), Y6)
            price_dist += 22
        elif item == '7':
            im.paste(Y7, (price_dist, 475), Y7)
            price_dist += 22
        elif item == '8':
            im.paste(Y8, (price_dist, 479), Y8)
            price_dist += 22
        elif item == '9':
            im.paste(Y9, (price_dist, 475), Y9)
            price_dist += 22
        elif item == ',':
            im.paste(Yc, (price_dist-7, 490), Yc)
            price_dist += 10
        elif item == ' ':
            price_dist += 14

    if w == True:
        price_dist = 537
    else:
        price_dist = 555
    for item in user_data['sprice']:
        if item == '0':
            im.paste(Y0, (price_dist, 518), Y0)
            price_dist += 22
        elif item == '1':
            im.paste(Y1, (price_dist, 518), Y1)
            price_dist += 22
        elif item == '2':
            im.paste(Y2, (price_dist, 518), Y2)
            price_dist += 22
        elif item == '3':
            im.paste(Y3, (price_dist, 518), Y3)
            price_dist += 22
        elif item == '4':
            im.paste(Y4, (price_dist, 518), Y4)
            price_dist += 22
        elif item == '5':
            im.paste(Y5, (price_dist, 518), Y5)
            price_dist += 22
        elif item == '6':
            im.paste(Y6, (price_dist, 518), Y6)
            price_dist += 22
        elif item == '7':
            im.paste(Y7, (price_dist, 518), Y7)
            price_dist += 22
        elif item == '8':
            im.paste(Y8, (price_dist, 524), Y8)
            price_dist += 22
        elif item == '9':
            im.paste(Y9, (price_dist, 518), Y9)
            price_dist += 22
        elif item == ',':
            im.paste(Yc, (price_dist-7, 527), Yc)
            price_dist += 10
        elif item == ' ':
            price_dist += 14
    im.show()
    im.save('tgbot/img/output.png')
