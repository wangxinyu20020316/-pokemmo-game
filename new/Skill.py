import Type_table
import Pokemon

class Skill:
    def __init__(self,CN_name,damage,damage_type,pp,Type_s,Accuracy=100,ability="none",ability_up=0):
        self.damage=damage
        self.damage_type=damage_type
        self.ability_up=ability_up
        self.ability=ability
        self.pp=pp
        self.Type_s=Type_s
        self.Accuracy=Accuracy
        self.CN_name=CN_name
        

    def __str__(self):
        return f"技能：{self.CN_name} | 属性：{self.Type_s} | 威力：{self.damage} | PP：{self.pp}"

    def __repr__(self):
        return f"技能：{self.CN_name} | 属性：{self.Type_s} | 威力：{self.damage} | PP：{self.pp}"








