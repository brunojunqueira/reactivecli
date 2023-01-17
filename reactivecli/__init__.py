from reactivecli.bin.elements.Menu import Menu
from reactivecli.bin.elements.Input import Input
from reactivecli.bin.elements.Option import Option
from reactivecli.bin.elements.Text import Text
from reactivecli.bin.elements.Title import Title
from reactivecli.bin.elements.Element import Element
from reactivecli.bin.elements.Link import Link
from reactivecli.bin.text import color, background


def create_root(callback, dev=False):
    menu = Menu(callback, dev)
    menu.render()
