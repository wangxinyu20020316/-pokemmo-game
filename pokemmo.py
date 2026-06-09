import random

class Pokemon:
    def __init__(self,Atrribute,base_blood,attack,defense,sattck,sdefense,speed,CN_name,skill_1,skill_2='none',skill_3='none',skill_4='none',level=0):
        self.Atrribute=Atrribute
        self.base_blood=base_blood
        self.attack=attack
        self.defense=defense
        self.sattck=sattck
        self.sdefense=sdefense
        self.speed=speed
        self.CN_name=CN_name
        self.skill_1=skill_1
        self.skill_2=skill_2
        self.skill_3=skill_3
        self.skill_4=skill_4
        self.level=level



class Skill:
    def __init__(self,damage,ability,ability_up,CN_name):
        self.damage=damage
        self.ability_up=ability_up
        self.ability=ability
        self.CN_name=CN_name
    


class Trainer:
    def __init__(self,name,poke_1,poke_2='none',poke_3='none',poke_4='none',poke_5='none',poke_6='none'):
        self.name=name
        self.poke_1=poke_1
        self.poke_2=poke_2
        self.poke_3=poke_3
        self.poke_4=poke_4
        self.poke_5=poke_5
        self.poke_6=poke_6

    def own_poke_level_up(self,poke_index):
        if 1<=poke_index<=6:
            poke_position=f'poke_{poke_index}'
            poke=getattr(self,poke_position)
            if poke!='none':
                poke.level+=1
                print(f"{self.name}的第{poke_index}号位宝可梦{poke.CN_name}提升了一级")
            else:
                print(f"定位错误，你的背包{poke_index}号位根本没有宝可梦")
        else:
            print('一个训练家的背包仅允许携带6只宝可梦')
        

##技能区域
Thunderbolt=Skill(90,0,'none','十万伏特')
Volt_Tackle=Skill(120,0,'none','伏特攻击')
Thunder_Shock=Skill(40,0,'none','电击')
Double_Team=Skill(0,2,'speed','影子分身')



##宝可梦区域
Pikachu=Pokemon('electric',50,0,0,0,0,70,'皮卡丘',Thunderbolt)
Squirtle=Pokemon('water',50,0,0,0,0,50,'杰尼龟',Volt_Tackle)
Charmander=Pokemon('fire',50,0,0,0,0,65,'小火龙',Volt_Tackle)
Bulbasaur=Pokemon('grass',50,0,0,0,0,10,'妙蛙种子',Double_Team)



##训练家区域
Trainer_1=Trainer('小白',Pikachu,Squirtle)
Trainer_2=Trainer('小美',Charmander,Bulbasaur)


##判断队伍首回合出战宝可梦（判断从第一个位置开始，哪个宝可梦血量不为0）
def judge_alive_position(Trainer_id):
    for i in range(1,7):
        poke_alive_1=f'poke_{i}'
        p=getattr(Trainer_id,poke_alive_1)
        if p.base_blood!=0:
            return p

##判断出手权，速度快的进攻方，速度慢的防御方
def judge_speed_priority(pokemon_1,pokemon_2):
    if pokemon_1.speed>pokemon_2.speed:
        return pokemon_1,pokemon_2
    elif pokemon_2>pokemon_1:
        return pokemon_2,pokemon_1
    else:
        temp=random.randint(1,2)
        if temp==1:
            return pokemon_1,pokemon_2
        else:
            return pokemon_2,pokemon_1

##展示宝可梦已经学会的技能
def show_skill_table(pokemon_1):
    for i in range(1,5):
        tem_string=f'skill_{i}'
        skill_name=getattr(pokemon_1,tem_string)
        if skill_name!='none':
            print(f"{i}.{skill_name.CN_name}")

##识别输入的技能
def skill_use_judge(pokemon_1,skill_temp):
    for i in range(1,5):
        skill_use=f'skill_{i}'
        a=getattr(pokemon_1,skill_use)
        if skill_temp==a.CN_name:
            return a

#计算伤害
def skill_damage_cal(defensive_side,skill_temp):
    a=defensive_side.base_blood-skill_temp.damage
    if a>=0:
        print(f"{defensive_side.CN_name}损失了{skill_temp.damage}血量，剩余{a}血")
    else:
        print(f"{defensive_side.CN_name}损失了{defensive_side.base_blood}血量，剩余0血")
        a=0
    return a

##检测血量
def alive_judge(pokemon):
    if pokemon.base_blood<=0:
        return 0
    else:
        return 1

##回合操作
def round_do(offensive_side,defensive_side):
    print(f"轮到{offensive_side.CN_name}出招了")
    show_skill_table(offensive_side)                                ##展示出场宝可梦已经学会的技能
    skill_use=input("请输入你想使用技能名字：")                     ##输入使用的技能
    skill_temp=skill_use_judge(offensive_side,skill_use)            ##识别输入的技能
    defensive_side.base_blood=skill_damage_cal(defensive_side,skill_temp)      ##根据识别出来的技能计算伤害
    return alive_judge(defensive_side)                                   ##检测防守方血量

    
      

##对战区域
for round in range(1,9999999999):
    if round==1:                                                    ##第一回合做特殊判断（判断首发宝可梦）
        p=judge_alive_position(Trainer_1)
        k=judge_alive_position(Trainer_2)
        offensive_side,defensive_side=judge_speed_priority(p,k)
    q=round_do(offensive_side,defensive_side)
    if q==0:
         print(f"游戏结束,{offensive_side.CN_name}击败了{defensive_side.CN_name}")
         sign=1
         break
    q=round_do(defensive_side,offensive_side)
    if q==-1:
        print(f"游戏结束,{defensive_side.CN_name}击败了{offensive_side.CN_name}")
        sign=-1
        break

    
        

    
    


