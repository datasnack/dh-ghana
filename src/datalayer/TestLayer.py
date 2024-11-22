from datalayers.datasources.base_layer import BaseLayer

class Testlayer(BaseLayer):
    def __init__(self) -> None:
        super().__init__()

    def download(self):
        raise NotImplementedError

    def process(self):
        raise NotImplementedError
