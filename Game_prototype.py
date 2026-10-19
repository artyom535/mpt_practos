import random

characters_db = {
    'Капитан': {
        'start_location': 'Порт',
        'description': 'Опытный мореплаватель. Начинает в порту.',
        'starting_items': ['компас', 'пистолет', 'паёк'],
        'health': 100,
        'dice_bonus': 1,
        'special': '+1 к броску кубика'
    },
    'Матрос': {
        'start_location': 'Корабль',
        'description': 'Крепкий моряк. Сразу в море на корабле.',
        'starting_items': ['верёвка', 'нож', 'паёк'],
        'health': 120,
        'dice_bonus': 0,
        'special': '+20 к здоровью'
    },
    'Картограф': {
        'start_location': 'Библиотека',
        'description': 'Умный исследователь. Начинает в библиотеке.',
        'starting_items': ['карта', 'ром', 'паёк'],
        'health': 80,
        'dice_bonus': 0,
        'special': 'Видит точное количество врагов'
    },
    'Повар': {
        'start_location': 'Кухня',
        'description': 'Сильный и находчивый. Начинает на кухне.',
        'starting_items': ['топор', 'еда', 'паёк'],
        'health': 100,
        'dice_bonus': 0,
        'special': 'Еда лечит +30'
    }
}

enemies_db = {
    'скелет_пирата': {
        'name': 'Скелет пирата',
        'health': 50,
        'damage': 15,
        'dice_sides': 6,
        'description': 'Скелет в лохмотьях с ржавой саблей!',
        'loot': [],
        'doubloons_reward': (10, 15),
        'hint': 'Сундук спрятан в пещере за водопадом!'
    },
    'пират_призрак': {
        'name': 'Пират-призрак',
        'health': 70,
        'damage': 20,
        'dice_sides': 8,
        'description': 'Полупрозрачный пират с горящими глазами!',
        'loot': ['зелье', 'паёк'],
        'doubloons_reward': (20, 25),
        'hint': 'Сундук на дне лагуны, у затонувшей мачты!'
    },
    'морской_волк': {
        'name': 'Морской волк',
        'health': 90,
        'damage': 25,
        'dice_sides': 10,
        'description': 'Огромный волк с оскаленными клыками!',
        'loot': [],
        'doubloons_reward': (30, 35),
        'hint': 'Сундук в гроте, за скалой с черепом!'
    },
    'капитан_нежить': {
        'name': 'Капитан-нежить',
        'health': 120,
        'damage': 30,
        'dice_sides': 12,
        'description': 'Огромный капитан-скелет с призрачной саблей!',
        'loot': ['зелье', 'зелье'],
        'doubloons_reward': (50, 60),
        'hint': 'Сундук в трюме моего старого корабля!'
    },
    'вражеское_судно': {
        'name': 'Вражеское судно',
        'health': 100,
        'damage': 28,
        'dice_sides': 10,
        'description': 'Вражеский корабль с абордажной командой идёт на таран!',
        'loot': ['талисман_удачи'],
        'doubloons_reward': (35, 45),
        'hint': ''
    }
}

items_db = {
    'компас': {'type': 'passive', 'description': 'Указывает путь к сокровищам. Помогает в море.'},
    'карта': {'type': 'passive', 'description': 'Подробная карта острова. Показывает количество врагов.'},
    'подзорная_труба': {'type': 'passive', 'description': 'Помогает видеть далёкие объекты и врагов.'},
    'верёвка': {'type': 'passive', 'description': 'Крепкая морская верёвка. Может пригодиться.'},
    'талисман_удачи': {'type': 'passive', 'description': 'Магический талисман. Даёт +1 к броску кубика в бою.'},
    'пистолет': {'type': 'weapon', 'description': 'Старый пистолет с одной пулей.', 'damage': 50},
    'нож': {'type': 'weapon', 'description': 'Острый матросский нож.', 'damage': 25},
    'топор': {'type': 'weapon', 'description': 'Тяжёлый кухонный топор.', 'damage': 35},
    'паёк': {'type': 'rest', 'description': 'Сухой паёк. Необходим для отдыха.'},
    'еда': {'type': 'healing', 'description': 'Вкусная еда. Лечит раны.', 'heal': 15},
    'ром': {'type': 'healing', 'description': 'Бутылка рома. Лечит и греет душу.', 'heal': 20},
    'лечебная_трава': {'type': 'healing', 'description': 'Лечебная трава. Лечит раны.', 'heal': 25},
    'зелье': {'type': 'healing', 'description': 'Магическое зелье лечения.', 'heal': 40},
    'ключ_от_сундука': {'type': 'passive', 'description': 'Магический ключ. Подсказывает один штифт сундука.'},
    'карта_торговца': {'type': 'passive', 'description': 'Подробная карта с секретными тропами.'}
}

merchant_db = {
    'карта_торговца': {'price': 40, 'description': 'Подробная карта с секретными тропами. Усиливает подсказки.'},
    'ключ_от_сундука': {'price': 60, 'description': 'Магический ключ. Подсказывает один штифт сундука.'},
    'талисман_удачи': {'price': 35, 'description': 'Магический талисман. Даёт +1 к броску кубика в бою.'},
    'лечебная_трава': {'price': 15, 'description': 'Лечебная трава. Лечит раны.'},
    'паёк': {'price': 20, 'description': 'Сухой паёк. Необходим для отдыха.'}
}

stage1_locations_db = {
    'Порт': {
        'description': 'Шумный порт. Корабли снуют туда-сюда, матросы кричат.',
        'npc': {
            'name': 'Старый моряк',
            'appearance': 'Вы видите старого моряка с деревянной ногой, сидящего на бочке у причала.',
            'dialogue': [
                {
                    'npc': 'Эй, молодой! Ищешь сокровища Черной Бороды?',
                    'options': [
                        {'text': 'Да! Расскажите всё что знаете, дедуля!', 'mood': 1},
                        {'text': 'Это не ваше дело, старик. Проваливайте.', 'mood': -1},
                        {'text': 'Может быть. А что вы можете предложить?', 'mood': 0}
                    ]
                },
                {
                    'npc': 'Хм... Я плавал с ним. Видел многое. Что скажешь?',
                    'options': [
                        {'text': 'Я готов слушать и учиться, уважаемый.', 'mood': 1},
                        {'text': 'Давай короче, не люблю болтовню.', 'mood': -1},
                        {'text': 'Продолжайте, мне интересно.', 'mood': 0}
                    ]
                },
                {
                    'npc': 'Последнее... Готов ли ты к опасностям?',
                    'options': [
                        {'text': 'Я благодарен за ваши советы, мудрец.', 'mood': 1},
                        {'text': 'Хватит меня пугать, я сам разберусь!', 'mood': -1},
                        {'text': 'Посмотрим. Время покажет.', 'mood': 0}
                    ]
                }
            ]
        }
    },
    'Библиотека': {
        'description': 'Старая библиотека с пыльными книгами и свечами.',
        'npc': {
            'name': 'Старый учёный',
            'appearance': 'За столом сидит старый учёный в очках, окружённый стопками книг.',
            'dialogue': [
                {
                    'npc': 'А, новый искатель знаний! Что привело тебя в мою библиотеку?',
                    'options': [
                        {'text': 'Я ищу древние карты, уважаемый мастер.', 'mood': 1},
                        {'text': 'Давай ключи от сокровищницы, быстро.', 'mood': -1},
                        {'text': 'Просто изучаю историю острова.', 'mood': 0}
                    ]
                },
                {
                    'npc': 'Знания - это сила. Но они требуют уважения.',
                    'options': [
                        {'text': 'Я готов учиться и уважать традиции.', 'mood': 1},
                        {'text': 'Мне некогда, у меня мало времени.', 'mood': -1},
                        {'text': 'Согласен. Что вы можете рассказать?', 'mood': 0}
                    ]
                },
                {
                    'npc': 'Последний вопрос... Зачем тебе сокровища?',
                    'options': [
                        {'text': 'Чтобы сохранить историю для потомков.', 'mood': 1},
                        {'text': 'Хочу разбогатеть и купить корабль!', 'mood': -1},
                        {'text': 'Просто люблю приключения.', 'mood': 0}
                    ]
                }
            ]
        }
    },
    'Кухня': {
        'description': 'Корабельная кухня. Пахнет едой и специями.',
        'npc': {
            'name': 'Юнга Томми',
            'appearance': 'Маленький юнга суетится у плиты, помешивая огромную кастрюлю.',
            'dialogue': [
                {
                    'npc': 'О, капитан! Вы голодны? У меня есть суп!',
                    'options': [
                        {'text': 'Спасибо, дружок! Ты настоящий помощник.', 'mood': 1},
                        {'text': 'Некогда мне есть, делай что говорят.', 'mood': -1},
                        {'text': 'Может позже. Что нового на корабле?', 'mood': 0}
                    ]
                },
                {
                    'npc': 'Я слышал, вы ищете сокровища. Я знаю кое-что...',
                    'options': [
                        {'text': 'Ты молодец! Расскажи всё, я тебя награжу.', 'mood': 1},
                        {'text': 'Мелкий ещё мне советы давать!', 'mood': -1},
                        {'text': 'Интересно. Что ты знаешь?', 'mood': 0}
                    ]
                },
                {
                    'npc': 'Будьте осторожны, капитан. Остров опасен.',
                    'options': [
                        {'text': 'Спасибо за заботу, береги себя.', 'mood': 1},
                        {'text': 'Не учи меня, мальчишка!', 'mood': -1},
                        {'text': 'Приму к сведению.', 'mood': 0}
                    ]
                }
            ]
        }
    }
}

stage3_locations_db = {
    'Остров_руин': {
        'description': 'Остров с древними руинами. Колонны поросли мхом, ветер воет в арках.',
        'investigation_spots': [
            'Вы видите брошенный алтарь. Наверняка там что-то есть.',
            'Старая статуя с протянутой рукой. В ладони что-то блестит.',
            'Развалины стены с надписями на неизвестном языке.'
        ],
        'hidden_items': ['лечебная_трава', 'паёк'],
        'enemies': ['скелет_пирата', 'морской_волк']
    },
    'Пещера_сокровищ': {
        'description': 'Тёмная пещера. Капли воды эхом разносятся в темноте.',
        'investigation_spots': [
            'Вы замечаете старый сундук в углу пещеры.',
            'На полу лежат кости и ржавое оружие.',
            'Странные символы на стенах светятся в темноте.'
        ],
        'hidden_items': ['ром', 'паёк'],
        'enemies': ['морской_волк', 'пират_призрак']
    },
    'Затонувший_корабль': {
        'description': 'Остов старого корабля. Мачты торчат из воды как мёртвые пальцы.',
        'investigation_spots': [
            'Капитанская каюта. Дверь полуоткрыта.',
            'Трюм корабля. Там что-то плещется в воде.',
            'Палуба покрыта водорослями и ракушками.'
        ],
        'hidden_items': ['зелье', 'паёк'],
        'enemies': ['пират_призрак', 'капитан_нежить']
    }
}

level_names = ('Знакомство', 'Плавание по морю', 'Исследование острова', 'Взлом сундука')
sea_directions = ('прямо', 'налево', 'направо')

inventory = []
current_enemies = []

collected_items = set()
defeated_enemies = set()
visited_locations = set()

player = {}
current_location = ''
chest_hint = ''
sea_choices = []
vault_sequence = []
doubloons = 0
hinted_pin = None
current_stage = 1


def print_separator():
    print("\n" + "=" * 60)

def show_help():
    print("\nСПРАВКА:")
    print("- В меню выбирайте номер варианта")
    print("- Типы предметов:")
    print("  - ЛЕЧЕБНЫЕ: ром, еда, лечебная_трава, зелье (в бою и вне)")
    print("  - БОЕВЫЕ: пистолет, нож, топор (только в бою)")
    print("  - ОТДЫХ: паёк (только для отдыха)")
    print("  - ПАССИВНЫЕ: компас, карта, талисман, ключ (дают подсказки)")
    print("- Команда 'помощь' работает в любом месте")
    print("- Команда 'статус' показывает ваше состояние\n")

def show_menu(options):
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        try:
            user_input = input("\n> ").strip().lower()
            
            if user_input == 'помощь':
                show_help()
                continue
            
            if user_input == 'статус':
                show_status()
                continue
            
            choice = int(user_input)
            if 1 <= choice <= len(options):
                return choice
            print(f"Введите число от 1 до {len(options)}, 'помощь' или 'статус'")
        except ValueError:
            print("Введите число, 'помощь' или 'статус'!")
        except EOFError:
            print("\nЗавершение игры.")
            return -1
        except KeyboardInterrupt:
            print("\nИгра прервана.")
            return -1

def show_status():
    print("\n" + "-" * 40)
    print(f"ИМЯ: {player['name']}")
    print(f"КЛАСС: {player['class']}")
    print(f"ЗДОРОВЬЕ: {player['health']}/{player['max_health']}")
    print(f"ДУБЛОНЫ: {doubloons}")
    print(f"\nБАФФЫ И СПОСОБНОСТИ:")
    print(f"  - {player['special']}")
    if 'талисман_удачи' in inventory:
        print("  - Талисман удачи: +1 к броску кубика")
    if 'компас' in inventory:
        print("  - Компас: подсказки в море")
    if 'карта' in inventory or 'карта_торговца' in inventory:
        print("  - Карта: подсказки в исследованиях")
    if 'ключ_от_сундука' in inventory:
        print("  - Ключ от сундука: подсказка одного штифта")
    print("-" * 40)

def show_inventory():
    print("\nВАШ ИНВЕНТАРЬ:")
    if not inventory:
        print("  Пусто")
    else:
        healing = [i for i in inventory if items_db.get(i, {}).get('type') == 'healing']
        weapons = [i for i in inventory if items_db.get(i, {}).get('type') == 'weapon']
        rest = [i for i in inventory if items_db.get(i, {}).get('type') == 'rest']
        passive = [i for i in inventory if items_db.get(i, {}).get('type') == 'passive']
        
        if healing:
            print("\n  ЛЕЧЕБНЫЕ:")
            for item in healing:
                print(f"    - {item.replace('_', ' ').capitalize()}: {items_db[item]['description']}")
        
        if weapons:
            print("\n  БОЕВЫЕ:")
            for item in weapons:
                print(f"    - {item.replace('_', ' ').capitalize()}: {items_db[item]['description']}")
        
        if rest:
            print("\n  ДЛЯ ОТДЫХА:")
            for item in rest:
                print(f"    - {item.replace('_', ' ').capitalize()}: {items_db[item]['description']}")
        
        if passive:
            print("\n  ПАССИВНЫЕ:")
            for item in passive:
                print(f"    - {item.replace('_', ' ').capitalize()}: {items_db[item]['description']}")
    
    print(f"\nЗдоровье: {player['health']}/{player['max_health']}")
    print(f"Дублоны: {doubloons}")
    total_bonus = player['dice_bonus'] + (1 if 'талисман_удачи' in inventory else 0)
    print(f"Бонус к кубику: +{total_bonus}")

def damage_player(amount):
    player['health'] -= amount
    
    if player['health'] <= 0:
        player['health'] = 0
        print(f"Вы получили {amount} урона!")
        print(f"Здоровье: 0/{player['max_health']}")
        print("\nВы погибли...")
        return False
    else:
        print(f"Вы получили {amount} урона!")
        print(f"Здоровье: {player['health']}/{player['max_health']}")
        return True

def heal_player(amount):
    old_health = player['health']
    player['health'] = min(player['health'] + amount, player['max_health'])
    healed = player['health'] - old_health
    print(f"Вы восстановили {healed} здоровья!")
    print(f"Здоровье: {player['health']}/{player['max_health']}")

def get_total_dice_bonus():
    bonus = player['dice_bonus']
    if 'талисман_удачи' in inventory:
        bonus += 1
    return bonus

def roll_dice(sides=6, bonus=None):
    if bonus is None:
        bonus = get_total_dice_bonus()
    roll = random.randint(1, sides)
    total = roll + bonus
    if bonus > 0:
        print(f"Бросок кубика: {roll} + {bonus} = {total}")
    else:
        print(f"Бросок кубика: {roll}")
    return total

def determine_sea_destination():
    straight = sea_choices.count('прямо')
    left = sea_choices.count('налево')
    right = sea_choices.count('направо')
    
    if straight >= left and straight >= right:
        return 'Остров_руин'
    elif left >= straight and left >= right:
        return 'Пещера_сокровищ'
    else:
        return 'Затонувший_корабль'

def get_compass_hint():
    if 'компас' in inventory:
        print("\nПОДСКАЗКА КОМПАСА:")
        print("   Стрелка компаса дрожит и указывает...")
        print("   Лучше всего плыть ПРЯМО - там древние руины с сокровищами!")
        print("   (Но помните, итоговое направление зависит от большинства ваших выборов)\n")

def get_map_hint(location):
    has_map = 'карта' in inventory or 'карта_торговца' in inventory
    if has_map:
        print("\nПОДСКАЗКА КАРТЫ:")
        print("   Вы разворачиваете карту и видите отметки...")
        location_data = stage3_locations_db[location]
        print(f"   Здесь {len(location_data['enemies'])} врага и {len(location_data['hidden_items'])} ценных предмета!")
        print("   Исследуйте все уголки, прежде чем идти в бой.\n")

def random_event():
    if random.random() < 0.3:
        global current_stage
        if current_stage == 2:
            events = [
                {'type': 'damage', 'text': 'Волна захлестнула палубу, вы ударились о мачту!', 'value': 10},
                {'type': 'damage', 'text': 'Вы поскользнулись на мокрой палубе!', 'value': 12},
                {'type': 'enemy', 'text': 'На горизонте показался вражеский корабль!', 'enemy': 'вражеское_судно'},
                {'type': 'item', 'text': 'В сети попалась странная бутылка с талисманом!', 'item': 'талисман_удачи'},
                {'type': 'item', 'text': 'Вы нашли забытый кем-то мешочек!', 'item': random.choice(['ром', 'лечебная_трава', 'паёк'])}
            ]
        else:
            events = [
                {'type': 'damage', 'text': 'Вы поскользнулись и упали!', 'value': 10},
                {'type': 'damage', 'text': 'Ядовитый паук укусил вас!', 'value': 15},
                {'type': 'damage', 'text': 'Камень упал с потолка и ударил вас!', 'value': 12},
                {'type': 'enemy', 'text': 'Из засады выскакивает враг!', 'enemy': random.choice(['скелет_пирата', 'пират_призрак', 'морской_волк'])},
                {'type': 'item', 'text': 'Вы нашли забытый кем-то мешочек!', 'item': random.choice(['ром', 'лечебная_трава', 'паёк'])}
            ]
        
        event = random.choice(events)
        print(f"\nСЛУЧАЙНОЕ СОБЫТИЕ:")
        print(f"{event['text']}")
        
        if event['type'] == 'damage':
            if not damage_player(event['value']):
                return False
        elif event['type'] == 'enemy':
            print(f"Это {enemies_db[event['enemy']]['name']}!")
            if not combat(enemies_db[event['enemy']]):
                return False
        elif event['type'] == 'item':
            inventory.append(event['item'])
            collected_items.add(event['item'])
            print(f"Вы получили: {event['item'].replace('_', ' ')}")
        
        print()
    
    return True

def choose_item_from_menu(items_list, title="Выберите предмет"):
    if not items_list:
        print("\nНет доступных предметов!")
        return None
    
    print(f"\n{title}:")
    options = [i.replace('_', ' ').capitalize() for i in items_list]
    options.append('Назад')
    
    choice = show_menu(options)
    if choice == -1:
        return None
    if choice == len(options):
        print("Возврат в предыдущее меню.")
        return None
    
    return items_list[choice - 1]

def use_item(item_name):
    if item_name not in inventory:
        print(f"У вас нет предмета '{item_name}'")
        return False
    
    item_data = items_db.get(item_name, {})
    item_type = item_data.get('type', 'passive')
    
    if item_type == 'healing':
        heal_amount = item_data.get('heal', 0)
        if item_name == 'еда' and player['class'] == 'Повар':
            heal_amount = 30
        heal_player(heal_amount)
        inventory.remove(item_name)
        print(f"Вы использовали {item_name.replace('_', ' ')}")
        return True
    else:
        print(f"Этот предмет нельзя использовать для лечения")
        return False

def merchant_menu():
    global doubloons
    print("\n" + "-" * 40)
    print("ТОРГОВЕЦ")
    print("-" * 40)
    print("\nСтарый пират в плаще раскладывает товары на камне.")
    print(f"Пират: 'Эй, моряк! Есть кое-что интересное. У меня {len(merchant_db)} товара.'\n")
    print(f"Ваши дублоны: {doubloons}\n")
    
    while True:
        print("Что хотите купить?")
        options = []
        for item_key, item_data in merchant_db.items():
            options.append(f"{item_key.replace('_', ' ').capitalize()} - {item_data['price']} дублонов")
        options.append('Уйти от торговца')
        
        choice = show_menu(options)
        if choice == -1:
            return
        
        if choice == len(options):
            print("Вы уходите от торговца.")
            return
        
        item_key = list(merchant_db.keys())[choice - 1]
        item_data = merchant_db[item_key]
        price = item_data['price']
        
        if doubloons >= price:
            doubloons -= price
            inventory.append(item_key)
            collected_items.add(item_key)
            print(f"\nВы купили: {item_key.replace('_', ' ').capitalize()}")
            print(f"Осталось дублонов: {doubloons}")
            print(f"{item_data['description']}\n")
        else:
            print(f"\nНедостаточно дублонов! Нужно {price}, у вас {doubloons}.\n")

def death_message():
    print("\n" + "=" * 60)
    print("КОНЕЦ ПУТИ")
    print("=" * 60)
    print(f"\n{player['class']} {player['name']} умирает смертью храбрых...")
    print(f"Его имя войдёт в легенды мореплавателей.")


def choose_character():
    print_separator()
    print("ВЫБОР ПЕРСОНАЖА")
    print_separator()
    print("\nВыберите своего искателя приключений:\n")
    
    char_list = list(characters_db.keys())
    for i, char_name in enumerate(char_list, 1):
        char = characters_db[char_name]
        print(f"{i}. {char_name}")
        print(f"   {char['description']}")
        print(f"   Начальные предметы: {', '.join(char['starting_items'])}")
        print(f"   Здоровье: {char['health']}")
        print(f"   Способность: {char['special']}")
        print()
    
    while True:
        choice = show_menu(char_list)
        if choice == -1:
            return None, None
        
        char_name = char_list[choice - 1]
        char = characters_db[char_name]
        
        print(f"\nВы выбрали: {char_name}")
        while True:
            try:
                name = input("Введите имя вашего персонажа: ").strip()
                if name and len(name) <= 20:
                    break
                print("Имя должно быть от 1 до 20 символов")
            except EOFError:
                return None, None
        
        player['name'] = name
        player['class'] = char_name
        player['health'] = char['health']
        player['max_health'] = char['health']
        player['dice_bonus'] = char['dice_bonus']
        player['special'] = char['special']
        
        for item in char['starting_items']:
            inventory.append(item)
            collected_items.add(item)
        
        print(f"\nДобро пожаловать, {name}!")
        print(f"Стартовая локация: {char['start_location']}")
        return char_name, char['start_location']


def level_1_intro():
    global current_stage
    current_stage = 1
    print_separator()
    
    print(f"\n{player['name']} осматривается вокруг.")
    print("Перед вами несколько мест, где можно начать поиски.\n")
    
    locations = list(stage1_locations_db.keys())
    print("Куда вы направитесь?")
    location_descriptions = [stage1_locations_db[loc]['description'] for loc in locations]
    
    choice = show_menu(location_descriptions)
    if choice == -1:
        return False
    
    global current_location
    current_location = locations[choice - 1]
    
    print(f"\nВы прибыли в: {current_location}")
    print(f"{stage1_locations_db[current_location]['description']}\n")
    
    if not random_event():
        return False
    
    npc_data = stage1_locations_db[current_location]['npc']
    npc_name = npc_data['name']
    
    print(npc_data['appearance'])
    
    dialogue = npc_data['dialogue']
    mood_score = 0
    
    for line in dialogue:
        print(f"\n{npc_name}: {line['npc']}\n")
        
        options = [opt['text'] for opt in line['options']]
        choice = show_menu(options)
        
        if choice == -1:
            return False
        
        selected = line['options'][choice - 1]
        mood_score += selected['mood']
        
        print(f"\n{player['name']}: {selected['text']}")
        
        if selected['mood'] > 0:
            print(f"{npc_name} одобряюще кивает.\n")
        elif selected['mood'] < 0:
            print(f"{npc_name} недовольно хмурится.\n")
        else:
            print(f"{npc_name} задумчиво смотрит на вас.\n")
    
    if mood_score >= 2:
        print(f"\n{npc_name} доволен вами!")
        gift = random.choice(['ром', 'лечебная_трава', 'зелье', 'паёк'])
        inventory.append(gift)
        collected_items.add(gift)
        print(f"{npc_name} дарит вам: {gift.replace('_', ' ')}")
        print(f"   {items_db[gift]['description']}")
    
    elif mood_score <= -2:
        print(f"\n{npc_name} в ярости! Он достаёт оружие!")
        print(f"{npc_name} нападает на вас!\n")
        
        npc_enemy = {
            'name': npc_name,
            'health': 40,
            'damage': 10,
            'dice_sides': 6,
            'description': f'{npc_name} атакует вас!',
            'loot': ['ром'],
            'doubloons_reward': (5, 8),
            'hint': ''
        }
        
        if not combat(npc_enemy):
            death_message()
            return False
    else:
        print(f"\n{npc_name} пожимает плечами.")
        print(f"{npc_name}: 'Ну, удачи тебе, незнакомец.'")
    
    print(f"\n{player['name']} прощается и идёт готовиться к отплытию.")
    visited_locations.add(current_location)
    return True


def level_2_sea():
    global current_stage, sea_choices, current_location
    current_stage = 2
    
    print_separator()
    
    print(f"\n{player['name']} поднимается на палубу корабля.")
    print("Море простирается во все стороны. Ветер надувает паруса.")
    print("Вам нужно определить курс. Будет 3 решения!\n")
    
    get_compass_hint()
    
    sea_choices = []
    
    for i in range(1, 4):
        print(f"\nРЕШЕНИЕ {i}")
        print("Куда направить корабль?")
        options = ['Плыть ПРЯМО', 'Плыть НАЛЕВО', 'Плыть НАПРАВО']
        
        choice = show_menu(options)
        if choice == -1:
            return False
        
        direction = sea_directions[choice - 1]
        sea_choices.append(direction)
        
        print(f"\nКорабль плывёт {direction}...")
        
        if not random_event():
            return False
        
        sea_events = [
            'Вы увидели стаю дельфинов, плывущих рядом.',
            'Неожиданно начался дождь, но быстро закончился.',
            'На горизонте показался другой корабль, но прошёл мимо.',
            'Ветер попутный, плывём быстро!',
            'Вы нашли в море старую бутылку с запиской.'
        ]
        event = random.choice(sea_events)
        print(f"{event}")
        
        if random.random() < 0.3:
            sea_loot = random.choice(['ром', 'лечебная_трава', 'паёк'])
            inventory.append(sea_loot)
            collected_items.add(sea_loot)
            print(f"Вы поймали в сети: {sea_loot.replace('_', ' ')}!")
    
    destination = determine_sea_destination()
    
    print(f"\nПосле всех решений вы прибыли к: {destination.replace('_', ' ')}")
    print("Бросаем якорь!\n")
    
    current_location = destination
    
    visited_locations.add('Море')
    return True


def level_3_exploration():
    global current_stage, chest_hint
    current_stage = 3
    
    print_separator()
    
    location_data = stage3_locations_db[current_location]
    print(f"\n{location_data['description']}")
    
    enemies_to_fight = location_data['enemies'].copy()
    random.shuffle(enemies_to_fight)
    
    investigation_spots = location_data['investigation_spots'].copy()
    hidden_items = location_data['hidden_items'].copy()
    
    print(f"\nВы замечаете несколько интересных мест для исследования.")
    
    has_map = 'карта' in inventory or 'карта_торговца' in inventory
    if has_map:
        print(f"Впереди маячат силуэты врагов: {len(enemies_to_fight)}")
    else:
        print("Впереди маячат какие-то силуэты...")
    
    print("\nТакже вы замечаете странного торговца в плаще у костра.")
    
    get_map_hint(current_location)
    
    while True:
        print("\nЧто вы хотите сделать?")
        options = []
        
        if investigation_spots:
            options.append('Исследовать местность')
        if enemies_to_fight:
            options.append(f'Идти на врагов (осталось: {len(enemies_to_fight)})')
        
        healing_items = [i for i in inventory if items_db.get(i, {}).get('type') == 'healing']
        if healing_items:
            options.append('Использовать лечебный предмет')
        
        if 'паёк' in inventory:
            options.append('Отдохнуть (съесть паёк)')
        else:
            options.append('Отдохнуть (нет пайка!)')
        
        options.append('Поговорить с торговцем')
        options.append('Статус')
        options.append('Инвентарь')
        
        if not enemies_to_fight:
            options.append('Идти дальше')
        
        choice = show_menu(options)
        if choice == -1:
            return False
        
        selected = options[choice - 1]
        
        if selected == 'Исследовать местность':
            if not random_event():
                return False
            if investigation_spots and hidden_items:
                spot = investigation_spots.pop(0)
                item = hidden_items.pop(0)
                
                print(f"\n{spot}")
                print(f"Вы нашли: {item.replace('_', ' ')}")
                print(f"   {items_db[item]['description']}")
                
                inventory.append(item)
                collected_items.add(item)
            elif investigation_spots:
                spot = investigation_spots.pop(0)
                print(f"\n{spot}")
                print("К сожалению, ничего ценного не нашли.")
            else:
                print("\nВы обыскали всё, что можно. Больше ничего интересного.")
        
        elif selected.startswith('Идти на врагов'):
            if not random_event():
                return False
            enemy_key = enemies_to_fight[0]
            enemy_data = enemies_db[enemy_key]
            print(f"\nВы сталкиваетесь с: {enemy_data['name']}")
            
            if not combat(enemy_data):
                death_message()
                return False
            
            defeated_enemies.add(enemy_key)
            enemies_to_fight.pop(0)
            
            chest_hint = enemy_data['hint']
            print(f"\nПобеждённый враг хрипит: '{chest_hint}'")
        
        elif selected == 'Использовать лечебный предмет':
            healing_items = [i for i in inventory if items_db.get(i, {}).get('type') == 'healing']
            item = choose_item_from_menu(healing_items, "Какой лечебный предмет использовать?")
            if item:
                use_item(item)
        
        elif selected.startswith('Отдохнуть'):
            if 'паёк' in inventory:
                inventory.remove('паёк')
                heal_player(30)
                print("Вы съели паёк и отдохнули. Силы восстановились!")
            else:
                print("У вас нет пайка для отдыха! Найдите его в игре.")
        
        elif selected == 'Поговорить с торговцем':
            merchant_menu()
        
        elif selected == 'Статус':
            show_status()
        
        elif selected == 'Инвентарь':
            show_inventory()
        
        elif selected == 'Идти дальше':
            print("\nВы исследовали локацию и готовы двигаться дальше!")
            visited_locations.add(current_location)
            return True


def combat(enemy_data):
    print_separator()
    print(f"БОЙ: {enemy_data['name'].upper()}")
    print_separator()
    print(f"\n{enemy_data['description']}")
    print(f"Здоровье врага: {enemy_data['health']}")
    print(f"Урон врага: {enemy_data['damage']}")
    print(f"Кубик врага: d{enemy_data['dice_sides']}")
    
    enemy_health = enemy_data['health']
    
    while enemy_health > 0 and player['health'] > 0:
        print("\nВаши действия:")
        options = ['Атаковать (бросить кубик)']
        
        healing_items = [i for i in inventory if items_db.get(i, {}).get('type') == 'healing']
        if healing_items:
            options.append('Использовать лечебный предмет')
        
        weapon_items = [i for i in inventory if items_db.get(i, {}).get('type') == 'weapon']
        if weapon_items:
            options.append('Использовать оружие')
        
        options.append('Инвентарь')
        
        choice = show_menu(options)
        if choice == -1:
            return False
        
        inventory_index = len(options)
        
        if choice == 1:
            print("\nВы бросаете кубик...")
            player_roll = roll_dice(6)
            
            print(f"\n{enemy_data['name']} бросает кубик...")
            enemy_roll = roll_dice(enemy_data['dice_sides'], bonus=0)
            
            if player_roll >= enemy_roll:
                damage = random.randint(20, 40)
                enemy_health -= damage
                print(f"\nВаш бросок {player_roll} >= {enemy_roll} врага!")
                print(f"Вы нанесли {damage} урона!")
                
                if enemy_health > 0:
                    print(f"Здоровье врага: {enemy_health}/{enemy_data['health']}")
                else:
                    print(f"\nВы победили {enemy_data['name']}!")
                    for loot_item in enemy_data['loot']:
                        inventory.append(loot_item)
                        collected_items.add(loot_item)
                        print(f"Получено: {loot_item.replace('_', ' ')}")
                    
                    global doubloons
                    min_d, max_d = enemy_data.get('doubloons_reward', (5, 10))
                    reward = random.randint(min_d, max_d)
                    doubloons += reward
                    print(f"Получено дублонов: {reward}")
                    print(f"Всего дублонов: {doubloons}")
                    return True
            else:
                print(f"\nВаш бросок {player_roll} < {enemy_roll} врага!")
                print(f"{enemy_data['name']} атакует вас!")
                if not damage_player(enemy_data['damage']):
                    return False
        
        elif options[choice - 1] == 'Использовать лечебный предмет':
            item = choose_item_from_menu(healing_items, "Какой лечебный предмет использовать?")
            if item:
                use_item(item)
        
        elif options[choice - 1] == 'Использовать оружие':
            weapon = choose_item_from_menu(weapon_items, "Какое оружие использовать?")
            if weapon:
                weapon_data = items_db[weapon]
                weapon_damage = weapon_data.get('damage', 0)
                
                print(f"\nВы используете {weapon.replace('_', ' ')}!")
                print(f"Наносите {weapon_damage} урона!")
                
                enemy_health -= weapon_damage
                inventory.remove(weapon)
                
                if enemy_health > 0:
                    print(f"Здоровье врага: {enemy_health}/{enemy_data['health']}")
                else:
                    print(f"\nВы победили {enemy_data['name']}!")
                    for loot_item in enemy_data['loot']:
                        inventory.append(loot_item)
                        collected_items.add(loot_item)
                        print(f"Получено: {loot_item.replace('_', ' ')}")
                    
                    min_d, max_d = enemy_data.get('doubloons_reward', (5, 10))
                    reward = random.randint(min_d, max_d)
                    doubloons += reward
                    print(f"Получено дублонов: {reward}")
                    print(f"Всего дублонов: {doubloons}")
                    return True
        
        elif choice == inventory_index:
            show_inventory()
    
    return player['health'] > 0


def level_4_vault_cracking():
    global current_stage, vault_sequence, hinted_pin
    current_stage = 4
    
    if not vault_sequence:
        vault_sequence = [random.randint(1, 5) for _ in range(3)]
    
    print_separator()
    
    print(f"\nСледуя подсказке: '{chest_hint}'")
    print("Вы находите старый сундук, покрытый пылью и паутиной!")
    print("На сундуке сложный замок с тремя штифтами.\n")
    
    if 'ключ_от_сундука' in inventory and hinted_pin is None:
        hinted_pin = random.randint(1, 3)
        print(f"КЛЮЧ ОТ СУНДУКА:")
        print(f"   Ключ светится и указывает на штифт {hinted_pin}!")
        print(f"   Его правильная высота: {vault_sequence[hinted_pin - 1]}\n")
    
    print("ПРАВИЛА ВЗЛОМА:")
    print("- У каждого штифта есть правильная высота (от 1 до 5)")
    print("- Нужно угадать все 3 высоты")
    print("- После каждой попытки замок подскажет, где верно")
    print("- У вас есть 3 попытки!")
    print("- Правильная последовательность не меняется!\n")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nПОПЫТКА {attempts}/{max_attempts}")
        print("Введите высоту для каждого штифта (1-5):")
        
        try:
            guess1 = int(input("  Штифт 1 (1-5): "))
            guess2 = int(input("  Штифт 2 (1-5): "))
            guess3 = int(input("  Штифт 3 (1-5): "))
        except ValueError:
            print("Введите числа!")
            attempts -= 1
            continue
        except EOFError:
            return False
        
        guesses = [guess1, guess2, guess3]
        
        if not all(1 <= g <= 5 for g in guesses):
            print("Числа должны быть от 1 до 5!")
            attempts -= 1
            continue
        
        print("\nРезультат:")
        all_correct = True
        for i, (g, c) in enumerate(zip(guesses, vault_sequence), 1):
            if g == c:
                print(f"  Штифт {i}: ВЕРНО!")
            elif g < c:
                print(f"  Штифт {i}: Слишком низко")
                all_correct = False
            else:
                print(f"  Штифт {i}: Слишком высоко")
                all_correct = False
        
        if all_correct:
            print("\n" + "=" * 60)
            print("Сундук открыт!")
            print("=" * 60)
            print("\nВнутри вы нашли:")
            treasures = ['золотые_дублоны', 'драгоценные_камни', 'старинная_карта']
            for treasure in treasures:
                print(f"  - {treasure.replace('_', ' ').capitalize()}")
                inventory.append(treasure)
                collected_items.add(treasure)
            return True
        else:
            if attempts < max_attempts:
                print(f"\nНеверно! Осталось попыток: {max_attempts - attempts}")
            else:
                print(f"\nПопытки закончились! Замок навсегда заблокирован.")
                print("Вы не смогли открыть сундук...")
                return False
    
    return False


def main():
    print("\n" + "=" * 60)
    print("ПРОКЛЯТИЕ ОСТРОВА ЧЁРНОЙ БОРОДЫ")
    print("=" * 60)
    print("\nДобро пожаловать, искатель приключений!")
    print("Вас ждут 4 испытания.")
    print("Найдите сокровища и вернитесь живым!\n")
    
    char_name, start_loc = choose_character()
    if not char_name:
        print("Игра завершена.")
        return
    
    global current_location
    current_location = start_loc
    
    if char_name == 'Матрос':
        print(f"\n{player['name']} уже на корабле в открытом море!")
        levels = [level_2_sea, level_3_exploration, level_4_vault_cracking]
    else:
        levels = [level_1_intro, level_2_sea, level_3_exploration, level_4_vault_cracking]
    
    for level_func in levels:
        success = level_func()
        
        if not success:
            return
    
    print("\n" + "=" * 60)
    print("ПОБЕДА!")
    print("=" * 60)
    print(f"\nПоздравляем, {player['name']}!")
    print("Вы нашли сундук Черной Бороды и полностью поменяли свою жизнь!")
    print("А вот что именно вы нашли и как это изменило вашу судьбу...")
    print("...узнаете в продолжении!")
    
    print("\nФИНАЛЬНЫЙ ИНВЕНТАРЬ:")
    show_inventory()
    
    print("\nСпасибо за игру!")


if __name__ == "__main__":
    main()