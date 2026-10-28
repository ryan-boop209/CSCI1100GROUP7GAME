"""
HealthBar.py
Ryan S

Making a visual of the healthbar instead of numbers
"""
import os
os.system("")




class HealthBar():
    def __init__(self, entity, length: int, is_colored, color):
        self.entity = entity
        self.length = length
        self.is_colored = is_colored
        self.max_heath = color
        