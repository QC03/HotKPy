
import keyboard

class HotKPy:

    def __init__(self):
        self.keys = []

    def addHKey(self, keyList: list):
        self.keys.append(keyList)
    
    def getHKey(self) -> list:
        return self.keys

    def removeHKey(self, keyList: list):
        if keyList not in self.keys:
            return
        self.keys.remove(keyList)
    
    def clearHKey(self):
        self.keys.clear()
    
    # Check Key List is HKey
    def isHKey(self, keyList: list) -> bool:
        if not self.keys:
            return False
        for keys in self.keys:
            if len(keys) != len(keyList):
                continue
            if all(key in keys for key in keyList):
                return True
        return False

    # return bool if HKey is Pressed
    def isHKeyPressed(self, keyList: list) -> bool:
        if not self.isHKey(keyList):
            return False
        for key in keyList:
            if not keyboard.is_pressed(key):
                return False
        return True
    
    # Call When HKey is pressed
    def onHKeyPressed(self, keyList: list, callback):
        if not self.isHKey(keyList):
            return
        keyboard.add_hotkey('+'.join(keyList), callback)