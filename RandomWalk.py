
import random
import csv
import pandas as pd

df = pd.read_excel('/Users/hsiehyuanlung/Desktop/新科展顆顆代入值.xlsx')    #讀取代入機率資料



x = 1  #起始x座標
   
y = 1  #起始y座標    
#測試次數 
test = 10000  
#最大移動步數    
movecount = 10000        
fall = 0
Falls = []
direct = None

#移動機率設定
#data = {'L': 1, 'R': 1, 'D': 1, 'U': 1}     

r = 100 #進度條長度


#依權重隨機選擇移動方向
def choice():
    global direct, value_sum
    value_sum = sum(data.values())
    t = random.uniform(0, value_sum)
    for direct, value in data.items():
        t -= value
        if t < 0:
            break

def walk():
    global x, y, fall, movecount, direct
    for i in range(0,movecount):
        choice()
        #print(direct)      #顯示移動方向
        if direct == 'L':
            x -= 1
        elif direct == 'R':
            x += 1
        elif direct == 'D':
            y -= 1
        elif direct == 'U':
            y += 1
        #print(str(x) + ',' + str(y))       #顯示座標
        if x * y == 0:
            fall += 1
            #print('Move : ' + str(i+1))        #顯示行走步數
            #print('Fall : ' + str(fall))       #顯示累積掉落次數
            break

for i in range(len(df)):        #測試不同移動機率
    fall = 0
    print(str(i+1)+ ' / ' + str(len(df))) #顯示測試到第幾個
    data = {'L': df.iat[i,0], 'R': df.iat[i,1], 'D': df.iat[i,2], 'U': df.iat[i,3]}    #將機率資料轉為dict
    print(data)

    for j in range(0,test):
        x = 1
        y = 1
        walk()

        #顯示進度條
        J = j+1
        k = int(test / r)
        q = int(test / k) 
        if J % k == 0:
            print('Progress: {}% '.format(int(J/test*100)),'(' +str(J) +'/' +str(test) +')' ,'▋' * (J // k),end='')
            print('.' * (q - ( J // k )  ) )
        
    Falls.append(fall)

#輸出結果
for i in range(len(df)):       

    data = {'L': df.iat[i,0], 'R': df.iat[i,1], 'D': df.iat[i,2], 'U': df.iat[i,3]}    #將機率資料轉為dict
    print()
    print(data)     #顯示機率設定
    print('Test time :' + str(test))
    print('Max Move :' + str(movecount))
    print('Fall : ' + str(Falls[i]))
    print('P = ' + str(Falls[i]/test))
    print('--------------------------------------------------')


#寫入 CSV 檔案
with open('/Users/hsiehyuanlung/Desktop/RandomWalk.csv', 'a', encoding = 'UTF-8', newline='') as csvFile:
    writer = csv.writer(csvFile)        # 建立 CSV 檔寫入器
    #writer.writerow(['L','R','D','U','測試次數','最多移動步數','掉落次數','掉落機率'])
    writer.writerow([])
    for i in range(len(df)):
        data = {'L': df.iat[i,0], 'R': df.iat[i,1], 'D': df.iat[i,2], 'U': df.iat[i,3]}    #將機率資料轉為dict
        p_fall = Falls[i] / test
        writer.writerow([data['L'],data['R'],data['D'],data['U'],test,movecount,Falls[i],p_fall])
