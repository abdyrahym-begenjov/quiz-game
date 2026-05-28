from random import choice
from time import sleep, time
from propython import pyread
from translator import *

while True:
    print('English  |  Русский')
    chosen_language=input()
    match chosen_language:
        case 'English':
            lang='en'
            lst=pyread('q1.json')
            v=['A', 'B', 'C', 'D']
            break
        case 'Русский':
            lang='ru'
            lst=pyread('q2.json')
            v=['А', 'Б', 'В', 'Г']
            break
        case _:
            print('Error!!!')

print(translator('Quiz', lang))
print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')

while True:
    print(translator('Timer      Infinity', lang))
    mode_game=input(translator('Choose a game mode: ', lang))
    mode_game=mode_game.title().strip()
    if lang=='ru':
        mode_game=translator(mode_game, 'en1')
    if mode_game=='Timer' or mode_game=='Infinity':
        break

print(translator('Loading...', lang))
sleep(2)

points=0
regular=0
irregular=0
number=0
heart=3

if mode_game=='Timer':
    while True:
        print(translator('Parameters of game: Easy (15), Normal (25), Hard (40), Dangerous (40 with surprise)', lang))
        parameter=input(translator('Enter the parameter of game: ', lang))
        parameter=parameter.title().strip()
        if lang=='ru':
            parameter=translator(parameter, 'en1')
        match parameter:
            case 'Easy':
                nums_question=15
                seconds=45
                break
            case 'Normal':
                nums_question=25
                seconds=60
                break
            case 'Hard' | 'Dangerous':
                nums_question=40
                seconds=90
                break
            case _:
                print(translator('Error!!!', lang))
    start_game=input(translator('Enter to start game: ', lang))
    print(translator('Let\'s Go!!!', lang))
else:
    print(f'{translator('You have', lang)} {heart} ❤️')

def answer_question(countdown=None, seconds=None):
    while True:
        if countdown and seconds:
            answer=input(f'{translator('Time: ', lang)}{countdown}. {translator('Enter the variant of answer: ', lang)}')
        else:
            answer=input(translator('Enter the variant of answer: ', lang))
        answer=answer.upper().strip()
        if answer in v:
            break
        else:
            print(translator('You must enter the variant!!!', lang))
    if countdown:
        return answer, seconds
    else:
        return answer

while True:
    match mode_game:
        case 'Timer':
            mins, secs=divmod(seconds, 60)
            countdown=f'{mins:02d}:{secs:02d}'
            if nums_question==0:
                print(f'{translator('Time: ', lang)}{countdown}. {translator('Regular: ', lang)}{regular}  {translator('Irregular: ', lang)}{irregular}')
                if regular==number:
                    print(translator('You Win!!!', lang))
                    print('⭐'*3)
                    final=True
                elif (regular/number)*100>=70:
                    print(translator('Good Work!!!', lang))
                    print('⭐'*2)
                    final=True
                elif (regular/number)*100>50:
                    print(translator('Weak, but still you\'re great!!!', lang))
                    print('⭐')
                    final=True
                elif regular==irregular:
                    print(translator('The final question to determine the outcome of the game.', lang))
                    nums_question+=1
                    continue
                else:
                    print(translator('Game Over!!!', lang))
                    print('💩')
                    final=True
                seconds=mins*60+secs
                if final:
                    points=regular+(seconds/(irregular+1))
                print(f'{translator('Points: ', lang)}{int(points)}')
                break
            elif seconds<=0:
                print(translator('Time: 00:00. Game Over!!!', lang))
                break
        case 'Infinity':
            if lst==[]:
                print(translator('You are ABSOLUTE CHAMPION!!!', lang))
                break
            elif heart==0:
                print(translator('Game Over!!!', lang))
                print(f'{translator('Our record: ', lang)}{points} {translator('points.', lang)}')
                break
    number+=1
    question=choice(lst)
    print(f'{number}) {question[0]}')
    print(f'{v[0]}) {question[1]:<35} {" ":>35} {v[2]}) {question[3]}')
    print(f'{v[1]}) {question[2]:<35} {" ":>35} {v[3]}) {question[4]}')
    if mode_game=='Timer':
        start=time()
        answer, seconds=answer_question(countdown, seconds)
        end=time()
        seconds=seconds-int(end-start)
    else:
        answer=answer_question()
    if answer==question[5]:
        print(translator('Yes', lang))
        if mode_game=='Timer':
            regular+=1
            seconds+=5
        else:
            points+=1
    else:
        print(translator('No', lang))
        if mode_game=='Timer' and parameter=='Dangerous':
            dict_variants={'Q': 0, v[0]: 1, v[1]: 2, v[2]: 3, v[3]: 4}
            old_question=question.copy()
            q=old_question[5]
            old_question.pop(5)
            old_question.pop(dict_variants[q])
            dict_variants={j: i for i, j in dict_variants.items()}
            old_question_index=[old_question.index(i) for i in old_question]
            bomb_list=[dict_variants[i] for i in old_question_index]
            bomb_list.remove('Q')
            bomb=choice(bomb_list)
            if answer==bomb:
                print(translator('💣 BOOM!!!', lang))
                seconds-=10
        if mode_game=='Infinity':
            heart-=1
            print(f'{translator('You have', lang)} {heart} ❤️.')
        else:
            irregular+=1
    if mode_game=='Timer':
        nums_question-=1
    lst.remove(question)

end=input(translator('Enter to exit: ', lang))