from models.bpmn.bpmnelement import BPMNElement

class Property(BPMNElement):

    def __init__(self, **args):
        BPMNElement.__init__(self, **args)