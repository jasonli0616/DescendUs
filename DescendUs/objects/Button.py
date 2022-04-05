import pygame

from .. import _globals

class Button:

    def __init__(self, text):
        """
        Create a button.

        Parameters
        ----------

        text: str
            the text that is displayed
        """

        self.rendered_text = _globals.Font.TEXT_FONT.render(text, False, _globals.Color.WHITE, _globals.Color.GRAY)


    def draw(self, surface: pygame.Surface, position):
        """
        Draw the button to the screen.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to draw the button onto

        position: list[int | float, int | float]
            the position that the circle is at
        """

        surface.blit(self.rendered_text, position)


    def get_width(self):
        return self.rendered_text.get_width()


    def get_height(self):
        return self.rendered_text.get_height()


    def is_pressed(self, ev: pygame.event.Event):
        """
        Check the events, and return whether or not the button is pressed.

        Counts a press as mouse up, not mouse down.

        Parameters
        ----------

        ev: pygame.event.Event
            the event that has occured

        Returns
        ----------

        bool
            whether or not the button is pressed
        """

        if ev.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            # TODO: Check mouse collision