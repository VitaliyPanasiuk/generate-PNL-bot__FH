from PIL import Image, ImageDraw, ImageFont



def generate(user_data):

    x = user_data['lavarage'].replace("x", "").replace("X", "").replace("х", "").replace("Х", "")
    # x = user_data['lavarage']
    # x = user_data['lavarage']
    # x = user_data['lavarage']
    print(x)
    if float(x) >= 100:
        im = Image.open('start2.png')
        w = True
    else:
        im = Image.open('start1.png')
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
        # lav_dist = 413
    else:
        lav_dist = 406
        # lav_dist = 408

    currency = user_data['currency'].upper() + ' ' + 'Perpetual'

    font = ImageFont.truetype('SFUIDisplay-Regular.ttf', size=42)
    draw_way = ImageDraw.Draw(im)
    draw_way.text(
        (187, 255),
        way,
        font=font,
        fill=way_color)

    font = ImageFont.truetype(
        'Fontspring-DEMO-neuevektor-b-medium.otf', size=42)
    draw_lev = ImageDraw.Draw(im)
    draw_lev.text(
        (lav_dist, 255),
        user_data['lavarage'].lower(),
        font=font,
        fill='#f8f4f3')

    font = ImageFont.truetype('SFUIText-Semibold.ttf', size=42)
    draw_cur = ImageDraw.Draw(im)
    if w == True:
        draw_cur.text(
            (605, 255),
            currency,
            font=font,
            fill='#f8f4f3')
    else:
        # draw_cur.text(
        #         (553, 258),
        #         currency,
        #         font=font,
        #         fill='#f8f4f3')

        start_length = 553
        for i in currency:
            draw_cur.text(
                (start_length, 258),
                i,
                font=font,
                fill='#f8f4f3')
            start_length += int(font.getsize(i)[0])-3

    Gplus = Image.open('plus.png')
    Gcom = Image.open('gcom.png')
    Gper = Image.open('per.png')
    G0 = Image.open('0.png')
    G1 = Image.open('1.png')
    G2 = Image.open('2.png')
    G3 = Image.open('3.png')
    G4 = Image.open('4.png')
    G5 = Image.open('5.png')
    G6 = Image.open('6.png')
    G7 = Image.open('7.png')
    G8 = Image.open('8.png')
    G9 = Image.open('9.png')

    # if w == True:
    # Gper = Gper.resize((90, 84))
    # Gcom = Gcom.resize((16, 27))
    # Gper = Gper.resize((142, 134))
    # Gcom = Gcom.resize((145, 130))
    Gplus = Gplus.resize((53, 53))
    # G0 = G0.resize((50, 84))
    # G1 = G1.resize((32, 84))
    # G2 = G2.resize((53, 84))
    # G3 = G3.resize((53, 84))
    # G4 = G4.resize((60, 84))
    # G5 = G5.resize((61, 84))
    # G6 = G6.resize((53, 84))
    # G7 = G7.resize((54, 84))
    # G8 = G8.resize((53, 84))
    # G9 = G9.resize((53, 84))
    # G0 = G0.resize((150, 130))
    # G1 = G1.resize((150, 130))
    # G2 = G2.resize((150, 130))
    # G3 = G3.resize((150, 130))
    # G4 = G4.resize((150, 130))
    # G5 = G5.resize((150, 130))
    # G6 = G6.resize((150, 130))
    # G7 = G7.resize((150, 130))
    # G8 = G8.resize((150, 130))
    # G9 = G9.resize((150, 130))
    
    Gper = Gper.resize((150, 137))
    Gcom = Gcom.resize((150, 130))
    # Gplus = Gplus.resize((150, 130))
    G0 = G0.resize((150, 138))
    G1 = G1.resize((150, 137))
    G2 = G2.resize((150, 140))
    G3 = G3.resize((150, 137))
    G4 = G4.resize((150, 137))
    G5 = G5.resize((150, 137))
    G6 = G6.resize((150, 137))
    G7 = G7.resize((150, 137))
    G8 = G8.resize((150, 137))
    G9 = G9.resize((150, 137))
    

    

    im.paste(Gplus, (165, 375), Gplus)
    profit_dist = 186
    for item in user_data['profit']:
        if item == '0':
            im.paste(G0, (profit_dist, 328), G0)
            profit_dist += 69
        elif item == '1':
            im.paste(G1, (profit_dist, 329), G1)
            profit_dist += 69
        elif item == '2':
            im.paste(G2, (profit_dist, 329), G2)
            profit_dist += 69
        elif item == '3':
            im.paste(G3, (profit_dist, 335), G3)
            profit_dist += 69
        elif item == '4':
            im.paste(G4, (profit_dist, 330), G4)
            profit_dist += 69
        elif item == '5':
            im.paste(G5, (profit_dist, 329), G5)
            profit_dist += 69
        elif item == '6':
            im.paste(G6, (profit_dist, 330), G6)
            profit_dist += 69
        elif item == '7':
            im.paste(G7, (profit_dist, 329), G7)
            profit_dist += 69
        elif item == '8':
            im.paste(G8, (profit_dist, 329), G8)
            profit_dist += 69
        elif item == '9':
            im.paste(G9, (profit_dist, 330), G9)
            profit_dist += 69
        elif item == ',':
            # im.paste(Gcom, (profit_dist, 427), Gcom)
            # profit_dist += 27
            im.paste(Gcom, (profit_dist-15, 376), Gcom)
            profit_dist += 42
        elif item == ' ':
            profit_dist += 32

    # im.paste(Gper, (profit_dist + 37, 354), Gper)
    im.paste(Gper, (profit_dist + 48, 332), Gper)
    
    Yc = Image.open('com.png')
    Y0 = Image.open('00.png')
    Y1 = Image.open('11.png')
    Y2 = Image.open('22.png')
    Y3 = Image.open('33.png')
    Y4 = Image.open('44.png')
    Y5 = Image.open('55.png')
    Y6 = Image.open('66.png')
    Y7 = Image.open('77.png')
    Y8 = Image.open('88.png')
    Y9 = Image.open('99.png')
    Yc = Yc.resize((46, 44))
    Y0 = Y0.resize((46, 44))
    Y1 = Y1.resize((46, 44))
    Y2 = Y2.resize((46, 44))
    Y3 = Y3.resize((46, 44))
    Y4 = Y4.resize((46, 44))
    Y5 = Y5.resize((46, 44))
    Y6 = Y6.resize((46, 44))
    Y7 = Y7.resize((46, 44))
    Y8 = Y8.resize((46, 44))
    Y9 = Y9.resize((46, 44))

    if w == True:
        price_dist = 537
    else:
        price_dist = 584
        
    for item in user_data['fprice']:
        if item == '0':
            im.paste(Y0, (price_dist, 473), Y0)
            price_dist += 22
        elif item == '1':
            im.paste(Y1, (price_dist, 473), Y1)
            price_dist += 22
        elif item == '2':
            im.paste(Y2, (price_dist, 473), Y2)
            price_dist += 22
        elif item == '3':
            im.paste(Y3, (price_dist, 474), Y3)
            price_dist += 22
        elif item == '4':
            im.paste(Y4, (price_dist, 473), Y4)
            price_dist += 22
        elif item == '5':
            im.paste(Y5, (price_dist, 473), Y5)
            price_dist += 22
        elif item == '6':
            im.paste(Y6, (price_dist, 473), Y6)
            price_dist += 22
        elif item == '7':
            im.paste(Y7, (price_dist-5, 473), Y7)
            price_dist += 22
        elif item == '8':
            im.paste(Y8, (price_dist, 473), Y8)
            price_dist += 22
        elif item == '9':
            im.paste(Y9, (price_dist, 473), Y9)
            price_dist += 22
        elif item == ',':
            im.paste(Yc, (price_dist-3, 488), Yc)
            price_dist += 17
        elif item == ' ':
            price_dist += 14

    if w == True:
        price_dist = 537
    else:
        price_dist = 584
    for item in user_data['sprice']:
        if item == '0':
            im.paste(Y0, (price_dist, 517), Y0)
            price_dist += 22
        elif item == '1':
            im.paste(Y1, (price_dist, 517), Y1)
            price_dist += 22
        elif item == '2':
            im.paste(Y2, (price_dist, 517), Y2)
            price_dist += 22
        elif item == '3':
            im.paste(Y3, (price_dist, 518), Y3)
            price_dist += 22
        elif item == '4':
            im.paste(Y4, (price_dist, 517), Y4)
            price_dist += 22
        elif item == '5':
            im.paste(Y5, (price_dist, 517), Y5)
            price_dist += 22
        elif item == '6':
            im.paste(Y6, (price_dist, 517), Y6)
            price_dist += 22
        elif item == '7':
            im.paste(Y7, (price_dist-5, 517), Y7)
            price_dist += 22
        elif item == '8':
            im.paste(Y8, (price_dist, 517), Y8)
            price_dist += 22
        elif item == '9':
            im.paste(Y9, (price_dist, 517), Y9)
            price_dist += 22
        elif item == ',':
            im.paste(Yc, (price_dist-3, 532), Yc)
            price_dist += 17
        elif item == ' ':
            price_dist += 14
    im.show()
    im.save('output.png')