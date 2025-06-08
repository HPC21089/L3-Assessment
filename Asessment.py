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
font = pygame.font.SysFont('freedom-font - Shortcut.lnk', 35)
WHITE = (255, 255, 255)
wave_num = 0
enemies_left = 100 #Temporary for now just to set up UI
ultimate_charge = 0
cooldown = 0

def draw_text(text, font, color, x, y):
    text = font.render(text, True, color)
    WINDOW.blit(text, (x, y))

def utimate_charge(): 
    """Sets the sprite on screen to the amount of charge points the player is at"""
    if ultimate_charge == 0: # Named this way because the number it represents is the precentage of the charge
        ultimate_gauge = gauge_0 # ultimate_gauge is named this way because it represents the sprite of the actual gauge itself
    elif ultimate_charge == 2:
        ultimate_gauge = uc_2
    elif ultimate_charge == 4:
        ultimate_gauge = uc_4
    elif ultimate_charge == 6:
        ultimate_gauge = uc_6
    elif ultimate_charge == 8:
        ultimate_gauge = uc_8
    elif ultimate_charge == 10:
        ultimate_gauge = uc_10
    elif ultimate_charge == 12:
        ultimate_gauge = uc_12
    elif ultimate_charge == 14:
        ultimate_gauge = uc_14
    elif ultimate_charge == 16:
        ultimate_gauge = uc_16
    elif ultimate_charge == 18:
        ultimate_gauge = uc_18
    elif ultimate_charge == 20:
        ultimate_gauge = uc_20
    elif ultimate_charge == 22:
        ultimate_gauge = uc_22
    elif ultimate_charge == 24:
        ultimate_gauge = uc_24
    elif ultimate_charge == 26:
        ultimate_gauge = uc_26
    elif ultimate_charge == 28:
        ultimate_gauge = uc_28
    elif ultimate_charge == 30:
        ultimate_gauge = uc_30
    elif ultimate_charge == 32:
        ultimate_gauge = uc_32
    elif ultimate_charge == 34:
        ultimate_gauge = uc_34
    elif ultimate_charge == 36:
        ultimate_gauge = uc_36
    elif ultimate_charge == 38:
        ultimate_gauge = uc_38
    elif ultimate_charge == 40:
        ultimate_gauge = uc_40
    elif ultimate_charge == 42:
        ultimate_gauge = uc_42
    elif ultimate_charge == 44:
        ultimate_gauge = uc_44
    elif ultimate_charge == 46:
        ultimate_gauge = uc_46
    elif ultimate_charge == 48:
        ultimate_gauge = uc_48
    elif ultimate_charge == 50:
        ultimate_gauge = uc_50
    elif ultimate_charge == 52:
        ultimate_gauge = uc_52
    elif ultimate_charge == 54:
        ultimate_gauge = uc_54
    elif ultimate_charge == 56:
        ultimate_gauge = uc_56
    elif ultimate_charge == 58:
        ultimate_gauge = uc_58
    elif ultimate_charge == 60:
        ultimate_gauge = uc_60
    elif ultimate_charge == 62:
        ultimate_gauge = uc_62
    elif ultimate_charge == 64:
        ultimate_gauge = uc_64
    elif ultimate_charge == 66:
        ultimate_gauge = uc_66
    elif ultimate_charge == 68:
        ultimate_gauge = uc_68
    elif ultimate_charge == 70:
        ultimate_gauge = uc_70
    elif ultimate_charge == 72:
        ultimate_gauge = uc_72
    elif ultimate_charge == 74:
        ultimate_gauge = uc_74
    elif ultimate_charge == 76:
        ultimate_gauge = uc_76
    elif ultimate_charge == 78:
        ultimate_gauge = uc_78
    elif ultimate_charge == 80:
        ultimate_gauge = uc_80
    elif ultimate_charge == 82:
        ultimate_gauge = uc_82
    elif ultimate_charge == 84:
        ultimate_gauge = uc_84
    elif ultimate_charge == 86:
        ultimate_gauge = uc_86
    elif ultimate_charge == 88:
        ultimate_gauge = uc_88
    elif ultimate_charge == 90:
        ultimate_gauge = uc_90
    elif ultimate_charge == 92:
        ultimate_gauge = uc_92
    elif ultimate_charge == 94:
        ultimate_gauge = uc_94
    elif ultimate_charge == 96:
        ultimate_gauge = uc_96
    elif ultimate_charge == 98:
        ultimate_gauge = uc_98
    elif ultimate_charge == 100:
        ultimate_gauge = uc_100
    else:
        ultimate_gauge = gauge_0
    
    WINDOW.blit(ultimate_gauge, (75,600))

def cooldown_charge():
    """Sets the sprite on screen to show how long the payer has to wait until the next time they can input a move"""
    if cooldown == 0: # Named this way because the number it represents exactly how long is left in the cooldown
        cooldown_gauge = gauge_0 # cooldown_gauge is named this way because it represents the sprite of the actual gauge itself
    elif cooldown == 2:
        cooldown_gauge = c_2
    elif cooldown == 4:
        cooldown_gauge = c_4
    elif cooldown == 6:
        cooldown_gauge = c_6
    elif cooldown == 8:
        cooldown_gauge = c_8
    elif cooldown == 10:
        cooldown_gauge = c_10
    elif cooldown == 12:
        cooldown_gauge = c_12
    elif cooldown == 14:
        cooldown_gauge = c_14
    elif cooldown == 16:
        cooldown_gauge = c_16
    elif cooldown == 18:
        cooldown_gauge = c_18
    elif cooldown == 20:
        cooldown_gauge = c_20
    elif cooldown == 22:
        cooldown_gauge = c_22
    elif cooldown == 24:
        cooldown_gauge = c_24
    elif cooldown == 26:
        cooldown_gauge = c_26
    elif cooldown == 28:
        cooldown_gauge = c_28
    elif cooldown == 30:
        cooldown_gauge = c_30
    elif cooldown == 32:
        cooldown_gauge = c_32
    elif cooldown == 34:
        cooldown_gauge = c_34
    elif cooldown == 36:
        cooldown_gauge = c_36
    elif cooldown == 38:
        cooldown_gauge = c_38
    elif cooldown == 40:
        cooldown_gauge = c_40
    elif cooldown == 42:
        cooldown_gauge = c_42
    elif cooldown == 44:
        cooldown_gauge = c_44
    elif cooldown == 46:
        cooldown_gauge = c_46
    elif cooldown == 48:
        cooldown_gauge = c_48
    elif cooldown == 50:
        cooldown_gauge = c_50
    elif cooldown == 52:
        cooldown_gauge = c_52
    elif cooldown == 54:
        cooldown_gauge = c_54
    elif cooldown == 56:
        cooldown_gauge = c_56
    elif cooldown == 58:
        cooldown_gauge = c_58
    elif cooldown == 60:
        cooldown_gauge = c_60
    elif cooldown == 62:
        cooldown_gauge = c_62
    elif cooldown == 64:
        cooldown_gauge = c_64
    elif cooldown == 66:
        cooldown_gauge = c_66
    elif cooldown == 68:
        cooldown_gauge = c_68
    elif cooldown == 70:
        cooldown_gauge = c_70
    elif cooldown == 72:
        cooldown_gauge = c_72
    elif cooldown == 74:
        cooldown_gauge = c_74
    elif cooldown == 76:
        cooldown_gauge = c_76
    elif cooldown == 78:
        cooldown_gauge = c_78
    elif cooldown == 80:
        cooldown_gauge = c_80
    elif cooldown == 82:
        cooldown_gauge = c_82
    elif cooldown == 84:
        cooldown_gauge = c_84
    elif cooldown == 86:
        cooldown_gauge = c_86
    elif cooldown == 88:
        cooldown_gauge = c_88
    elif cooldown == 90:
        cooldown_gauge = c_90
    elif cooldown == 92:
        cooldown_gauge = c_92
    elif cooldown == 94:
        cooldown_gauge = c_94
    elif cooldown == 96:
        cooldown_gauge = c_96
    elif cooldown == 98:
        cooldown_gauge = c_98
    elif cooldown == 100:
        cooldown_gauge = c_100
    else:
        cooldown_gauge = gauge_0

    WINDOW.blit(cooldown_gauge, (935,600))

def ui_blit():
    """Displays all parts of the base game UI"""
    # -----Display text-----
    #Wave number
    if wave_num <= 9:
        draw_text("Wave: " + str(wave_num), font, WHITE, 595, 10)
    elif wave_num <= 99:
        draw_text("Wave: " + str(wave_num), font, WHITE, 595, 10) #CHANGE X POS FOR SPACING, 2 didgits
    
    #Enemies left
    if enemies_left <= 999:
        draw_text("Enemies Left: " + str(enemies_left), font, WHITE, 545, 687)
    elif enemies_left <= 99:
        draw_text("Enemies Left: " + str(enemies_left), font, WHITE, 545, 687) #CHANGE X POS FOR SPACING, 2 didgits
    elif enemies_left <= 9:
        draw_text("Enemies Left: " + str(enemies_left), font, WHITE, 545, 687) #CHANGE X POS FOR SPACING, single digit

    #-----Gauges-----
    utimate_charge()

    cooldown_charge()

#Loadning background
background = pygame.image.load('images/DDDZA-Background.png')
background = pygame.transform.scale_by(background, 5)

#-----Loading the gauge sprites----
gauge_0 = pygame.image.load('images/gauges/Gauge-0%.png')
gauge_0 = pygame.transform.scale_by(gauge_0, 5)

#Ultimate Charge sprites (abbreviated with 'uc')
uc_2 = pygame.image.load('images/gauges/ultimate-charge/UC-2%.png')
uc_2 = pygame.transform.scale_by(uc_2, 5)
uc_4 = pygame.image.load('images/gauges/ultimate-charge/UC-4%.png')
uc_4 = pygame.transform.scale_by(uc_4, 5)
uc_6 = pygame.image.load('images/gauges/ultimate-charge/UC-6%.png')
uc_6 = pygame.transform.scale_by(uc_6, 5)
uc_8 = pygame.image.load('images/gauges/ultimate-charge/UC-8%.png')
uc_8 = pygame.transform.scale_by(uc_8, 5)
uc_10 = pygame.image.load('images/gauges/ultimate-charge/UC-10%.png')
uc_10 = pygame.transform.scale_by(uc_10, 5)
uc_12 = pygame.image.load('images/gauges/ultimate-charge/UC-12%.png')
uc_12 = pygame.transform.scale_by(uc_12, 5)
uc_14 = pygame.image.load('images/gauges/ultimate-charge/UC-14%.png')
uc_14 = pygame.transform.scale_by(uc_14, 5)
uc_16 = pygame.image.load('images/gauges/ultimate-charge/UC-16%.png')
uc_16 = pygame.transform.scale_by(uc_16, 5)
uc_18 = pygame.image.load('images/gauges/ultimate-charge/UC-18%.png')
uc_18 = pygame.transform.scale_by(uc_18, 5)
uc_20 = pygame.image.load('images/gauges/ultimate-charge/UC-20%.png')
uc_20 = pygame.transform.scale_by(uc_20, 5)
uc_22 = pygame.image.load('images/gauges/ultimate-charge/UC-22%.png')
uc_22 = pygame.transform.scale_by(uc_22, 5)
uc_24 = pygame.image.load('images/gauges/ultimate-charge/UC-24%.png')
uc_24 = pygame.transform.scale_by(uc_24, 5)
uc_26 = pygame.image.load('images/gauges/ultimate-charge/UC-26%.png')
uc_26 = pygame.transform.scale_by(uc_26, 5)
uc_28 = pygame.image.load('images/gauges/ultimate-charge/UC-28%.png')
uc_28 = pygame.transform.scale_by(uc_28, 5)
uc_30 = pygame.image.load('images/gauges/ultimate-charge/UC-30%.png')
uc_30 = pygame.transform.scale_by(uc_30, 5)
uc_32 = pygame.image.load('images/gauges/ultimate-charge/UC-32%.png')
uc_32 = pygame.transform.scale_by(uc_32, 5)
uc_34 = pygame.image.load('images/gauges/ultimate-charge/UC-34%.png')
uc_34 = pygame.transform.scale_by(uc_34, 5)
uc_36 = pygame.image.load('images/gauges/ultimate-charge/UC-36%.png')
uc_36 = pygame.transform.scale_by(uc_36, 5)
uc_38 = pygame.image.load('images/gauges/ultimate-charge/UC-38%.png')
uc_38 = pygame.transform.scale_by(uc_38, 5)
uc_40 = pygame.image.load('images/gauges/ultimate-charge/UC-40%.png')
uc_40 = pygame.transform.scale_by(uc_40, 5)
uc_42 = pygame.image.load('images/gauges/ultimate-charge/UC-42%.png')
uc_42 = pygame.transform.scale_by(uc_42, 5)
uc_44 = pygame.image.load('images/gauges/ultimate-charge/UC-44%.png')
uc_44 = pygame.transform.scale_by(uc_44, 5)
uc_46 = pygame.image.load('images/gauges/ultimate-charge/UC-46%.png')
uc_46 = pygame.transform.scale_by(uc_46, 5)
uc_48 = pygame.image.load('images/gauges/ultimate-charge/UC-48%.png')
uc_48 = pygame.transform.scale_by(uc_48, 5)
uc_50 = pygame.image.load('images/gauges/ultimate-charge/UC-50%.png')
uc_50 = pygame.transform.scale_by(uc_50, 5)
uc_52 = pygame.image.load('images/gauges/ultimate-charge/UC-52%.png')
uc_52 = pygame.transform.scale_by(uc_52, 5)
uc_54 = pygame.image.load('images/gauges/ultimate-charge/UC-54%.png')
uc_54 = pygame.transform.scale_by(uc_54, 5)
uc_56 = pygame.image.load('images/gauges/ultimate-charge/UC-56%.png')
uc_56 = pygame.transform.scale_by(uc_56, 5)
uc_58 = pygame.image.load('images/gauges/ultimate-charge/UC-58%.png')
uc_58 = pygame.transform.scale_by(uc_58, 5)
uc_60 = pygame.image.load('images/gauges/ultimate-charge/UC-60%.png')
uc_60 = pygame.transform.scale_by(uc_60, 5)
uc_62 = pygame.image.load('images/gauges/ultimate-charge/UC-62%.png')
uc_62 = pygame.transform.scale_by(uc_62, 5)
uc_64 = pygame.image.load('images/gauges/ultimate-charge/UC-64%.png')
uc_64 = pygame.transform.scale_by(uc_64, 5)
uc_66 = pygame.image.load('images/gauges/ultimate-charge/UC-66%.png')
uc_66 = pygame.transform.scale_by(uc_66, 5)
uc_68 = pygame.image.load('images/gauges/ultimate-charge/UC-68%.png')
uc_68 = pygame.transform.scale_by(uc_68, 5)
uc_70 = pygame.image.load('images/gauges/ultimate-charge/UC-70%.png')
uc_70 = pygame.transform.scale_by(uc_70, 5)
uc_72 = pygame.image.load('images/gauges/ultimate-charge/UC-72%.png')
uc_72 = pygame.transform.scale_by(uc_72, 5)
uc_74 = pygame.image.load('images/gauges/ultimate-charge/UC-74%.png')
uc_74 = pygame.transform.scale_by(uc_74, 5)
uc_76 = pygame.image.load('images/gauges/ultimate-charge/UC-76%.png')
uc_76 = pygame.transform.scale_by(uc_76, 5)
uc_78 = pygame.image.load('images/gauges/ultimate-charge/UC-78%.png')
uc_78 = pygame.transform.scale_by(uc_78, 5)
uc_80 = pygame.image.load('images/gauges/ultimate-charge/UC-80%.png')
uc_80 = pygame.transform.scale_by(uc_80, 5)
uc_82 = pygame.image.load('images/gauges/ultimate-charge/UC-82%.png')
uc_82 = pygame.transform.scale_by(uc_82, 5)
uc_84 = pygame.image.load('images/gauges/ultimate-charge/UC-84%.png')
uc_84 = pygame.transform.scale_by(uc_84, 5)
uc_86 = pygame.image.load('images/gauges/ultimate-charge/UC-86%.png')
uc_86 = pygame.transform.scale_by(uc_86, 5)
uc_88 = pygame.image.load('images/gauges/ultimate-charge/UC-88%.png')
uc_88 = pygame.transform.scale_by(uc_88, 5)
uc_90 = pygame.image.load('images/gauges/ultimate-charge/UC-90%.png')
uc_90 = pygame.transform.scale_by(uc_90, 5)
uc_92 = pygame.image.load('images/gauges/ultimate-charge/UC-92%.png')
uc_92 = pygame.transform.scale_by(uc_92, 5)
uc_94 = pygame.image.load('images/gauges/ultimate-charge/UC-94%.png')
uc_94 = pygame.transform.scale_by(uc_94, 5)
uc_96 = pygame.image.load('images/gauges/ultimate-charge/UC-96%.png')
uc_96 = pygame.transform.scale_by(uc_96, 5)
uc_98 = pygame.image.load('images/gauges/ultimate-charge/UC-98%.png')
uc_98 = pygame.transform.scale_by(uc_98, 5)
uc_100 = pygame.image.load('images/gauges/ultimate-charge/UC-100%.png')
uc_100 = pygame.transform.scale_by(uc_100, 5)

#Cooldown sprites (abbreviated with 'c')
c_2 = pygame.image.load('images/gauges/cooldown/C-2%.png')
c_2 = pygame.transform.scale_by(c_2, 5)
c_4 = pygame.image.load('images/gauges/cooldown/C-4%.png')
c_4 = pygame.transform.scale_by(c_4, 5)
c_6 = pygame.image.load('images/gauges/cooldown/C-6%.png')
c_6 = pygame.transform.scale_by(c_6, 5)
c_8 = pygame.image.load('images/gauges/cooldown/C-8%.png')
c_8 = pygame.transform.scale_by(c_8, 5)
c_10 = pygame.image.load('images/gauges/cooldown/C-10%.png')
c_10 = pygame.transform.scale_by(c_10, 5)
c_12 = pygame.image.load('images/gauges/cooldown/C-12%.png')
c_12 = pygame.transform.scale_by(c_12, 5)
c_14 = pygame.image.load('images/gauges/cooldown/C-14%.png')
c_14 = pygame.transform.scale_by(c_14, 5)
c_16 = pygame.image.load('images/gauges/cooldown/C-16%.png')
c_16 = pygame.transform.scale_by(c_16, 5)
c_18 = pygame.image.load('images/gauges/cooldown/C-18%.png')
c_18 = pygame.transform.scale_by(c_18, 5)
c_20 = pygame.image.load('images/gauges/cooldown/C-20%.png')
c_20 = pygame.transform.scale_by(c_20, 5)
c_22 = pygame.image.load('images/gauges/cooldown/C-22%.png')
c_22 = pygame.transform.scale_by(c_22, 5)
c_24 = pygame.image.load('images/gauges/cooldown/C-24%.png')
c_24 = pygame.transform.scale_by(c_24, 5)
c_26 = pygame.image.load('images/gauges/cooldown/C-26%.png')
c_26 = pygame.transform.scale_by(c_26, 5)
c_28 = pygame.image.load('images/gauges/cooldown/C-28%.png')
c_28 = pygame.transform.scale_by(c_28, 5)
c_30 = pygame.image.load('images/gauges/cooldown/C-30%.png')
c_30 = pygame.transform.scale_by(c_30, 5)
c_32 = pygame.image.load('images/gauges/cooldown/C-32%.png')
c_32 = pygame.transform.scale_by(c_32, 5)
c_34 = pygame.image.load('images/gauges/cooldown/C-34%.png')
c_34 = pygame.transform.scale_by(c_34, 5)
c_36 = pygame.image.load('images/gauges/cooldown/C-36%.png')
c_36 = pygame.transform.scale_by(c_36, 5)
c_38 = pygame.image.load('images/gauges/cooldown/C-38%.png')
c_38 = pygame.transform.scale_by(c_38, 5)
c_40 = pygame.image.load('images/gauges/cooldown/C-40%.png')
c_40 = pygame.transform.scale_by(c_40, 5)
c_42 = pygame.image.load('images/gauges/cooldown/C-42%.png')
c_42 = pygame.transform.scale_by(c_42, 5)
c_44 = pygame.image.load('images/gauges/cooldown/C-44%.png')
c_44 = pygame.transform.scale_by(c_44, 5)
c_46 = pygame.image.load('images/gauges/cooldown/C-46%.png')
c_46 = pygame.transform.scale_by(c_46, 5)
c_48 = pygame.image.load('images/gauges/cooldown/C-48%.png')
c_48 = pygame.transform.scale_by(c_48, 5)
c_50 = pygame.image.load('images/gauges/cooldown/C-50%.png')
c_50 = pygame.transform.scale_by(c_50, 5)
c_52 = pygame.image.load('images/gauges/cooldown/C-52%.png')
c_52 = pygame.transform.scale_by(c_52, 5)
c_54 = pygame.image.load('images/gauges/cooldown/C-54%.png')
c_54 = pygame.transform.scale_by(c_54, 5)
c_56 = pygame.image.load('images/gauges/cooldown/C-56%.png')
c_56 = pygame.transform.scale_by(c_56, 5)
c_58 = pygame.image.load('images/gauges/cooldown/C-58%.png')
c_58 = pygame.transform.scale_by(c_58, 5)
c_60 = pygame.image.load('images/gauges/cooldown/C-60%.png')
c_60 = pygame.transform.scale_by(c_60, 5)
c_62 = pygame.image.load('images/gauges/cooldown/C-62%.png')
c_62 = pygame.transform.scale_by(c_62, 5)
c_64 = pygame.image.load('images/gauges/cooldown/C-64%.png')
c_64 = pygame.transform.scale_by(c_64, 5)
c_66 = pygame.image.load('images/gauges/cooldown/C-66%.png')
c_66 = pygame.transform.scale_by(c_66, 5)
c_68 = pygame.image.load('images/gauges/cooldown/C-68%.png')
c_68 = pygame.transform.scale_by(c_68, 5)
c_70 = pygame.image.load('images/gauges/cooldown/C-70%.png')
c_70 = pygame.transform.scale_by(c_70, 5)
c_72 = pygame.image.load('images/gauges/cooldown/C-72%.png')
c_72 = pygame.transform.scale_by(c_72, 5)
c_74 = pygame.image.load('images/gauges/cooldown/C-74%.png')
c_74 = pygame.transform.scale_by(c_74, 5)
c_76 = pygame.image.load('images/gauges/cooldown/C-76%.png')
c_76 = pygame.transform.scale_by(c_76, 5)
c_78 = pygame.image.load('images/gauges/cooldown/C-78%.png')
c_78 = pygame.transform.scale_by(c_78, 5)
c_80 = pygame.image.load('images/gauges/cooldown/C-80%.png')
c_80 = pygame.transform.scale_by(c_80, 5)
c_82 = pygame.image.load('images/gauges/cooldown/C-82%.png')
c_82 = pygame.transform.scale_by(c_82, 5)
c_84 = pygame.image.load('images/gauges/cooldown/C-84%.png')
c_84 = pygame.transform.scale_by(c_84, 5)
c_86 = pygame.image.load('images/gauges/cooldown/C-86%.png')
c_86 = pygame.transform.scale_by(c_86, 5)
c_88 = pygame.image.load('images/gauges/cooldown/C-88%.png')
c_88 = pygame.transform.scale_by(c_88, 5)
c_90 = pygame.image.load('images/gauges/cooldown/C-90%.png')
c_90 = pygame.transform.scale_by(c_90, 5)
c_92 = pygame.image.load('images/gauges/cooldown/C-92%.png')
c_92 = pygame.transform.scale_by(c_92, 5)
c_94 = pygame.image.load('images/gauges/cooldown/C-94%.png')
c_94 = pygame.transform.scale_by(c_94, 5)
c_96 = pygame.image.load('images/gauges/cooldown/C-96%.png')
c_96 = pygame.transform.scale_by(c_96, 5)
c_98 = pygame.image.load('images/gauges/cooldown/C-98%.png')
c_98 = pygame.transform.scale_by(c_98, 5)
c_100 = pygame.image.load('images/gauges/cooldown/C-100%.png')
c_100 = pygame.transform.scale_by(c_100, 5)

#Game loop
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.blit(background, (0,0))
        
        #Comepleteley temp and for show while I'm bored doing image exporting
        if ultimate_charge < 100:
            ultimate_charge += 2
        else:
            ultimate_charge = 0

        if cooldown > 0:
            cooldown -= 2
        else:
            cooldown = 100

        game_active = True #This is temp for now just setting up the UI

        if game_active:
            ui_blit()
        
        CLOCK.tick(FRAME_RATE)
        pygame.display.update()