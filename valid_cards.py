
import csv
o = open("card_details.csv", "r")
data = o.read()
info = []
data = data.split('\n')
l =len(data)
data = data[:l-1]
for i in data:
    ldata = i.split(',')
    num = ldata[1]
    card = ldata[2]
    code = ldata[3]
    f = num[0:2]
    if f != '+9':
        print("fdg")
        continue
    else :
        kunal =''
        s = num[2]
        if s == '1':
            temp = num[3:]
            we = temp[0]
            if (ord(we) == ord(' ') or ord(we) == ord('-')) and (ord(temp[1]) == ord('7') or ord(temp[1]) == ord('8')  or ord(temp[1]) == ord('9'))\
                    and (ord(temp[5]) == ord(' ') or ord(temp[5]) == ord('-')) and len(num[3:]) == 12:
                if code == "IND":
                    kunal = num
                else:
                    continue
            else:
                continue
        elif s == '6':
            temp = num[3:]
            we = temp[1]
            if ord(temp[0]) == ord ('8') and ord(we) == ord('-')  and  ord(temp[6]) == ord('-') and len(num[3:]) == 11:
                continue
            if ord(temp[0]) == ord ('8') and (ord(we) == ord(' ')  or ord(we) == ord('-')) and (ord(temp[1]) == ord('9')) and (ord(temp[6]) == ord(' ') or ord(temp[6]) == ord('-')) and len(num[3:]) == 11:
                if code == "OMN":
                    kunal = num
                else:
                    continue
            elif temp[0] == '8' and (temp[1] == ' ' or ord(we) == ord('-')) and temp[2] == '9'  and len(num[3:]) == 10:
                if code == "OMN":
                    kunal = num
                else:
                    continue
            else:
                continue

        elif s == '7':
            temp = num[3:]
            we = temp[1]
            if temp[2] =='5' and (temp[3] =='0' or temp[3] =='2' or temp[3] == '5' or temp[3] =='6') and ord(temp[0]) == ord('1') and (ord(we) == ord(' ') or ord(we) == ord('-')) and (ord(temp[4]) == ord(' ') or ord(temp[4]) == ord('-')) and len(num[3:]) == 12:
                if code == "ARE":
                    kunal = num
                else:
                    continue
            else:
                continue
        else:
            continue
        #print(kunal)

    if len(card) == 16 and card[0] == '4':
        kuna = card
        cardname = "VISA"
    elif len(card) == 16:
        if card[0] == '5' and (card[1] == '1' or card[1] == '2' or card[1] == '3' or card[1] == '4' or card[1] == '5'):
            kuna = card
            cardname = "MasterCard"
        elif card[0] == '2':
            dig = int(card[1:4])
            if dig >=  221 and dig <= 720:
                kuna = card
                cardname = "MasterCard"

            else:
                continue
        else:
            continue
    elif len(card) == 14 and card[0] == '3':
        if card[1] == '0' and  (card[2] == '0' or card[2] =='1' or card[2] =='2' or card[2] =='3' or card[2] =='4' or card[2] == '5'):
            kuna = card
            cardname = "Diners Club"

        elif card[1] == '6' or card[1] == '8':
            kuna = card
            cardname = "Diners Club"

        else:
            continue
    else:
        continue

    tempory = []
    tempory.append(ldata[0])
    tempory.append(ldata[1])
    tempory.append(ldata[2])
    tempory.append(ldata[3])
    tempory.append(cardname)
    info.append(tempory)

o = open("valid_cards.csv", "w")
writer = csv.writer(o, delimiter=',')
for i in info:
    writer.writerow(i)
o.close()
