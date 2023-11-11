from models import Thread 

class ThreadReporistory:
    def __init__(self) -> None:
        self.__data = []
    
    def add(self, t: Thread) -> None:
        self.__data.append(t)
    
    def get_all(self):
        return self.__data