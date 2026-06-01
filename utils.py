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

def draw_leaderboard(base, name, lang):
    a, b=[], []
    for i in base[name].values():
        a.append(str(i[0]))
        b.append(str(i[1]))
    a=[translator(i, lang) for i in a]
    a=[f'{i:<14}|' for i in a]
    b=[f'{i:<14}|' for i in b]
    a=' '.join(a)
    b=' '.join(b)
    name1=f'{name} |'
    line1=f'|{translator('GAME MODE |', lang):>20} {a:<14}'
    line2=f'|{name1:>20} {b:<14}'
    line='-'*len(line1)
            
    print(line)
    print(line1)
    print(line)
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