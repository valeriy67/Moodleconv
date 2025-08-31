#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'gbrva'

from translit import *
from PIL import Image, ImageOps, UnidentifiedImageError
import random
import os, time
# resample-алгоритм сумісний із різними версіями Pillow
RESAMPLE = getattr(Image, "LANCZOS", getattr(Image, "ANTIALIAS", Image.BICUBIC))
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
    loginusr = transliterate(tmplogin.lower().replace(" ", ""))
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


def _retry(func, *args, attempts=5, delay=0.2):
    """Повторює файлову операцію кілька разів, щоб обійти тимчасові локи Windows."""
    for i in range(attempts):
        try:
            return func(*args)
        except PermissionError:
            if i == attempts - 1:
                raise
            time.sleep(delay)
def fix_ukr_i(s: str) -> str:
    """Замінює латинські i/I на українські і/І (тільки для текстів типу назви групи)."""
    if not s:
        return s
    return s.replace('i', 'і').replace('I', 'І')
def CreateImg(fpath, oldfile, newname, max_size=(800, 600)):
    """
    Перейменовує фото у тій самій папці, що й вхідний файл.
    Якщо перевищує max_size — пропорційно зменшує (вписує у рамку),
    виправляє EXIF-орієнтацію, а для JPEG ще й зрізає EXIF.
    Захищено від WinError 32 (операції з файлами після закриття).
    """



    base_dir = os.path.split(fpath)[0]
    old_path = os.path.join(base_dir, oldfile)
    if not os.path.exists(old_path):
        return None

    _, ext = os.path.splitext(oldfile)
    ext = (ext or ".jpg").lower()                     # ".jpg", ".png", ...
    new_path = os.path.join(base_dir, f"{newname}{ext}")
    fmt = "JPEG" if ext in (".jpg", ".jpeg") else ext.lstrip(".").upper()

    made_new_file = False

    try:
        with Image.open(old_path) as img:
            # виправити орієнтацію за EXIF, щоб коректно рахувались розміри
            img = ImageOps.exif_transpose(img)
            w, h = img.size

            if w > max_size[0] or h > max_size[1]:
                img.thumbnail(max_size, resample=RESAMPLE)

                # JPEG вимагає RGB
                if fmt == "JPEG" and img.mode not in ("RGB", "L"):
                    img = img.convert("RGB")

                # Збереження (для JPEG ще зрізаємо EXIF повністю)
                if fmt == "JPEG":
                    img.save(new_path, format="JPEG", optimize=True, quality=88, exif=b'')
                elif fmt == "PNG":
                    img.save(new_path, format="PNG", optimize=True)
                else:
                    img.save(new_path, format=fmt)
                made_new_file = True

    except UnidentifiedImageError:
        # не зображення/пошкоджене — далі просто спробуємо перейменувати
        pass
    except Exception as e:
        print(f"Не вдалося обробити зображення {old_path}: {e}")
        return None

    # Тут файл уже закрито → безпечно видаляти/перейменовувати
    try:
        if made_new_file:
            if old_path != new_path and os.path.exists(old_path):
                _retry(os.remove, old_path)
        else:
            if old_path != new_path:
                if os.path.exists(new_path):
                    _retry(os.remove, new_path)
                _retry(os.replace, old_path, new_path)  # атомарна заміна
    except Exception as e:
        print(f"Помилка фіналізації для {old_path} → {new_path}: {e}")

    return None

def Convert_1c(fread, fwrite, flag, max_img_size=(800, 600)):
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

        n += 1
        lst = line.split('|')

        # БЕЗПЕЧНИЙ доступ до індексів
        last_name  = lst[0] if len(lst) > 0 else ''
        first_name = lst[1] if len(lst) > 1 else ''
        pass_1     = lst[7] if len(lst) > 7 else ''
        pass_2     = lst[9] if len(lst) > 9 else ''
        faculty    = lst[20].strip() if len(lst) > 20 else ''
        group_name = lst[21].strip() if len(lst) > 21 else ''
        if group_name == '':
            continue
        photo_file = lst[13].strip() if len(lst) > 13 else ''

        # Логін рахуємо відразу — він знадобиться і для перейменування фото
        loginusr = CreateLogin(last_name, first_name, pass_2)
        if loginusr == '':
            # Якщо логін не згенерувався — просто пропускаємо весь запис
            # (і фото перейменувати тоді нема як)
            continue

        # Якщо ГРУПА ПУСТА → фото все одно перейменувати (якщо просили), але
        # у CSV нічого не писати.
        if group_name == '':
            if flag and photo_file:
                CreateImg(fread, photo_file, loginusr, max_size=max_img_size)
            # пропускаємо запис без групи
            continue

        # Когорта (можете залишити свою заміну літер для faculty, якщо потрібно)
        cohorts = f"{faculty} ({group_name})"

        # Пароль/емейл
        passvdusr = CreatePass(pass_1, pass_2, loginusr)
        usermail  = loginusr + Email

        # ПИШЕМО РЯДОК У CSV
        lstv = [loginusr, passvdusr, last_name, first_name, usermail,
                TypeStud, cohorts, City, Country, Userlang]
        fw.write(','.join(lstv) + '\n')

        # Перейменування фото (якщо треба)
        if flag and photo_file:
            CreateImg(fread, photo_file, loginusr, max_size=max_img_size)

        if (n % step) == 0:
            print('Виконано: ', str(n * 100 / count), '%')

    fr.close()
    fw.close()
    return None


def Convert_Text(fread, fwrite):
    """
    Очікуваний формат вхідного тексту:
      Прізвище|Імя|форма(п/з)|Факультет|Група|... (можливі додаткові поля)
    Формує CSV для Moodle з заголовком Lst1 (включно з полем 'lang').
    """

    # --- читання вхідного (пробуємо UTF-8, якщо не вийде — cp1251) ---
    try:
        fr = open(fread, encoding='utf8')
    except UnicodeDecodeError:
        fr = open(fread, encoding='cp1251')

    # --- запис вихідного CSV у UTF-8 з BOM (зручно для Excel) ---
    fw = open(fwrite, 'w', encoding='utf8')
    fw.write('\ufeff')  # BOM
    writestr = ','.join(Lst1) + '\n'   # Lst1 вже містить 'lang'
    fw.write(writestr)

    count = ReadCount(fread)
    step = 10
    n = 0

    while True:
        line = fr.readline()
        if len(line) == 0:
            break

        n += 1
        line = line.strip()
        if not line:
            continue

        lst = line.split('|')

        # Безпечний доступ до полів (індексів може не бути — тоді підставляємо '')
        last_name   = lst[0] if len(lst) > 0 else ''
        first_name  = lst[1] if len(lst) > 1 else ''
        form        = lst[2] if len(lst) > 2 else ''       # п/з
        faculty     = lst[3] if len(lst) > 3 else ''
        group_code  = lst[4] if len(lst) > 4 else ''

        # Якщо у вас у текстовому файлі є додаткові колонки для CreatePass,
        # наприклад дати/номери на позиціях 7 і 9 — беремо їх, інакше ''.
        pass_src_1  = lst[7] if len(lst) > 7 else ''
        pass_src_2  = lst[9] if len(lst) > 9 else ''

        # Когорта (налаштуйте як вам потрібно)
        cohorts = f"{form}{fix_ukr_i(faculty)} ({group_code.strip()})"

        # Логін/пароль
        loginusr  = CreateLogin(last_name, first_name, pass_src_2 or group_code or '000')
        if loginusr == '':
            continue
        passvdusr = CreatePass(pass_src_1, pass_src_2, loginusr)

        usermail = loginusr + Email

        # ДОДАЛИ поле мови (Userlang) наприкінці, щоб відповідало заголовку Lst1
        lstv = [loginusr, passvdusr, last_name, first_name, usermail,
                TypeStud, cohorts, City, Country, Userlang]

        writestr = ','.join(lstv) + '\n'
        fw.write(writestr)

        # Правильний прогрес: кожні `step` рядків
        if (n % step) == 0:
            print('Виконано: ', str(n * 100 / count), '%')

    fr.close()
    fw.close()
    return None
