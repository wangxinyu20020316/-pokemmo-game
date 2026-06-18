import Type_table
import random
import math


class Pokemon_Dex:
    def __init__(self,Type_1,Type_2,b_blood,b_at,b_de,b_sa,b_sd,b_speed,CN_name,evolu="none",*skill):
        self.Type_1=Type_1
        self.Type_2=Type_2
        self.b_blood=b_blood
        self.b_at=b_at
        self.b_de=b_de
        self.b_sa=b_sa
        self.b_sd=b_sd
        self.b_speed=b_speed
        self.CN_name=CN_name
        self.evolu=evolu
        self.skill=skill

    def print_CN(self):
        return self.CN_name

    def __str__(self):
        return (
            f"【宝可梦】{self.CN_name}"
        )



class Pokemon_own:                       
    def __init__(self,dex:Pokemon_Dex,blood,at,de,st,sd,speed,level,*skills):
        self.dex=dex

        #个体值
        self.blood=blood
        self.at=at
        self.de=de
        self.st=st
        self.sd=sd
        self.speed=speed
        self.level=level
        self.skills=skills
        
        #基础点数
        self.ev_hp = 0
        self.ev_at = 0
        self.ev_de = 0
        self.ev_st = 0
        self.ev_sd = 0
        self.ev_speed = 0

        #总点数
        self.total_ev=0

        #总数值(受种族，个体值以及基础点数影响）
        self.hp_own = math.floor(((self.dex.b_blood * 2 + self.blood + self.ev_hp//4) * self.level / 100) + self.level + 10)
        self.at_own = math.floor(((self.dex.b_at * 2 + self.at + self.ev_at//4) * self.level / 100) + 5)
        self.de_own = math.floor(((self.dex.b_de * 2 + self.de + self.ev_de//4) * self.level / 100) + 5)
        self.st_own = math.floor(((self.dex.b_sa * 2 + self.st + self.ev_st//4) * self.level / 100) + 5)
        self.sd_own = math.floor(((self.dex.b_sd * 2 + self.sd + self.ev_sd//4) * self.level / 100) + 5)
        self.speed_own = math.floor(((self.dex.b_speed * 2 + self.speed + self.ev_speed//4) * self.level / 100) + 5)
        #公式来源宝可梦官网

    def alive_ju(self):
        if self.blood==0:
            return False
        else:
            return True
        
    #每次战斗都会增加基础点数(2026/6/17:暂时没想到好的办法解决if嵌套过多的问题)
    def inc_ev(self,ev_str:str,num:int):
        if self.total_ev>=510:
            print("基础点数已满，无法增加")
        if ev_str=="ev_hp":
            if self.ev_hp>=225:
                print("基础点数已满，无法增加")
            else:
                self.ev_hp+=num
                self.total_ev+=num
        elif ev_str=="ev_at":
            if self.ev_at>=225:
                print("基础点数已满，无法增加")
            else:
                self.ev_at+=num
                self.total_ev+=num
        elif ev_str=="ev_de":
            if self.ev_de>=225:
                print("基础点数已满，无法增加")
            else:
                self.total_ev+=num
                self.ev_de+=num
        elif ev_str=="ev_st":
            if self.ev_st>=225:
                print("基础点数已满，无法增加")
            else:
                self.ev_st+=num
                self.total_ev+=num
        elif ev_str=="ev_sd":
            if self.ev_sd>=225:
                print("基础点数已满，无法增加")
            else:
                self.ev_sd+=num
                self.total_ev+=num
        elif ev_str=="ev_speed":
            if self.ev_speed>=225:
                print("基础点数已满，无法增加")
            else:
                self.ev_speed+=num
                self.total_ev+=num

    def name_print(self):
        return self.dex.CN_name
        
        

    def __str__(self):
        return (
            f"【宝可梦】{self.dex.CN_name} Lv.{self.level}\n"
            f"个体值："
            f"血量：{self.blood} | 攻击：{self.at} | 防御：{self.de}\n"
            f"特攻：{self.st} | 特防：{self.sd} | 速度：{self.speed}\n"
            f"结算值："
            f"当前血量：{self.hp_own} | 攻击：{self.at_own} | 防御：{self.de_own}\n"
            f"特攻：{self.st_own} | 特防：{self.sd_own} | 速度：{self.speed_own}"
        )


    def __repr__(self):
        return (
            f"【宝可梦】{self.dex.CN_name} Lv.{self.level}\n"
            f"个体值："
            f"血量：{self.blood} | 攻击：{self.at} | 防御：{self.de}\n"
            f"特攻：{self.st} | 特防：{self.sd} | 速度：{self.speed}\n"
            f"结算值："
            f"当前血量：{self.hp_own} | 攻击：{self.at_own} | 防御：{self.de_own}\n"
            f"特攻：{self.st_own} | 特防：{self.sd_own} | 速度：{self.speed_own}"
        )



class Pokemon_wild(Pokemon_own):
    #宝可梦个体随机器
    def __init__(self,dex:Pokemon_Dex,min_level,max_level,iv_min=0,iv_max=31):
        self.dex=dex
        self.min_level=min_level
        self.max_level=max_level
        self.iv_min=iv_min
        self.iv_max=iv_max

    def random_pokemon(self):
        hp=random.randint(self.iv_min,self.iv_max)
        at=random.randint(self.iv_min,self.iv_max)
        de=random.randint(self.iv_min,self.iv_max)
        st=random.randint(self.iv_min,self.iv_max)
        sd=random.randint(self.iv_min,self.iv_max)
        speed=random.randint(self.iv_min,self.iv_max)
        level=random.randint(self.min_level,self.max_level)
        return Pokemon_own(self.dex,hp,at,de,st,sd,speed,level)

    def __str__(self):
        return f"{self.dex}出现了,hp为{self.hp},攻击为{self.at},防御为{self.de},特攻为{self.st},特防为{self.sd},速度为{self.speed}"
        

        
     




