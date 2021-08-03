class SharedData:
    def __init__(self):
        self.data = {}

    def put(self, id, value):
        self.data[f'{id}'] = value

    def create(self, id):
        value = {}
        self.data[f'{id}'] = value
        return value

    def get(self, id):
        key = f'{id}'
        if key in self.data:
            return self.data[key]
        else:
            return None

    def getOrCreate(self, id):
        value = self.get(id)
        if value == None:
            value = self.create(id)
        return value

    def saveData(self, dataRecorder):
        dataRecorder.record('data', self.data)
