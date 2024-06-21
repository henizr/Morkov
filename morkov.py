import pygame
import sys
from pygame.locals import *
from typing import (
    Union
)

class Rectangle:
    def __init__(
            self, 
            surface: pygame.Surface, 
            width: int = 100, 
            height:int = 100, 
            x: int = 10, 
            y: int = 10, 
            color: tuple=(0,0,0), 
            border_radius: int=0,
            thickness: int=0
    ) -> None:
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.border_radius = border_radius
        self.thickness = thickness

    def draw(self):
        pygame.draw.rect(
            surface=self.surface,
            color=self.color,
            rect=(self.x, self.y, self.width, self.height),
            border_radius=self.border_radius,
            width=self.thickness
        )
        
class Square:
    def __init__(
            self, 
            surface: pygame.Surface, 
            side: int = 100, 
            x: int = 10, 
            y: int = 10, 
            color: tuple=(0,0,0), 
            border_radius: int=0,
            thickness: int=0
    ) -> None:
        pygame.draw.rect(
        surface=surface,
        color=color,
        rect=(x, y, side, side),
        border_radius=border_radius,
        width=0
    )
        
class Circle:
    def __init__(
            self,
            surface: pygame.Surface,
            color: Union[tuple, str] = (255,255,0),
            center_x: Union[int,float] = 0,
            center_y: Union[int,float] = 0,
            radius: Union[int,float] = 50,
            thickness: Union[int,float] = 0
    ):
        pygame.draw.circle(
            surface=surface,
            color=color,
            center=(center_x, center_y),
            radius=radius,
            width=thickness
        )

class Ellipse:
    def __init__(
            self, 
            surface: pygame.Surface, 
            width: int = 100, 
            height:int = 50, 
            x: int = 100, 
            y: int = 100, 
            color: tuple=(255,0,255), 
            border_radius: int=0,
            thickness: int=0
    ) -> None:
        pygame.draw.ellipse(
            surface=surface,
            color=color,
            rect=(x, y, width, height),
            width=thickness
        )

class Picture:
    def __init__(self) -> None:
        pass