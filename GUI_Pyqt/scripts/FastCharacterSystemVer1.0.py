import random 


role = int(input('''Соло - 1 
Рокер - 2
Нетраннер - 3
Медиа - 4
Номад - 5
Фиксер - 6
Коп - 7
Копрпорат - 8
Техник - 9
Медтехник - 10
'''))

stats = []
for i in range(10):
    stats.append(random.randint(2, 10))


stats.sort()
stats.reverse()
inte = 0
ref = 0
teh = 0
cool = 0
char = 0
luck = 0
mov = 0
body = 0
emp = 0
special = 0


special = stats.pop(0)
if role == 1:
    # СОЛО
    ref = stats.pop(0)
    body = stats.pop(0)
    cool = stats.pop(0)
    
    inte = stats.pop(0)
    teh = stats.pop(0)
    char = stats.pop(0)
    mov = stats.pop(0)
    emp = stats.pop(0)
    luck = stats.pop(0)
elif role == 2:
    # РОКЕР
    cool = stats.pop(0)
    char = stats.pop(0)
    emp = stats.pop(0)
    
    inte = stats.pop(0)
    ref = stats.pop(0)
    teh = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    luck = stats.pop(0)
elif role == 3:
    # НЕТРАННЕР
    inte = stats.pop(0)
    teh = stats.pop(0)
    
    ref = stats.pop(0)
    cool = stats.pop(0)
    char = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    emp = stats.pop(0)
    luck = stats.pop(0)
elif role == 4:
    #МЕДИА
    emp = stats.pop(0)
    inte = stats.pop(0)
    char = stats.pop(0)
    
    ref = stats.pop(0)
    teh = stats.pop(0)
    cool = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    luck = stats.pop(0)
elif role == 5:
    # НОМАД
    ref = stats.pop(0)
    body = stats.pop(0)
    teh = stats.pop(0)

    inte = stats.pop(0)
    cool = stats.pop(0)
    char = stats.pop(0)    
    mov = stats.pop(0)
    emp = stats.pop(0)
    luck = stats.pop(0)
elif role == 6:
    # ФИКСЕР
    emp = stats.pop(0)
    char = stats.pop(0)
    teh = stats.pop(0)

    inte = stats.pop(0)
    ref = stats.pop(0)
    cool = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    luck = stats.pop(0)
elif role == 7:
    # КОП
    ref = stats.pop(0)
    cool = stats.pop(0)
    emp = stats.pop(0)

    inte = stats.pop(0)
    teh = stats.pop(0)
    char = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    luck = stats.pop(0)
elif role == 8:
    # КОРПОРАТ
    cool = stats.pop(0)
    char = stats.pop(0)
    ref = stats.pop(0)

    inte = stats.pop(0)
    teh = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    emp = stats.pop(0)
    luck = stats.pop(0)
elif role == 9:
    # ТЕХНИК
    teh = stats.pop(0)
    inte = stats.pop(0)

    ref = stats.pop(0)
    cool = stats.pop(0)
    char = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    emp = stats.pop(0)
    luck = stats.pop(0)
elif role == 10:
    # МЕДТЕХНИК
    teh = stats.pop(0)
    inte = stats.pop(0)
    luck = stats.pop(0)

    ref = stats.pop(0)
    cool = stats.pop(0)
    char = stats.pop(0)
    mov = stats.pop(0)
    body = stats.pop(0)
    emp = stats.pop(0)

BodyMod = body // 2

toughnes = int(input('''Сложность НПС
Уличный - 1
Продвинутый - 2
Корпоратский - 3
'''))


cybernetics = []

if toughnes == 1:
    if role == 1:
        for i in range(2):
            temp = random.randint(1, 10)
            if temp == 1:
                #ОПТИКА
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Инфракрасная оптика')
                elif temp2 == 2:
                    cybernetics.append('Ночное зрение')
                elif temp2 == 3:
                    cybernetics.append('Камера')
                elif temp2 == 4:
                    cybernetics.append('Дротикомет')
                elif temp2 == 5:
                    cybernetics.append('Антиослепление')
                elif temp2 == 6:
                    cybernetics.append('Прицельный интерфейс')
            if temp == 2:
                # КИБЕР РУКА С ОРУЖИЕМ
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Средний пистолет')
                if temp2 == 2:
                    cybernetics.append('Легкий пистолет')
                if temp2 == 3:
                    cybernetics.append('Средний пистолет')
                if temp2 == 4:
                    cybernetics.append('Легкий ПП')
                if temp2 == 5:
                    cybernetics.append('Очень тяжелый пистолет')
                if temp2 == 6:
                    cybernetics.append('Тяжелый пистолет')
            if temp == 3:
                # КИБЕР АУДИО
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Музыкальный имплант')
                if temp2 == 2:
                    cybernetics.append('Перехватчик сигнала')
                if temp2 == 3:
                    cybernetics.append('Телефон')
                if temp2 == 4:
                    cybernetics.append('Улучшенный слух')
                if temp2 == 5:
                    cybernetics.append('Редактор слуха')
                if temp2 == 6:
                    cybernetics.append('Звукозаписывающее устройство')
            if temp == 4:
                cybernetics.append('Большие костяшки')
            if temp == 5:
                cybernetics.append('Потрошители')
            if temp == 6:
                cybernetics.append('Руки богомола')
            if temp == 7:
                cybernetics.append('Керезников')
            if temp == 8:
                cybernetics.append('Сандевистан')
            if temp == 9:
                cybernetics.append('Вампиры')
            if temp == 10:
                pass
    else:
        for i in range(1):
            temp = random.randint(1, 10)
            if temp == 1:
                #ОПТИКА
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Инфракрасная оптика')
                elif temp2 == 2:
                    cybernetics.append('Ночное зрение')
                elif temp2 == 3:
                    cybernetics.append('Камера')
                elif temp2 == 4:
                    cybernetics.append('Дротикомет')
                elif temp2 == 5:
                    cybernetics.append('Антиослепление')
                elif temp2 == 6:
                    cybernetics.append('Прицельный интерфейс')
            if temp == 2:
                # КИБЕР РУКА С ОРУЖИЕМ
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Средний пистолет')
                if temp2 == 2:
                    cybernetics.append('Легкий пистолет')
                if temp2 == 3:
                    cybernetics.append('Средний пистолет')
                if temp2 == 4:
                    cybernetics.append('Легкий ПП')
                if temp2 == 5:
                    cybernetics.append('Очень тяжелый пистолет')
                if temp2 == 6:
                    cybernetics.append('Тяжелый пистолет')
            if temp == 3:
                # КИБЕР АУДИО
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Музыкальный имплант')
                if temp2 == 2:
                    cybernetics.append('Перехватчик сигнала')
                if temp2 == 3:
                    cybernetics.append('Телефон')
                if temp2 == 4:
                    cybernetics.append('Улучшенный слух')
                if temp2 == 5:
                    cybernetics.append('Редактор слуха')
                if temp2 == 6:
                    cybernetics.append('Звукозаписывающее устройство')
            if temp == 4:
                cybernetics.append('Большие костяшки')
            if temp == 5:
                cybernetics.append('Потрошители')
            if temp == 6:
                cybernetics.append('Руки богомола')
            if temp == 7:
                cybernetics.append('Керезников')
            if temp == 8:
                cybernetics.append('Сандевистан')
            if temp == 9:
                cybernetics.append('Вампиры')
            if temp == 10:
                pass

if toughnes == 2:
    if role == 1:
        for i in range(4):
            temp = random.randint(1, 10)
            if temp == 1:
                #ОПТИКА
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Инфракрасная оптика')
                elif temp2 == 2:
                    cybernetics.append('Ночное зрение')
                elif temp2 == 3:
                    cybernetics.append('Камера')
                elif temp2 == 4:
                    cybernetics.append('Дротикомет')
                elif temp2 == 5:
                    cybernetics.append('Антиослепление')
                elif temp2 == 6:
                    cybernetics.append('Прицельный интерфейс')
            if temp == 2:
                # КИБЕР РУКА С ОРУЖИЕМ
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Средний пистолет')
                if temp2 == 2:
                    cybernetics.append('Легкий пистолет')
                if temp2 == 3:
                    cybernetics.append('Средний пистолет')
                if temp2 == 4:
                    cybernetics.append('Легкий ПП')
                if temp2 == 5:
                    cybernetics.append('Очень тяжелый пистолет')
                if temp2 == 6:
                    cybernetics.append('Тяжелый пистолет')
            if temp == 3:
                # КИБЕР АУДИО
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Музыкальный имплант')
                if temp2 == 2:
                    cybernetics.append('Перехватчик сигнала')
                if temp2 == 3:
                    cybernetics.append('Телефон')
                if temp2 == 4:
                    cybernetics.append('Улучшенный слух')
                if temp2 == 5:
                    cybernetics.append('Редактор слуха')
                if temp2 == 6:
                    cybernetics.append('Звукозаписывающее устройство')
            if temp == 4:
                cybernetics.append('Большие костяшки')
            if temp == 5:
                cybernetics.append('Потрошители')
            if temp == 6:
                cybernetics.append('Руки богомола')
            if temp == 7:
                cybernetics.append('Керезников')
            if temp == 8:
                cybernetics.append('Сандевистан')
            if temp == 9:
                cybernetics.append('Вампиры')
            if temp == 10:
                pass
    else:
        for i in range(2):
            temp = random.randint(1, 10)
            if temp == 1:
                #ОПТИКА
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Инфракрасная оптика')
                elif temp2 == 2:
                    cybernetics.append('Ночное зрение')
                elif temp2 == 3:
                    cybernetics.append('Камера')
                elif temp2 == 4:
                    cybernetics.append('Дротикомет')
                elif temp2 == 5:
                    cybernetics.append('Антиослепление')
                elif temp2 == 6:
                    cybernetics.append('Прицельный интерфейс')
            if temp == 2:
                # КИБЕР РУКА С ОРУЖИЕМ
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Средний пистолет')
                if temp2 == 2:
                    cybernetics.append('Легкий пистолет')
                if temp2 == 3:
                    cybernetics.append('Средний пистолет')
                if temp2 == 4:
                    cybernetics.append('Легкий ПП')
                if temp2 == 5:
                    cybernetics.append('Очень тяжелый пистолет')
                if temp2 == 6:
                    cybernetics.append('Тяжелый пистолет')
            if temp == 3:
                # КИБЕР АУДИО
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Музыкальный имплант')
                if temp2 == 2:
                    cybernetics.append('Перехватчик сигнала')
                if temp2 == 3:
                    cybernetics.append('Телефон')
                if temp2 == 4:
                    cybernetics.append('Улучшенный слух')
                if temp2 == 5:
                    cybernetics.append('Редактор слуха')
                if temp2 == 6:
                    cybernetics.append('Звукозаписывающее устройство')
            if temp == 4:
                cybernetics.append('Большие костяшки')
            if temp == 5:
                cybernetics.append('Потрошители')
            if temp == 6:
                cybernetics.append('Руки богомола')
            if temp == 7:
                cybernetics.append('Керезников')
            if temp == 8:
                cybernetics.append('Сандевистан')
            if temp == 9:
                cybernetics.append('Вампиры')
            if temp == 10:
                pass

if toughnes == 3:
    if role == 1:
        for i in range(6):
            temp = random.randint(1, 10)
            if temp == 1:
                #ОПТИКА
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Инфракрасная оптика')
                elif temp2 == 2:
                    cybernetics.append('Ночное зрение')
                elif temp2 == 3:
                    cybernetics.append('Камера')
                elif temp2 == 4:
                    cybernetics.append('Дротикомет')
                elif temp2 == 5:
                    cybernetics.append('Антиослепление')
                elif temp2 == 6:
                    cybernetics.append('Прицельный интерфейс')
            if temp == 2:
                # КИБЕР РУКА С ОРУЖИЕМ
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Средний пистолет')
                if temp2 == 2:
                    cybernetics.append('Легкий пистолет')
                if temp2 == 3:
                    cybernetics.append('Средний пистолет')
                if temp2 == 4:
                    cybernetics.append('Легкий ПП')
                if temp2 == 5:
                    cybernetics.append('Очень тяжелый пистолет')
                if temp2 == 6:
                    cybernetics.append('Тяжелый пистолет')
            if temp == 3:
                # КИБЕР АУДИО
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Музыкальный имплант')
                if temp2 == 2:
                    cybernetics.append('Перехватчик сигнала')
                if temp2 == 3:
                    cybernetics.append('Телефон')
                if temp2 == 4:
                    cybernetics.append('Улучшенный слух')
                if temp2 == 5:
                    cybernetics.append('Редактор слуха')
                if temp2 == 6:
                    cybernetics.append('Звукозаписывающее устройство')
            if temp == 4:
                cybernetics.append('Большие костяшки')
            if temp == 5:
                cybernetics.append('Потрошители')
            if temp == 6:
                cybernetics.append('Руки богомола')
            if temp == 7:
                cybernetics.append('Керезников')
            if temp == 8:
                cybernetics.append('Сандевистан')
            if temp == 9:
                cybernetics.append('Вампиры')
            if temp == 10:
                pass
    else:
        for i in range(3):
            temp = random.randint(1, 10)
            if temp == 1:
                #ОПТИКА
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Инфракрасная оптика')
                elif temp2 == 2:
                    cybernetics.append('Ночное зрение')
                elif temp2 == 3:
                    cybernetics.append('Камера')
                elif temp2 == 4:
                    cybernetics.append('Дротикомет')
                elif temp2 == 5:
                    cybernetics.append('Антиослепление')
                elif temp2 == 6:
                    cybernetics.append('Прицельный интерфейс')
            if temp == 2:
                # КИБЕР РУКА С ОРУЖИЕМ
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Средний пистолет')
                if temp2 == 2:
                    cybernetics.append('Легкий пистолет')
                if temp2 == 3:
                    cybernetics.append('Средний пистолет')
                if temp2 == 4:
                    cybernetics.append('Легкий ПП')
                if temp2 == 5:
                    cybernetics.append('Очень тяжелый пистолет')
                if temp2 == 6:
                    cybernetics.append('Тяжелый пистолет')
            if temp == 3:
                # КИБЕР АУДИО
                temp2 = random.randint(1, 6)
                if temp2 == 1:
                    cybernetics.append('Музыкальный имплант')
                if temp2 == 2:
                    cybernetics.append('Перехватчик сигнала')
                if temp2 == 3:
                    cybernetics.append('Телефон')
                if temp2 == 4:
                    cybernetics.append('Улучшенный слух')
                if temp2 == 5:
                    cybernetics.append('Редактор слуха')
                if temp2 == 6:
                    cybernetics.append('Звукозаписывающее устройство')
            if temp == 4:
                cybernetics.append('Большие костяшки')
            if temp == 5:
                cybernetics.append('Потрошители')
            if temp == 6:
                cybernetics.append('Руки богомола')
            if temp == 7:
                cybernetics.append('Керезников')
            if temp == 8:
                cybernetics.append('Сандевистан')
            if temp == 9:
                cybernetics.append('Вампиры')
            if temp == 10:
                pass

gear = []

if toughnes == 1:
    temp = random.randint(1, 3)
    if role == 7 or role == 5:
        temp += 2
    if role == 1:
        temp += 3
    else:
        pass
    if temp == 1:
        gear.append('Тяжелая кожа, Нож')
    elif temp == 2:
        gear.append('Бронежилет, легкий пистолет')
    elif temp == 3:
        gear.append('Легкая бронекуртка, средний пистолет')
    elif temp == 4:
        gear.append('Легкая бронекуртка, тяжелый пистолет')
    elif temp == 5:
        gear.append('Средняя бронекуртка, тяжелый пистолет')
    elif temp == 6:
        gear.append('Средняя бронекуртка, легкий ПП')

if toughnes == 2:
    temp = random.randint(2, 6)
    if role == 7 or role == 5:
        temp += 2
    if role == 1:
        temp += 3
    else:
        pass
    if temp == 1:
        gear.append('Тяжелая кожа, Нож')
    elif temp == 2:
        gear.append('Бронежилет, легкий пистолет')
    elif temp == 3:
        gear.append('Легкая бронекуртка, средний пистолет')
    elif temp == 4:
        gear.append('Легкая бронекуртка, тяжелый пистолет')
    elif temp == 5:
        gear.append('Средняя бронекуртка, тяжелый пистолет')
    elif temp == 6:
        gear.append('Средняя бронекуртка, легкий ПП')
    elif temp == 6:
        gear.append('Средняя бронекуртка, легкий ПП')
    elif temp == 7:
        gear.append('Средняя бронекуртка, легкая штурмовая винтовка')
    elif temp == 8:
        gear.append('Тяжелая бронекуртка, средняя штурмовая винтовка')
    elif temp == 9:
        gear.append('Тяжелая бронекуртка, тяжелая штурмовая винтовка')

if toughnes == 3:
    temp = random.randint(4, 9)
    if role == 7 or role == 5:
        temp += 2
    if role == 1:
        temp += 3
    else:
        pass
    if temp == 1:
        gear.append('Тяжелая кожа, Нож')
    elif temp == 2:
        gear.append('Бронежилет, легкий пистолет')
    elif temp == 3:
        gear.append('Легкая бронекуртка, средний пистолет')
    elif temp == 4:
        gear.append('Легкая бронекуртка, тяжелый пистолет')
    elif temp == 5:
        gear.append('Средняя бронекуртка, тяжелый пистолет')
    elif temp == 6:
        gear.append('Средняя бронекуртка, легкий ПП')
    elif temp == 7:
        gear.append('Средняя бронекуртка, легкая штурмовая винтовка')
    elif temp == 8:
        gear.append('Тяжелая бронекуртка, средняя штурмовая винтовка')
    elif temp == 9:
        gear.append('Тяжелая бронекуртка, тяжелая штурмовая винтовка')
    elif temp >= 10:
        gear.append('Метал Гир, тяжелая штурмовая винтовка')


print('----------СТАТЫ----------')

print('Инт:', inte)
print('Реф:', ref)
print('Тех:', teh)
print('Крут:', cool)
print('Првл:', char)
print('Удч:', luck)
print('Пер:', mov)
print('Тел:', body)
print('Эмп:', emp)
print('Спец:', special)

print('Модификатор тела:', BodyMod)
print('СПАС:', body)

print('--------КИБЕРНЕТИКА--------')

for i in range(len(cybernetics)):
    print(cybernetics[i])

print('--------СНАРЯЖЕНИЕ---------')

print(*gear)

print('----------------------------')
print('')