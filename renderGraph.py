import json

class renderGraph:
    def __init__(self):
        self.renderPasses = []
        return

    def addRenderPass(self, renderPass):
        self.renderPasses.append(renderPass)
        return

    def deserialize(self, jsonFile):
        pass

    def serialize(self):
        pass

    def numberOfPasses(self):
        return len(self.renderPasses)

    