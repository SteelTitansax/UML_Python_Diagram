from abc import ABC, abstractmethod

class NetworkInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def transfer(self):
        pass


class RealNetwork(NetworkInterface):

    def connect(self):
        # connect to something for real
        return

    def transfer(self):
        # transfer a bunch of data
        return


class FakeNetwork(NetworkInterface):

    def connect(self):
        # don't actually connect to anything!
        return

    def transfer(self):
        # don't transfer anything!
        return