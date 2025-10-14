"""Project: Level 3 Programming Asessment.

Author: Isaac Smith
School: Hauraki Plains College
Date: 03/06/2025 - 17/10/2025
"""

# ---------- IMPORTS ----------


import pygame
import random
import time


# ---------- INITIIALIZING ----------


pygame.init()
CLOCK = pygame.time.Clock()
pygame.font.init()


# ---------- CONSTANTS ----------


FRAME_RATE = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SMALL = pygame.font.SysFont('freedom-font - Shortcut.lnk', 25)
MEDIUM = pygame.font.SysFont('freedom-font - Shortcut.lnk', 35)
BIG = pygame.font.SysFont('freedom-font - Shortcut.lnk', 50)
WAY_TOO_BIG = pygame.font.SysFont('freedom-font - Shortcut.lnk', 100)
MAX_INPUTS = 4
BASE_INPUTS = ['up', 'left', 'down', 'right', 'buffer']
UNKNOWN_BASIC = "Unknown"
UKNOWN_WITH_HYPHEN = " - Unknown"
COMBOS = {
    'failed combo': {'name': 'Failed',
                     'damage': 0,
                     'cooldown level': 100,
                     'charge unit': 0},
    'combo1': {'name':
               'Standard Up',
               'damage': 10,
               'cooldown level': 3.5,
               'charge unit': 10,
               'input combo': ['up', 'up', 'up', 'up']},
    'combo2': {'name':
               'Standard Down',
               'damage': 10,
               'cooldown level': 3.5,
               'charge unit': 10,
               'input combo': ['down', 'down', 'down', 'down']},
    'combo3': {'name': 'Standard Left',
               'damage': 10,
               'cooldown level': 3.5,
               'charge unit': 10,
               'input combo': ['left', 'left', 'left', 'left']},
    'combo4': {'name': 'Standard Right',
               'damage': 10,
               'cooldown level': 3.5,
               'charge unit': 10,
               'input combo': ['right', 'right', 'right', 'right']},
    'combo5': {'name': 'Floss',
               'damage': 15,
               'cooldown level': 3,
               'charge unit': 15,
               'input combo': ['left', 'right', 'left', 'right']},
    'combo6': {'name': 'The Hype',
               'damage': 15,
               'cooldown level': 3,
               'charge unit': 15,
               'input combo': ['up', 'up', 'down', 'down']},
    'combo7': {'name': "Flippin' Sexy",
               'damage': 20,
               'cooldown level': 2.5,
               'charge unit': 20,
               'input combo': ['down', 'down', 'left', 'right']},

    'ultimate combo': {'name': 'Ultimate Combo',
                       'damage': 1000000000,
                       'cooldown level': 1000000000,
                       'charge unit': 0,
                       'input combo': ['up', 'left', 'down', 'right']}
}


# ---------- VARIABLES ----------


wave_num = 1
ultimate_charge = 0
cooldown_charge = 0
ultimate_status = False
cooldown = False
game_state = "start"
start_level = "base"
main_menu_level = "base"
arrow_limit = 0
arrow_pos = 1
inputs = []
player_name = ''
enemy_list = []
walk_direction = 1
last_update_time = 0
animation_delay = 150
enemy = 0
walk_direction = 1
countdown = 6
bid_num = 0
stage_two_moves = "unknown"
stage_three_moves = "unknown"
runs_completed = 0
total_runs = 0
enemies_defeated = 0
z_was_down_before_win = False
ignore_next_z_keyup = False


# ---------- CLASSES ----------


class DisplayManager:
    """Handle the window and its sizing."""

    def __init__(self, base_res=(1280, 720)):
        """
        Create a frame to render images onto.
        The frame is able to be resized and contains letterboxing.
        """
        # Set the base resolution
        self.base_res = base_res

        # Create the frame
        self.display_surface = pygame.display.set_mode(
            base_res, pygame.RESIZABLE)
        pygame.display.set_caption("Dance Dance Zombie Revolution")

        # Create where it's actually rendering
        self.render_surface = pygame.Surface(base_res)

    def get_window(self):
        """Return the surface where the game should draw its graphics."""
        return self.render_surface

    def update_display(self):
        """Scale the frame and the letterboxing and render it to the window."""
        # Gather info for the display
        window_width, window_height = self.display_surface.get_size()
        base_width, base_height = self.base_res

        # Keep the aspect ratio
        scale = min(window_width / base_width, window_height / base_height)
        scaled_width = int(base_width * scale)
        scaled_height = int(base_height * scale)

        # Create the buffer
        x_offset = (window_width - scaled_width) // 2
        y_offset = (window_height - scaled_height) // 2

        # Scale the game render relative to the screen size
        scaled_surface = pygame.transform.smoothscale(
            self.render_surface, (scaled_width, scaled_height)
        )

        # Blit buffer and the screen
        self.display_surface.fill((0, 0, 0))
        self.display_surface.blit(scaled_surface, (x_offset, y_offset))


class Character(pygame.sprite.Sprite):
    """Handles character traits and enemy spawnging, moving, and animation."""

    def __init__(
            self, health, damage, speed, left_spawn_x, right_spawn_x,
            left_stop_x, right_stop_x, x=0, y=0,
            animation_frames=None, animation_delay=200, spawn_y=0):
        """Set all traits for characters and enemies."""
        # Sets base chararistics
        super().__init__()
        self.health = health
        self.damage = damage
        self.speed = speed

        # Sets enemy animation perameters
        self.animation_frames = animation_frames or []
        if self.animation_frames:
            self.image = self.animation_frames[0]
        else:
            self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x or 0, y or 0))
        self.animation_delay = animation_delay
        self.last_animation_time = pygame.time.get_ticks()
        self.current_frame_index = 0

        # Sets where the enemy spawns and where it damages the player
        self.left_spawn_x = left_spawn_x
        self.right_spawn_x = right_spawn_x
        self.left_stop_x = left_stop_x
        self.right_stop_x = right_stop_x
        self.spawn_y = spawn_y

        # Sets enemy damaging peramters
        self.damaging = False
        self.damage_direction = 0

    def copy(self):
        """Every peramter that copies over to every individual enemy."""
        return Character(
            self.health,
            self.damage,
            self.speed,
            self.left_spawn_x,
            self.right_spawn_x,
            self.left_stop_x,
            self.right_stop_x,
            self.rect.x,
            self.rect.y,
            self.animation_frames[:],
            self.animation_delay,
            self.spawn_y
        )

    def update(self):
        """Enemy movement and damaging."""
        if not self.damaging:
            # General Enemy Movement
            if self.rect.x > self.right_stop_x:
                self.rect.x -= self.speed
            elif self.rect.x < self.left_stop_x:
                self.rect.x += self.speed

            # Damage Player
            if (
                self.right_stop_x + 5 > self.rect.x < self.right_stop_x + 10
                and self.rect.x > 600
            ):
                self.damaging = True
                self.damage_direction = 1
                player.health -= enemy.damage
            elif (
                self.left_stop_x - 10 < self.rect.x > self.left_stop_x - 5
                and self.rect.x < 600
            ):
                self.damaging = True
                self.damage_direction = -1
                player.health -= enemy.damage

        # Reset Enemy Pos After Damaging
        else:
            self.rect.x += self.damage_direction * 10
            if (
                self.damage_direction == 1
                and self.rect.x >= enemy.right_spawn_x
            ):
                self.damaging = False
            elif (
                self.damage_direction == -1
                and self.rect.x <= enemy.left_spawn_x
            ):
                self.damaging = False

    def animate(self, direction=1):
        """Enemy animation."""
        current_time = pygame.time.get_ticks()
        if (  # Checks to see if it's time to change the frame
            current_time - self.last_animation_time >= self.animation_delay
            and self.animation_frames
        ):
            self.current_frame_index = ( # Sets the frame to the next in line
                (self.current_frame_index + direction) % len(
                    self.animation_frames))
            self.image = self.animation_frames[self.current_frame_index]
            self.rect = self.image.get_rect(center=self.rect.center)
            self.last_animation_time = current_time


# Character characteristeics
player = Character(100, None, None, None, None, None, None, None)
snothler = Character(
    15, 15, 2, -255, 1455, 390, 645, 0, 0, None, 600, spawn_y=10)
boulder_bro = Character(
    40, 30, 1, -481, 1275, 165, 640, 0, 0, None, 700, spawn_y=50)
little_timmy = Character(
    15, 5, 20, -220, 1310, 420, 646, 0, 0, None, 0, spawn_y=300)
the_vulture = Character(
    20, 30, 5, -655, 1200, -20, 640, 0, 0, None, 0, spawn_y=50)

# Enemey animation varibales
snothler_frames = [
    pygame.transform.scale_by(
        pygame.image.load('images/enemies/Snothler-1.png'), 5),
    pygame.transform.scale_by(
        pygame.image.load('images/enemies/Snothler-2.png'), 5)
]
snothler.animation_frames = snothler_frames
snothler.image = snothler.animation_frames[0]
snothler.current_frame_index = 0
snothler.rect = snothler.image.get_rect()

boulder_bro_frames = [
    pygame.transform.scale_by(
        pygame.image.load('images/enemies/Boulder-bro-walking-1.png'), 5),
    pygame.transform.scale_by(
        pygame.image.load('images/enemies/Boulder-Bro-Stationary.png'), 5)
]
boulder_bro.animation_frames = boulder_bro_frames
boulder_bro.image = boulder_bro.animation_frames[0]
boulder_bro.current_frame_index = 0
boulder_bro.rect = boulder_bro.image.get_rect()

little_timmy_frames = [
    pygame.transform.scale_by(
        pygame.image.load('images/enemies/Little-Timmy.png'), 5)
]
little_timmy.animation_frames = little_timmy_frames
little_timmy.image = little_timmy.animation_frames[0]
little_timmy.current_frame_index = 0
little_timmy.rect = little_timmy.image.get_rect()

the_vulture_frames = [
    pygame.transform.scale_by(
        pygame.image.load('images/enemies/The-Vulture.png'), 5)
]
the_vulture.animation_frames = the_vulture_frames
the_vulture.image = the_vulture.animation_frames[0]
the_vulture.current_frame_index = 0
the_vulture.rect = the_vulture.image.get_rect()

# Sprite group
enemy_group = pygame.sprite.Group()


class Wave:
    """Handles the creation of new enemies."""

    def __init__(self, enemy_type, enemies_left, time_between, enemy_count):
        """Create peramters needed to spawn new enemies."""
        self.enemy_type = enemy_type
        self.enemies_left = enemies_left
        self.time_between = time_between
        self.enemy_count = enemy_count
        self.last_spawn_time = 0
        self.enemy_x = 0
        self.enemy_y = 0

    def enemy_spawn(self):
        """Spawn a new enemy after time has progressed."""
        current_time = pygame.time.get_ticks()
        if (  # Checks if it's time to spawn a new enemy
            current_time - self.last_spawn_time >= self.time_between * 1000
            and self.enemies_left > 0 or len(enemy_group) == 0
        ):
            # Chooses where to spawn the new enemy
            edge = random.choice(['left', 'right'])
            # Copies enemy data
            new_enemy = self.enemy_type.copy()

            # Flips enemy sprite if spawned on left side
            if edge == 'left':
                new_enemy.rect.x = enemy.left_spawn_x
                new_enemy.animation_frames = [
                    pygame.transform.flip(
                        f, True, False) for f in new_enemy.animation_frames]
                new_enemy.image = new_enemy.animation_frames[0]
            else:
                new_enemy.rect.x = enemy.right_spawn_x
            new_enemy.rect.y = self.enemy_type.spawn_y

            # Adds it to the enemy group
            enemy_group.add(new_enemy)

            # Resets timer
            self.last_spawn_time = current_time

        return self.enemy_x, self.enemy_y


# Wave characterisitcs
wave1 = Wave(snothler, 7, 7, 7)
wave2 = Wave(boulder_bro, 5, 12, 5)
wave3 = Wave(little_timmy, 15, 5, 15)
wave4 = Wave(the_vulture, 10, 7, 10)

# Works with set_wave to set wave_num to a wave
waves = {
    1: wave1,
    2: wave2,
    3: wave3,
    4: wave4,
}


class Achievements():
    """Tracks all achievements and handels displays related to them."""

    def __init__(self):
        """
        Set all achievements to false.

        Also set the default for other variables.
        """
        # Completion achievements
        self.complete_one_run = False
        self.complete_five_runs = False
        self.complete_ten_runs = False

        # Enemy achievements
        self.defeat_ten_enemies = False
        self.defeat_twenty_five_enemies = False
        self.defeat_fifty_enemies = False

        # Wave achievements
        self.complete_wave_one = False
        self.complete_wave_two = False
        self.complete_wave_three = False

        # Other variables
        self.run_achievements = 0
        self.ach_ban_x = -520

    def check(self, runs_completed, enemies_defeated, wave_num):
        """
        Check if achievements have been completed within a run.

        Keep track of how many have been completed in one run.
        """
        # Completion achievements
        if runs_completed >= 1 and not self.complete_one_run:
            self.complete_one_run = True
            self.run_achievements += 1
        if runs_completed >= 5 and not self.complete_five_runs:
            self.complete_five_runs = True
            self.run_achievements += 1
        if runs_completed >= 10 and not self.complete_ten_runs:
            self.complete_ten_runs = True
            self.run_achievements += 1

        # Enemy achievements
        if enemies_defeated >= 10 and not self.defeat_ten_enemies:
            self.defeat_ten_enemies = True
            self.run_achievements += 1
        if enemies_defeated >= 25 and not self.defeat_twenty_five_enemies:
            self.defeat_twenty_five_enemies = True
            self.run_achievements += 1
        if enemies_defeated >= 50 and not self.defeat_fifty_enemies:
            self.defeat_fifty_enemies = True
            self.run_achievements += 1

        # Wave achievements
        if wave_num > 1 and not self.complete_wave_one:
            self.complete_wave_one = True
            self.run_achievements += 1
        if wave_num > 2 and not self.complete_wave_two:
            self.complete_wave_two = True
            self.run_achievements += 1
        if wave_num > 3 and not self.complete_wave_three:
            self.complete_wave_three = True
            self.run_achievements += 1

        return self.run_achievements

    def menu_display(self):
        """Handle positioning and logic for main display in main menu."""
        # Header text
        draw_text("Achievements:", BIG, WHITE, 515, 100)

        # Completion achievements
        draw_text("Complete 1 Run", MEDIUM, WHITE, 150, 200)
        if self.complete_one_run:
            WINDOW.blit(yes, (400, 195))
        else:
            WINDOW.blit(no, (400, 195))
        draw_text("Complete 5 Runs", MEDIUM, WHITE, 150, 400)
        if self.complete_five_runs:
            WINDOW.blit(yes, (400, 395))
        else:
            WINDOW.blit(no, (400, 395))
        draw_text("Complete 10 Runs", MEDIUM, WHITE, 150, 600)
        if self.complete_ten_runs:
            WINDOW.blit(yes, (400, 595))
        else:
            WINDOW.blit(no, (400, 595))

        # Enemy achievements
        draw_text("Defeat 10 Enemies", MEDIUM, WHITE, 500, 200)
        if self.defeat_ten_enemies:
            WINDOW.blit(yes, (750, 195))
        else:
            WINDOW.blit(no, (750, 195))
        draw_text("Defeat 25 Enemies", MEDIUM, WHITE, 500, 400)
        if self.defeat_twenty_five_enemies:
            WINDOW.blit(yes, (750, 395))
        else:
            WINDOW.blit(no, (750, 395))
        draw_text("Defeat 50 Enemies", MEDIUM, WHITE, 500, 600)
        if self.defeat_fifty_enemies:
            WINDOW.blit(yes, (750, 595))
        else:
            WINDOW.blit(no, (750, 595))

        # Wave achievements
        draw_text("Complete Wave 1", MEDIUM, WHITE, 850, 200)
        if self.complete_wave_one:
            WINDOW.blit(yes, (1100, 195))
        else:
            WINDOW.blit(no, (1100, 195))
        draw_text("Complete Wave 2", MEDIUM, WHITE, 850, 400)
        if self.complete_wave_two:
            WINDOW.blit(yes, (1100, 395))
        else:
            WINDOW.blit(no, (1100, 395))
        draw_text("Complete Wave 3", MEDIUM, WHITE, 850, 600)
        if self.complete_wave_three:
            WINDOW.blit(yes, (1100, 595))
        else:
            WINDOW.blit(no, (1100, 595))

    def other_displays(self):
        """Handle other achievement related logic for other menu displays."""
        # Enemy menu
        if total_runs != 0:
            snothler_awareness = "known"
        else:
            snothler_awareness = "unknown"
        if self.complete_wave_one:
            bro_awareness = "known"
        else:
            bro_awareness = "uknown"

        # Enemy and move menu
        if self.complete_wave_two:
            stage_two_moves = timmy_awareness = "known"
        else:
            stage_two_moves = timmy_awareness = "unknown"
        if self.complete_wave_three:
            stage_three_moves = vulture_awareness = "known"
        else:
            stage_three_moves = vulture_awareness = "unknown"

        return (stage_two_moves, stage_three_moves, snothler_awareness,
                bro_awareness, timmy_awareness, vulture_awareness)

    def animation(self):
        """Run the achievement banner if new achievement/s."""
        if self.run_achievements != 0:
            # Sets banner to singular if only one achievement complete
            if self.run_achievements == 1:
                ach_ban = pygame.transform.scale_by(
                    pygame.image.load('images/Ach-banner-sing.png'), 5)
            else:
                # Sets banner to multiple if multiple achievements complete
                ach_ban = pygame.transform.scale_by(
                    pygame.image.load('images/Ach-ban-mul.png'), 5)
            WINDOW.blit(ach_ban, (self.ach_ban_x, 50))

            # Baner movement
            if self.ach_ban_x < 0:
                self.ach_ban_x += 10
        else:
            pass

        return self.ach_ban_x


# ---------- INSTANCES ----------


achievements = Achievements()
display = DisplayManager((1280, 720))
WINDOW = display.get_window()


# ---------- FUNCTIONS ----------

def draw_text(text, font, color, x, y):
    """Create stencil for drawing text."""
    text = font.render(text, True, color)
    WINDOW.blit(text, (x, y))


def load_uc_images(start=2, end=100, step=2, scale=5):
    """Load all ultimate charge sprites."""
    uc_images = {}
    # Loop through every number from 2 to 100 in multiples of two
    for i in range(start, end + 1, step):
        # Apply every number to the base file path for ultimate charge
        path = f'images/gauges/ultimate-charge/UC-{i}%.png'
        uc_image = pygame.image.load(path)
        # Scale the image up to the screen resiolution
        scaled_image = pygame.transform.scale_by(uc_image, scale)
        uc_images[i] = scaled_image
    return uc_images


def ultimate_blit():
    """Blits the ultimate charge based on how full it is."""
    # Makes it empty if no charge
    if ultimate_charge == 0:
        ultimate_gauge = gauge_0
    else:
        # Clamps the charge to the nearest lower even number between 2 and 100
        clamped_uc_charge = min(max(2, int(ultimate_charge // 2 * 2)), 100)
        ultimate_gauge = ultimate_charge_images.get(clamped_uc_charge, gauge_0)

    WINDOW.blit(ultimate_gauge, (75, 600))


def load_c_images(start=2, end=100, step=2, scale=5):
    """Load all cooldown sprites."""
    c_images = {}
    # Loop through every number from 2 to 100 in multiples of two
    for i in range(start, end + 1, step):
        # Apply every number to the base file path for cooldown
        path = f'images/gauges/cooldown/C-{i}%.png'
        c_image = pygame.image.load(path)
        # Scale the image up to the screen resiolution
        scaled_image = pygame.transform.scale_by(c_image, scale)
        c_images[i] = scaled_image
    return c_images


def cooldown_blit():
    """Blit all the cooldown sprites based on how full it is."""
    # Makes it empty if no charge
    if cooldown_charge == 0:
        cooldown_gauge = gauge_0
    else:
        # Clamps the charge to the nearest lower even number between 2 and 100
        clamped_c_charge = min(max(2, int(cooldown_charge // 2 * 2)), 100)
        cooldown_gauge = cooldown_charge_images.get(clamped_c_charge, gauge_0)

    WINDOW.blit(cooldown_gauge, (935, 600))


def on_cooldown(cooldown, cooldown_charge):
    """Turn off cooldown after certian amount of time based on move used."""
    if cooldown:
        cooldown_charge -= COMBOS[output_combo]['cooldown level']
        if cooldown_charge <= 0:
            cooldown_charge = 0
            cooldown = False
    return cooldown, cooldown_charge


def load_hb_images(start=4, end=100, step=4, scale=5):
    """Load all health bar sprites."""
    hb_images = {}
    # Loop through every number from 4 to 100 in multiples of four
    for i in range(start, end + 1, step):
        # Apply every number to the base file path for cooldown
        path = f'images/health bar/HB-{i}%.png'
        hb_image = pygame.image.load(path)
        # Scale the image up to the screen resiolution
        scaled_image = pygame.transform.scale_by(hb_image, scale)
        hb_images[i] = scaled_image
    return hb_images


def hb_blit():
    """Blit all the health bar sprites based on how full it is."""
    # Makes it empty if no charge
    if player.health <= 0:
        health_bar = hb_empty
    else:
        # Clamps the charge to the nearest lower even number between 4 and 100
        clamped_player_health = min(max(4, int(player.health // 4 * 4)), 100)
        health_bar = hb_images.get(clamped_player_health, hb_empty)

    WINDOW.blit(health_bar, (1125, 30))


def arrows_functionality():
    """Change arrow sprite when the corresponding key is pressed."""
    # Left arrow
    if key_pressed[pygame.K_LEFT]:
        left_arrow = left_arrow_pressed
        WINDOW.blit(left_arrow, (425, 565))
    else:
        left_arrow = left_arrow_base
        WINDOW.blit(left_arrow, (420, 560))

    # Up arrow
    if key_pressed[pygame.K_UP]:
        up_arrow = up_arrow_pressed
        WINDOW.blit(up_arrow, (545, 565))
    else:
        up_arrow = up_arrow_base
        WINDOW.blit(up_arrow, (540, 560))

    # Down arrow
    if key_pressed[pygame.K_DOWN]:
        down_arrow = down_arrow_pressed
        WINDOW.blit(down_arrow, (665, 565))
    else:
        down_arrow = down_arrow_base
        WINDOW.blit(down_arrow, (660, 560))

    # Right arrow
    if key_pressed[pygame.K_RIGHT]:
        right_arrow = right_arrow_pressed
        WINDOW.blit(right_arrow, (785, 565))
    else:
        right_arrow = right_arrow_base
        WINDOW.blit(right_arrow, (780, 560))


def inputs_display():
    """Display input list above arrows."""
    # Input 1
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

    # Input 2
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

    # Input 3
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

    # Input 4
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

    # Blit input list
    WINDOW.blit(inputs0, (450, 530))
    WINDOW.blit(inputs1, (480, 530))
    WINDOW.blit(inputs2, (510, 530))
    WINDOW.blit(inputs3, (540, 530))

    # Blit ultimate combo above ultimate charge
    if ultimate_status:
        WINDOW.blit(mini_arrow_up, (110, 530))
        WINDOW.blit(mini_arrow_left, (140, 530))
        WINDOW.blit(mini_arrow_down, (170, 530))
        WINDOW.blit(mini_arrow_right, (200, 530))


def check_combo():
    """Match the input list to an existing combo, otherwise fail."""
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
    elif inputs == COMBOS['combo7']['input combo']:
        output_combo = 'combo7'
    elif inputs == COMBOS['ultimate combo']['input combo']:
        output_combo = 'ultimate combo'
    else:
        output_combo = 'failed combo'

    return output_combo


def player_pointing():
    """Show the player pointing in the direction of arrows being pressed."""
    # Only off cooldown as input list isnt updated on cooldown
    if not cooldown:
        # Left
        if key_pressed[pygame.K_LEFT]:
            player = player_pointing_left
            player_x = 1055
            player_y = 70

        # Right
        elif key_pressed[pygame.K_RIGHT]:
            player = player_pointing_right
            player_x = 1145
            player_y = 70

        # Up
        elif key_pressed[pygame.K_UP]:
            player = player_pointing_up
            player_x = 1145
            player_y = 10

        # Down
        elif key_pressed[pygame.K_DOWN]:
            player = player_pointing_down
            player_x = 1145
            player_y = 70

        # Neutral
        else:
            player = player_default
            player_x = 1145
            player_y = 70
    else:
        player = player_default
        player_x = 1145
        player_y = 70

    WINDOW.blit(player, (player_x, player_y))


def set_wave(wave_num):
    """Return waves so wave_num gets applied to the wave class."""
    return waves.get(wave_num, None)


def set_enemy(enemy):
    """Set the enemy to the wave they spawn in."""
    if wave_num == 1:
        enemy = snothler
    elif wave_num == 2:
        enemy = boulder_bro
    elif wave_num == 3:
        enemy = little_timmy
    elif wave_num == 4:
        enemy = the_vulture
    else:
        pass

    return enemy


def reset(wave_num, ultimate_charge, cooldown, countdown):
    """Reset all variables needed to be reset before a new run begins."""
    player.health = 100
    enemy_group.empty()
    wave1.enemies_left = 7
    wave2.enemies_left = 5
    wave3.enemies_left = 15
    wave4.enemies_left = 10
    wave_num = 1
    ultimate_charge = 0
    cooldown = 0
    countdown = 6

    return wave_num, ultimate_charge, cooldown, countdown


def gray_overlay():
    """Create and blit the gray overlay used in most game states."""
    overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)
    overlay.fill((128, 128, 128, 150))
    WINDOW.blit(overlay, (0, 0))


def multi_ui_display():
    """Blit UI text used both in active and paused game states."""
    # Wave number
    draw_text("Wave: " + str(wave_num), MEDIUM, WHITE, 596, 10)

    # Enemies left
    draw_text("Enemies Left: " + str(
        wave.enemies_left), MEDIUM, WHITE, 545, 687)

    # Gauge titles
    draw_text("Ultimate Charge", SMALL, WHITE, 142.5, 575)
    draw_text("Cooldown", SMALL, WHITE, 1027.5, 575)

    # Player name
    draw_text(player_name, SMALL, WHITE, 1135, 15)

    # Gauges
    ultimate_blit()
    cooldown_blit()
    hb_blit()


def tutorial():
    """Blit the text with info needed to know what to do in your first run."""
    draw_text("Use the arrow keys to create combos", SMALL, WHITE, 25, 70)
    draw_text(
        "Press Z to execute them, or X to clear your current inputs",
        SMALL, WHITE, 25, 95)


#GAME STATES


def active_ui_blit(key_pressed, wave):
    """Display all parts of the base game UI."""
    # Stuff also used in pause menu
    multi_ui_display()

    # Esc to pause
    WINDOW.blit(esc_bg, (25, 25))
    draw_text("esc", SMALL, BLACK, 31, 35)
    draw_text("to pause", SMALL, WHITE, 70, 35)

    # Arrows/pointing
    arrows_functionality()
    inputs_display()
    player_pointing()

    # Tutorial
    if total_runs == 0:
        tutorial()


def pause_screen(arrow_limit):
    """Display all parts of the pause UI."""
    # Stuff also used in active UI
    multi_ui_display()

    # Gray overlay
    gray_overlay()

    # Arrows
    left_arrow = left_arrow_base
    up_arrow = up_arrow_base
    down_arrow = down_arrow_base
    right_arrow = right_arrow_base
    WINDOW.blit(left_arrow, (420, 560))
    WINDOW.blit(up_arrow, (540, 560))
    WINDOW.blit(down_arrow, (660, 560))
    WINDOW.blit(right_arrow, (780, 560))

    # Selection Text
    draw_text("CONTINUE", BIG, WHITE, 547.5, 250)
    draw_text("BACK TO MAIN MENU", BIG, WHITE, 460, 400)

    # Selection arrow
    arrow_limit = 2
    if arrow_pos == 1:
        WINDOW.blit(selection_arrow, (465, 240))
    elif arrow_pos == 2:
        WINDOW.blit(selection_arrow, (377.5, 390))

    return arrow_limit


def start_screen(arrow_limit):
    """Display all parts of the start screen UI."""
    # Gray overlay
    gray_overlay()

    # Logo
    WINDOW.blit(logo, (280, 100))

    # Controls
    draw_text("Z to confirm", SMALL, WHITE, 592.5, 660)
    draw_text(
        "X to uhhh, do the opposite or whatever", SMALL, WHITE, 483, 680)
    draw_text("Arrow keys to move to arrow", SMALL, WHITE, 520, 700)

    # Base screen
    if start_level == "base":
        # Selection text
        draw_text("NEW PLAYER", BIG, WHITE, 525.5, 475)
        draw_text("RETURNING PLAYER", BIG, WHITE, 467.5, 575)

        # Selection arrow
        arrow_limit = 2
        if arrow_pos == 1:
            WINDOW.blit(selection_arrow, (443, 465))
        elif arrow_pos == 2:
            WINDOW.blit(selection_arrow, (385, 565))

    # New player screen
    if start_level == "new player":
        draw_text("INPUT NAME:", BIG, WHITE, 527.5, 475)
        draw_text("BACK", BIG, WHITE, 590, 600)
        draw_text(player_name, BIG, WHITE, 525.5, 525)

        # Player name instructions
        if player_name != '':
            draw_text("Enter to confirm", SMALL, WHITE, 756, 489)

        # Selection arrow
        arrow_limit = 2
        if arrow_pos == 1:
            WINDOW.blit(selection_arrow, (444, 465))
        elif arrow_pos == 2:
            WINDOW.blit(selection_arrow, (507.5, 590))

    return arrow_limit


def death_screen(arrow_limit):
    """Display all parts of the death screen UI."""
    # Gray overlay
    gray_overlay()

    # Game over display
    WINDOW.blit(game_over, (410, 150))

    # Selection text
    draw_text("NEW RUN", BIG, WHITE, 557.5, 475)
    draw_text("MAIN MENU", BIG, WHITE, 540.5, 575)

    # Selection arrow
    arrow_limit = 2
    if arrow_pos == 1:
        WINDOW.blit(selection_arrow, (475, 465))
    elif arrow_pos == 2:
        WINDOW.blit(selection_arrow, (452, 565))

    return arrow_limit


def main_menu(arrow_limit, countdown, last_update_time, bid_num):
    """Display all parts of the main menu UI."""
    # Calling info needed from achievements class
    (stage_two_moves, stage_three_moves, snothler_awareness,
     bro_awareness, timmy_awareness, vulture_awareness
     ) = achievements.other_displays()

    # Gray overlay
    gray_overlay()

    # Top left display
    WINDOW.blit(small_logo, (0, 0))
    WINDOW.blit(player_default, (19, 65))
    draw_text(player_name, MEDIUM, WHITE, 150, 18)

    # Base screen
    if main_menu_level == "base":
        # Selection text
        draw_text("NEW RUN", BIG, WHITE, 560, 150)
        draw_text("ENEMIES", BIG, WHITE, 565.5, 225)
        draw_text("MOVES", BIG, WHITE, 578.5, 300)
        draw_text("ACHIEVEMENTS", BIG, WHITE, 502.5, 375)
        draw_text("SAVE & QUIT", BIG, WHITE, 530, 450)

        # Stats display
        draw_text(f"Total Runs: {total_runs}", BIG, WHITE, 532, 600)
        draw_text(f"Runs Completed: {runs_completed}", BIG, WHITE, 483, 640)
        draw_text(f"Enemies Defeated: {enemies_defeated}",
                  BIG, WHITE, 472, 680)

        # Selection arrow
        arrow_limit = 5
        if arrow_pos == 1:
            WINDOW.blit(selection_arrow, (477.5, 140))
        elif arrow_pos == 2:
            WINDOW.blit(selection_arrow, (483, 215))
        elif arrow_pos == 3:
            WINDOW.blit(selection_arrow, (496, 290))
        elif arrow_pos == 4:
            WINDOW.blit(selection_arrow, (420, 365))
        elif arrow_pos == 5:
            WINDOW.blit(selection_arrow, (447.5, 440))

    # Enemy screen
    if main_menu_level == 'enemies':
        # Header text
        draw_text("Enemies:", BIG, WHITE, 530, 15)

        # Set enemy display text based on if you have seen it before
        # Snothler
        if snothler_awareness == "known":
            snothler_name = "Snothler"
            snothler_health = snothler.health
            snothler_damage = snothler.damage
        else:
            snothler_name = snothler_health = snothler_damage = UNKNOWN_BASIC

        # Boulder Bro
        if bro_awareness == "known":
            bro_name = "Boulder Bro"
            bro_health = boulder_bro.health
            bro_damage = boulder_bro.damage
        else:
            bro_name = bro_damage = bro_health = UNKNOWN_BASIC

        # Little Timmy
        if timmy_awareness == "known":
            timmy_name = "Little Timmy"
            timmy_health = little_timmy.health
            timmy_damage = little_timmy.damage
        else:
            timmy_name = timmy_health = timmy_damage = UNKNOWN_BASIC

        # The Vulture
        if vulture_awareness == "known":
            vulture_name = "The Vulture"
            vulture_health = the_vulture.health
            vulture_damage = the_vulture.damage
        else:
            vulture_name = vulture_health = vulture_damage = UNKNOWN_BASIC

        # Blit small and flipped enemy + info
        # Snothler
        WINDOW.blit(pygame.transform.flip(
            pygame.image.load(
                'images/enemies/Snothler-1.png'), True, False), (528, 60))
        draw_text(f"{snothler_name}", MEDIUM, WHITE, 650, 60)
        draw_text(f"Health: {snothler_health}", SMALL, WHITE, 650, 80)
        draw_text(f"Damage: {snothler_damage}", SMALL, WHITE, 650, 95)

        # Boulder Bro
        WINDOW.blit(pygame.transform.flip(
            pygame.image.load(
                'images/enemies/Boulder-Bro-Stationary.png'), True, False),
                (498, 245))
        draw_text(f"{bro_name}", MEDIUM, WHITE, 650, 245)
        draw_text(f"Health: {bro_health}", SMALL, WHITE, 650, 265)
        draw_text(f"Damage: {bro_damage}", SMALL, WHITE, 650, 280)

        # Little Timmy
        WINDOW.blit(pygame.transform.flip(
            pygame.image.load(
                'images/enemies/Little-Timmy.png'), True, False), (528, 455))
        draw_text(f"{timmy_name}", MEDIUM, WHITE, 650, 455)
        draw_text(f"Health: {timmy_health}", SMALL, WHITE, 650, 475)
        draw_text(f"Damage: {timmy_damage}", SMALL, WHITE, 650, 490)

        # The Vulture
        WINDOW.blit(
            pygame.transform.flip(
                pygame.image.load(
                    'images/enemies/The-Vulture.png'), True, False),
                    (480, 560))
        draw_text(f"{vulture_name}", MEDIUM, WHITE, 650, 560)
        draw_text(f"Health: {vulture_health}", SMALL, WHITE, 650, 580)
        draw_text(f"Damage: {vulture_damage}", SMALL, WHITE, 650, 595)

    # Moves screen
    if main_menu_level == 'moves':
        # Header text
        draw_text("Moves:", BIG, WHITE, 530, 150)

        # Rotate through the four different basic combos
        current_time = time.time()
        if current_time - last_update_time >= 1 and bid_num < 4:
            bid_num += 1
            if bid_num == 4:
                bid_num = 0
            last_update_time = current_time
        base_inputs_display = BASE_INPUTS[bid_num]

        # Set basic combo variables
        if base_inputs_display == BASE_INPUTS[0]:
            move_arrow_base = mini_arrow_up
        elif base_inputs_display == BASE_INPUTS[1]:
            move_arrow_base = mini_arrow_left
        elif base_inputs_display == BASE_INPUTS[2]:
            move_arrow_base = mini_arrow_down
        elif base_inputs_display == BASE_INPUTS[3]:
            move_arrow_base = mini_arrow_right

        # Display basic combos
        WINDOW.blit(move_arrow_base, (530, 200))
        WINDOW.blit(move_arrow_base, (560, 200))
        WINDOW.blit(move_arrow_base, (590, 200))
        WINDOW.blit(move_arrow_base, (620, 200))

        # Basic combo info
        draw_text(" - Basic Combo", MEDIUM, WHITE, 640, 200)
        draw_text("Damage: 10", SMALL, WHITE, 530, 230)

        # Keep stage 2 combos hidden if not known
        if stage_two_moves == "known":
            hype_arrow_one = mini_arrow_up
            hype_arrow_two = mini_arrow_up
            hype_arrow_three = mini_arrow_down
            hype_arrow_four = mini_arrow_down

            floss_arrow_one = mini_arrow_left
            floss_arrow_two = mini_arrow_right
            floss_arrow_three = mini_arrow_left
            floss_arrow_four = mini_arrow_right

            hype_name = f" - {COMBOS['combo6']['name']}"
            floss_name = f" - {COMBOS['combo5']['name']}"
        else:
            (hype_arrow_one, hype_arrow_two, hype_arrow_three, hype_arrow_four,
             floss_arrow_one, floss_arrow_two, floss_arrow_three,
             floss_arrow_four) = unknown_arrow
            hype_name = floss_name = UKNOWN_WITH_HYPHEN

        # Display stage 2 combos
        # The Hype
        WINDOW.blit(hype_arrow_one, (530, 300))
        WINDOW.blit(hype_arrow_two, (560, 300))
        WINDOW.blit(hype_arrow_three, (590, 300))
        WINDOW.blit(hype_arrow_four, (620, 300))

        # The Floss
        WINDOW.blit(floss_arrow_one, (530, 400))
        WINDOW.blit(floss_arrow_two, (560, 400))
        WINDOW.blit(floss_arrow_three, (590, 400))
        WINDOW.blit(floss_arrow_four, (620, 400))

        # Stage 2 combos info
        # The Hype
        draw_text(hype_name, MEDIUM, WHITE, 640, 300)
        draw_text(f"Damage: {COMBOS['combo6']['damage']}",
                  SMALL, WHITE, 530, 330)

        # The Floss
        draw_text(floss_name, MEDIUM, WHITE, 640, 400)
        draw_text(f"Damage: {COMBOS['combo6']['damage']}",
                  SMALL, WHITE, 530, 430)

        # Keep stage 3 combos hidden if not known
        if stage_three_moves == "known":
            flippin_arrow_one = mini_arrow_down
            flippin_arrow_two = mini_arrow_down
            flippin_arrow_three = mini_arrow_left
            flippin_arrow_four = mini_arrow_right

            flippin_name = f" - {COMBOS['combo7']['name']}"
        else:
            (flippin_arrow_one, flippin_arrow_two, flippin_arrow_three,
             flippin_arrow_four) = unknown_arrow
            flippin_name = UKNOWN_WITH_HYPHEN

        # Display stage 3 combos
        WINDOW.blit(flippin_arrow_one, (530, 500))
        WINDOW.blit(flippin_arrow_two, (560, 500))
        WINDOW.blit(flippin_arrow_three, (590, 500))
        WINDOW.blit(flippin_arrow_four, (620, 500))

        # Stage 3 combos info
        draw_text(flippin_name, MEDIUM, WHITE, 640, 500)
        draw_text(f"Damage: {COMBOS['combo7']['damage']}",
                  SMALL, WHITE, 530, 530)

    # Achievements screen
    if main_menu_level == 'achievements':
        achievements.menu_display()

    return arrow_limit, countdown, last_update_time, bid_num


def inbetween(game_state, countdown, last_update_time):
    """Display all parts of the in-between UI"""
    # Gray overlay
    gray_overlay()

    #Wave display text
    draw_text(f"Wave: {str(wave_num)}", WAY_TOO_BIG, WHITE, 515, 250)

    # Countdown
    draw_text(f"{str(countdown)}", WAY_TOO_BIG, WHITE, 625, 350)

    # Redeuce countdown by 1 after 1 second
    current_time = time.time()
    if current_time - last_update_time >= 1 and countdown > 0:
        countdown -= 1
        last_update_time = current_time

    # Move on if countdown has completed
    if countdown == 0:
        game_state = 'active'

    return game_state, countdown, last_update_time


def win(arrow_limit):
    """Display all parts of the win screen UI"""
    # Gray overlay
    gray_overlay()

    # Game complete display
    WINDOW.blit(win_screen, (370, 150))

    # Selection text
    draw_text("NEW RUN", BIG, WHITE, 557.5, 475)
    draw_text("MAIN MENU", BIG, WHITE, 540.5, 575)

    # Selection text
    arrow_limit = 2
    if arrow_pos == 1:
        WINDOW.blit(selection_arrow, (475, 465))
    elif arrow_pos == 2:
        WINDOW.blit(selection_arrow, (452, 565))

    return arrow_limit


# ---------- SPRITES ----------


# Placeholder image
blank = pygame.transform.scale_by(pygame.image.load('images/Blank.png'), 5)

# Loading background
background = pygame.transform.scale_by(
    pygame.image.load('images/DDDZA-Background.png'), 5)

# Gauge sprites
gauge_0 = pygame.transform.scale_by(
    pygame.image.load('images/gauges/Gauge-0%.png'), 5)
hb_empty = pygame.transform.scale_by(
    pygame.image.load('images/health bar/HB-Empty.png'), 5)
ultimate_charge_images = load_uc_images()
cooldown_charge_images = load_c_images()
hb_images = load_hb_images()

# Arrows
up_arrow_base = pygame.transform.scale_by(
    pygame.image.load('images/arrows/up-arrow.png'), 5)
up_arrow_pressed = pygame.transform.scale_by(
    pygame.image.load('images/arrows/up-arrow-pressed.png'), 5)
down_arrow_base = pygame.transform.scale_by(
    pygame.image.load('images/arrows/down-arrow.png'), 5)
down_arrow_pressed = pygame.transform.scale_by(
    pygame.image.load('images/arrows/down-arrow-pressed.png'), 5)
left_arrow_base = pygame.transform.scale_by(
    pygame.image.load('images/arrows/left-arrow.png'), 5)
left_arrow_pressed = pygame.transform.scale_by(
    pygame.image.load('images/arrows/left-arrow-pressed.png'), 5)
right_arrow_base = pygame.transform.scale_by(
    pygame.image.load('images/arrows/right-arrow.png'), 5)
right_arrow_pressed = pygame.transform.scale_by(
    pygame.image.load('images/arrows/right-arrow-pressed.png'), 5)

# Escape image
esc_bg = pygame.transform.scale_by(
    pygame.image.load('images/esc.png'), 5)

# Selection arrow
selection_arrow = pygame.transform.scale_by(
    pygame.image.load('images/arrows/Arrow.png'), 5)

# Mini arrows that tell you what your inputs currently look like
mini_arrow_up = pygame.transform.scale_by(
    pygame.image.load('images/arrows/Input-list-up.png'), 5)
mini_arrow_down = pygame.transform.scale_by(
    pygame.image.load('images/arrows/Input-list-down.png'), 5)
mini_arrow_left = pygame.transform.scale_by(
    pygame.image.load('images/arrows/Input-list-left.png'), 5)
mini_arrow_right = pygame.transform.scale_by(
    pygame.image.load('images/arrows/Input-list-right.png'), 5)
unknown_arrow = pygame.transform.scale_by(
    pygame.image.load('images/?.png'), 5)

# Player sprites
player_default = pygame.transform.scale_by(
    pygame.image.load('images/Player/Player-Standard.png'), 5)
player_pointing_up = pygame.transform.scale_by(
    pygame.image.load('images/Player/Pointing/Player-Pointing-Up.png'), 5)
player_pointing_down = pygame.transform.scale_by(
    pygame.image.load('images/Player/Pointing/Player-Pointing-Down.png'), 5)
player_pointing_left = pygame.transform.scale_by(
    pygame.image.load('images/Player/Pointing/Player-Pointing-Left.png'), 5)
player_pointing_right = pygame.transform.scale_by(
    pygame.image.load('images/Player/Pointing/Player-Pointing-Right.png'), 5)

# Logos
logo = pygame.transform.scale_by(pygame.image.load('images/Logo.png'), 5)
small_logo = pygame.image.load('images/Logo.png')
game_over = pygame.transform.scale_by(
    pygame.image.load('images/Death Screen.png'), 5)
win_screen = pygame.transform.scale_by(
    pygame.image.load('images/Win Screen.png'), 5)

# Achievement completion signals
yes = pygame.transform.scale_by(pygame.image.load('images/Yes.png'), 5)
no = pygame.transform.scale_by(pygame.image.load('images/No.png'), 5)


# ---------- GAME LOOP ----------


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# ---------- INPUTS ----------

            if event.type == pygame.KEYDOWN:
                # Player name input
                if game_state == "start":
                    if start_level == "new player":
                        if arrow_pos == 1:
                            # Remove last character
                            if event.key == pygame.K_BACKSPACE:
                                player_name = player_name[:-1]
                            # No input from any of these keys
                            elif (
                                event.key == pygame.K_RETURN
                                or event.key == pygame.K_ESCAPE
                                or event.key
                                    ) == pygame.K_TAB:
                                pass
                            else:
                                # Give a character limit of 6
                                if len(player_name) < 6:
                                    # Key inputs add to player_name
                                    player_name += event.unicode

                if game_state == "active":
                    if not cooldown:
                        # Combo input tracking
                        if event.key == pygame.K_LEFT:
                            inputs.append('left')
                        if event.key == pygame.K_RIGHT:
                            inputs.append('right')
                        if event.key == pygame.K_UP:
                            inputs.append('up')
                        if event.key == pygame.K_DOWN:
                            inputs.append('down')

                        # Executing a combo
                        if event.key == pygame.K_z:
                            output_combo = check_combo()
                            # Check if combo done was ultimate combo
                            if output_combo == 'ultimate combo':
                                # Fail it if ultimate charge isn't full
                                if ultimate_status:
                                    inputs = []
                                    ultimate_charge = 0
                                else:
                                    output_combo = 'failed combo'
                            else:
                                # Reset inputs if fail
                                if output_combo == 'failed combo':
                                    inputs = []

                                # Update ultimate charge and cooldown
                                else:
                                    inputs = []
                                    ultimate_charge += COMBOS[
                                        output_combo]['charge unit']
                                    cooldown = True
                                    cooldown_charge = 100

                                    # Stops z press from registering on win
                                    if (
                                        wave_num == 4 and wave.enemies_left
                                            ) == 1:
                                        keys = pygame.key.get_pressed()
                                        z_was_down_before_win = keys[
                                            pygame.K_z]
                                        (ignore_next_z_keyup
                                         ) = z_was_down_before_win

                            # Damaging oldest enemy
                            if len(enemy_group) > 0:
                                oldest = enemy_group.sprites()[0]
                                oldest.health -= COMBOS[output_combo]['damage']

                                # Kill enemy if health reaches 0
                                if oldest.health <= 0:
                                    oldest.kill()
                                    enemies_defeated += 1
                                    wave.enemies_left -= 1
                            else:
                                pass

                        # Clearing combo list
                        if event.key == pygame.K_x:
                            inputs = []

                # Limits the number of recorded inputs at a time to 4
                if len(inputs) > MAX_INPUTS:
                    inputs.pop(0)

            # Switching between all screens
            if event.type == pygame.KEYUP:
                # Progression
                if event.key == pygame.K_z:
                    # Start screens
                    if game_state == "start":
                        if start_level == "base":
                            # Base to new player
                            if arrow_pos == 1:
                                start_level = "new player"
                            # Base to returning player
                            if arrow_pos == 2:
                                start_level = "returning"
                        # New player to base
                        if start_level == "new player":
                            if arrow_pos == 2:
                                start_level = "base"

                    # Pause screen
                    elif game_state == "paused":
                        # Unpause
                        if arrow_pos == 1:
                            game_state = "active"
                        # Back to main menu
                        if arrow_pos == 2:
                            arrow_pos = 1
                            total_runs += 1
                            main_menu_level = 'base'
                            game_state = "main menu"

                    # Death and win screens
                    elif game_state == "dead" or game_state == 'win':
                        # Stop final combo confirmation from registering
                        if ignore_next_z_keyup:
                            ignore_next_z_keyup = False
                        else:
                            # New run
                            if arrow_pos == 1:
                                (wave_num, ultimate_charge,
                                 cooldown, countdown) = reset(
                                     wave_num, ultimate_charge,
                                     cooldown, countdown)
                                game_state = "active"
                            # Back to main menu
                            if arrow_pos == 2:
                                game_state = "main menu"
                                main_menu_level = "base"

                    # Main menu's
                    elif game_state == "main menu":
                        current_time = pygame.time.get_ticks()
                        if main_menu_level == "base":
                            # New run
                            if arrow_pos == 1:
                                last_spawn_time = current_time
                                game_state = "active"
                            # Base to enemies
                            if arrow_pos == 2:
                                main_menu_level = 'enemies'
                            # Base to moves
                            if arrow_pos == 3:
                                main_menu_level = 'moves'
                            # Base to achievements
                            if arrow_pos == 4:
                                main_menu_level = 'achievements'
                            # Quit the game
                            if arrow_pos == 5:
                                pygame.quit()
                                exit()

                # Going back
                if event.key == pygame.K_x:
                    # Start screens
                    if game_state == "start":
                        # New / returning player to base
                        if (start_level == "new player"
                            and arrow_pos == 2
                                or start_level) == "returning":
                            start_level = "base"

                    # Pause screen
                    elif game_state == "paused":
                        # Unpause
                        game_state = "active"

                    # Main menu's
                    elif game_state == 'main menu':
                        # Enemies / moves / achievements back to base
                        if main_menu_level != 'base':
                            main_menu_level = 'base'

                # Using escape key to go from being paused to unpaused
                if event.key == pygame.K_ESCAPE:
                    # Pausing
                    if game_state == "active":
                        game_state = "paused"
                        arrow_pos = 1

                    # Unpausing
                    elif game_state == "paused":
                        game_state = "active"
                        arrow_pos = 1

                # Start screen to main menu
                if event.key == pygame.K_RETURN:
                    if game_state == 'start':
                        if start_level == "new player":
                            # Only progress if player has inputted a name
                            if arrow_pos == 1 and player_name != '':
                                game_state = "main menu"
                                main_menu_level = 'base'

                # Selection arrow movement
                if game_state != "active":
                    if event.key == pygame.K_DOWN:
                        arrow_pos += 1
                    elif event.key == pygame.K_UP:
                        arrow_pos -= 1

# ---------- MISCELLANEOUS OPERATIONS ----------

        # Set key_pressed as varible for ease of use
        key_pressed = pygame.key.get_pressed()

        # Blit background
        WINDOW.blit(background, (0 ,0))

        # Set wave_num to each wave
        wave = set_wave(wave_num)

        # Set enemy to each wave
        enemy = set_enemy(enemy)

        # Animate enemies
        for enemy in enemy_group:
            enemy.animate(walk_direction)

        # Keeping the selection arrow in it's boundaries
        if arrow_pos > arrow_limit:
            arrow_pos = 1
        elif arrow_pos <= 0:
            arrow_pos = arrow_limit

        # Checking to enable ultimate status
        if ultimate_charge >= 100:
            ultimate_status = True
        else:
            ultimate_status = False

# ---------- GAME STATES ----------

        # Start
        if game_state == "start":
            arrow_limit = start_screen(arrow_limit)

        # Main menu
        elif game_state == "main menu":
            (arrow_limit, countdown, last_update_time, bid_num
             ) = main_menu(
                    arrow_limit, countdown, last_update_time, bid_num)
            achievements.ach_ban_x = -520
            achievements.run_achievements = 0
            (wave_num, ultimate_charge, cooldown, countdown
             ) = reset(wave_num, ultimate_charge, cooldown, countdown)

        # Active
        elif game_state == "active":
            # Cooldown animation
            cooldown, cooldown_charge = on_cooldown(cooldown, cooldown_charge)

            enemy_x, enemy_y = wave.enemy_spawn()
            enemy_group.draw(WINDOW)
            enemy_group.update()

            # Blit game ui
            active_ui_blit(key_pressed, wave)
            run_achievements = achievements.check(
                runs_completed, enemies_defeated, wave_num)

            countdown = 6

            # Check if player is dead
            if player.health <= 0:
                # Switch to death screen
                game_state = "dead"
                total_runs += 1

            # Check if all enemies in a wave have been defeated
            if wave.enemies_left == 0 and wave_num < 4:
                # Set up next wave
                wave_num += 1
                player.health = 100
                enemy_group.empty()
                ultimate_charge = 0
                cooldown_charge = 0
                inputs = []
                # Switch to in-between countdown
                game_state = 'inbetween'

            # Check if player has met conditions to win game
            elif wave.enemies_left == 0 and wave_num == 4:
                # Increase stats
                total_runs += 1
                runs_completed += 1
                # Switch to win screen
                game_state = 'win'

        # Paused
        elif game_state == "paused":
            # Blit pause screen
            arrow_limit = pause_screen(arrow_limit)
            ach_ban_x = achievements.animation()

        # Inbetween
        elif game_state == 'inbetween':
            (game_state, countdown, last_update_time
             ) = inbetween(game_state, countdown, last_update_time)

        # Dead
        elif game_state == "dead":
            arrow_limit = death_screen(arrow_limit)
            # Play achievement animation if needed
            ach_ban_x = achievements.animation()

        # Win
        elif game_state == 'win':
            arrow_limit = win(arrow_limit)
            # Play achievement animation if needed
            ach_ban_x = achievements.animation()

# ---------- UPDATES ----------

        display.update_display()
        CLOCK.tick(FRAME_RATE)
        pygame.display.update()
