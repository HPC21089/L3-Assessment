"""Project: Level 3 Programming Asessment.

Author: Isaac Smith
School: Hauraki Plains College
Date: 03/06/2024
"""

# Imports
import pygame

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
cooldown = 0
ultimate_status = False
player_health = 100 #ENTIRELEY TEMP VARIABLE ONLY HERE 'TIL CLASSES
game_state = "active" #ENTIRELEY TEMP VARIABLE ONLY HERE 'TIL CLASSES
pause_level = 0
arrow_limit = 0
arrow_pos = 1
inputs = []
max_inputs = 4

def draw_text(text, font, color, x, y):
    text = font.render(text, True, color)
    WINDOW.blit(text, (x, y))

def utimate_charge(): 
    """Sets the sprite on screen to the amount of charge points the player is at"""
    if ultimate_charge == 0: # Named this way because the number it represents is the precentage of the charge
        ultimate_gauge = gauge_0 # ultimate_gauge is named this way because it represents the sprite of the actual gauge itself
    elif ultimate_charge > 0 and ultimate_charge <= 2:
        ultimate_gauge = uc_2
    elif ultimate_charge > 2 and ultimate_charge <= 4:
        ultimate_gauge = uc_4
    elif ultimate_charge > 4 and ultimate_charge <= 6:
        ultimate_gauge = uc_6
    elif ultimate_charge > 6 and ultimate_charge <= 8:
        ultimate_gauge = uc_8
    elif ultimate_charge > 8 and ultimate_charge <= 10:
        ultimate_gauge = uc_10
    elif ultimate_charge > 10 and ultimate_charge <= 12:
        ultimate_gauge = uc_12
    elif ultimate_charge > 12 and ultimate_charge <= 14:
        ultimate_gauge = uc_14
    elif ultimate_charge > 14 and ultimate_charge <= 16:
        ultimate_gauge = uc_16
    elif ultimate_charge > 16 and ultimate_charge <= 18:
        ultimate_gauge = uc_18
    elif ultimate_charge > 18 and ultimate_charge <= 20:
        ultimate_gauge = uc_20
    elif ultimate_charge > 20 and ultimate_charge <= 22:
        ultimate_gauge = uc_22
    elif ultimate_charge > 22 and ultimate_charge <= 24:
        ultimate_gauge = uc_24
    elif ultimate_charge > 24 and ultimate_charge <= 26:
        ultimate_gauge = uc_26
    elif ultimate_charge > 26 and ultimate_charge <= 28:
        ultimate_gauge = uc_28
    elif ultimate_charge > 28 and ultimate_charge <= 30:
        ultimate_gauge = uc_30
    elif ultimate_charge > 30 and ultimate_charge <= 32:
        ultimate_gauge = uc_32
    elif ultimate_charge > 32 and ultimate_charge <= 34:
        ultimate_gauge = uc_34
    elif ultimate_charge > 34 and ultimate_charge <= 36:
        ultimate_gauge = uc_36
    elif ultimate_charge > 36 and ultimate_charge <= 38:
        ultimate_gauge = uc_38
    elif ultimate_charge > 38 and ultimate_charge <= 40:
        ultimate_gauge = uc_40
    elif ultimate_charge > 40 and ultimate_charge <= 42:
        ultimate_gauge = uc_42
    elif ultimate_charge > 42 and ultimate_charge <= 44:
        ultimate_gauge = uc_44
    elif ultimate_charge > 44 and ultimate_charge <= 46:
        ultimate_gauge = uc_46
    elif ultimate_charge > 46 and ultimate_charge <= 48:
        ultimate_gauge = uc_48
    elif ultimate_charge > 48 and ultimate_charge <= 50:
        ultimate_gauge = uc_50
    elif ultimate_charge > 50 and ultimate_charge <= 52:
        ultimate_gauge = uc_52
    elif ultimate_charge > 52 and ultimate_charge <= 54:
        ultimate_gauge = uc_54
    elif ultimate_charge > 54 and ultimate_charge <= 56:
        ultimate_gauge = uc_56
    elif ultimate_charge > 56 and ultimate_charge <= 58:
        ultimate_gauge = uc_58
    elif ultimate_charge > 58 and ultimate_charge <= 60:
        ultimate_gauge = uc_60
    elif ultimate_charge > 60 and ultimate_charge <= 62:
        ultimate_gauge = uc_62
    elif ultimate_charge > 62 and ultimate_charge <= 64:
        ultimate_gauge = uc_64
    elif ultimate_charge > 64 and ultimate_charge <= 66:
        ultimate_gauge = uc_66
    elif ultimate_charge > 66 and ultimate_charge <= 68:
        ultimate_gauge = uc_68
    elif ultimate_charge > 68 and ultimate_charge <= 70:
        ultimate_gauge = uc_70
    elif ultimate_charge > 70 and ultimate_charge <= 72:
        ultimate_gauge = uc_72
    elif ultimate_charge > 72 and ultimate_charge <= 74:
        ultimate_gauge = uc_74
    elif ultimate_charge > 74 and ultimate_charge <= 76:
        ultimate_gauge = uc_76
    elif ultimate_charge > 76 and ultimate_charge <= 78:
        ultimate_gauge = uc_78
    elif ultimate_charge > 78 and ultimate_charge <= 80:
        ultimate_gauge = uc_80
    elif ultimate_charge > 80 and ultimate_charge <= 82:
        ultimate_gauge = uc_82
    elif ultimate_charge > 82 and ultimate_charge <= 84:
        ultimate_gauge = uc_84
    elif ultimate_charge > 84 and ultimate_charge <= 86:
        ultimate_gauge = uc_86
    elif ultimate_charge > 86 and ultimate_charge <= 88:
        ultimate_gauge = uc_88
    elif ultimate_charge > 88 and ultimate_charge <= 90:
        ultimate_gauge = uc_90
    elif ultimate_charge > 90 and ultimate_charge <= 92:
        ultimate_gauge = uc_92
    elif ultimate_charge > 92 and ultimate_charge <= 94:
        ultimate_gauge = uc_94
    elif ultimate_charge > 94 and ultimate_charge <= 96:
        ultimate_gauge = uc_96
    elif ultimate_charge > 96 and ultimate_charge <= 98:
        ultimate_gauge = uc_98
    elif ultimate_charge > 98 and ultimate_charge <= 100:
        ultimate_gauge = uc_100
        ultimate_status = True
    else:
        ultimate_gauge = gauge_0
    
    WINDOW.blit(ultimate_gauge, (75,600))

def cooldown_charge():
    """Sets the sprite on screen to show how long the payer has to wait until the next time they can input a move"""
    if cooldown == 0: # Named this way because the number it represents exactly how long is left in the cooldown
        cooldown_gauge = gauge_0 # cooldown_gauge is named this way because it represents the sprite of the actual gauge itself
    elif cooldown > 0 and cooldown <= 2:
        cooldown_gauge = c_2
    elif cooldown > 2 and cooldown <= 4:
        cooldown_gauge = c_4
    elif cooldown > 4 and cooldown <= 6:
        cooldown_gauge = c_6
    elif cooldown > 6 and cooldown <= 8:
        cooldown_gauge = c_8
    elif cooldown > 8 and cooldown <= 10:
        cooldown_gauge = c_10
    elif cooldown > 10 and cooldown <= 12:
        cooldown_gauge = c_12
    elif cooldown > 12 and cooldown <= 14:
        cooldown_gauge = c_14
    elif cooldown > 14 and cooldown <= 16:
        cooldown_gauge = c_16
    elif cooldown > 16 and cooldown <= 18:
        cooldown_gauge = c_18
    elif cooldown > 18 and cooldown <= 20:
        cooldown_gauge = c_20
    elif cooldown > 20 and cooldown <= 22:
        cooldown_gauge = c_22
    elif cooldown > 22 and cooldown <= 24:
        cooldown_gauge = c_24
    elif cooldown > 24 and cooldown <= 26:
        cooldown_gauge = c_26
    elif cooldown > 26 and cooldown <= 28:
        cooldown_gauge = c_28
    elif cooldown > 28 and cooldown <= 30:
        cooldown_gauge = c_30
    elif cooldown > 30 and cooldown <= 32:
        cooldown_gauge = c_32
    elif cooldown > 32 and cooldown <= 34:
        cooldown_gauge = c_34
    elif cooldown > 34 and cooldown <= 36:
        cooldown_gauge = c_36
    elif cooldown > 36 and cooldown <= 38:
        cooldown_gauge = c_38
    elif cooldown > 38 and cooldown <= 40:
        cooldown_gauge = c_40
    elif cooldown > 40 and cooldown <= 42:
        cooldown_gauge = c_42
    elif cooldown > 42 and cooldown <= 44:
        cooldown_gauge = c_44
    elif cooldown > 44 and cooldown <= 46:
        cooldown_gauge = c_46
    elif cooldown > 46 and cooldown <= 48:
        cooldown_gauge = c_48
    elif cooldown > 48 and cooldown <= 50:
        cooldown_gauge = c_50
    elif cooldown > 50 and cooldown <= 52:
        cooldown_gauge = c_52
    elif cooldown > 52 and cooldown <= 54:
        cooldown_gauge = c_54
    elif cooldown > 54 and cooldown <= 56:
        cooldown_gauge = c_56
    elif cooldown > 56 and cooldown <= 58:
        cooldown_gauge = c_58
    elif cooldown > 58 and cooldown <= 60:
        cooldown_gauge = c_60
    elif cooldown > 60 and cooldown <= 62:
        cooldown_gauge = c_62
    elif cooldown > 62 and cooldown <= 64:
        cooldown_gauge = c_64
    elif cooldown > 64 and cooldown <= 66:
        cooldown_gauge = c_66
    elif cooldown > 66 and cooldown <= 68:
        cooldown_gauge = c_68
    elif cooldown > 68 and cooldown <= 70:
        cooldown_gauge = c_70
    elif cooldown > 70 and cooldown <= 72:
        cooldown_gauge = c_72
    elif cooldown > 72 and cooldown <= 74:
        cooldown_gauge = c_74
    elif cooldown > 74 and cooldown <= 76:
        cooldown_gauge = c_76
    elif cooldown > 76 and cooldown <= 78:
        cooldown_gauge = c_78
    elif cooldown > 78 and cooldown <= 80:
        cooldown_gauge = c_80
    elif cooldown > 80 and cooldown <= 82:
        cooldown_gauge = c_82
    elif cooldown > 82 and cooldown <= 84:
        cooldown_gauge = c_84
    elif cooldown > 84 and cooldown <= 86:
        cooldown_gauge = c_86
    elif cooldown > 86 and cooldown <= 88:
        cooldown_gauge = c_88
    elif cooldown > 88 and cooldown <= 90:
        cooldown_gauge = c_90
    elif cooldown > 90 and cooldown <= 92:
        cooldown_gauge = c_92
    elif cooldown > 92 and cooldown <= 94:
        cooldown_gauge = c_94
    elif cooldown > 94 and cooldown <= 96:
        cooldown_gauge = c_96
    elif cooldown > 96 and cooldown <= 98:
        cooldown_gauge = c_98
    elif cooldown > 98 and cooldown <= 100:
        cooldown_gauge = c_100
    else:
        cooldown_gauge = gauge_0

    WINDOW.blit(cooldown_gauge, (935,600))

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

def player_health_sprite():
    #YOU ARE GONNA HAVE TO CHANGE THE PLAYER HEALTH VARIABLES WHEN YOU ADD CLASSES
    if player_health == 0:
        health_bar = hb_empty
    elif player_health > 0 and player_health <= 4:
        health_bar = hb_4
    elif player_health > 4 and player_health <= 8:
        health_bar = hb_8
    elif player_health > 8 and player_health <= 12:
        health_bar = hb_12
    elif player_health > 12 and player_health <= 16:
        health_bar = hb_16
    elif player_health > 16 and player_health <= 20:
        health_bar = hb_20
    elif player_health > 20 and player_health <= 24:
        health_bar = hb_24
    elif player_health > 24 and player_health <= 28:
        health_bar = hb_28
    elif player_health > 28 and player_health <= 32:
        health_bar = hb_32
    elif player_health > 32 and player_health <= 36:
        health_bar = hb_36
    elif player_health > 36 and player_health <= 40:
        health_bar = hb_40
    elif player_health > 40 and player_health <= 44:
        health_bar = hb_44
    elif player_health > 44 and player_health <= 48:
        health_bar = hb_48
    elif player_health > 48 and player_health <= 52:
        health_bar = hb_52
    elif player_health > 52 and player_health <= 56:
        health_bar = hb_56
    elif player_health > 56 and player_health <= 60:
        health_bar = hb_60
    elif player_health > 60 and player_health <= 64:
        health_bar = hb_64
    elif player_health > 64 and player_health <= 68:
        health_bar = hb_68
    elif player_health > 68 and player_health <= 72:
        health_bar = hb_72
    elif player_health > 72 and player_health <= 76:
        health_bar = hb_76
    elif player_health > 76 and player_health <= 80:
        health_bar = hb_80
    elif player_health > 80 and player_health <= 84:
        health_bar = hb_84
    elif player_health > 84 and player_health <= 88:
        health_bar = hb_88
    elif player_health > 88 and player_health <= 92:
        health_bar = hb_92
    elif player_health > 92 and player_health <= 96:
        health_bar = hb_96
    elif player_health > 96 and player_health <= 100:
        health_bar = hb_100
    else:
        health_bar = hb_100
    
    WINDOW.blit(health_bar, (1125,30))

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

    #Esc to pause
    WINDOW.blit(esc_bg, (25, 25))
    draw_text("esc", font_small, BLACK, 31, 35)
    draw_text("to pause", font_small, WHITE, 70, 35)

    #-----Gauges-----
    utimate_charge()
    cooldown_charge()

    #Gauge titles
    draw_text("Ultimate Charge", font_small, WHITE, 142.5, 575)
    draw_text("Cooldown", font_small, WHITE, 1027.5, 575)

    #-----Arrows-----
    arrows_functionality()

    #-----Health Bar-----
    player_health_sprite()
        
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

    if pause_level == 1:
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

#Loading background
background = pygame.transform.scale_by(pygame.image.load('images/DDDZA-Background.png'), 5)

#-----Loading the gauge sprites----
gauge_0 = pygame.transform.scale_by(pygame.image.load('images/gauges/Gauge-0%.png'), 5)

#Ultimate Charge sprites (abbreviated with 'uc')
uc_2 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-2%.png'), 5)
uc_4 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-4%.png'), 5)
uc_6 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-6%.png'), 5)
uc_8 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-8%.png'), 5)
uc_10 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-10%.png'), 5)
uc_12 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-12%.png'), 5)
uc_14 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-14%.png'), 5)
uc_16 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-16%.png'), 5)
uc_18 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-18%.png'), 5)
uc_20 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-20%.png'), 5)
uc_22 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-22%.png'), 5)
uc_24 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-24%.png'), 5)
uc_26 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-26%.png'), 5)
uc_28 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-28%.png'), 5)
uc_30 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-30%.png'), 5)
uc_32 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-32%.png'), 5)
uc_34 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-34%.png'), 5)
uc_36 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-36%.png'), 5)
uc_38 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-38%.png'), 5)
uc_40 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-40%.png'), 5)
uc_42 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-42%.png'), 5)
uc_44 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-44%.png'), 5)
uc_46 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-46%.png'), 5)
uc_48 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-48%.png'), 5)
uc_50 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-50%.png'), 5)
uc_52 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-52%.png'), 5)
uc_54 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-54%.png'), 5)
uc_56 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-56%.png'), 5)
uc_58 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-58%.png'), 5)
uc_60 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-60%.png'), 5)
uc_62 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-62%.png'), 5)
uc_64 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-64%.png'), 5)
uc_66 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-66%.png'), 5)
uc_68 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-68%.png'), 5)
uc_70 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-70%.png'), 5)
uc_72 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-72%.png'), 5)
uc_74 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-74%.png'), 5)
uc_76 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-76%.png'), 5)
uc_78 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-78%.png'), 5)
uc_80 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-80%.png'), 5)
uc_82 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-82%.png'), 5)
uc_84 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-84%.png'), 5)
uc_86 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-86%.png'), 5)
uc_88 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-88%.png'), 5)
uc_90 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-90%.png'), 5)
uc_92 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-92%.png'), 5)
uc_94 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-94%.png'), 5)
uc_96 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-96%.png'), 5)
uc_98 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-98%.png'), 5)
uc_100 = pygame.transform.scale_by(pygame.image.load('images/gauges/ultimate-charge/UC-100%.png'), 5)

#Cooldown sprites (abbreviated with 'c')
c_2 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-2%.png'), 5)
c_4 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-4%.png'), 5)
c_6 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-6%.png'), 5)
c_8 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-8%.png'), 5)
c_10 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-10%.png'), 5)
c_12 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-12%.png'), 5)
c_14 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-14%.png'), 5)
c_16 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-16%.png'), 5)
c_18 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-18%.png'), 5)
c_20 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-20%.png'), 5)
c_22 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-22%.png'), 5)
c_24 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-24%.png'), 5)
c_26 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-26%.png'), 5)
c_28 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-28%.png'), 5)
c_30 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-30%.png'), 5)
c_32 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-32%.png'), 5)
c_34 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-34%.png'), 5)
c_36 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-36%.png'), 5)
c_38 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-38%.png'), 5)
c_40 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-40%.png'), 5)
c_42 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-42%.png'), 5)
c_44 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-44%.png'), 5)
c_46 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-46%.png'), 5)
c_48 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-48%.png'), 5)
c_50 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-50%.png'), 5)
c_52 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-52%.png'), 5)
c_54 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-54%.png'), 5)
c_56 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-56%.png'), 5)
c_58 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-58%.png'), 5)
c_60 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-60%.png'), 5)
c_62 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-62%.png'), 5)
c_64 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-64%.png'), 5)
c_66 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-66%.png'), 5)
c_68 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-68%.png'), 5)
c_70 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-70%.png'), 5)
c_72 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-72%.png'), 5)
c_74 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-74%.png'), 5)
c_76 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-76%.png'), 5)
c_78 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-78%.png'), 5)
c_80 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-80%.png'), 5)
c_82 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-82%.png'), 5)
c_84 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-84%.png'), 5)
c_86 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-86%.png'), 5)
c_88 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-88%.png'), 5)
c_90 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-90%.png'), 5)
c_92 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-92%.png'), 5)
c_94 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-94%.png'), 5)
c_96 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-96%.png'), 5)
c_98 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-98%.png'), 5)
c_100 = pygame.transform.scale_by(pygame.image.load('images/gauges/cooldown/C-100%.png'), 5)

#Loading arrows
up_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/up-arrow.png'), 5)
up_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/up-arrow-pressed.png'), 5)
down_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/down-arrow.png'), 5)
down_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/down-arrow-pressed.png'), 5)
left_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/left-arrow.png'), 5)
left_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/left-arrow-pressed.png'), 5)
right_arrow_base = pygame.transform.scale_by(pygame.image.load('images/arrows/right-arrow.png'), 5)
right_arrow_pressed = pygame.transform.scale_by(pygame.image.load('images/arrows/right-arrow-pressed.png'), 5)

#Loading in health bar (abbreviated to HB)
hb_4 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-4%.png'), 5)
hb_8 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-8%.png'), 5)
hb_12 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-12%.png'), 5)
hb_16 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-16%.png'), 5)
hb_20 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-20%.png'), 5)
hb_24 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-24%.png'), 5)
hb_28 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-28%.png'), 5)
hb_32 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-32%.png'), 5)
hb_36 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-36%.png'), 5)
hb_40 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-40%.png'), 5)
hb_44 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-44%.png'), 5)
hb_48 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-48%.png'), 5)
hb_52 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-52%.png'), 5)
hb_56 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-56%.png'), 5)
hb_60 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-60%.png'), 5)
hb_64 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-64%.png'), 5)
hb_68 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-68%.png'), 5)
hb_72 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-72%.png'), 5)
hb_76 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-76%.png'), 5)
hb_80 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-80%.png'), 5)
hb_84 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-84%.png'), 5)
hb_88 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-88%.png'), 5)
hb_92 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-92%.png'), 5)
hb_96 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-96%.png'), 5)
hb_100 = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-100%.png'), 5)
hb_empty = pygame.transform.scale_by(pygame.image.load('images/health bar/HB-Empty.png'), 5)

#Loading Escape Image
esc_bg = pygame.transform.scale_by(pygame.image.load('images/esc.png'), 5)

#Loading Selection Arrow
selection_arrow = pygame.transform.scale_by(pygame.image.load('images/arrow.png'), 5)

#Game loop
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    #Setting the switch for changing game states + resetting variables
                    if game_state == "active":
                        game_state = "paused"
                        pause_level = 1
                        arrow_pos = 1
                    elif game_state == "paused":
                        game_state = "active"
                        pause_level = 0
                        arrow_pos = 1

            if game_state == "paused":
                #Selection arrow movement
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        arrow_pos += 1
                    elif event.key == pygame.K_UP:
                        arrow_pos -= 1

            if game_state == "active":
                #Combo input tracking
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        inputs.append('left')
                    if event.key == pygame.K_RIGHT:
                        inputs.append('right')
                    if event.key == pygame.K_UP:
                        inputs.append('up')
                    if event.key == pygame.K_DOWN:
                        inputs.append('down')
                
                #Limits the number of recorded inpits at a time to 0
                if len(inputs) > max_inputs:
                    inputs.pop(0)
                    
        key_pressed = pygame.key.get_pressed()

        WINDOW.blit(background, (0,0))

        if game_state == "active":
            ui_blit(key_pressed)  
        elif game_state == "paused":   
            arrow_limit = pause_screen(arrow_limit)
            if arrow_pos > arrow_limit:
                arrow_pos = arrow_limit
            elif arrow_pos <= 0:
                arrow_pos = 1
        
        print(inputs)

        CLOCK.tick(FRAME_RATE)
        pygame.display.update()