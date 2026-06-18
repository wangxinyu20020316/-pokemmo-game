ground = {"grass":0.5, "dark":2.0}
dark = {"Psychic":2.0, "Fighting":0.5}
normal = {"rock":0.5}
fire = {"water":0.5, "grass":2.0}
water = {"fire":2.0, "grass":0.5}
grass={"water":2,"fire":0.5}
type_map = {
    "ground": ground,
    "dark": dark,
    "normal": normal,
    "fire": fire,
    "water": water,
    "grass": grass
}

# 统一查询函数(一般场景是技能打在宝可梦身上，所以只需要技能的属性以及防守方宝可梦的属性)
def get_type_effect(attack_skill_type, defend_pokemon_type):
    # 根据攻击属性拿到对应的克制字典
    attack_dict = type_map[attack_skill_type]

    #获取防守方宝可梦的两个属性
    type_1=defend_pokemon_type.dex.Type_1
    type_2=defend_pokemon_type.dex.Type_2
    
    #防御属性不在字典里，默认倍率1.0
    #如果在字典里，获取倍率
    rate_1=attack_dict.get(type_1, 1.0)
    print(rate_1)
    rate_2=attack_dict.get(type_2, 1.0)
    print(rate_2)

    #最终倍率为两个相乘
    return rate_1*rate_2



#测试
##if __name__ == "__main__":
##    import data
##    print(get_type_effect("fire",data.Sandile_own))
