inventory = []

def addtoinventory(item):
  inventory.append(item)

def removefrominventory(item):
  if item in inventory:
    inventory.remove(item)