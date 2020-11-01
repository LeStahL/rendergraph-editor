class RenderPass:
    idCounter = 0

    Buffer = 'Buffer'
    Screen = 'Screen'

    def __init__(self):
        self.id = self.idCounter
        self.idCounter += 1
        self.name = "Buffer-" + str(self.id)
        self.type = self.Buffer
        self.bufferUniforms = dict()
        return

    def addBufferUniform(self, uniformName, buffer):
        self.bufferUniforms[uniformName] = buffer
