#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'gbrva'

from translit import *
import random
import os

FName = 'Data/dp2000.txt'
F2Name = 'Data/dp2000.cvs'
Lst1 = ['username', 'password', 'lastname', 'firstname', 'email', 'type1', 'cohort1', 'city', 'country', 'lang']

Email = '@elr.tnpu.edu.ua'
City = 'Тернопіль'
Country = 'UA'
Userlang = 'uk_UTF-8'
TypeTeach = '2'
TypeStud = '6'


def ReadCount(fread):
    f = open(fread, encoding='cp1251')
    n = 0
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        else:
            n = n + 1
    f.close()
    return n


def CreateLogin(name1, name2, number):
    # tmpindx = random.randint(10, 99)
    tmpindx = number[len(number)-3:len(number)]
    tmplogin = name1[:4] + name2[:2] + str(tmpindx)
    loginusr = transliterate(tmplogin.lower())
    if (len(loginusr)<=2):
        loginusr = loginusr+loginusr+loginusr
    return loginusr


def CreatePass(strdata1, strdata2, login):
    if strdata1 != '' and strdata2 != '':
        user_pass = strdata1[3:6] + strdata2[3:-1]
    else:
        if strdata2 == '' and  strdata1 != '':
            user_pass = strdata1[3:6] + str(ord(login[1])) + str(ord(login[2]))
        else:
            if strdata1 == '' and  strdata2 != '':
                user_pass = strdata2[3:6] + str(ord(login[1])) + str(ord(login[2]))
            else:
                user_pass = login[4:6] + login[0:3]
    return user_pass


def CreateImg(fpath, oldfile, newname):
    # Перевіряємо чи існує вихідний файл
    tmpname = os.path.split(fpath)
    oldfile = os.path.join(tmpname[0], oldfile)
    if os.path.exists(oldfile):
        # Отримали шлях і створюємо новий до вхідного файлу
        tmpname = os.path.split(oldfile)
        # створюємо нове імя і перейменовуємо його
        extname = tmpname[1].split('.')
        imgname = os.path.join(tmpname[0], newname + '.' + extname[1])
        os.rename(oldfile, imgname)
    return None


def Convert_1c(fread, fwrite, flag):
    fr = open(fread, encoding='cp1251')
    fw = open(fwrite, 'w', encoding='utf8')
    fw.write('\ufeff')
    writestr = ','.join(Lst1) + '\n'
    fw.write(writestr)
    count = ReadCount(fread)
    step = 10
    n = 0
    while True:
        line = fr.readline()
        if len(line) == 0:
            break
        else:
            n = n + 1
            lst = line.split('|')
            cohorts = lst[20] + ' (' + lst[21] + ')'
            loginusr = CreateLogin(lst[0], lst[1], lst[9])
            if loginusr == '':
                continue
            passvdusr = CreatePass(lst[7], lst[9], loginusr)
            usermail = loginusr + Email
            lstv = [loginusr, passvdusr, lst[0], lst[1], usermail, TypeStud, cohorts, City, Country]
            writestr = ','.join(lstv) + '\n'
            fw.write(writestr)
            # Створюмо файли з фотографіями
            if flag and (lst[13] != ''):
                CreateImg(fread, lst[13], lstv[0])

            if (count % step) == 0:
                print('Виконано: ', str(n * 100 / count), '%')

    fr.close()
    fw.close()
    return None


def Convert_Text(fread, fwrite):
    '''
        Функція приймає на вхід файл такого формату
        Прізвище, Імя, форма навчання(п-післядипломна, з-заочна), Факультет, Група
         [0          1     2     3           4]
        Кукурікін, Петро, п, Іноземна мова, 21
        Кукурікін, Василь, з, Іноземна мова, 22
    '''

    fr = open(fread)
    fw = open(fwrite, 'w')
    writestr = ','.join(Lst1) + '\n'
    fw.write(writestr)
    count = ReadCount(fread)
    step = 10
    n = 0
    while True:
        line = fr.readline()
        if len(line) == 0:
            break
        else:
            n = n + 1
            lst = line.split('|')
            cohorts = lst[2] + lst[3] + ' (' + lst[4] + ')'
            loginusr = CreateLogin(lst[0], lst[1], lst[9])
            passvdusr = CreatePass(lst[7], lst[9], loginusr)
            usermail = loginusr + Email
            lstv = [loginusr, passvdusr, lst[0], lst[1], usermail, TypeStud, cohorts, City, Country]
            writestr = ','.join(lstv) + '\n'
            fw.write(writestr)
            if (count % step) == 0:
                print('Виконано: ', str(n * 100 / count), '%')

    fr.close()
    fw.close()
    return None
