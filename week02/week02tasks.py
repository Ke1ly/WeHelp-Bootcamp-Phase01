#Task01

def find_and_print(messages, current_station):
    stations = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xiaobitan",
    "Qizhang",
    "Xindian City Hall",
    "Xindian"]
    # 從 dict 中抓取每個人的訊息，做成 only_messages list 
    only_messages=list(messages.values())
    
    # 從每個人的訊息中抓取站名，並計算站名與給定車站之間的距離，存入 difference 中
    difference=[]
    for message in only_messages:
        for station in stations:
            if station in message:
                difference.append(abs(stations.index(station)-stations.index(current_station)))
    # 取 difference list 中值最小者，並印出它的人名
    print(list(messages.keys())[difference.index(min(difference))])


messages = {
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages,"Songshan") # print Copper
find_and_print(messages,"Qizhang") # print Leslie
find_and_print(messages,"Ximen") # print Bob
find_and_print(messages,"Xindian City Hall") # print Vivian

#Task02
consultants = [
{"name":"John","rate":4.5,"price":1000},
{"name":"Bob","rate":3,"price":1200},
{"name":"Jenny","rate":3.8,"price":800}]
# 為每位 consultants 建立可預約時間表
for consultant in consultants:
    consultant.update({"time":[
    8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
  ]})

def book(consultants, hour, duration, criteria):
     # 建立預約時段 list，篩選出有空的諮商師，將其 criteria 儲存至 candidates list
    candidates=[]
    appointment_time=[]
    for i in range(duration):
        appointment_time.append(hour+i)
    for consultant in consultants:
        if all(ele in consultant["time"] for ele in appointment_time):
            candidates.append(consultant[criteria])

    # 從 candidates list 中依據不同 criteria，篩選出最適者，並將其被預約時段刪除
    if candidates == []:
        print("No Service")
    else:
        if criteria == "price":
            value = min(candidates)
        else:
            value = max(candidates)
        for consultant in consultants:
            if consultant[criteria]==value:
                print (consultant["name"])
                del consultant["time"][consultant["time"].index(hour):consultant["time"].index(hour + duration)]

book(consultants, 15, 1,"price") # Jenny
book(consultants, 11, 2,"price") # Jenny
book(consultants, 10, 2,"price") # John
book(consultants, 20, 2,"rate") # John
book(consultants, 11, 1,"rate") # Bob
book(consultants, 11, 2,"rate") # No Service
book(consultants, 14, 3,"price") # John

#Task03
def func(*data):
    # 取出所有名字的中間字，與其名字，存入 name_middle_word dict
    name_middle_word={}
    for name in data:
        if len(name) <=3:
            name_middle_word[name]=name[1]
        else:
            name_middle_word[name]=name[2]

    # 從 name_middle_word dict 取出 value，存入 middle_word
    # 再從 middle_word 中取不重複字，回推這個字在 name_middle_word dict 中的 key，將名字打印出來
    middle_word=list(name_middle_word.values())
    specific=""
    for word in middle_word:
        if 0<middle_word.count(word)<2:
            specific=word

    if specific =="":
        print("沒有")
    else:
        print (list(name_middle_word.keys())[list(name_middle_word.values()).index(specific)])

func("彭大牆","陳王明雅","吳明") # print 彭大牆
func("郭靜雅","王立強","郭林靜宜","郭立恆","林花花") # print 林花花
func("郭宣雅","林靜宜","郭宣恆","林靜花") # print 沒有
func("郭宣雅","夏曼藍波安","郭宣恆") # print 夏曼藍波安


#Task04
def get_number(index):
    sum = 0
    i = 0
    while i < index:
        if i%3 == 0 or i%3 == 1:
            sum+=4
        elif i%3==2:
             sum-=1
        i+=1
    print(sum)
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


#Task05
def find(spaces, stat, n):
    available_seats=[spaces[i]*stat[i]for i in range(len(spaces))]
    car_number=[i for i in available_seats if i >=n]
    if not car_number:
        print(-1)
    else:
        print (available_seats.index(min(car_number)))

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2