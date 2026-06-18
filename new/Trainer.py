import Pokemon


class Trainer:
    def __init__(self,name,*pokeOwn:Pokemon.Pokemon_own):
        self.name=name
        self.pokeOwn=pokeOwn

        self.flag=0

    def battle_situ_judge(self):
        for i in self.pokeOwn:
            if i.hp_own>=1:
                self.flag=1
                break
            else:
                self.flag=0

    def __str__(self):
        return (
            f"self.name"
        )

        




#将对象放入列表，元组等容器中打印容器时，会打印repr魔方方法的内容
##print(wxy.pokeOwn)
