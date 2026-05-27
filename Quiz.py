from random import choice
from time import sleep, time
from propython import pyread

print('Quiz')
print('Created by Abdyrahym Begenjov     (GitHub: abdyrahym-begenjov)')

while True:
    print('Timer      Infinity')
    mode=input('Choose mode of game: ')
    mode=mode.title().strip()
    if mode=='Timer' or mode=='Infinity':
        break

print('Loading...')
sleep(2)

lst=pyread('q1.json')
v=['A)', 'B)', 'C)', 'D)']

points=0
num=0
heart=3

if mode=='Timer':
    while True:
        print('Parameters of game: Easy (15), Normal (25), Hard (40)')
        parameter=input('Enter the parameter of game: ')
        parameter=parameter.title().strip()
        match parameter:
            case 'Easy':
                num1=15
                break
            case 'Normal':
                num1=25
                break
            case 'Hard':
                num1=40
                break
            case _:
                print('Error!!!')
    seconds=60
    print('Let\' go')
else:
    print(f'You have {heart} ❤️')

def func(timer=None, seconds=None):
    while True:
        if timer and seconds:
            answer=input(f'Time: {timer}. Enter the variant of answer: ')
        else:
            answer=input('Enter the variant of answer: ')
        answer=answer.upper().strip()
        if answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print('You must enter the variant!!!')
    if timer:
        return answer, seconds
    else:
        return answer

while True:
    match mode:
        case 'Timer':
            mins, secs=divmod(seconds, 60)
            timer=f'{mins:02d}:{secs:02d}'
            if num1==0:
                print(f'Time: {timer}. You received {points} points.')
                break
            elif seconds<=0:
                print(f'Time: 00:00. Game Over!!!')
                break
        case 'Infinity':
            if lst==[]:
                print('You an ABSOLUTE CHAMPION!!!')
                break
            elif heart==0:
                print('Game Over!!!')
                print(f'Our record: {points} points.')
                break
    num+=1
    question=choice(lst)
    print(f'{num}) {question[0]}')
    print(f'{v[0]} {question[1]:<35} {" ":>35} {v[2]} {question[3]}')
    print(f'{v[1]} {question[2]:<35} {" ":>35} {v[3]} {question[4]}')
    if mode=='Timer':
        start=time()
        answer, seconds=func(timer, seconds)
        end=time()
        seconds=seconds-int(end-start)
    else:
        answer=func()
    if answer==question[5]:
        print('Yes')
        points+=1
        if mode=='Timer':
            seconds+=5
    else:
        print('No')
        if mode=='Infinity':
            heart-=1
            print(f'You have {heart} ❤️.')
    if mode=='Timer':
        num1-=1
    lst.remove(question)

end=input('Enter to exit: ')