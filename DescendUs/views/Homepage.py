import pygame
import os
import webbrowser

from .. import objects
from .. import _globals


class Homepage:

    def __init__(self):
        self.homepage = pygame.Rect(0, 0, _globals.Window.WIDTH, _globals.Window.HEIGHT)
        self.background = pygame.image.load(os.path.join(_globals.Game.ASSETS_DIR, 'titlescreen.png'))


    def show(self, surface: pygame.Surface):
        """
        Render the homepage to the screen.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to render the homepage onto
        """

        # Set background
        surface.blit(self.background, (0, 0))

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

        title_text = 'Descend Us'
        rendered_title = _globals.Font.TITLE_FONT.render(title_text, False, _globals.Color.WHITE)
        title_position = (self.homepage.centerx - (rendered_title.get_width() / 2), 0)

        surface.blit(rendered_title, title_position)

        # Play button
        self.play_button = objects.Button("Play")
        self.play_button.draw(surface, (self.homepage.centerx - (self.play_button.get_width() / 2), self.homepage.centery - 40))

        # Instructions button
        self.instructions_button = objects.Button("Instructions")
        self.instructions_button.draw(surface, (self.homepage.centerx - (self.instructions_button.get_width() / 2), self.homepage.centery + 40))


    def _handle_event(self):
        ev = pygame.event.poll()

        if self.play_button.is_pressed(ev):
            # TODO: Handle play button press
            pass

        # Open instructions page on button click
        if self.instructions_button.is_pressed(ev):
            instructions_path = os.path.join(_globals.Game.ASSETS_DIR, 'descendus.html')
            webbrowser.open(f'file://{instructions_path}')