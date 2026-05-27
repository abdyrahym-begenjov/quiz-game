# quiz-game
# Quiz Game (Викторина)
## English
A lightweight, terminal-based trivia game written in Python. It features two game modes, dynamic time calculation, a custom question-bank system, and difficulty options for timed runs.
### Features
 * **Two Unique Modes**:
   * **Infinity**: Classic survival trivia. You start with 3 lives and try to answer as many questions correctly as possible until you run out.
   * **Timer**: Beat the clock! Start with 60 seconds and gain 5 extra seconds for each correct response. The game ends when the timer hits zero or you finish your requested question pool.
 * **Variable Difficulties**: In Timer mode, choose between Easy (15 questions), Normal (25 questions), or Hard (40 questions).
 * **Clean Formatting**: Alignment tweaks ensure choices are formatted nicely in columns for comfortable reading.
 * **Modular IO**: Includes a reusable custom file handler (propython.py) that implements Python's modern pattern-matching (match/case) syntax to seamlessly process .txt and .json extensions.
### File Structure
 * Quiz.py: The main game loop handles user inputs, time limits, scoring, and UI output.
 * propython.py: A helper utility for safe and concise file reads and writes using structural pattern matching.
 * q1.json: The standard database containing over 100 questions across multiple categories like science, history, geography, and literature.
### How to Play
 1. Run the script using Python: python Quiz.py
 2. Follow the prompt to choose either Timer or Infinity.
 3. If playing in Timer mode, input your difficulty preference (Easy, Normal, or Hard).
 4. Type your answers as A, B, C, or D and press Enter.

## Русский
Игра-викторина (для терминала)
Легковесная викторина для командной строки, написанная на языке Python. Игра поддерживает два режима, динамический расчет оставшегося времени, настраиваемую базу вопросов и несколько уровней сложности для режима на время.
### Особенности игры
 * **Два уникальных режима**:
   * **Infinity (Бесконечный)**: Классическая игра на выживание. У вас есть 3 жизни, а цель — дать как можно больше правильных ответов подряд.
   * **Timer (На время)**: Успейте ответить за отведенное время! Игра начинается с 60 секундами на таймере, а за каждый верный ответ добавляется еще 5 секунд. Игра заканчивается, если время истекло или закончился лимит вопросов.
 * **Выбор сложности**: В режиме Таймера можно выбрать пулы на 15 (Easy), 25 (Normal) или 40 (Hard) вопросов.
 * **Удобное отображение**: Варианты ответов выравниваются в две аккуратные колонки, что делает текст в терминале легко читаемым.
 * **Модульный ввод-вывод**: Включает вспомогательный скрипт (propython.py), использующий современный синтаксис сопоставления шаблонов (match/case) для чтения и записи файлов формата .txt и .json.
### Структура файлов
 * Quiz.py: Основной исполняемый файл игры. Управляет игровым циклом, таймером, подсчетом очков и выводом текста.
 * propython.py: Утилита для безопасного чтения и записи файлов с использованием механизма структурного паттерн-матчинга.
 * q1.json: База данных, содержащая более 100 вопросов на самые разные темы: от науки и истории до географии и литературы.
### Как запустить
 1. Запустите скрипт через терминал: python Quiz.py
 2. Выберите режим игры, введя Timer или Infinity.
 3. Если выбран режим таймера, укажите желаемую сложность (Easy, Normal или Hard).
 4. Вводите буквы ответов (A, B, C или D) и нажимайте Enter.
