import pygame
import os
import random

from .. import objects
from .. import _globals
from .. import views


class Game:

    def __init__(self):
        """
        Change view to game.
        """

        self.rect = pygame.Rect(0, 0, _globals.Window.WIDTH, _globals.Window.HEIGHT)
        self.background = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'background.png'))

        _globals.Music.play(_globals.Music.START_SFX_PATH)


    def show(self, surface: pygame.Surface):
        """
        Render the page to the screen.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to render the page onto
        """

        # Set background
        surface.blit(self.background, (0, 0))

        # Play music
        if not pygame.mixer.music.get_busy():
            _globals.Music.play(_globals.Music.BACKGROUND_MUSIC_PATH, infinite=True)

        self._draw(surface)
        self._handle_event()


    def _draw(self, surface: pygame.Surface):
        """
        Draw components to the screen.

        This method is private because it is automatically called in Homepage.show()

        Parameters
        ----------

        surface: pygame.Surface
            the surface to render the components onto
        """

        # Display Earth
        if not _globals.Earth.earth:
            _globals.Earth.earth = objects.Earth()

        earth = _globals.Earth.earth
        earth.draw(surface)

        # Display player
        if not _globals.Game.player:
            _globals.Game.player = objects.Player(surface, self.rect)

        self.player = _globals.Game.player
        self.player.draw()

        # Display lasers
        for laser in _globals.Game.lasers:
            laser.draw(surface)

        # Display amount of ammo
        rendered_ammo_text = _globals.Font.TEXT_FONT.render(f'Ammo: {_globals.Game.ammo}', False, _globals.Color.WHITE)
        surface.blit(rendered_ammo_text, ( _globals.Window.WIDTH - rendered_ammo_text.get_width(), 0 ))

        # Display km to Earth
        rendered_km_text = _globals.Font.TEXT_FONT.render(f'KM to Earth: {int(_globals.Game.km_to_earth)}', False, _globals.Color.WHITE)
        surface.blit(rendered_km_text, (0, 0))

        # Display HP
        rendered_hp_text = _globals.Font.TEXT_FONT.render(f'HP: {_globals.Game.hp}', False, _globals.Color.WHITE)
        surface.blit(rendered_hp_text, (0, 30))

        # Generate collidable (asteroid / ammo)
        new_collidable = self._generate_collidable()
        if new_collidable:
            _globals.Game.collidables.append(new_collidable)

        # Display collidables
        for collidable in _globals.Game.collidables:
            collidable.draw(surface)

        # Display win screen
        if _globals.Game.won:
            win_image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'win_screen.png'))
            surface.blit(win_image, ( 0 + (surface.get_width() - win_image.get_width())/2, 400 ))

        # Display lose screen
        if _globals.Game.lost:
            lose_image = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'lose_screen.png'))
            surface.blit(lose_image, ( 0 + (surface.get_width() - lose_image.get_width())/2, 400 ))

        # Display play again screen
        if _globals.Game.won or _globals.Game.lost:
            self.play_again_button = objects.Button('Play again?')
            self.play_again_button.draw(surface, (surface.get_width()/2 - self.play_again_button.get_width()/2, 325))


    def _handle_event(self):
        ev = pygame.event.poll()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            # On mouse click, shoot laser
            if self.player.ammo > 0 and (not _globals.Game.won and not _globals.Game.lost):
                self.player.gun.shoot_laser()
                _globals.Game.ammo -= 1

        for collidable in _globals.Game.collidables:

            # Handle collisions
            if collidable.has_collided(self.player):

                # Regenerate ammo
                if isinstance(collidable, objects.Collidable.Ammo):
                    _globals.Game.ammo += 10
                    _globals.Game.collidables.remove(collidable)

                # Hit asteroid
                elif isinstance(collidable, objects.Collidable.Asteroid) and collidable.can_collide:
                    _globals.Game.hp -= 5
                    collidable.collided_image_change()

            # Laser shot asteroid
            if isinstance(collidable, objects.Collidable.Asteroid) and collidable.can_collide:
                asteroid_shot_laser = collidable.has_been_shot()
                if asteroid_shot_laser:

                    _globals.Game.collidables.remove(collidable)
                    _globals.Game.lasers.remove(asteroid_shot_laser)

                    # Descend 50 km
                    _globals.Game.km_to_earth -= 50

        # Descend at regular pace
        if not _globals.Game.won and not _globals.Game.lost:
            _globals.Game.km_to_earth -= 1 / _globals.Window.FPS

        if _globals.Game.km_to_earth <= 0:
            self._win()

        if self.player.has_died():
            self._lose()


        # Handle play again
        try:
            if self.play_again_button.is_pressed(ev):
                pygame.mixer.music.unload()
                self.clear_global_variables()
                _globals.Game.view = views.Homepage()
                return
        except AttributeError:
            # If button does not exist, ignore
            pass


    def _generate_collidable(self):
        """
        Randomly generate asteroid or laser ammo pack.

        Random chance:
            1 in 50 - asteroid
            1 in 100 - laser

        Random chance once per frame (60 times per second).

        Does not generate if the player is close to Earth (20 km).

        Returns
        ----------
        
        DescendUs.objects.Collidable.Asteroid | DescendUs.objects.Collidable.Ammo | None
            the collidable, if randomly generated, or none
        """

        if _globals.Game.km_to_earth > 20 and not _globals.Game.lost:

            if random.randint(0, 50) == 1:
                return objects.Collidable.Asteroid( (random.randint(0, _globals.Window.WIDTH), _globals.Window.HEIGHT) )
            elif random.randint(0, 100) == 1:
                return objects.Collidable.Ammo( (random.randint(0, _globals.Window.WIDTH), _globals.Window.HEIGHT) )


    def _win(self):
        """
        Handle game win.
        """

        if not _globals.Game.won:
            _globals.Music.play(_globals.Music.WIN_SFX_PATH)

        _globals.Game.km_to_earth = 0
        _globals.Game.won = True


    def _lose(self):
        """
        Handle game loss.
        """

        if not _globals.Game.lost:
            _globals.Music.play(_globals.Music.LOSE_SFX_PATH)

        _globals.Game.hp = 0
        _globals.Game.lost = True

    
    @staticmethod
    def clear_global_variables():
        """
        Restore all global variables to the original.
        """

        _globals.Game.view = None
        _globals.Game.player = None
        _globals.Game.ammo = 10
        _globals.Game.hp = 100
        _globals.Game.lasers = []
        _globals.Game.collidables = []
        _globals.Game.km_to_earth = 1000
        _globals.Game.won = False
        _globals.Game.lost = False
        _globals.Earth.earth = None