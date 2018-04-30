import random
#import easygui as g
import os
class Jay():
    def __init__(self):
        # Album list
        self.Jay_Album=['Jay','范特西','范特西EP','八度空间','叶惠美','《寻找周杰伦EP》','《七里香》','《J III(EP)》','《十一月的萧邦》','《依然范特西》','《我很忙》']
    # songs
        self.musicstar_Jay={'Jay':['可爱女人','完美主义','星晴','娘子','斗牛','黑色幽默','伊斯坦堡','印地安老斑鸠','龙卷风','反方向的钟'],
    '范特西':['爱在西元前','爸我回来了','简单爱','忍者','开不了口','上海一九四三','对不起','威廉古堡','双截棍','安静'],
    '范特西EP':['蜗牛','你比从前快乐','世界末日'],
    '八度空间':['半兽人','半岛铁盒','暗号','龙拳','火车叨位去','分裂（内地名离开）','爷爷泡的茶','回到过去','米兰的小铁匠','最后的战役'],
    '叶惠美':['以父之名','懦夫','晴天','三年二班','东风破','你听得到','同一种调调','她的睫毛','爱情悬崖','梯田','双刀'],
    '《寻找周杰伦EP》':['轨迹','断了的弦'],
    '《七里香》':['我的地盘','七里香','借口','外婆','将军','搁浅','乱舞春秋','困兽之斗','园游会','止战之殇'],
    '《J III(EP)》':['飘移','一路向北'],
    '《十一月的萧邦》':['夜曲','蓝色风暴','发如雪','黑色毛衣','四面楚歌','枫','浪漫手机','逆鳞','麦芽糖','珊瑚海'],
    '《依然范特西》':['夜的第七章','听妈妈的话','千里之外','本草纲目','退后','红模仿','心雨','白色风车','迷迭香','菊花台'],
    '《我很忙》':['牛仔很忙','彩虹','青花瓷','阳光宅男','蒲公英的约定','无双','我不配(又名距离)','扯','甜甜的','最长的电影']}
        self.answer_sel=[]

    def musicgame(self):
    
        num0=random.randint(0,10) 
        answer_album=self.Jay_Album[num0]   # the answer album
        answer_song=self.musicstar_Jay[answer_album] # the answer songs
        answer=answer_song[random.randint(0,len(answer_song)-1)] #the answer song
        self.musicstar_Jay.pop(answer_album) # the complete album in addition to the answer album
        other_songs=list(self.musicstar_Jay.values())  # the whole songs except answer album including its songs
        other_songlen=len(other_songs)
        while other_songlen:
            self.answer_sel.extend(other_songs[other_songlen-1])
            other_songlen-=1

        other_sel=random.sample(self.answer_sel,3)
        randomplace=random.randint(0,3)
        other_sel.insert(randomplace,answer) # answer selection
        return [answer,answer_album,other_sel]
class Eason():
    def __init__(self):
        # Album list
        self.Eason_Album=['与我常在','我的快乐时代 ','打得火热','Shall We Dance? Shall We Talk!','反正是我','Special thanks to','U87','我的最好时代','H3M','time flies']
    # songs
        self.musicstar_Eason={'与我常在':['《现场直播》','《与我常在》','《爱没有左右》','《生命有几好》','《抱拥这分钟》','《那一夜有没有雪？》','《伴游》','《跟我走好吗》','《今天等我来》','《敌人》'],
    '我的快乐时代 ':['我的快乐时代','我什么都没有','天下无双','黄金时代','愈想愈无谓','反高潮','时代曲','多一点','相信相依','两种讲法'],
    '婚礼的祝福':['《婚礼的祝福》','《拔河》','《我的开始在这里》','《转机》','《My Girl》','《掏空》','《伤心证明书》','《Just Between The Two Of Us》','《存在》'],
    '打得火热':['《K歌之王》','《打得火热》','《新广告歌》','《低等动物》','《绵绵》','《美丽谎言》','《吹微风》','《温室效应》','《活跃症》'],
    'Shall We Dance? Shall We Talk!':['嚟喇','Shall We Dance','Shall We Talk','2001太空漫游','失恋太少','单车','天使的礼物','孤独探戈','信心花舍'],
    '反正是我':['《Because You\'re Good To Me》','《低等动物》','《不如这样》','《爱是怀疑》','《我也不会那样做》','《没有你》','《全世界失眠》','《Good Times》'],
    'Special thanks to':['人造卫星','你会不会','你的背包','想哭','没有手机的日子','狂人日记','男人的错','谢谢侬','跳蚤市场','故事'],
    'U87':['《烂》','《阿牛》','《夕阳无限好》','《浮夸》','《葡萄成熟时》','《三个人的探戈》','《不良嗜好》'],
    '我的最好时代':['《十面埋伏》','《岁月如歌》','《明年今日》','《1874》','《少见不怪》','《单车》'],
    'H3M':['《Allegro, Opus 3.3 a.m.》','《还有什么可以送给你》','《于心有愧》','《七百年后》','《Life Goes On》','《今天只做一件事》','《沙龙》','《不来也不去》'],
    'time flies':['《无人之境》','《大人》','《一丝不挂》','《陀飞轮》','《心腹》','《味之素》']}
        self.answer_sel=[]

    def musicgame(self):
    
        num0=random.randint(0,len(self.Eason_Album)-1) 
        answer_album=self.Eason_Album[num0]   # the answer album
        answer_song=self.musicstar_Eason[answer_album] # the answer songs
        answer=answer_song[random.randint(0,len(answer_song)-1)] #the answer song
        self.musicstar_Eason.pop(answer_album) # the complete album in addition to the answer album
        other_songs=list(self.musicstar_Eason.values())  # the whole songs except answer album including its songs
        other_songlen=len(other_songs)
        while other_songlen:
            self.answer_sel.extend(other_songs[other_songlen-1])
            other_songlen-=1

        other_sel=random.sample(self.answer_sel,3)
        randomplace=random.randint(0,3)
        other_sel.insert(randomplace,answer) # answer selection
        return [answer,answer_album,other_sel]
class tang():
    def __init__(self):
        self.index=['干妈','前女友','室友','前前女友','电影','成都旅游团','大学','研究生','专业','生活','明星','人物','母亲','星座','文学','女歌星']
        self.answer0={'干妈':'唐小澈的干妈叫什么名字？','前女友':'唐小澈的前女友叫啥？','室友':'唐小澈现在的室友叫啥?','前前女友':'唐小澈的高中女朋友叫啥？','电影':'唐小澈最爱的电影？','成都旅游团':'哪个女孩子唐小澈最喜欢？'
        ,'大学':'唐小澈的大学是哪所？','研究生':'唐小澈就读的研究生大学？','专业':'唐小澈的专业？（现在）','生活':'下面谁最能把唐小澈照顾好？','明星':'唐小澈最常听的歌星',
        '人物':'唐小澈的梦中情人？','母亲':'唐小澈妈妈的星座？','星座':'唐小澈的星座？','文学':'唐小澈最爱的兴趣？','女歌星':'唐小澈最爱的女歌星？'}
        self.answer1={'干妈':'唐山清','前女友':'何倩文','室友':'阿大','前前女友':'小雨','电影':'霸王别姬','成都旅游团':'陈颖怡',
        '大学':'西华大学','研究生':'unsw','专业':'人工智能','生活':'林媛','明星':'陈奕迅',
        '人物':'路小雨','母亲':'白羊座','星座':'天蝎座','文学':'历史','女歌星':'杨千嬅'}
        self.answer2={'干妈':['林媛','杨屹立','何倩文'],'前女友':['张晨云','林媛','杨屹立'],'室友':['阿飞','阿宇','阿爆'],'前前女友':['何倩文','林媛','杨屹立'],
        '电影':['让子弹飞','肖申克的救赎','黑暗骑士'],'成都旅游团':['郁同彤','徐小乖','杨屹立'],
        '大学':['成都理工大学','清华大学','东南大学'],'研究生':['UQ','USYD','UM'],'专业':['土木工程','电气工程','语言学'],'生活':['张晨云','何倩文','路小雨'],'明星':['张学友','王菲','李荣浩'],
        '人物':['王祖贤','紫霞','桂纶镁'],'母亲':['天蝎座','双子座','双鱼座'],'星座':['狮子座','射手座','处女座'],'文学':['历史','诗歌','科幻'],'女歌星':['王菲','张惠妹','谢安琪']}
    def musicgame(self):
        secretn=random.randint(0,len(self.index)-1)
        x=self.index[secretn]
        question=self.answer0[x]
        answer=self.answer1[x]
        otheran=self.answer2[x]
        randomplace=random.randint(0,3)
        otheran.insert(randomplace,answer)
        return [answer,question,otheran]






def choose():
    import easygui as g
    msg_1='Welcome to guessing songs game '
    title1='唐霸天出品'
    originaltitle=g.msgbox(msg_1,title1,)
    set_0=['Jay','Eason','Tang']
    Jay1=Jay()
    Eason1=Eason()
    Tang1=tang()
    
    msg_0='Please choose character who you like'
    
    choice_chara=g.buttonbox(msg_0,title1,set_0)
    index_0=set_0.index(choice_chara)
    count=10
    mark=0
    num1=random.randint(0,1)
    
    
    while count:
        set_1=[Jay(),Eason(),tang()]


        allsongs=set_1[index_0].musicgame()
        if choice_chara != 'Tang':

            msg2='Which song is issued in the album of '+choice_chara+':'+ allsongs[1]
            title2='唐霸天是大英雄'

            choice_2=allsongs[2]
            selection=g.choicebox(msg2,title2,choice_2)
        else:
            msg2=allsongs[1]
            title2='唐霸天是大英雄'
            choice_2=allsongs[2]
            selection=g.choicebox(msg2,title2,choice_2)

        if selection==allsongs[0]:
            mark+=10
        else:
            mark-=10
        count-=1
    msg3='Game over, the mark:'+str(mark)
    finalltitle=g.msgbox(msg3,title1)

def account():
    account='Tomtang110'
    password='god110'
    information=[account,password]
    import easygui as g
    msg1='Please input your account and password'
    title_1='大王叫我来巡山'
    Initial=['Account','Password']
    inputaccount=g.multpasswordbox(msg1,title_1,Initial)

    y=3

    while y:
        if inputaccount==information:
            choose()
            break
        else:
            msg4='Account or password is wrong,Please input again'
            
            inputaccount=g.multpasswordbox(msg4,title_1,Initial)
        y-=1
account()
            

    




    
    

    
    


        






    # filedir='/Users/tomtang110/Desktop/code/python/python_code/music_star.txt'

    

