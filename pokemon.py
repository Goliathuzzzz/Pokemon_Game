import pygame
import spritesheet as ss
from random import randint


class Pokemon(pygame.sprite.Group):
    def __init__(self, group, name, index, hp, attack, defence, spattack, spdefence, speed, move1, move2, move3, move4,
                 type1, type2, ability):
        super().__init__(group)
        self.name = name
        self.index = index
        self.stats = [hp, attack, defence, spattack, spdefence, speed]
        self.moves = [move1, move2, move3, move4]
        self.type = [type1, type2]
        self.ability = ability
        front = pygame.image.load(f'graphics/pokemon/Sprites/{self.index}.png')
        back = pygame.image.load(f'graphics/pokemon/Sprites/back/{self.index}.png')
        self.front = pygame.transform.scale(front, size=(384, 384))
        self.back = pygame.transform.scale(back, size=(384, 384))
        self.front_rect = self.front.get_rect(center=(175 * 4, 45 * 5.6))
        self.front_rect = self.front.get_rect(center=(65 * 4, 105 * 5.6))
    def battle_sprites(self):
        # loads all sprite images of given pokemon

