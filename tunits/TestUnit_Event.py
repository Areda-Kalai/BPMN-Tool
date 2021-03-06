from models.bpmn.event import Event
from models.bpmn.enums.eventtype import EventType
from models.bpmn.enums.eventdefinition import EventDefinition
import xml.etree.ElementTree as et

def run():
    
    e = Event(type=EventType.IntermediateCatch, definition=EventDefinition.Message)
    element = e.serialize()
    # print (element.tag)

    for event_type in list(EventType):
        for event_definition in list(EventDefinition):
            event_element = Event(type=event_type, definition=event_definition)
            print (et.tostring(event_element.serialize()))

