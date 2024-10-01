import random
from enum import Enum, IntEnum

class State(Enum):
    Regular=100,
    Advantage=101,
    Disadvantage=102

class Bonus_type(IntEnum):
    D4 = 4,
    D6 = 6,
    D8 = 8,
    D10 = 10,
    D12 = 12,
    D20 = 20

class Dice():
    def __init__(self, side=20) -> None:
        self.side = side
        
    def roll(self):
        val = random.randint(1,self.side)
        return val
    
class BG3_sampler():
    def __init__(self) -> None:
        self.basic_dice = Dice()
        self.dice_list = []
        self.behavior = {State.Regular: lambda a, b:  a,
                         State.Advantage: max,
                         State.Disadvantage: min,}
        self.clear()
        
    def clear(self):
        self.dice_list.clear()
        
    def sample(self, state: State, bonus_list: list[Bonus_type], modifier = 0):
        val1 = self.basic_dice.roll()
        val2 = self.basic_dice.roll()
        bouns = 0
        if len(bonus_list) != 0:
            for i,d_type in enumerate(bonus_list):
                d = Dice(d_type.value)
                bouns += d.roll()
        val = self.behavior[state](val1, val2) + bouns + modifier
        dice_rst = f"骰子點數為 : {val1} ; " if state == State.Regular else f"骰子點數為 : {val1} , {val2} ; "
        
        rst = f"擲骰結果為 : {val}.\n" + \
              dice_rst + \
              f"調整值 : {modifier} ; bouns : {bouns}"
        # print(rst)
        return val , rst
    
if __name__ == "__main__":
    sampler = BG3_sampler()
    s = State.Disadvantage
    b = [Bonus_type.D4]
    sampler.sample(s,b)
    
        