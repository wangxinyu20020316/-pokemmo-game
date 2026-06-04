companion_1='皮卡丘'
skill_1='十万伏特'
skill_2='伏特攻击'
skill_3='电击'
skill_4='影子分身'
p_fast=0
p_attack=0
p_sattack=0
p_blood=50
p_defense=0
p_sdefense=0
companion_2='杰尼龟'
skill_5='水枪'
skill_6='攻击提升'
skill_7='特攻提升'
skill_8='影子分身'
j_fast=0
j_attack=0
j_sattack=0
j_blood=50
j_defense=0
j_sdefense=0
while p_blood and j_blood:
    print("皮卡丘能使用的技能有")
    print(f"1.{skill_1}",f"2.{skill_2}",sep=' ')
    print(f"3.{skill_3}",f"4.{skill_4}",sep=' ')
    skill=input("请输入你要使用的技能：")
    user='皮卡丘'
    if skill==skill_1:
        if user=='皮卡丘':
            j_blood=j_blood-10-p_sattack
            print(f"杰尼龟剩余{j_blood}血")
        else:
            p_blood=p_blood-5
    elif skill==skill_2:
        if user=='皮卡丘':
            j_blood=j_blood-20-p_attack
            print(f"杰尼龟剩余{j_blood}血")
        else:
            p_blood=p_blood-5
    elif skill==skill_3:
        if user=='皮卡丘':
            j_blood=j_blood-2-p_sattack
            print(f"杰尼龟剩余{j_blood}血")
        else:
            p_blood=p_blood-5
    elif skill==skill_4:
        if user=='皮卡丘':
            p_fast=p_fast+2
            print(f"皮卡丘速度等级提升2，现在已经提升{p_fast}")
        else:
            j_fast=j_fast+2
            print(f"杰尼龟速度等级提升2，现在已经提升{j_fast}")
    elif skill==skill_5:
        if user=='皮卡丘':
            j_blood=j_blood-2
        else:
            p_blood=p_blood-10-j_sattack
            print(f"皮卡丘剩余{p_blood}血")
    elif skill==skill_6:
        if user=='皮卡丘':
            j_blood=j_blood-2
        else:
            j_attack=j_attack+2
            print(f"杰尼龟攻击等级提升2，现在已经提升{j_attack}")
    elif skill==skill_7:
        if user=='皮卡丘':
            j_blood=j_blood-2
        else:
            p_sattack=p_sattack+2
            print(f"杰尼龟特工等级提升2，现在已经提升{p_sattack}")
    else:
        pass
    if p_blood==0 or j_blood==0:
        break
    print("杰尼龟能使用的技能有")
    print(f"1.{skill_5}",f"2.{skill_6}",sep=' ')
    print(f"3.{skill_7}",f"4.{skill_8}",sep=' ')
    skill=input("请输入你要使用的技能：")
    user='杰尼龟'
    if skill==skill_1:
        if user=='皮卡丘':
            j_blood=j_blood-10-p_sattack
            print(f"杰尼龟剩余{j_blood}血")
        else:
            p_blood=p_blood-5
    elif skill==skill_2:
        if user=='皮卡丘':
            j_blood=j_blood-20-p_attack
            print(f"杰尼龟剩余{j_blood}血")
        else:
            p_blood=p_blood-5
    elif skill==skill_3:
        if user=='皮卡丘':
            j_blood=j_blood-2-p_sattack
            print(f"杰尼龟剩余{j_blood}血")
        else:
            p_blood=p_blood-5
    elif skill==skill_4:
        if user=='皮卡丘':
            p_fast=p_fast+2
            print(f"皮卡丘速度等级提升2，现在已经提升{p_fast}")
        else:
            j_fast=j_fast+2
            print(f"杰尼龟速度等级提升2，现在已经提升{j_fast}")
    elif skill==skill_5:
        if user=='皮卡丘':
            j_blood=j_blood-2
        else:
            p_blood=p_blood-10-j_sattack
            print(f"皮卡丘剩余{p_blood}血")
    elif skill==skill_6:
        if user=='皮卡丘':
            j_blood=j_blood-2
        else:
            j_attack=j_attack+2
            print(f"杰尼龟攻击等级提升2，现在已经提升{j_attack}")
    elif skill==skill_7:
        if user=='皮卡丘':
            j_blood=j_blood-2
        else:
            j_sattack=j_sattack+2
            print(f"杰尼龟特工等级提升2，现在已经提升{p_sattack}")
    else:
        pass
    if p_blood==0 or j_blood==0:
        break
    
