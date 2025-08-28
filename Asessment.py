"""Project: Level 3 Programming Asessment.

Author: Isaac Smith
School: Hauraki Plains College
Date: 03/06/2024
"""

# Imports
import pygame, json

#Initialize
pygame.init()
WINDOW = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dance Dance Dance: Zombie Apocalypsse")
CLOCK = pygame.time.Clock()
pygame.font.init()

#Variables
FRAME_RATE = 60
font_big = pygame.font.SysFont('freedom-font - Shortcut.lnk', 50)
font_medium = pygame.font.SysFont('freedom-font - Shortcut.lnk', 35)
font_small = pygame.font.SysFont('freedom-font - Shortcut.lnk', 25)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
wave_num = 0
enemies_left = 100 #Temporary for now just to set up UI
ultimate_charge = 0
cooldown_charge = 0
ultimate_status = False
cooldown = False
player_health = 100 #ENTIRELEY TEMP VARIABLE ONLY HERE 'TIL CLASSES
game_state = "start"
pause_level = "base"
start_level = "base"
arrow_limit = 0
arrow_pos = 1
inputs = []
max_inputs = 4
player_name = ''

COMBOS = {
    'failed combo': {'name': 'Failed', 'damage': 0, 'cooldown level': 100, 'charge unit': 0},
    'combo1': {'name': 'Standard Up', 'damage': 5, 'cooldown level': 5, 'charge unit': 10, 'input combo': ['up', 'up', 'up', 'up']},
    'combo2': {'name': 'Standard Down', 'damage' : 5, 'cooldown level': 5, 'charge unit': 10, 'input combo': ['down', 'down', 'down', 'down']},
    'combo3': {'name': 'Standard Left', 'damage': 5, 'cooldown level': 5, 'charge unit': 10, 'input combo': ['left', 'left', 'left', 'left']},
    'combo4': {'name': 'Standard Right', 'damage': 5, 'cooldown level': 5, 'charge unit': 10, 'input combo': ['right', 'right', 'right', 'right']},
    'combo5': {'name': 'Floss', 'damage': 7, 'cooldown level': 3.5, 'charge unit': 15, 'input combo': ['left', 'right', 'left', 'right']},
    'combo6': {'name': 'The Hype', 'damage': 7, 'cooldown level': 3.5, 'charge unit': 15, 'input combo': ['up', 'up', 'down', 'down']},

    'ultimate combo': {'name': 'Ultimate Combo', 'damage': 1000000000, 'cooldown level': 1000000000, 'charge unit': 0, 'input combo': ['up', 'left', 'down', 'right']}
}


class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    
    

def draw_text(text, font, color, x, y):
    text = font.render(text, True, color)
    WINDOW.blit(text, (x, y))

#-----ULTIMATE CHARGE LOAD AND BLIT-----
def load_uc_images(start=2, end=100, step=2, scale=5):
    uc_images = {}
    for i in range(start, end + 1, step):
        path = f'images/gauges/ultimate-charge/UC-{i}%.png'
        uc_image = pygame.image.load(path)
        scaled_image = pygame.transform.scale_by(uc_image, scale)
        uc_images[i] = scaled_image
    return uc_images

def ultimate_blit():
    if ultimate_charge == 0:
        ultimate_gauge = gauge_0
    else:
        # Clamp the charge to the nearest lower even number between 2 and 100
        clamped_uc_charge = min(max(2, int(ultimate_charge // 2 * 2)), 100)
        ultimate_gauge = ultimate_charge_images.get(clamped_uc_charge, gauge_0)

    WINDOW.blit(ultimate_gauge, (75, 600))

#-----COOLDOWN LOAD AND BLIT-----
def load_c_images(start=2, end=100, step=2, scale=5):
    c_images = {}
    for i in range(start, end + 1, step):
        path = f'images/gauges/cooldown/C-{i}%.png'
        c_image = pygame.image.load(path)
        scaled_image = pygame.transform.scale_by(c_image, scale)
        c_images[i] = scaled_image
    return c_images

def cooldown_blit():
    if cooldown_charge == 0:
        cooldown_gauge = gauge_0
    else:
        clamped_c_charge = min(max(2, int(cooldown_charge // 2 * 2)), 100)
        cooldown_gauge = cooldown_charge_images.get(clamped_c_charge, gauge_0)

    WINDOW.blit(cooldown_gauge, (935,600))

def on_cooldown(cooldown, cooldown_charge):
    if cooldown:
        cooldown_charge -= COMBOS[output_combo]['cooldown level']
        if cooldown_charge <= 0:
            cooldown_charge = 0
            cooldown = False
    return cooldown, cooldown_charge

#-----HEALTH BAR LOAD AND BLIT-----
def load_hb_images(start=4, end=100, step=4, scale=5):
    hb_images = {}
    for i in range(start, end + 1, step):
        path = f'images/health bar/HB-{i}%.png'
        hb_image = pygame.image.load(path)
        scaled_image = pygame.transform.scale_by(hb_image, scale)
        hb_images[i] = scaled_image
    return hb_images

def hb_blit():
    if player_health == 0:
        health_bar = hb_empty
    else:
        clamped_player_health = min(max(4, int(player_health // 4 * 4)), 100)
        health_bar = hb_images.get(clamped_player_health, hb_empty)

    WINDOW.blit(health_bar, (1125,30))

#-----PLAYER INPUTS REACTIVITY-----
def arrows_functionality():
    if key_pressed[pygame.K_LEFT]:
        left_arrow = left_arrow_pressed
        WINDOW.blit(left_arrow, (425,565))
    else:
        left_arrow = left_arrow_base
        WINDOW.blit(left_arrow, (420,560))
    
    if key_pressed[pygame.K_UP]:
        up_arrow = up_arrow_pressed
        WINDOW.blit(up_arrow, (545,565))
    else:   
        up_arrow = up_arrow_base
        WINDOW.blit(up_arrow, (540,560))
    
    if key_pressed[pygame.K_DOWN]:
        down_arrow = down_arrow_pressed
        WINDOW.blit(down_arrow, (665,565))
    else:
        down_arrow = down_arrow_base
        WINDOW.blit(down_arrow, (660,560))

    if key_pressed[pygame.K_RIGHT]:
        right_arrow = right_arrow_pressed
        WINDOW.blit(right_arrow, (785,565))
    else:
        right_arrow = right_arrow_base
        WINDOW.blit(right_arrow, (780,560))

def inputs_display():
    if inputs and len(inputs) > 0:
        if inputs[0] == 'up':
            inputs0 = mini_arrow_up
        elif inputs[0] == 'down':
            inputs0 = mini_arrow_down
        elif inputs[0] == 'left':
            inputs0 = mini_arrow_left
        elif inputs[0] == 'right':
            inputs0 = mini_arrow_right
        else:
            inputs0 = blank
    else:
        inputs0 = blank

    if inputs and len(inputs) > 1:
        if inputs[1] == 'up':
            inputs1 = mini_arrow_up
        elif inputs[1] == 'down':
            inputs1 = mini_arrow_down
        elif inputs[1] == 'left':
            inputs1 = mini_arrow_left
        elif inputs[1] == 'right':
            inputs1 = mini_arrow_right
        else:
            inputs1 = blank
    else:
        inputs1 = blank

    if inputs and len(inputs) > 2:
        if inputs[2] == 'up':
            inputs2 = mini_arrow_up
        elif inputs[2] == 'down':
            inputs2 = mini_arrow_down
        elif inputs[2] == 'left':
            inputs2 = mini_arrow_left
        elif inputs[2] == 'right':
            inputs2 = mini_arrow_right
        else:
            inputs2 = blank
    else:
        inputs2 = blank

    if inputs and len(inputs) > 3:
        if inputs[3] == 'up':
            inputs3 = mini_arrow_up
        elif inputs[3] == 'down':
            inputs3 = mini_arrow_down
        elif inputs[3] == 'left':
            inputs3 = mini_arrow_left
        elif inputs[3] == 'right':
            inputs3 = mini_arrow_right
        else:
            inputs3 = blank
    else:
        inputs3 = blank

    WINDOW.blit(inputs0, (450, 530))
    WINDOW.blit(inputs1, (480, 530))
    WINDOW.blit(inputs2, (510, 530))
    WINDOW.blit(inputs3, (540, 530))
        
    if ultimate_status:
        WINDOW.blit(mini_arrow_up, (110, 530))
        WINDOW.blit(mini_arrow_left, (140, 530))
        WINDOW.blit(mini_arrow_down, (170, 530))
        WINDOW.blit(mini_arrow_right, (200, 530))

#-----CHECK FOR COMBOS-----
def check_combo():
    #Regular combos
    if inputs == COMBOS['combo1']['input combo']:
        output_combo = 'combo1'
    elif inputs == COMBOS['combo2']['input combo']:
        output_combo = 'combo2'
    elif inputs == COMBOS['combo3']['input combo']:
        output_combo = 'combo3'
    elif inputs == COMBOS['combo4']['input combo']:
        output_combo = 'combo4'
    elif inputs == COMBOS['combo5']['input combo']:
        output_combo = 'combo5'
    elif inputs == COMBOS['combo6']['input combo']:
        output_combo = 'combo6'
    elif inputs == COMBOS['ultimate combo']['input combo']:
            output_combo = 'ultimate combo'
    else: 
        output_combo = 'failed combo'
        
    return output_combo

def player_pointing():
    if not cooldown:
        #Player Pointing Animation
        if key_pressed[pygame.K_LEFT]:
            player = player_pointing_left
            player_x = 1055
            player_y = 70
        elif key_pressed[pygame.K_RIGHT]:
            player = player_pointing_right
            player_x = 1145
            player_y = 70
        elif key_pressed[pygame.K_UP]:
            player = player_pointing_up
            player_x = 1145
            player_y = 10
        elif key_pressed[pygame.K_DOWN]:
            player = player_pointing_down
            player_x = 1145
            player_y = 70
        else: 
            player = player_default
            player_x = 1145
            player_y = 70
    else:
        player = player_default
        player_x = 1145
        player_y = 70

    WINDOW.blit(player, (player_x, player_y))

#-----DISPLAY GAME UI-----
def ui_blit(key_pressed):
    """Displays all parts of the base game UI"""
    # -----Display text-----
    #Wave number
    if wave_num <= 9:
        draw_text("Wave: " + str(wave_num), font_medium, WHITE, 596, 10)
    elif wave_num <= 99:
        draw_text("Wave: " + str(wave_num), font_medium, WHITE, 595, 10) #CHANGE X POS FOR SPACING, 2 didgits
    
    #Enemies left
    if enemies_left <= 999:
        draw_text("Enemies Left: " + str(enemies_left), font_medium, WHITE, 545, 687)
    elif enemies_left <= 99:
        draw_text("Enemies Left: " + str(enemies_left), font_medium, WHITE, 545, 687) #CHANGE X POS FOR SPACING, 2 didgits
    elif enemies_left <= 9:
        draw_text("Enemies Left: " + str(enemies_left), font_medium, WHITE, 545, 687) #CHANGE X POS FOR SPACING, single digit

    draw_text(player_name, font_small, WHITE, 1135, 15)

    #Esc to pause
    WINDOW.blit(esc_bg, (25, 25))
    draw_text("esc", font_small, BLACK, 31, 35)
    draw_text("to pause", font_small, WHITE, 70, 35)

    #-----Gauges-----
    ultimate_blit()
    cooldown_blit()

    #Gauge titles
    draw_text("Ultimate Charge", font_small, WHITE, 142.5, 575)
    draw_text("Cooldown", font_small, WHITE, 1027.5, 575)

    #-----Arrows-----
    arrows_functionality()
    inputs_display()

    #-----Health Bar-----
    hb_blit()    
        
    player_pointing()

#DISPLAY PAUSE SCREEN
def pause_screen(arrow_limit):
    #Gray overlay
    overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)  
    overlay.fill((128, 128, 128, 150))
    WINDOW.blit(overlay, (0, 0))

    #Esc to play
    WINDOW.blit(esc_bg, (25, 25))
    draw_text("esc", font_small, BLACK, 31, 35)
    draw_text("to play", font_small, WHITE, 70, 35)
    draw_text("Z to confirm", font_small, WHITE, 31, 75)

    if pause_level == "base":
        #Selection Text
        draw_text("ENEMIES", font_big, WHITE, 562.5, 135)
        draw_text("MOVES", font_big, WHITE, 577.5, 265)
        draw_text("ACHIEVEMENTS", font_big, WHITE, 502.5, 400)
        draw_text("QUIT", font_big, WHITE, 597.5, 535)

        arrow_limit = 4
        
        if arrow_pos == 1:
            WINDOW.blit(selection_arrow, (480, 125))
        elif arrow_pos == 2:
            WINDOW.blit(selection_arrow, (495, 255))
        elif arrow_pos == 3:
            WINDOW.blit(selection_arrow, (420, 390))
        elif arrow_pos == 4:
            WINDOW.blit(selection_arrow, (515, 525))

    return arrow_limit

#Display start screen
def start_screen(arrow_limit):
    #Gray overlay
    overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)  
    overlay.fill((128, 128, 128, 150))
    WINDOW.blit(overlay, (0, 0))

    #Logo
    WINDOW.blit(logo, (280, 100))

    draw_text("Z to confirm", font_small, WHITE, 592.5, 660)
    draw_text("X to uhhh, do the opposite or whatever", font_small, WHITE, 483, 680)
    draw_text("Arrow keys to move to arrow", font_small, WHITE, 520, 700)

    if start_level == "base":
        draw_text("NEW PLAYER", font_big, WHITE, 525.5, 475)
        draw_text("RETURNING PLAYER", font_big, WHITE, 467.5, 575)

        arrow_limit = 2
        
        if arrow_pos == 1:
            WINDOW.blit(selection_arrow, (443, 465))
        elif arrow_pos == 2:
            WINDOW.blit(selection_arrow, (385, 565))

    if start_level == "new player":
        draw_text("INPUT NAME:", font_big, WHITE, 527.5, 475)
        draw_text("BACK", font_big, WHITE, 590, 600)
        
        draw_text(player_name, font_big, WHITE, 525.5, 525)

        if player_name != '':
            draw_text("Enter to confirm", font_small, WHITE, 756, 489)

        arrow_limit = 2

        if arrow_pos == 1:
            WINDOW.blit(selection_arrow, (444, 465))
        elif arrow_pos == 2:
            WINDOW.blit(selection_arrow, (507.5, 590))

    return arrow_limit

blank = pygame.transform.scale_by(pygame.image.load('images/Blank.png'), 5)

#Loading background
background = pygame.transform.scale_by(pygame.image.load('images/DDDZA-Background.png'), 5)

#-----Loading the gauge sprites-----#
gauge_0 = pygame.transform.scale_by(pygame.image.load('images/gauges/Gauge-0%.png'), 5)
hb_empty = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-Empty.png'), 5)
ultimate_charge_images = load_uc_images()
cooldown_charge_images = load_c_images()
hb_images = load_hb_images()

#Loading arrows
up_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/up-arrow.png'), 5)
up_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/up-arrow-pressed.png'), 5)
down_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/down-arrow.png'), 5)
down_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/down-arrow-pressed.png'), 5)
left_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/left-arrow.png'), 5)
left_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/left-arrow-pressed.png'), 5)
right_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/right-arrow.png'), 5)
right_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/right-arrow-pressed.png'), 5)

#Loading Escape Image
esc_bg = pygame.transform.scale_by(pygame.image.load('images/esc.png'), 5)

#Loading Selection Arrow
selection_arrow = pygame.transform.scale_by(pygame.image.load('images/arrows/Arrow.png'), 5)

#Loading mini arrows that tell you what your inputs currently look like
mini_arrow_up = pygame.transform.scale_by(pygame.image.load('images/arrows/Input-list-up.png'), 5)
mini_arrow_down = pygame.transform.scale_by(pygame.image.load('images/arrows/Input-list-down.png'), 5)
mini_arrow_left = pygame.transform.scale_by(pygame.image.load('images/arrows/Input-list-left.png'), 5)
mini_arrow_right = pygame.transform.scale_by(pygame.image.load('images/arrows/Input-list-right.png'), 5)

#Loading Player Sprites
player_default = pygame.transform.scale_by(pygame.image.load('images/Player/Player-Standard.png'), 5)
player_pointing_up = pygame.transform.scale_by(pygame.image.load('images/Player/Pointing/Player-Pointing-Up.png'), 5)
player_pointing_down = pygame.transform.scale_by(pygame.image.load('images/Player/Pointing/Player-Pointing-Down.png'), 5)
player_pointing_left = pygame.transform.scale_by(pygame.image.load('images/Player/Pointing/Player-Pointing-Left.png'), 5)
player_pointing_right = pygame.transform.scale_by(pygame.image.load('images/Player/Pointing/Player-Pointing-Right.png'), 5)

logo = pygame.transform.scale_by(pygame.image.load('images/Logo.png'), 5)

#Game loop
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                

            if event.type == pygame.KEYDOWN:
                
                if game_state == "start":
                    if start_level == "new player":
                        if arrow_pos == 1:
                            if event.key == pygame.K_BACKSPACE:
                                player_name = player_name[:-1]
                            elif event.key == pygame.K_RETURN:
                                pass
                            else:
                                if len(player_name) < 6:
                                    player_name += event.unicode
                
                if game_state == "active":
                    if not cooldown:
                        
                        #Combo input tracking
                        if event.key == pygame.K_LEFT:
                            inputs.append('left')
                        if event.key == pygame.K_RIGHT:
                            inputs.append('right')
                        if event.key == pygame.K_UP:
                            inputs.append('up')
                        if event.key == pygame.K_DOWN:
                            inputs.append('down')

                        #Executing a combo
                        if event.key == pygame.K_z:
                            output_combo = check_combo()
                            if output_combo == 'ultimate combo':
                                if ultimate_status:
                                    inputs = []
                                    ultimate_charge = 0
                                else:
                                    output_combo = 'failed combo'
                            else:
                                if output_combo == 'failed combo':
                                    inputs = []
                                else:
                                    inputs = []
                                    ultimate_charge += COMBOS[output_combo]['charge unit']
                                    cooldown = True
                                    cooldown_charge = 100
                        
                        #Clearing combo list
                        if event.key == pygame.K_x:
                            inputs = []
                    
                #Limits the number of recorded inpits at a time to 0
                if len(inputs) > max_inputs:
                    inputs.pop(0)

            if event.type == pygame.KEYUP:
                
                #Switching between all screens
                if event.key == pygame.K_z:
                    if game_state == "start":
                        if start_level == "base":
                            if arrow_pos == 1:
                                start_level = "new player"
                            if arrow_pos == 2:
                                start_level = "returning"
                        if start_level == "new player":
                            if arrow_pos == 2:
                                start_level = "base"   
                    if game_state == "paused":
                        if pause_level == "base":
                            if arrow_pos == 1:
                                pause_state = "enemies"
                            if arrow_pos == 2:
                                pause_state = "moves"
                            if arrow_pos == 3:
                                pause_state = "achievements"
                            if arrow_pos == 4:
                                game_state = "start"
                                start_level = "base"
                                arrow_pos = 1
                
                if event.key == pygame.K_x:
                    if game_state == "start":
                        if start_level == "new player" and arrow_pos == 2 or start_level == "returning":
                            start_level = "base"
                    if game_state == "paused":
                        if pause_level == "enemies" or pause_level == "moves" or pause_level == "achievements":
                            pause_level = "base"
                
                if event.key == pygame.K_ESCAPE:
                    if game_state == "active":
                        game_state = "paused"
                        pause_level = "base"
                        arrow_pos = 1
                    elif game_state == "paused":
                        game_state = "active"
                        pause_level = "base"
                        arrow_pos = 1
                if event.key == pygame.K_RETURN:
                    if start_level == "new player":
                            if arrow_pos == 1 and player_name != '':
                                game_state = "active"

                #Selection arrow movement
                if game_state == "paused" or game_state == "start":
                    if event.key == pygame.K_DOWN:
                        arrow_pos += 1
                    elif event.key == pygame.K_UP:
                        arrow_pos -= 1
                         
        key_pressed = pygame.key.get_pressed()

        WINDOW.blit(background, (0,0))
        
        #Keeping the selection arrow only on 
        if arrow_pos > arrow_limit:
            arrow_pos = 1
        elif arrow_pos <= 0:
            arrow_pos = arrow_limit

        #Checking to enable ultimate status
        if ultimate_charge >= 100:
            ultimate_status = True
        else: 
            ultimate_status = False

        if game_state == "start":
            #Blit start screen
            arrow_limit = start_screen(arrow_limit)

        elif game_state == "active":
            #Blit game ui 
            ui_blit(key_pressed)

            #Cooldown animation
            cooldown, cooldown_charge = on_cooldown(cooldown, cooldown_charge)
        
        elif game_state == "paused":
            #Blit pause screen
            arrow_limit = pause_screen(arrow_limit)
        
        CLOCK.tick(FRAME_RATE)
        pygame.display.update()