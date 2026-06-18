import random
import Pokemon


class Grass:
    def __init__(self,name,min_level,max_level,*pokemon:Pokemon.Pokemon_Dex):
        self.name=name
        self.min_level=min_level
        self.max_level=max_level
        self.pokemon=pokemon


    def poke_made(self):
        hax=random.randint(1,100)
        if 0<hax<=10:
            temp=Pokemon.Pokemon_wild(self.pokemon[0],self.min_level,self.max_level)
        elif 10<hax<=30:
            temp=Pokemon.Pokemon_wild(self.pokemon[1],self.min_level,self.max_level)
        elif 30<hax<=65:
            temp=Pokemon.Pokemon_wild(self.pokemon[2],self.min_level,self.max_level)
        else:
            temp=Pokemon.Pokemon_wild(self.pokemon[3],self.min_level,self.max_level)
        return temp.random_pokemon()
            
        
        
        






##new_poke=Grass_1.poke_made()
##print(new_poke)
##new_poke.inc_ev("ev_hp",2)
##print(new_poke.ev_hp)
