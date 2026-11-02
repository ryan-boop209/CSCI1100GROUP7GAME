"""
HealthBar.py
Ryan S

Making a visual of the healthbar instead of numbers
"""
import os
import colorama
from colorama import Fore, Style, init
colorama.init()
os.system("")






class HealthBar():
    symbol_remaining: str = "♡"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {
            "red": Fore.LIGHTRED_EX,
            "green": Fore.LIGHTGREEN_EX,
            "default": Style.RESET_ALL
        
        }
    
    def __init__(self, entity, length: int = 20, is_colored:bool = True, color:str = "default"):
        self.entity = entity
        self.length = length
        self.is_colored = is_colored
        self.max_health = entity.max_health
        
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]
    
    def update(self) -> None:
        self.current_value = self.entity.health
    
    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_health * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s Health: {self.entity.health} / {self.entity.max_health}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
    
        