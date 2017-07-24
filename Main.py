from DMG.CreateDMG import CreateDMG
from Graph.CreateGraph import CreateGraph

DMG = [
    CreateDMG('D:\\result\\2017-07\\DMG01_0703-0715.txt',
              'D:\\result\\2017-07\\DMG01_0703-0722.xlsx'),
    CreateDMG('D:\\result\\2017-07\\DMG02_0703-0715.txt',
              'D:\\result\\2017-07\\DMG02_0703-0722.xlsx')]
graph = CreateGraph(DMG)
