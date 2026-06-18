import Pokemon
import Skill
import Trainer
import Outside


#技能数据
Tackle=Skill.Skill("撞击",40,"physical",35,"normal")
Crunch=Skill.Skill("咬碎",80,"physical",15,"dark")




##宝可梦图鉴数据
Bulbasaur=Pokemon.Pokemon_Dex("grass","poison",45,49,49,65,65,45,"妙蛙种子",16)
Sandile=Pokemon.Pokemon_Dex("ground","Dark",50,72,35,35,35,65,"黑眼鳄",28)
Eevee=Pokemon.Pokemon_Dex("normal","none",55,55,50,45,65,55,"伊布","进化石")
Pidgey=Pokemon.Pokemon_Dex("normal","Flying",40,45,40,35,35,56,"波波",16)


##宝可梦个体数据
Bulbasaur_own=Pokemon.Pokemon_own(Bulbasaur,10,20,30,20,10,20,15,Tackle)
Sandile_own=Pokemon.Pokemon_own(Sandile,10,20,30,20,10,20,15,Tackle,Crunch)

#训练家数据
wxy=Trainer.Trainer("帅哥",Sandile_own)
lzs=Trainer.Trainer("劲敌",Bulbasaur_own)


#野外数据
Grass_1=Outside.Grass("1号草丛",1,10,Eevee,Bulbasaur,Sandile,Pidgey)
