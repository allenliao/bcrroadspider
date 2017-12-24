import json
from sikuli.Sikuli import *


tableList=[]

def readConfig():
    Settings.ObserveScanRate = 0.2# the observer will look every 5 seconds
    buConfigFile = open('buconfig.json','r')
    #buconfigFile.read()
    buConfigStr=buConfigFile.read()
    #print buConfigStr
    
    buConfigObj=json.loads(buConfigStr)
    buurl=buConfigObj['buurl']
    username=buConfigObj['username']
    password=buConfigObj['password']
    print buurl
    openWebSiter(buurl)
    loginAndOpenGame(username,password)

def openWebSiter(buurl):
    openApp(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe "+buurl)
    
def loginAndOpenGame(username,password):
    
    wait("loginBtn.png", 10)
    
    if screenRegion.find("account_cache.png"):
        screenRegion.find("loginBtn.png").click()
    else:
        screenRegion.find("account.png").click()
        type(username)
        screenRegion.find("password.png").click()
        type(password)
        screenRegion.find("loginBtn.png").click()
    
    screenRegion.find("loginConfirmBtn.png").click()
    screenRegion.find("LDRBtn.png").click()#真人娛樂
    screenRegion.find("SAGameBtn.png").click()#沙龍魚樂
    wait("bigRoadView.png", FOREVER)#等大路檢視
    screenRegion.find("bigRoadView.png").click()#多人頭注
    
    
    #TODO:抽到設定檔 
    tableList.append(TableObj("BU002", "Table 1", 195,372,401,95,16,16,6,25))
    tableList.append(TableObj("BU002", "Table 2", 609,372,401,95,16,16,6,25))


    
    #getTableInfo(tableList[0])
    #getTableInfo(tableList[1])
    
    
    
class TableObj:
    tableName="Allen"
    BUCode="BU001"
    tableRegion=Region(194,372,401,95)
    bigRoadRegionList=[]
    bigRoadStrList=[]
    
    bigRoadMaxHCount=0
    bigRoadMaxWCount=0
    def __init__(self, _BUCode, _tableName, startX,startY,
                 tableW,tableH,bigRoadUnitW,bigRoadUnitH,_bigRoadMaxHCount,_bigRoadMaxWCount):
        #直的 有 幾個格子= maxHCount
        #橫的 有 幾個格子= maxWcount
        print(_tableName+" Create TableObj!!")
        self.tableName = _tableName
        self.BUCode = _BUCode
        self.tableRegion=Region(194,372,401,95)
        self.tableRegion.setX(startX)
        self.tableRegion.setY(startY)
        self.tableRegion.setW(tableW)
        self.tableRegion.setH(tableH)
        self.bigRoadMaxHCount=_bigRoadMaxHCount
        self.bigRoadMaxWCount=_bigRoadMaxWCount
        self.createBigRoadRegionUnit(startX,startY,bigRoadUnitW,bigRoadUnitH)
        self.tableRegion.onChange(self.roadChange)#listen road change
        #self.tableRegion.onAppear("countDownStart.png", self.roadChange)#倒數
        self.tableRegion.observe(FOREVER ,background=True)
    
    def roadChange(self, event):
        print(self.tableName+" road Changed!!")
        for y in xrange(0, self.bigRoadMaxHCount): #直6
            for x in xrange(0, self.bigRoadMaxWCount): #橫25
                _region=self.bigRoadRegionList[y][x]
                if _region.exists(Pattern("bankerball.png").similar(0.7),0)!=None :
                    self.bigRoadStrList[y][x]="B"
                elif _region.exists(Pattern("playerball.png").similar(0.7),0)!=None :
                    self.bigRoadStrList[y][x]="P"
                #_region.getLastMatch().highlight()
            print ','.join(self.bigRoadStrList[y])
        #print("self.bigRoadRegionList: "+self.bigRoadRegionList)
                    
                    
        
    def createBigRoadRegionUnit(self, startX,startY,uW,uH):
        self.bigRoadRegionList = []
        self.bigRoadStrList=[]
        px=startX
        py=startY
        for y in xrange(0, self.bigRoadMaxHCount): #直6
            self.bigRoadRegionList.append([])
            self.bigRoadStrList.append([])
            py=startY+(y*uH)
            for x in xrange(0, self.bigRoadMaxWCount): #橫25
                px=startX+(x*uW)
                print '%d _ %d' % (px, py)
                self.bigRoadRegionList[y].append(Region(px,py,uW,uH))
                self.bigRoadStrList[y].append("E")
                #val=str(y)+"_"+str(x)
                #print '%d _ %d = %s' % (x, y, val)
                



def getTableInfo(tableRegion):
    #路紙範圍
    #TODO:抽到設定檔
    print ("getTableInfo!! called")



    
'''
def getName(tableRegion):
    return {
        tableRegion1: "Table 1",
        tableRegion2: "Table 2"
    }.get(tableRegion, "Table 1")    # 'Table 1' is default if tableRegion not found
'''
    

if __name__ == "__main__":
    screenRegion = Screen()
    readConfig()
    #getTableInfo()
    #load config
    #login
    
    #observeFunc(folder_tblRegion)
    #observeFunc(file_tblRegion)