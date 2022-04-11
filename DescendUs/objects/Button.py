import pygame

from .. import _globals

class Button:
    """
    Represents a clickable button, with text.
    """

    def __init__(self, text, position=None):
        """
        Create a button.

        Parameters
        ----------

        text: str
            the text that is displayed

        position: list[int | float, int | float]
            optional: the position that the button is at
        """

        self.rendered_text = _globals.Font.TEXT_FONT.render(text, False, _globals.Color.WHITE, _globals.Color.GRAY)

        if position:
            self.position = position


    def draw(self, surface: pygame.Surface, position):
        """
        Draw the button to the screen.

        Parameters
        ----------

        surface: pygame.Surface
            the surface to draw the button onto

        position: list[int | float, int | float]
            the position that the button is at
        """

        self.position = position
        surface.blit(self.rendered_text, position)


    def get_width(self):
        return self.rendered_text.get_width()


    def get_height(self):
        return self.rendered_text.get_height()


    def is_pressed(self, ev: pygame.event.Event):
        """
        Check the events, and return whether or not the button is pressed.

        When mouse click is released, return whether the mouse position is in the range of the button.

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

            button_x_range = range(int(self.position[0]), int(self.position[0]) + self.get_width())
            button_y_range = range(int(self.position[1]), int(self.position[1]) + self.get_height())

            return (mouse_position[0] in button_x_range) and (mouse_position[1] in button_y_range)