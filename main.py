import time
import smtplib
import random
#-*- coding: utf-8 -*-
switch = True


with open('data','r') as file:
    line=file.readlines()
Quotes=line[2]

file.close()


E_MAIL = 'zlote.mysli.3b.9@gmail.com'
PASSWORD = 'npg.3b.temat9'

MAIN_TARGET = E_MAIL #bazowe ustawienie
subject = 'Quote of the day'

Time = 15
avalible_list = []

def create_avalible_id_list():
    file_r = open('ids')
    lines = file_r.readlines()
    for el in lines:
        if el != "\n":
            avalible_list.append(el)


def get_random_quote():
    if len(avalible_list)==0:
        print('Wyczerpanie bazy danych, ponawianie cytatów')
        reset_used()
        create_avalible_id_list()

    id = random.choice(avalible_list)
    avalible_list.remove(id)
    id=int(id)

    print('Cytat wybrany', id-99)

    file_r = open('msg')
    lines = file_r.readlines()
    body = str(lines[id-100])

    with open('ids', 'r') as file:
        avalible = file.read()
    avalible = avalible.replace(str(id), "")
    with open('ids', 'w') as file:
        file.write(avalible)


    file_r.close()
    file.close()

    return body,id

def spam(TARGET):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(E_MAIL, PASSWORD)

        body = 'Ayayaya!'
        msg = f'Subject: {subject}\n\n{body}'
        while True:
            smtp.sendmail(E_MAIL, TARGET, msg)
            print('Wiadomosc wyslana')



def send_email(TARGET):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(E_MAIL, PASSWORD)

        content=tuple(get_random_quote())

        id=abs(content[1])-99
        body=content[0]

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(E_MAIL,TARGET,msg)
        print('Wiadomosc wyslana, cytat nr -', id)

def send_repeat(TARGET):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(E_MAIL, PASSWORD)
        while True:
            content = tuple(get_random_quote())
            id = abs(content[1]) - 99
            body = content[0]
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(E_MAIL, TARGET, msg)
            print('Wiadomosc wyslana, cytat nr -', id)
            time.sleep(Time)


def reset_used():
    with open('ids_rplc', 'r') as file:
        data = file.read()
    with open('ids', 'w') as file:
        file.write(data)


def add_quote(amount):
    print('Podaj cytat')
    new_quote = input()
    new_amount=int(amount)+1
    with open('ids_rplc', 'a') as file:
        file.write("\n" + str(new_amount))
    file.close()

    with open('ids', 'a') as file:
        file.write("\n" + str(new_amount))
    file.close()

    with open('msg','a') as file:
        file.write("\n" + str(new_quote))
    file.close()

    with open('data', 'r') as file:
        lines = file.read()
    lines = lines.replace(str(amount),str(new_amount))
    with open('data','w') as file:
        file.write(lines)

    file.close()


    print("Cytat dodany")
    return new_amount

def set_time():
    new_time=0
    print('Podaj jesnostke - sec/min/h/d:')
    case = input()
    if case=='sec':
        print('Podaj ilosc:')
        new_time=int(input())
    elif case=='min':
        print('Podaj ilosc:')
        new_time=60*int(input())
    elif case=='h':
        print('Podaj ilosc:')
        new_time=3600*int(input())
    elif case=='sec':
        print('Podaj ilosc:')
        new_time=86400*int(input())
    else:
        print('Nieprawidłowa wartość')

    print('Ustawiono nowy czas\n')
    return new_time



create_avalible_id_list()

print("set_target - ustawia adres odbiorcy\n"
      "send - wysyła wiadomość\n"
      "show_target - pokazuje obecny adres odbiorcy\n"
      "start - zaczyna proces regularnego wysyłania wiadmości\n"
      "help - pokazuje liste komend\n"
      "end - konczy dzialanie programu\n"
      "reset- resetuje stan dostępnych cytatow\n"
      "add_quote - dodaje cytat do listy mozliwych\n"
      "set_time - ustawia czas między wysłaniem dwóch wiadomości"
      "show_time - pokazuje czas między wysłaniem dwóch wiadomości\n"
      "show_amount - pokazuje ile jest cytatów w bazie danych\n"
      "spam - zaczyna spam\n"
      )

while switch:
    task = input()

    if task == 'set_target':
        print('Podaj adres odbiorcy: \n')
        MAIN_TARGET=input()


    elif task=='send':
        send_email(MAIN_TARGET)


    elif task=='show_target':
        print(MAIN_TARGET, "\n")

    elif task=='reset':
        reset_used()

    elif task=='start':
        start = send_repeat(MAIN_TARGET)

    elif task=='add_quote':
        if int(Quotes)<1000:
            new_amount = add_quote(Quotes)
            Quotes=new_amount
        else:
            print('Brak miejsca')

    elif task=="set_time":
        Time=set_time()

    elif task=="show_time":
        print(Time)

    elif task=="show_amount":
        print(int(Quotes)-100)
    elif task=='spam':
        spam(MAIN_TARGET)

    elif task == 'help':
        print("set_target - ustawia adres odbiorcy\n"
              "send - wysyła wiadomość\n"
              "show_target - pokazuje obecny adres odbiorcy\n"
              "start - zaczyna proces regularnego wysyłania wiadmości\n"
              "help - pokazuje liste komend\n"
              "end - konczy dzialanie programu\n"
              "reset- resetuje stan dostępnych cytatow\n"
              "add_quote - dodaje cytat do listy mozliwych\n"
              "set_time - ustawia czas między wysłaniem dwóch wiadomości"
              "show_time - pokazuje czas między wysłaniem dwóch wiadomości\n"
              "show_amount - pokazuje ile jest cytatów w bazie danych\n"
              "spam - zaczyna spam\n"
              )


    elif task=='end':
        switch = False




