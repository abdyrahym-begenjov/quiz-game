rutranslate={
    'Quiz': 'Викторина',
    'Timer      Infinity': 'Таймер      Бесконечность',
    'Timer': 'Таймер',
    'Infinity': 'Бесконечность',
    'Parameters of game: Easy (15), Normal (25), Hard (40), Dangerous (40 with surprise)': 'Параметры игры: Лёгкий (15), Нормальный (25), Сложный (40), Опасный (40 с сюрпризом)',
    'You have': 'У вас есть',
    'Time: ': 'Время: ',
    'Enter the variant of answer: ': 'Введите вариант ответа: ',
    'You must enter the variant!!!': 'Вы должны ввести вариант!!!',
    'Regular: ': 'Правильные: ',
    'Irregular: ': 'Неправильные: ',
    'You Win!!!': 'Вы выиграли!!!',
    'Good Work!!!': 'Хорошая работа!!!',
    'Weak, but still you\'re great!!!': 'Слабовато, но все же ты молодец!!!',
    'The final question to determine the outcome of the game.': 'Последний вопрос, который определит исход игры.', 
    'Game Over!!!': 'Игра окончена!!!',
    'Points: ': 'Очки: ',
    'Time: 00:00. Game Over!!!': 'Время: 00:00. Игра окончена!!!',
    'You are ABSOLUTE CHAMPION!!!': 'Ты АБСОЛЮТНЫЙ ЧЕМПИОН!!!',
    'Our record: ': 'Ваш рекорд: ',
    'points.': 'очки. ',
    'Yes': 'Да',
    '💣 BOOM!!!': '💣 БУМ!!!',
    'Error!!!': 'Ошибка!!!',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'Enter the parameter of game: ': 'Введите параметр игры: ',
    'Easy': 'Лёгкий',
    'Normal': 'Нормальный',
    'Hard': 'Сложный',
    'Dangerous': 'Опасный',
    'Enter to exit: ': 'Введите для выхода: ',
    'Let\'s Go!!!': 'Начнём!!!',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Enter to exit: ': 'Введите для выхода: ',
    'Enter your name: ': 'Введите свое имя: ',
    'Enter to exit mode: ': 'Войдите в режим выхода: ',
    'Game      Highscores      Settings      Exit': 'Игра      Рекорды      Настройки      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change parameters (Enter \"Name\" or \"Language\"): ': 'Хотите ли вы изменить параметры (введите \"Имя\" или \"Язык\"): ',
    'Do you want to exit (\"Yes\" or \"No\"): ': 'Вы хотите завершить (\"Да\" или \"Нет\"): ',
    'Goodbye!!!': 'До свидания!!',
    'Highscores': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход', 
    'Name': 'Имя',
    'Language': 'Язык',
    'Game': 'Игра',
    'GAME MODE |': 'РЕЖИМ ИГРЫ |',
    'No': 'Нет'
             }


entranslate={j: i for i, j in rutranslate.items()}


def translator(word, language):
    match language:
        case 'en':
            return word
        case 'en1':
            if word not in entranslate:
                return 'Error!!!'
            return entranslate[word]
        case 'ru':
            return rutranslate[word]
        case _:
            return '???'