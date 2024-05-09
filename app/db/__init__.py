from abc import ABC, abstractmethod


class DB(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_one(self, id: str):
        pass

    @abstractmethod
    def delete_one(self, id: str):
        pass

    @abstractmethod
    def update_one(self, id: str, model: any):
        pass

    @abstractmethod
    def create_one(self, model: any):
        pass
