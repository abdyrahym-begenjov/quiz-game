from random import choice
from time import sleep
from propython import pyread

print('Quiz')
print('Created by Abdyrahym Begenjov     (GitHub: abdyrahym-begenjov)')

while True:
    print('Simple  |  Infinity')
    mode=input('Choose mode of game: ')
    mode=mode.title().strip()
    if mode=='Simple' or mode=='Infinity':
        break

print('Loading...')
sleep(2)

lst=pyread('q1.json')
v=['A)', 'B)', 'C)', 'D)']

points=0
num=0
heart=3

if mode=='Simple':
    while True:
        num1=(input('Enter the number of questions for game: '))
        try:
            num1=int(num1)
            if num1>len(lst):
                print('This number is bigger than number of list of question!!!')
            else:
                break
        except ValueError:
            print('Error!!!')
    print('Let\' go')
else:
    print(f'You have {heart} ❤️')

while True:
    if mode=='Simple' and num1==0:
        print(f'You received {points} points.')
        break
    elif mode=='Infinity' and heart==0:
        print('Game Over!!!')
        print(f'Our record: {points} points.')
        break
    else:
        num+=1
        question=choice(lst)
        print(f'{num}) {question[0]}')
        print(f'{v[0]} {question[1]:<35} {" ":>35} {v[2]} {question[3]}')
        print(f'{v[1]} {question[2]:<35} {" ":>35} {v[3]} {question[4]}')
        answer=input('Enter the variant of answer: ')
        answer=answer.upper().strip()
        if answer==question[5]:
            print('Yes')
            points+=1
        elif answer=='':
            print('You must enter the variant!!!')
            if mode=='Infinity':
                heart-=1
                print(f'You have {heart} ❤️.')
        else:
            print('No')
            if mode=='Infinity':
                heart-=1
                print(f'You have {heart} ❤️.')
    if mode=='Simple':
        num1-=1
    lst.remove(question)

end=input('Enter to exit: ')