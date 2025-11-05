from abc import ABC, abstractmethod

class BaseSensor(ABC):
    def __init__(self, name: str, bucket: str):
        self.name = name
        self.bucket = bucket

    @abstractmethod
    def read(self) -> dict:
        """Liefert ein Messwert-Dictionary mit sensor, type, value"""
        pass
