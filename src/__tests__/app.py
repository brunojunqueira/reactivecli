from bin.elements.Title import Title
from bin.elements.Text import Text
from bin.elements.Input import Input

def app():
	title = Title("Hello World")
	name_input = Input()
	return [title, Text('Insert Name:'), name_input]
