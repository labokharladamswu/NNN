# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

WORLD_MAP = [

['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

# ui
BAR_HEIGHT = 20
EXP_BAR_WIDTH = 100
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'Zelda-main/1 - level/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
EXP_COLOR = '#00ff00'
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue' 
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword':{'cooldown': 100, 'damage': 15,'graphic':'Zelda-main/1 - level/graphics/weapons/sword/full.png'},
    'axe':{'cooldown': 300, 'damage': 20,'graphic':'Zelda-main/1 - level/graphics/weapons/axe/full.png'},
    'lance':{'cooldown': 400, 'damage': 30,'graphic':'Zelda-main/1 - level/graphics/weapons/lance/full.png'},
    'rapier':{'cooldown': 50, 'damage': 8,'graphic':'Zelda-main/1 - level/graphics/weapons/rapier/full.png'},
    'sai':{'cooldown': 80, 'damage': 10,'graphic':'Zelda-main/1 - level/graphics/weapons/sai/full.png'},
}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic':'Zelda-main/1 - level/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic':'Zelda-main/1 - level/graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound':'Zelda-main/1 - level/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound':'Zelda-main/1 - level/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 150, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound':'Zelda-main/1 - level/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound':'Zelda-main/1 - level/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}