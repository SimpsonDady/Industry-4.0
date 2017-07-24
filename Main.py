from DMG.CreateDMG import CreateDMG
from Graph.CreateGraph import CreateGraph

DMG = [
    CreateDMG('C:\\Users\\User\\Google 雲端硬碟\\漢翔-Industry4.0\\2017-07\\DMG01_0708-0716.txt',
              'C:\\Users\\User\\Google 雲端硬碟\\漢翔-Industry4.0\\2017-07\\DMG01_0703-0707.xlsx'),
    CreateDMG('C:\\Users\\User\\Google 雲端硬碟\\漢翔-Industry4.0\\2017-07\\DMG02_0708-0716.txt',
              'C:\\Users\\User\\Google 雲端硬碟\\漢翔-Industry4.0\\2017-07\\DMG02_0703-0707.xlsx')]
graph = CreateGraph(DMG)
