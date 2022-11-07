import sys
import pygame
from pytmx.util_pygame import load_pygame
from settings import *
from dialogue import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('graphics/player/player_front.png').convert_alpha(), size=(56, 84))
        self.rect = self.image.get_rect(bottomleft=position)
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.player_index = 0

        # player animation surfaces
        self.player_front = pygame.transform.scale(
            pygame.image.load('graphics/player/player_front.png').convert_alpha(), size=(56, 84))
        self.player_back = pygame.transform.scale(pygame.image.load('graphics/player/player_back.png').convert_alpha(),
                                                  size=(56, 84))
        self.player_right = pygame.transform.scale(
            pygame.image.load('graphics/player/player_right.png').convert_alpha(), size=(56, 84))
        self.player_left = pygame.transform.scale(pygame.image.load('graphics/player/player_left.png').convert_alpha(),
                                                  size=(56, 84))
        self.player_run_left = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_left.png').convert_alpha(), size=(56, 84))
        self.player_run_right = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_right.png').convert_alpha(), size=(56, 84))

        # walking animations
        player_walk_up_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_up_1.png').convert_alpha(), size=(56, 84))
        player_walk_up_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_up_2.png').convert_alpha(), size=(56, 84))
        self.player_walk_up = [player_walk_up_1, player_walk_up_2]

        player_walk_down_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_down_1.png').convert_alpha(), size=(56, 84))
        player_walk_down_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_down_2.png').convert_alpha(), size=(56, 84))
        self.player_walk_down = [player_walk_down_1, player_walk_down_2]

        player_walk_left_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_left_1.png').convert_alpha(), size=(56, 84))
        player_walk_left_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_left_2.png').convert_alpha(), size=(56, 84))
        self.player_walk_left = [player_walk_left_1, self.player_left, player_walk_left_2, self.player_left]

        player_walk_right_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_right_1.png').convert_alpha(), size=(56, 84))
        player_walk_right_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_walk_right_2.png').convert_alpha(), size=(56, 84))
        self.player_walk_right = [player_walk_right_1, self.player_right, player_walk_right_2, self.player_right]

        # running animations
        player_run_up_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_up_1.png').convert_alpha(), size=(56, 84))
        player_run_up_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_up_2.png').convert_alpha(), size=(56, 84))
        self.player_run_up = [player_run_up_1, player_run_up_2]

        player_run_down_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_down_1.png').convert_alpha(), size=(56, 84))
        player_run_down_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_down_2.png').convert_alpha(), size=(56, 84))
        self.player_run_down = [player_run_down_1, player_run_down_2]

        player_run_left_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_left_1.png').convert_alpha(), size=(56, 84))
        player_run_left_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_left_2.png').convert_alpha(), size=(56, 84))
        self.player_run_left = [player_run_left_1, self.player_run_left, player_run_left_2, self.player_run_left]

        player_run_right_1 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_right_1.png').convert_alpha(), size=(56, 84))
        player_run_right_2 = pygame.transform.scale(
            pygame.image.load('graphics/player/player_run_right_2.png').convert_alpha(), size=(56, 84))
        self.player_run_right = [player_run_right_1, self.player_run_right, player_run_right_2, self.player_run_right]

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.direction.x = 0
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.direction.x = 0
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.direction.y = 0
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.direction.y = 0
        else:
            self.direction.x = 0
            self.direction.y = 0

        if keys[pygame.K_LSHIFT]:
            self.speed = 6
        else:
            self.speed = 3

    def animation(self):
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYUP:
            pygame.event.clear()
            if event.key == pygame.K_UP and self.direction.x == 0 and self.direction.y == 0:
                self.image = self.player_back
            elif event.key == pygame.K_DOWN and self.direction.x == 0 and self.direction.y == 0:
                self.image = self.player_front
            elif event.key == pygame.K_RIGHT and self.direction.x == 0 and self.direction.y == 0:
                self.image = self.player_right
            elif event.key == pygame.K_LEFT and self.direction.x == 0 and self.direction.y == 0:
                self.image = self.player_left
        if self.direction.x == 1 and self.direction.y == 0:
            pygame.event.clear()
            self.player_index += 0.12
            if self.player_index >= len(self.player_walk_right):
                self.player_index = 0
            self.image = self.player_walk_right[int(self.player_index)]
        if self.direction.x == -1 and self.direction.y == 0:
            pygame.event.clear()
            self.player_index += 0.12
            if self.player_index >= len(self.player_walk_left):
                self.player_index = 0
            self.image = self.player_walk_left[int(self.player_index)]
        if self.direction.y == 1 and self.direction.x == 0:
            pygame.event.clear()
            self.player_index += 0.08
            if self.player_index >= len(self.player_walk_down):
                self.player_index = 0
            self.image = self.player_walk_down[int(self.player_index)]
        if self.direction.y == -1 and self.direction.x == 0:
            pygame.event.clear()
            self.player_index += 0.08
            if self.player_index >= len(self.player_walk_up):
                self.player_index = 0
            self.image = self.player_walk_up[int(self.player_index)]
        if keys[pygame.K_LSHIFT]:
            if self.direction.x == 1 and self.direction.y == 0:
                pygame.event.clear()
                self.player_index += 0.12
                if self.player_index >= len(self.player_run_right):
                    self.player_index = 0
                self.image = self.player_run_right[int(self.player_index)]
            if self.direction.x == -1 and self.direction.y == 0:
                pygame.event.clear()
                self.player_index += 0.12
                if self.player_index >= len(self.player_run_left):
                    self.player_index = 0
                self.image = self.player_run_left[int(self.player_index)]
            if self.direction.y == 1 and self.direction.x == 0:
                pygame.event.clear()
                self.player_index += 0.08
                if self.player_index >= len(self.player_run_down):
                    self.player_index = 0
                self.image = self.player_run_down[int(self.player_index)]
            if self.direction.y == -1 and self.direction.x == 0:
                pygame.event.clear()
                self.player_index += 0.08
                if self.player_index >= len(self.player_run_up):
                    self.player_index = 0
                self.image = self.player_run_up[int(self.player_index)]

    def collision(self):
        if pygame.sprite.spritecollide(self, obstacle_group, False) or pygame.sprite.spritecollide(self, npc_group, False):
            if self.direction.x < 0:
                self.rect.x += 1 * self.speed
            if self.direction.x > 0:
                self.rect.x -= 1 * self.speed
            if self.direction.y < 0:
                self.rect.y += 1 * self.speed
            if self.direction.y > 0:
                self.rect.y -= 1 * self.speed

    def update(self):
        self.collision()
        self.input()
        self.rect.bottomleft += self.direction * self.speed
        self.animation()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()

    # groups
        self.tile_group = tile_group
        self.obstacle_group = obstacle_group
        self.exit_group = exit_group
        self.npc_group = npc_group
        self.grass_group = grass_group
        self.water_group = water_group
        self.dirty_grass_group = dirty_grass_group
        self.sand_group = sand_group
        self.cave_sand_group = cave_sand_group
        self.sa_entrance_group = sa_entrance_group
        self.bt_entrance_group = bt_entrance_group
        self.cave_entrance_group = cave_entrance_group

    # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display.get_size()[0] // 2
        self.half_y = self.display.get_size()[1] // 2

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_y

    def custom_draw(self, target):
        # center player
        self.center_target_camera(target)

        # draw floor
        for sprite in self.tile_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw obstacles
        for sprite in self.obstacle_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw entrances and exits
        for sprite in self.exit_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        for sprite in self.sa_entrance_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        for sprite in self.bt_entrance_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        for sprite in self.cave_entrance_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw grass
        for sprite in self.grass_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw water
        for sprite in self.water_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw dirty grass
        for sprite in self.dirty_grass_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw sand
        for sprite in self.sand_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw cave sand
        for sprite in self.cave_sand_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw NPCs
        for sprite in self.npc_group.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

        # draw player
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)


class StarterArea:
    def __init__(self, pos):
        self.display = pygame.display.get_surface()
        self.map = load_pygame('maps/starter_area.tmx')
        self.camera_group = CameraGroup()
        self.player = Player(position=pos, group=self.camera_group)
        self.prof_rowan = StillNPC(surface=pygame.image.load('graphics/NPCs/prof_rowan/prof_rowan_front.png').convert_alpha(), position=(7 * 64, 6 * 64), group=npc_group)
        self.text_index = 0

    def create_map(self):
        start_floor = self.map.get_layer_by_name('Floor')
        start_obstacles = self.map.get_layer_by_name('Furniture and Walls')
        exit_tiles = self.map.get_layer_by_name('Exit')

        for x, y, surf in start_floor.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=tile_group)

        for x, y, surface in start_obstacles.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surface, group=obstacle_group)

        for x, y, surface in exit_tiles.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surface, group=exit_group)

    def run(self):
        prof_rowan_dialogue_rect = pygame.draw.rect(self.display, 'black', [7 * 64 - 10, 5 * 64 - 2, 84, 84])
        self.camera_group.custom_draw(self.player)
        self.camera_group.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER and self.player.rect.colliderect(prof_rowan_dialogue_rect):
                if self.text_index >= len(prof_rowan_dialogue) - 0.1:
                    self.text_index = 0
                self.text_index += 0.008
                text_box(prof_rowan_dialogue[int(self.text_index)])
        else:
            self.text_index += 0


class HunterArea:
    def __init__(self, pos):
        self.display = pygame.display.get_surface()
        self.map = load_pygame('maps/hunting_area.tmx')
        self.camera_group = CameraGroup()
        self.player = Player(position=pos, group=self.camera_group)

    def create_map(self):
        floor = self.map.get_layer_by_name('Floor')
        grass = self.map.get_layer_by_name('Grass')
        obstacles = self.map.get_layer_by_name('Objects')
        sand = self.map.get_layer_by_name('Sand')
        water = self.map.get_layer_by_name('Water')
        dirty_grass = self.map.get_layer_by_name('Dirty Grass')
        sa_entrance = self.map.get_layer_by_name('SA Entrance')
        bt_entrance = self.map.get_layer_by_name('BT Entrance')
        cave_entrance = self.map.get_layer_by_name('Cave Entrance')

        for x, y, surf in floor.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=tile_group)

        for x, y, surf in grass.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=grass_group)

        for x, y, surf in obstacles.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=obstacle_group)

        for x, y, surf in sand.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=sand_group)

        for x, y, surf in water.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=water_group)

        for x, y, surf in dirty_grass.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=dirty_grass_group)

        for x, y, surf in sa_entrance.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=sa_entrance_group)

        for x, y, surf in bt_entrance.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=bt_entrance_group)

        for x, y, surf in cave_entrance.tiles():
            pos = (x * 32, y * 32)
            Tile(position=pos, surface=surf, group=cave_entrance_group)

    def run(self):
        self.camera_group.custom_draw(self.player)
        self.camera_group.update()


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, surface, group):
        super().__init__(group)
        self.image = pygame.transform.scale(surface, size=(32, 32)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class StillNPC(pygame.sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.image = pygame.transform.scale(surface, size=(64, 80)).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=position)


def text_box(text):
    box = pygame.draw.rect(screen, 'white', [0, 580, 600, 60])
    text_font = pygame.font.Font('fonts/Roboto-Black.ttf', 20)
    text_surf = text_font.render(text, True, 'black').convert_alpha()
    text_rect = text_surf.get_rect(topleft=(10, 600))
    return box, screen.blit(text_surf, text_rect)


# init pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battle Challenge')
clock = pygame.time.Clock()

# maps and groups
tile_group = pygame.sprite.Group()
npc_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
grass_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
dirty_grass_group = pygame.sprite.Group()
sand_group = pygame.sprite.Group()
cave_sand_group = pygame.sprite.Group()
sa_entrance_group = pygame.sprite.Group()
bt_entrance_group = pygame.sprite.Group()
cave_entrance_group = pygame.sprite.Group()

start_area = StarterArea((480, 500))
hunter_area = HunterArea((0, 0))

start_active = False
hunt_active = False
create_map = False

# camera setup
camera_group = CameraGroup()

# intro screen
intro_surf = pygame.image.load('graphics/intro_screen/intro_background.png').convert()
intro_surf = pygame.transform.scale(intro_surf, size=(960, 640))
intro_rect = intro_surf.get_rect(topleft=(0, 0))
intro_font = pygame.font.Font('fonts/Pokemon Solid.ttf', 60)
game_title_surf = intro_font.render('Pokémon Battle Challenge', False, 'red').convert()
game_title_rect = game_title_surf.get_rect(midbottom=(480, 200))
instructions_surf = intro_font.render('''Press 'Space' to begin''', False, 'red').convert()
instructions_rect = instructions_surf.get_rect(midbottom=(480, 600))

# game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_active = True
                create_map = True

    if start_active:
        if create_map:
            start_area.create_map()
            create_map = False
        screen.fill('black')
        start_area.run()
        if pygame.sprite.spritecollide(start_area.player, exit_group, False):
            exit_group.empty()
            obstacle_group.empty()
            tile_group.empty()
            npc_group.empty()
            camera_group.empty()
            start_active = False
            create_map = True
            hunt_active = True
            hunter_area = HunterArea(pos=(10 * 32, 9 * 32))

    elif hunt_active:
        if create_map:
            hunter_area.create_map()
            create_map = False
        screen.fill('black')
        hunter_area.run()

    else:
        screen.blit(intro_surf, intro_rect)
        screen.blit(game_title_surf, game_title_rect)
        screen.blit(instructions_surf, instructions_rect)

    pygame.display.update()
    clock.tick(fps)

