#!/usr/bin/python3

class myDictionary:
  workshopDict = {"names": [], "gender": []}

  def __init__(self):
    print("Creating a Dictionary")


# the keyName is the key you are adding to
# the newVal is the item you want to add to the list
  def addVal(self, keyName, newVal):
    """to complete this method use what you learned to add an item to a dictionary along with the append method for a list, then print the dictionary"""
    self.workshopDict.update({keyName : newVal})
    for (key, value) in self.workshopDict.items():

      print(key, " :: ", value)
    
    pass


# the newKey parameter is the name of the new key to be added
# the valueType parameter of this key will default to an empty list
  def addKey(self, newKey, valueType):
    """To complete this method use what you learned about adding a key to the dictionary, then print the dictionary. """
    self.workshopDict[newKey] = valueType
    for (key, value) in self.workshopDict.items():

      print(key, " :: ", value)
    
    pass


# keyToDRemove is the name of the key to remove
  def deleteKey(self, keyToRemove):
    """to complete this method use what we learned to remove a key from a dictionary, then print the dictionary"""
    del self.workshopDict[keyToRemove]
    for (key, value) in self.workshopDict.items():

      print(key, " :: ", value)
    
    pass


def main():
  print("initializing the myDictionary class to call in main")
  thisDict = myDictionary()

  print("adding names and genders to the list, in the dictionary")
  thisDict.addVal("names", "Abigail")
  thisDict.addVal("names", "Bryan")
  thisDict.addVal("names", "Glen")
  thisDict.addVal("names", "Mary")
  thisDict.addVal("gender", "female")
  thisDict.addVal("gender", "male")
  thisDict.addVal("gender", "male")
  thisDict.addVal("gender", "female")

  print("adding a new key to the dictionary with a default value type of an empty list")
  thisDict.addKey("age", [])

  print("adding values to the list associated with the new key that was added")
  thisDict.addVal("age", 33)
  thisDict.addVal("age", 21)

  print("removing the specified key from the dictionary")
  thisDict.deleteKey("gender")



if __name__ == "__main__":
  main()