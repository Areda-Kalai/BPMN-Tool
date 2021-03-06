from helpers.stringhelper import camel_case, generate_code
from models.xmlserializable import XMLSerializable
from resources.namespaces import bpmn

import xml.etree.ElementTree as et

class BPMNElement(XMLSerializable):

    def __init__(self, **args):
        self.id = args.get('id', self.get_tag() + '_' + generate_code())
        self.name = self.expects(args, 'name')
        self.ignore = ['ignore']

    def expects(self, args, name, default=None):
        return default if name not in args else args[name]

    def configure(self, **args):
        """
        A setter for the element's attributes, and an alternative for the constructor
        """
        for key in args:
            if hasattr(self, key):
                setattr(self, key, args[key])

    # Add attributes to be ignored in attribute serialization
    def ignore_attrs(self, *args):
        self.ignore = self.ignore + list(args)

    # A default serialization
    def serialize(self):
        e = et.Element(bpmn + self.get_tag())
        # Foreach property in class, add it as an attribute to the element
        for attr in vars(self):
            if attr not in self.ignore and getattr(self, attr) != None:
                e.attrib[attr] = str(getattr(self, attr))
        return e

    # toString
    def __str__(self):
        return str(self.id)

    # get tag
    def get_tag(self):
        return camel_case(self.__class__.__name__)
