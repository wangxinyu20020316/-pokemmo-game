import random
import data
import Type_table
import Outside
import re
import math
      

##对战区域
def battle(Trainer_1,Trainer_2):
    #先进行对战宝可梦状态更新（宝可梦生命值全为0不可以进入战斗状态）
    Trainer_1.battle_situ_judge()
    Trainer_2.battle_situ_judge()
    if Trainer_1.flag==0:
        print(f"{Trainer_1}的宝可梦都精疲力尽了")
    elif Trainer_2.flag==0:
        print(f"{Trainer_2}的宝可梦都精疲力尽了")

    #回合开始
    for round in range(1,9999999999):
        #首回合特殊处理
        if round==1:
            att_side,def_side=judge_speed_priority(Trainer_1.pokeOwn[0],Trainer_2.pokeOwn[0])
        print(f"round {round}")

        #测试使用，不测试时记得注释掉
        print(att_side)
        print(def_side)
        print(f"{att_side.name_print()}获得先手权")
        round_do(att_side,def_side)
        round_do(def_side,att_side)


#判断先手权(传入两个个体宝可梦)
def judge_speed_priority(pokemon_1,pokemon_2):
    if pokemon_1.speed_own>pokemon_2.speed_own:
        return pokemon_1,pokemon_2
    elif pokemon_1.speed_own<pokemon_2.speed_own:
        return pokemon_2,pokemon_1
    else:
        a=random.randint(1,2)
        if a==1:
            return pokemon_1,pokemon_2
        else:
            return pokemon_2,pokemon_1

#回合操作(传入两个个体宝可梦)
def round_do(pokemon_1,pokemon_2):
    count=0
    for i in pokemon_1.skills:
        count+=1
        print(f"{count}:{i}")

    #输入技能序号
    #2026/6/18：先以技能序号为准，后面再写技能名称
    temp=input("请输入你要使用的技能序号:")
    skill_number=re.findall(r"\d",temp)
    print(skill_number)

    #根据输入的序号识别技能
##    print(skill_number[0])
##    print(int(skill_number[0]))
    k=pokemon_1.skills[int(skill_number[0])-1] #获取到技能对象
    a=cal_damage(k,pokemon_1,pokemon_2)
    cause_damage(a,pokemon_2)


def cause_damage(a,pokemon):
    pokemon.hp=pokemon.hp_own-a
    print(f"{pokemon.dex.CN_name}受到了{a}点伤害,还剩{pokemon.hp}点血量")


def get_stab_rate(skill,pokemon):
    if skill.Type_s==pokemon.dex.Type_1 or skill.Type_s==pokemon.dex.Type_2:
        return 1.5
    else:
        return 1

    
#暴击倍率
def crit():
    a=random.randint(1,24)
    if a==1:
        return 2
    else:
        return 1


#传入参数使用的技能，攻击方宝可梦，防御方宝可梦
def cal_damage(skill,pokemon_1,pokemon_2):

    #物攻，特攻，变化三种技能数据不同
    if skill.damage_type=="physical":
        att_stat=pokemon_1.at_own
        de_stat=pokemon_2.de_own
    elif skill.damage_type=="special":
        att_stat=pokemon_1.st_own
        de_stat=pokemon_2.sd_own
    elif skill.damage_type=="change":
        pass

    #修正系数 总修正系数 = 天气 × 场地 × 属性克制 × 本系加成 × 道具 × 暴击 × 随机 (0.85~1.0)
    #2026/6/18：未加入天气，场地，道具。暂时只考虑克制，本系加成，暴击以及随机
    modifier_1=Type_table.get_type_effect(skill.Type_s,pokemon_2)    #属性克制修正系数
    modifier_2=get_stab_rate(skill, pokemon_1)     #本系加成修正
    modifier_3=crit()     #暴击概率修正
    modifier_4=round(random.uniform(0.85, 1.0), 2)   #随机数修正
    modifier=modifier_1*modifier_2*modifier_3*modifier_4
    
    

    #伤害数值  分三部分，后期方便维护
    part_1=(2*pokemon_1.level)/5+2   #第一部分为等级相关伤害计算
    part_2=(part_1*skill.damage*att_stat)/de_stat #第二部分为招式威力以及攻击方能力，防御方能力相关计算
    part_3=math.floor(((part_2/50)*modifier)+1)

    return part_3
     
    
    
    
    

    

battle(data.wxy,data.lzs)

    
        

    
    


