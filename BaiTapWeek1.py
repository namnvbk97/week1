# create two dictionaries
from random import choice

questions={
    "strong":"Do ye like yer drinks strong?",
    "salty":"Do ye like it with a salty tang?",
    "bitter":"Are ye a lubber who likes it bitter?",
    "sweet":"Would ye like a bit of sweetness with yer poison?",
    "fruity":"Are ye one for a fruity finish?",
    }
ingredients={
    "strong":["glug of rum ","slug of whisky","splash of gin"],
    "salty":["olive on stick","salt-dusted rim","rasher of bacon"],
    "bitter":["shake of bitters","splash of tonic","twist of lemon peel"],
    "sweet":["sugar cube","spoonful of honey","spash of cola"],
    "fruity":["slice of orange","dash of cassis","cherry on top"],
    }
state_list=list(questions)
kickthuoc=len(state_list)

def question():
    
    state_ramdom=choice(state_list)
    ques_ramdom=questions[state_ramdom]
    print(ques_ramdom)
    answer=input("answer yes or no   :")
    while True:
        if answer == "yes":
            mon=choice(ingredients[state_ramdom])
            break
        elif answer != "no":
                answer=input("answer is wrong,please again :")
        elif answer == "no": 
            mon=""
            break
    state_list.remove(state_ramdom)
    return mon
mon_da_chon='Các món quý khách đã chọn là :'
for i in range(kickthuoc):
    mon=question()
    mon=str(mon)
    if mon != "":
        if mon_da_chon != 'Các món quý khách đã chọn là :':
            mon_da_chon=mon_da_chon+ " and "+ mon
        else:
            mon_da_chon=mon_da_chon+ mon
    if len(state_list)==0:
        print(mon_da_chon)
        break
