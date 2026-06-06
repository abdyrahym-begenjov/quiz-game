from random import choice
from time import sleep, time
from propython import pyread, pywrite
from translator import translator
from utils import *

while True:
    base=pyread('base.json')
    data=pyread('data.json')

    name=data['name']
    lang=data['language']
    lst=data['questions']
    v=data['variants']

    if lang=='' and lst==[] and v==[]:
        lang, lst, v=enter_lang(data)
        clear_screen()

    if name=='':
        name=enter_name(lang, data)
        clear_screen()

    if name not in base:
        base[name]=[0, 0]

    print(translator('Quiz', lang))
    print(f'{translator("Creator: Abdyrahym Begenjov", lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=new_word(mode, lang)
    clear_screen()
    match mode:
        case 'Game':
            while True:
                print(translator('Timer      Infinity', lang))
                mode_game=input(translator('Choose a game mode: ', lang))
                mode_game=new_word(mode_game, lang)
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
                    parameter=new_word(parameter, lang)
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
                print(f'{translator("You have", lang)} {heart} ❤️')

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
                            elif (regular/number)*100==50:
                                print(translator('The final question to determine the outcome of the game.', lang))
                                nums_question+=1
                                final=False
                                continue
                            else:
                                print(translator('Game Over!!!', lang))
                                print('💩')
                                break
                            if final:
                                seconds=mins*60+secs
                                points=int(regular+(seconds/(irregular+1)))
                                print(f'{translator("Points: ", lang)}{points}')
                                base[name][0]+=points
                                pywrite('base.json', base)
                                break
                        elif seconds<=0:
                            print(translator('Time: 00:00. Game Over!!!', lang))
                            break
                    case 'Infinity':
                        if lst==[]:
                            print(translator('You are ABSOLUTE CHAMPION!!!', lang))
                            base[name][1]=points
                            pywrite('base.json', base)
                            break
                        elif heart==0:
                            print(translator('Game Over!!!', lang))
                            print(f'{translator("Points: ", lang)}{points}')
                            if base[name][1]<points:
                                print('OUR NEW HIGHSCORE!!!')
                                base[name][1]=points
                                pywrite('base.json', base)
                            break
                number+=1
                question=choice(lst)
                print(f'{number}) {question[0]}')
                print(f'{v[0]}) {question[1]:<35} {" ":>35} {v[2]}) {question[3]}')
                print(f'{v[1]}) {question[2]:<35} {" ":>35} {v[3]}) {question[4]}')
                if mode_game=='Timer':
                    start=time()
                    answer, seconds=answer_question(lang, v, countdown, seconds)
                    end=time()
                    seconds=seconds-int(end-start)
                else:
                    answer=answer_question(lang, v)
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
                        bomb=choose_bomb(question, v)
                        if answer==bomb:
                            print(translator('💣 BOOM!!!', lang))
                            seconds-=10
                    if mode_game=='Infinity':
                        heart-=1
                        print(f'{translator("You have", lang)} {heart} ❤️.')
                    else:
                        irregular+=1
                if mode_game=='Timer':
                    nums_question-=1
                lst.remove(question)

            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Rules':
            if lang=='ru':
                rules=pyread('ru_rules.txt')
            else:
                rules=pyread('en_rules.txt')
            print(rules)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Highscores':
            draw_leaderboard(base, lang)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Settings':
            while True:
                print(f'{translator("Name", lang)}: {data['name']}')
                print(f'{translator("Language", lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=new_word(change, lang)
                match change:
                    case 'Name':
                        name=enter_name(lang, data)
                        if name not in base:
                            base[name]=[0, 0]
                        clear_screen()
                    case 'Language':
                        lang, lst, v=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break

        case _:
            clear_screen()