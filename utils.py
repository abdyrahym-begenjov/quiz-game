from subprocess import run
from platform import system
from translator import *
from propython import pyread, pywrite
from random import choice

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        match chosen_language:
            case 'Русский':
                lang='ru'
                lst=pyread('q2.json')
                v=['А', 'Б', 'В', 'Г']
                break
            case 'English':
                lang='en'
                lst=pyread('q1.json')
                v=['A', 'B', 'C', 'D']
                break
            case _:
                continue
    
    data['language']=lang
    data['questions']=lst
    data['variants']=v
    pywrite('data.json', data)
    return lang, lst, v

def enter_name(lang, data):
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name
        
def answer_question(lang, v, countdown=None, seconds=None):
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

def draw_leaderboard(base, lang):
    base=list(base.items())
    base.sort(key=lambda x: x[1][0]+x[1][1], reverse=True)
    base=dict(base)

    lst=['Timer', 'Infinity', 'Overall Result']
    lst=[translator(i, lang) for i in lst]
    lst=[f'{i.upper().strip():<16}|' for i in lst]
    lst=' '.join(lst)
    line1=f'|{translator('NAME |', lang):>18} {lst:<16}'
    line='-'*len(line1)
    print(line)
    print(line1)
    print(line)

    for i, j in base.items():
        name=i
        a=str(j[0])
        b=str(j[1])
        c=j[0]+j[1]
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}| {b:<16}| {c:<16}|'
        print(line2)
        print(line)

def choose_bomb(question, v):
    dict_variants={'Q': 0, v[0]: 1, v[1]: 2, v[2]: 3, v[3]: 4}
    old_question=question.copy()
    q=old_question[5]
    old_question.pop(5)
    old_question.pop(dict_variants[q])
    dict_variants={j: i for i, j in dict_variants.items()}
    old_question_index=[old_question.index(i) for i in old_question]
    bomb_list=[dict_variants[i] for i in old_question_index[1:4]]
    bomb=choice(bomb_list)
    return bomb

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word