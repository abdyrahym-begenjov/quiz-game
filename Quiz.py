from random import choice
from time import sleep, time
from propython import pyread

print('Quiz')
print('Created by Abdyrahym Begenjov     (GitHub: abdyrahym-begenjov)')

while True:
    print('Timer      Infinity')
    mode_game=input('Choose mode of game: ')
    mode_game=mode_game.title().strip()
    if mode_game=='Timer' or mode_game=='Infinity':
        break

print('Loading...')
sleep(2)

lst=pyread('q1.json')
v=['A)', 'B)', 'C)', 'D)']

points=0
regular=0
irregular=0
number=0
heart=3

if mode_game=='Timer':
    while True:
        print('Parameters of game: Easy (15), Normal (25), Hard (40), Danger (40 with surprise)')
        parameter=input('Enter the parameter of game: ')
        parameter=parameter.title().strip()
        match parameter:
            case 'Easy':
                nums_question=15
                seconds=45
                break
            case 'Normal':
                nums_question=25
                seconds=60
                break
            case 'Hard' | 'Danger':
                nums_question=40
                seconds=90
                break
            case _:
                print('Error!!!')
    print('Let\'s go')
else:
    print(f'You have {heart} ❤️')

def answer_question(countdown=None, seconds=None):
    while True:
        if countdown and seconds:
            answer=input(f'Time: {countdown}. Enter the variant of answer: ')
        else:
            answer=input('Enter the variant of answer: ')
        answer=answer.upper().strip()
        if answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print('You must enter the variant!!!')
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
                print(f'Time: {countdown}. Regular: {regular}  Irregular: {irregular}')
                if regular==number:
                    print('You Win!!!')
                    print('⭐'*3)
                    final=True
                elif (regular/number)*100>=70:
                    print('Good Work!!!')
                    print('⭐'*2)
                    final=True
                elif (regular/number)*100>50:
                    print('Weak, but still you\'re great!!!')
                    print('⭐')
                    final=True
                elif regular==irregular:
                    print('The final question to determine the outcome of the game.')
                    nums_question+=1
                    continue
                else:
                    print('Game Over!!!')
                    print('💩')
                    final=True
                seconds=mins*60+secs
                if final:
                    points=regular+(seconds/(irregular+1))
                print(f'Points: {int(points)}')
                break
            elif seconds<=0:
                print(f'Time: 00:00. Game Over!!!')
                break
        case 'Infinity':
            if lst==[]:
                print('You are ABSOLUTE CHAMPION!!!')
                break
            elif heart==0:
                print('Game Over!!!')
                print(f'Our record: {points} points.')
                break
    number+=1
    question=choice(lst)
    print(f'{number}) {question[0]}')
    print(f'{v[0]} {question[1]:<35} {" ":>35} {v[2]} {question[3]}')
    print(f'{v[1]} {question[2]:<35} {" ":>35} {v[3]} {question[4]}')
    if mode_game=='Timer':
        start=time()
        answer, seconds=answer_question(countdown, seconds)
        end=time()
        seconds=seconds-int(end-start)
    else:
        answer=answer_question()
    if answer==question[5]:
        print('Yes')
        if mode_game=='Timer':
            regular+=1
            seconds+=5
        else:
            points+=1
    else:
        print('No')
        if mode_game=='Timer' and parameter=='Danger':
            dict_variants={'Q': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4}
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
                print('💣 BOOM!!!')
                seconds-=10
        if mode_game=='Infinity':
            heart-=1
            print(f'You have {heart} ❤️.')
        else:
            irregular+=1
    if mode_game=='Timer':
        nums_question-=1
    lst.remove(question)

end=input('Enter to exit: ')