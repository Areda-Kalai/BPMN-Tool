import xml.etree.ElementTree as et
from models.bpmn.bpmnelement import BPMNElement
from helpers.stringhelper import camel_case, to_pretty_xml

class Container(BPMNElement):

    def __init__(self, **args):
        BPMNElement.__init__(self, **args)

        self.elements = {}

        self.ignore_attrs('elements')

    def add(self, name, *items):
        # Initialize an empty list
        if name not in self.elements:
            self.elements[name] = []
        # Add element after checking if it exists
        for i in items:
            if i not in self.elements[name]:
                self.elements[name].append(i)

    def remove(self, name, item):
        if name in self.elements:
            if item in self.elements[name]:
                self.elements[name].remove(item)

    def nokey_remove(self, item):
        for key in self.elements:
            if item in self.elements[key]:
                self.remove(key, item)

    def serialize(self):
        element = BPMNElement.serialize(self)
        # For each element in the dictionary of lists..
        for key in self.elements:
            if key not in ['lane', 'message']:
                for i in self.elements[key]:
                    element.append(i.serialize())
                    if i.__class__.__name__ == 'DataObject':
                        element.append(i.reference.serialize())
        return element
