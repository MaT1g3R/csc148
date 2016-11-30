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
import math
import pygame
from tree_data import FileSystemTree
from population import PopulationTree

# Screen dimensions and coordinates
ORIGIN = (0, 0)
WIDTH = 1024
HEIGHT = 720
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
        pygame.Surface.fill(screen, i[1], i[0])
        # pygame.draw.rect(screen, i[1], i[0])
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
        # Mouse events
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            current_color = screen.get_at(pos)[:3]
            _mouse_event(selected_leaf, event, tree, current_color)
        # Keyboard events
        if event.type == pygame.KEYUP:
            _keyboard_event(selected_leaf, event)

        # rendering event with path
        if selected_leaf != [] and selected_leaf != [None]:
            render_display(screen, tree,
                           selected_leaf[0].get_path_and_size())
        # rendering empty
        else:
            render_display(screen, tree, '')


def _mouse_event(selected_leaf, event, tree, current_color):
    """ helper to process mouse events
    @type selected_leaf: list[FileSystemTree | PopulationTree]
    @type event: pygame.event
    @type tree: FileSystemTree | PopulationTree
    @type current_color: (int, int, int)
    @rtype: None
    """
    if event.button == 1:  # left click
        # nothing is selected
        if selected_leaf == []:
            selected_leaf.append(tree.get_item_by_color(current_color))
        # Deselect event
        elif selected_leaf[0] == tree.get_item_by_color(current_color):
            selected_leaf.clear()
        # General
        else:
            selected_leaf.clear()
            selected_leaf.append(tree.get_item_by_color(current_color))
    elif event.button == 3:  # right click
        deleting = tree.get_item_by_color(current_color)
        # clear selected if deleted == selected
        if selected_leaf != []:
            if deleting == selected_leaf[0]:
                selected_leaf.clear()
        if deleting is not None:
            tree.delete_item(deleting)


def _keyboard_event(selected_leaf, event):
    """ helper to process mouse events
    @type selected_leaf: list[FileSystemTree | PopulationTree]
    @type event: pygame.event
    @rtype: None
    """
    if selected_leaf != []:
        changed_size = math.ceil(selected_leaf[0].data_size / 100)
        if event.key == pygame.K_UP:
            selected_leaf[0].re_calculate_size(changed_size)
        elif event.key == pygame.K_DOWN:
            selected_leaf[0].re_calculate_size(-changed_size)


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
    python_ta.check_all(config='pylintrc.txt')

    # To check your work for Tasks 1-4, try uncommenting the following function
    # call, with the '' replaced by a path like
    # 'C:\\Users\\David\\Documents\\csc148\\assignments' (Windows) or
    # '/Users/dianeh/Documents/courses/csc148/assignments' (OSX)
    # _macdr = '/Users/PeijunsMac/Desktop/csc148'
    run_treemap_file_system('A:/Python Projects/csc148 _backup')
    # run_treemap_file_system('/Users/PeijunsMac/Desktop/mkv')
    # run_treemap_file_system('/Users/PeijunsMac/Desktop/csc148/assignments')

    # To check your work for Task 5, uncomment the following function call.
    # run_treemap_population()
    # import os
    # EXAMPLE_PATH = os.path.join('example-data', 'B')
    # run_treemap_file_system(EXAMPLE_PATH)
