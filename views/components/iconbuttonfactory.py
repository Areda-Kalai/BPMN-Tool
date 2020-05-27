from resources.colors import *
from views.components.iconbutton import IconButton

def MainButton(master, text, iconPath: str, btnCmd = None):
    return IconButton(master, text, '-size 11 -weight bold', teal, 'resources/icons/ui/' + iconPath, 17, {'bg': teal, 'fg': '#ffffff'}, teal, 40, btnCmd, highlightbackground=border, highlightthickness=1, padx=5, pady=10, bg='#ffffff')

def SecondaryButton(master, text, iconPath: str, btnCmd = None):
    return IconButton(master, text, '-size 11 -weight bold', white, 'resources/icons/ui/' + iconPath, 17, {'fg': teal, 'bg': white, 'config': {'highlightbackground':border, 'highlightthickness':1}}, teal, 40, btnCmd, padx=5, pady=10, bg=teal)