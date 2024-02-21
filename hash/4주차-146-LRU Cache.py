from collections import OrderedDict
class LRUCache:
    
    def __init__(self, capacity: int):
        self.__capacity=capacity
        self.__cache=OrderedDict()

    def get(self, key: int) -> int:
        value=self.__cache.get(key,-1)
        if value !=-1: 
            self.__cache.move_to_end(key,last=True) 
        return value
        
    def put(self, key: int, value: int) -> None:
        if self.__cache.get(key,False): 
            self.__cache.move_to_end(key,last=True) 
        elif len(self.__cache)==self.__capacity: 
            self.__cache.popitem(last=False) # FIFO           
        self.__cache[key]=value 