from pygame import init, quit, Color, Surface, Rect, KEYUP, K_SPACE, K_RETURN, K_z, K_LSHIFT, K_RSHIFT, K_CAPSLOCK, K_BACKSPACE
from pygame.display import set_caption, set_mode, update
from pygame.font import SysFont, Font
from pygame.event import poll
from pygame.key import get_pressed, name


class Window:
    # A Window represents a display window with a title bar,
    # close box and interior drawing surface.

    def __init__(self, title, width, height):
        # Create and open a window to draw in.
        # - self is the new Window
        # - title is the str title of the window
        # - width is the int pixel width of the window
        # - height is the int pixel height of the window

        init()
        self.__surface__ = set_mode((width, height), 0, 0)
        set_caption(title)
        self.__font_name__ = ''
        self.__font_size__ = 18
        self.__font__ = SysFont(self.__font_name__, self.__font_size__, True)
        self.__font_color__ = 'white'
        self.__bg_color__ = 'black'
        self.__auto_update__ = True

    def close(self):
        # Close the window
        # - self is the Window

        quit()

    def set_font_name(self, name):
        # Set the name of the window font used to draw strings
        # - self is the Window
        # - name is the str name of the font

        self.__font_name__ = name
        self.__font__ = SysFont(self.__font_name__, self.__font_size__, True)

    def set_font_size(self, point_size):
        # Set the point size of the window font used to draw strings
        # - self is the Window
        # - point_size is the int point size of the font

        self.__font_size__ = point_size
        self.__font__ = SysFont(self.__font_name__, self.__font_size__, True)

    def set_font_color(self, color_string):
        # Set the font color used to draw in the window
        # - self is the Window
        # - color_string is the str name of the font color

        self.__font_color__ = color_string

    def set_bg_color(self, color_string):
        # Set the background color used to draw in the window
        # - self is the Window
        # - color_string is the str name of the background color

        self.__bg_color__ = color_string

    def set_auto_update(self, true_false):
        # Set the background color used to draw in the window
        # - self is the Window
        # - true_or_false is a Boolean indicating if auto update should be on or off

        self.__auto_update__ = true_false

    def get_font_height(self):
        # Return the int pixel height of the current font.
        # - self is the Window

        return self.__font__.size('')[1]

    def get_font_color(self):
        # Return a str that represents the current window
        # font color
        # - self is the Window

        return self.__font_color__

    def get_bg_color(self):
        # Return a str that represents the current window
        # background color
        # - self is the Window

        return self.__bg_color__

    def get_width(self):
        # Return the int pixel width of the window's drawable
        # interior surface
        # - self is the Window

        return self.__surface__.get_width()

    def get_height(self):
        # Return the int pixel height of the window's drawable
        # interior surface
        # - self is the Window

        return self.__surface__.get_height()

    def clear(self):
        # Erase the window contents
        # - self is the Window

        if self.__auto_update__:
            update()

    def get_surface(self):
        # Return the Pygame.Surface object that represents the
        # interior drawing surface of the window
        # - self is the Window

        return self.__surface__

    def draw_string(self, string, x, y, bg):
        # Draw a string in the window using the current font and
        # colors
        # - self is the Window
        # - string is the str object to draw
        # - x is the int x coord of the upper left corner of the
        #   string in the window
        # - y is the int y coord of the upper left corner of the
        #   string in the window

        text_image = self.__font__.render(string, True, Color(self.__font_color__), bg)
        self.__surface__.blit(text_image, (x, y))
        if self.__auto_update__:
            text_rect = Rect((x, y), text_image.get_size())
            update(text_rect)

    def input_string(self, prompt, x, y):
        # Draw a prompt string in the window using the current font
        # and colors. Check keys pressed by the user until an enter
        # key is pressed and return the sequence of key presses as a
        # str object.
        # - self is the Window
        # - prompt is the str to display
        # - x is the int x coord of the upper left corner of the
        #   string in the window
        # - y is the int y coord of the upper left corner of the
        #   string in the window

        key = K_SPACE
        answer = ''
        while key != K_RETURN:
            self.draw_string(prompt + answer + '    ', x, y)
            if not self.__auto_update__:
                update()
            key = self._get_key()
            key_state = get_pressed()
            if (K_SPACE <= key <= K_z):
                if key == K_SPACE:
                    letter = ' '
                else:
                    letter = name(key)
                if key_state[K_LSHIFT] or key_state[K_RSHIFT] or key_state[K_CAPSLOCK]:
                    letter = letter.upper()
                answer = answer + letter
            if key == K_BACKSPACE:
                answer = answer[0:len(answer)-1]
        return answer

    def get_string_width(self, string):
        # Return the int pixel width of the string using the current
        # font.
        # - self is the Window
        # - string is the str object

        return self.__font__.size(string)[0]

    def update(self):
        # Update the window by copying all drawn objects from the
        # frame buffer to the display.
        # - self is the Window

        update()

    def _get_key(self):
        # Poll the events until the user presses a key and return it.
        # Discard all other events.
        # - self is the Window

        event = poll()
        while event.type != KEYUP:
            event = poll()
        return event.key
