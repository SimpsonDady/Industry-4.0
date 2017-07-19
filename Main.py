from DMG.CreateDMG import CreateDMG
from Graph.CreateGraph import CreateGraph

DMG = [CreateDMG('DMG01_0703-0707.txt', 'DMG01_0703-0707.xlsx'), CreateDMG('DMG02_0703-0707.txt', 'DMG02_0703-0707.xlsx')]
graph = CreateGraph(DMG)
