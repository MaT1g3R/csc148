"""Assignment 2: Treemap Visualiser

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code to run the treemap visualisation program.
It is responsible for initializing an instance of AbstractTree (using a
concrete subclass, of course), rendering it to the user using pygame,
and detecting user events like mouse clicks and key presses and responding
to them.
"""
import pygame
from tree_data import FileSystemTree
from population import PopulationTree


# Screen dimensions and coordinates
ORIGIN = (0, 0)
WIDTH = 1024
HEIGHT = 768
FONT_HEIGHT = 30                       # The height of the text display.
TREEMAP_HEIGHT = HEIGHT - FONT_HEIGHT  # The height of the treemap display.

# Font to use for the treemap program.
FONT_FAMILY = 'Consolas'


def run_visualisation(tree):
    """Display an interactive graphical display of the given tree's treemap.

    @type tree: AbstractTree
    @rtype: None
    """
    # Setup pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Render the initial display of the static treemap.
    render_display(screen, tree, '')

    # Start an event loop to respond to events.
    event_loop(screen, tree)


def render_display(screen, tree, text):
    """Render a treemap and text display to the given screen.

    Use the constants TREEMAP_HEIGHT and FONT_HEIGHT to divide the
    screen vertically into the treemap and text comments.

    @type screen: pygame.Surface
    @type tree: AbstractTree
    @type text: str
        The text to render.
    @rtype: None
    """
    # First, clear the screen
    pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                     (0, 0, WIDTH, HEIGHT))
    treemap = tree.generate_treemap((0, 0, WIDTH, TREEMAP_HEIGHT))
    for i in treemap:
        if i == treemap[-1]:  # Treatment of the very last block
            x, y, width, height = i[0]
            width += WIDTH - (x+width)
            height += HEIGHT - (y + height + FONT_HEIGHT)
            pygame.draw.rect(screen, i[1], (x, y, width, height))
        else:
            pygame.draw.rect(screen, i[1], i[0])
    _render_text(screen, text)
    # This must be called *after* all other pygame functions have run.
    pygame.display.flip()


def _render_text(screen, text):
    """Render text at the bottom of the display.

    @type screen: pygame.Surface
    @type text: str
    @rtype: None
    """
    # The font we want to use
    font = pygame.font.SysFont(FONT_FAMILY, FONT_HEIGHT - 8)
    text_surface = font.render(text, 1, pygame.color.THECOLORS['white'])

    # Where to render the text_surface
    text_pos = (0, HEIGHT - FONT_HEIGHT + 4)
    screen.blit(text_surface, text_pos)


def event_loop(screen, tree):
    """Respond to events (mouse clicks, key presses) and update the display.

    Note that the event loop is an *infinite loop*: it continually waits for
    the next event, determines the event's type, and then updates the state
    of the visualisation or the tree itself, updating the display if necessary.
    This loop ends when the user closes the window.

    @type screen: pygame.Surface
    @type tree: AbstractTree
    @rtype: None
    """
    # We strongly recommend using a variable to keep track of the currently-
    # selected leaf (type AbstractTree | None).
    # But feel free to remove it, and/or add new variables, to help keep
    # track of the state of the program.
    selected_leaf = []
    while True:
        # Wait for an event
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        # Remember to call render_display if any data_sizes change,
        # as the treemap will change in this case.
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            current_color = screen.get_at(pos)[:3]
            if event.button == 1:  # left click
                selected_leaf.clear()
                selected_leaf += [tree.get_item_by_color(current_color)]
                if selected_leaf[0] is None:
                    render_display(screen, tree, '')
                else:
                    render_display(screen, tree, str(selected_leaf[0]._root) + ' ' + str(selected_leaf[0].data_size))
            elif event.button == 3:  # right click
                if selected_leaf != []:
                    if tree.get_item_by_color(current_color) == selected_leaf[0]:
                        selected_leaf.clear()
                deleting = tree.get_item_by_color(current_color)
                if deleting is not None:
                    deleted_size = -deleting.data_size
                    deleting.re_calculate_size(deleted_size)
                    tree.delete_item(deleting)
                    render_display(screen, tree, '')


def run_treemap_file_system(path):
    """Run a treemap visualisation for the given path's file structure.

    Precondition: <path> is a valid path to a file or folder.

    @type path: str
    @rtype: None
    """
    file_tree = FileSystemTree(path)
    run_visualisation(file_tree)


def run_treemap_population():
    """Run a treemap visualisation for World Bank population data.

    @rtype: None
    """
    pop_tree = PopulationTree(True)
    run_visualisation(pop_tree)


if __name__ == '__main__':
    import python_ta
    # Remember to change this to check_all when cleaning up your code.
    python_ta.check_errors(config='pylintrc.txt')

    # To check your work for Tasks 1-4, try uncommenting the following function
    # call, with the '' replaced by a path like
    # 'C:\\Users\\David\\Documents\\csc148\\assignments' (Windows) or
    # '/Users/dianeh/Documents/courses/csc148/assignments' (OSX)
    macdr = '/Users/PeijunsMac/Desktop/csc148'
    windr = 'A:/Python Projects/csc148/'


    run_treemap_file_system(windr)

    # To check your work for Task 5, uncomment the following function call.
    # run_treemap_population()
