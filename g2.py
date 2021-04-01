#Midterm Project

import random

def pi(x):
  print(input(x))

Q = ['招式以慈悲與佛法聞名江湖的門派是哪個？ \n1.少林\n2.雲夢\n3.華山\n4.暗香','《西遊記》中孫悟空是由(__)變化來的。 \n1.器皿\n2.頑石\n3.朽木\n4.青竹葉','荳蔻是指幾歲？ \n1.二十\n2.十八\n3.十五\n4.十三','"(____)，心有靈犀一點通" \n1.人生自古誰無死\n2.畫樓西畔桂堂東\n3.身無彩鳳雙飛翼\n4.昨夜星辰昨夜風','"詩中有畫，畫中有詩"是蘇軾對誰的評價？ \n1.杜甫\n2.白居易\n3.李白\n4.王維','楚留香以甚麼功夫聞名江湖？ \n1.輕功\n2.隱身\n3.劍術\n4.棍法','"詩仙"是指哪位詩人？ \n1.杜甫\n2.李清照\n3.王維\n4.李白','"賣炭翁，伐薪燒炭南山中"中的南山指的是？\n1.華山\n2.泰山\n3.終南山\n4.西陵山','戰國時提出"民為貴"的思想家為？ \n1.孔子\n2.孟子\n3.墨子\n4.韓非','杜甫漂泊一生，留下不少住所，其中最著名的杜甫草堂位於(__)？\n1.重慶\n2.昆明\n3.成都\n4.貴陽','"北冥有魚，其名為鯤"出自？ \n1.老子\n2.孟子\n3.論語\n4.莊子','《水滸傳》中綽號"神行太保"的是？ \n1.吳用\n2.戴宗\n3.盧俊義\n4.公孫勝','西湖白堤是因紀念某個詩人而得名。"賣炭翁，伐薪燒炭南山中"是他的作品。試問此詩人為誰？ \n1.杜甫\n2.李白\n3.白居易\n4.白娘子','趙州橋始建於哪個朝代？ \n1.隋朝\n2.戰國\n3.北宋\n4.唐朝','"李長吉"是？ \n1.李鬼\n2.李賀\n3.李世民','《水滸傳》中，綽號為"一枝花"的是（__） \n1.蔡福\n2.燕青\n3.蔡慶\n4.李俊','"鍥而捨之，（__）；鍥而不捨，（__）"  \n1.與山間之明月；耳得之而為聲\n2.望帝春心托杜鵑；滄海月明珠有淚\n3.朽木不折；金石可鏤\n4.千里澄江似練；征帆去棹殘陽裡','諸葛亮曾在襄陽隆中隱居，躬耕苦讀幾年？ \n1.五年\n2.十年\n3.十五年\n4.二十年','"文章合為時而著，歌詩合為事而作"是由誰提出的？ \n1.劉禹錫\n2.周敦頤\n3.柳宗元\n4.白居易','"兩情若是長久時，又豈在朝朝暮暮"語出：\n1.曾鞏\n2.蘇軾\n3.秦觀\n4.李清照','"將相和"這個故事的主人公是趙國的(_) \n1.廉頗與藺相如\n2.大將秦瓊與秦國的丞相\n3.呂不韋與嬴政','"入木三分"原意用來形容（__） \n1.射箭本領高\n2.雕刻技術高\n3.書法筆力強勁\n4.文章深刻','"新來瘦，非乾病酒，不是悲秋"出自以下哪個詞人？ \n1.辛棄疾\n2.蘇軾\n3.李煜\n4.李清照','漢代編戶制度實施的主要目的是？ \n1.實行寬舒政策\n2.組織農業生產\n3.控制和剝削人民\n4.抵抗水旱災害','"曉看紅濕處，花重錦官城"中所指的"錦官城"是指現代的哪座城市？ \n1.成都\n2.揚州\n3.杭州\n4.蘇州','以下歷史事件中，與關羽無關的是： \n1.大意失荊州\n2.單刀赴會\n3.水淹七軍\n4.七擒七縱','孫悟空為醫活人參樹，去三島求方，請問是哪三島？ \n1.蓬萊、瀛洲、瑤池\n2.蓬萊、瀛洲、方丈\n3.蓬萊、普陀、方丈\n4.蓬萊、普陀、瑤池','歷史上"圍魏救趙"戰術最初運用於（__）之戰 \n1.城淮\n2.桂陵\n3.馬陵\n4.長平','朱震亨是金元時期傑出的醫學家，他學醫雖晚，但終成大器，這主要得益於他潛心研究了被後人奉為"醫家之宗"的典籍（__） \n1.《黃帝內經》\n2.《千金方》\n3.《唐本草》\n4.《本草綱目》','下列史實，在《史記》和《漢書》中皆有記載的是（__） \n1.班超出使西域\n2.評定七國之亂\n3.城濮之戰\n4.設西域都護']
A = ['1','2','4','3','4','1','4','3','2','3','4','2','3','1','2','3','3','2','4','3','1','3','4','3','1','4','2','2','1','2']
x = 0

def game():
  print('你遇到一個書生，手拿著書纏著你不放，堅持要問你問題。\n有什麼辦法呢？你也很無奈啊。\n「讓我來考考你！」\n\n*答題時請輸入阿拉伯數字，請勿加上其他符號\n')
  items = range(29)
  nums = random.sample(items,5)
  global x

  for n in nums:
    print('\n'+ Q[n])
    ans = input('你的回答：')
    if ans == A[n]:
      print('正確答案！')
      x += 1
    else:
      print('答錯囉，正確答案是' , A[n])
  if x == 5:
    print('\n「少俠真是學富五車！」\n書生鼓鼓掌，\n「在下受益良多，下回再向少俠討教！」')
  elif 1 < x < 5:
    print('\n「少俠的學問已相當不錯，只是難免有闕漏之處......希望下次見到少俠時能有長進！」')
  else:
    print('\n「少俠的學問......稍嫌不足啊！」\n書生搖了搖頭，晃晃手中書卷，\n「還請多多充實自我，下回再向少俠討教！」')
  pi('\n書生話音方落，你只感一陣暈眩。')

def showGameMessege():
  pi('\n初入江湖，聲名鵲起，\n你，將與誰相遇？\n\n*每個選擇都會影響最後的故事結局，請謹慎抉擇\n*所有選擇請Enter後輸入阿拉伯數字\n\n————你的江湖夢，由你自己定義————')

def start():
  pi('恍恍惚惚虛虛實實真真假假。\n\n迷迷糊糊之間，你已不知身處何方，\n環顧四周，只見一人————')
  pi('手中抱一把古琴，信手撫弄，翩翩公子模樣')
  pi('你莫名覺得那身影熟悉，欲將對方瞧得更仔細；\n當你向他邁步之時，他亦驀地轉身向你————')

def final():
  pi('江湖一夢，塵緣已定。\n人生無回頭路可走，只待下回奈何橋上再相逢，\n一笑泯恩仇，\n一飲忘愛恨。')

def ysy31():
  pi('還沒回神，他已走了過來。')
  pi('「在下無爭公子原隨雲，久聞閣下大名，今日得一見風采，真乃原某有幸。」\n\n......不正是你上次拒絕的邀請者？')
  pi('旁人都恭恭敬敬地問好，你還愣著，\n還是你朋友撞了一下你，\n這才忙地回禮————在這也能遇到無爭公子！')
  pi('你與原隨雲聊了幾句，發現傳聞不假，\n原隨雲的確是博學多聞，溫文儒雅，\n兩人意外地投機。')
  pi('「原某倒是想起一事，上回恰逢家父壽宴，原某記得是邀請了閣下的，爾後卻渺無音信？」')
  pi('你愣了下。\n這是不是道送命題？')
  pi('「實是抱歉，那日恰與朋友有約，無法赴宴，也是在下心頭遺憾。」\n你隨口撒個謊打諢過去，並且戳戳朋友要他掩護。')
  pi('「對！不知那日恰是無爭山莊大宴！還望公子海涵。」\n你朋友也真是跟你一搭一唱得麻溜。')
  pi('原隨雲只微微一笑。\n你有種被看穿的感覺，忍不住縮了一下。')
  pi('「那麼，原某期待來日能與閣下一聚。」\n\n他特意在「來日」兩字加重了咬字，\n並且得體而不失禮貌的一笑，旋即離開。')
  pi('「哎我去！這無爭公子怎麼對你這麼有興趣？」\n「......我怎麼知道！」')

def ysy32():
  pi('你感覺有點尷尬，就像偷窺被發現了。\n即使對方目不可視。')
  pi('「看誰啊？原隨雲？」\n你那朋友順著你的視線看過去，揶揄地笑，\n「眼光挺好啊，我之前幾次想和他聊聊都被拒絕。」')
  pi('出乎意料地，你在朋友話音方落時，\n看到原隨雲唇角轉瞬即逝地勾起，\n你似乎可以聽到他鼻間輕輕一哼，\n不是鄙夷的那種，而是......覺得有趣的。')
  pi('你有點懵逼。')
  pi('你覺得怪怪的，有種不妙的感覺。\n還是快跑吧。')
  pi('假藉著尿遁之名，實則開溜，\n好歹也是「江湖新秀」，輕功還是挺不錯的。')
  pi('返家後，你滿腦子都是原隨雲一笑的模樣。')
  pi('更大一部分是尷尬的場面。')
  pi('......好亂啊。\n人生好難。')
  pi('鹹魚你也，發出深深的感慨。')

def ysy41():
  pi('你嚇傻了，當下只想到自保。\n你縮了一下，躲在原隨雲身後，\n彷彿把他當作肉盾。')
  pi('你閉上眼。')
  pi('沒聽見預想的刀刃刺入肉中的聲音，\n反而是原隨雲袖子一揮，\n山賊的眉心已多了一枚透骨針。\n\n你怯懦地抬頭看他，他嘴角只是一抹冷笑。')
  pi('「方才若是原某沒有擋住，想來閣下也會成為刀下亡魂，或是被抓回去當壓寨夫人。」\n他聲音寒若冰霜，\n「不知閣下更喜歡哪種？」')
  pi('他又冷笑一聲，隨即自己轉身上了車，\n滿地鮮血裡，他一身白格外顯眼。')
  pi('染血的貴公子。')
  pi('你默默跟在他身後上了車，一路無語。')
  pi('「今日被山林匪盜擾了遊興，原某送閣下返家吧。」\n又回到了起初的疏遠。')
  pi('你站在家門口，默默聽著馬車離去的聲音。')
  pi('達達馬蹄，滾滾紅塵，自此兩相別。')

def ysy42():
  pi('「小心身後！」\n\n你把首當其衝的原隨雲一把推開，\n暗器直衝你而來————')
  pi('然而原隨雲將你摟了過來，面色陰鷙，\n袖子一揮，\n山賊的眉心已多了一枚透骨針，\n往後倒在塵土與血泊之中。')
  pi('你抬眼看他，他輕聲笑了，\n你飛快掙脫他的懷抱，面上像火燒一樣地紅。')
  pi('「原某謝過少俠救命之恩。」\n他聲音鏗鏘，煞有其事地朝你一拜，\n\n你側身避開，「哪裡的事⋯⋯」')

def ysy51():
  pi('終究是按捺不住，你選擇前往無爭山莊。')
  pi('你打車，馬伕聽到你要去無爭山莊卻是十分驚訝。\n\n「姑娘啊⋯⋯不是我要說，無爭山莊不是大宴的日子，去不得呀⋯⋯」\n「江湖兒女，有什麼去不得的地方！」')
  pi('馬伕摸摸鼻子，心不甘情不願地出發了。\n你的荷包有點痛。')
  pi('沒關係，原隨雲有錢。')
  pi('那馬伕到了入口便不願再送，\n你只好自己走進去。')
  pi('「敢問閣下何許人也。」\n\n門口守衛把你擋在門外，\n你正愁該如何回答，卻見一人走來，\n湊在守衛耳邊吩咐幾句，你聽不清，\n那守衛卻放你進去了。')
  pi('「姑娘請跟我來。」')
  pi('無爭山莊很大，大的不可思議，\n是你一輩子都攢不到的財富堆積起來的。\n\n金碧輝煌，雕梁畫棟。\n你一邊走一邊讚嘆，領路的僕人眼神流露出不屑。')
  pi('你走的腳都發痠了，領路的人卻還沒停。\n你正想抱怨，他突然停了下來。\n\n你險些撞上。')
  pi('「公子在這邊，姑娘請自己進去吧。」\n那僕人狀似恭敬，誰都聽得出他的厭惡。')
  pi('你推開檀木大門，淡淡薰香迎面而來，\n那翩翩公子坐在庭院當中，輕輕抿一口茶，\n\n你走上前去，一屁股坐在他對面的椅子上。')
  pi('「閣下大費周章來尋原某，可是有何急事？」\n他放下茶盞，對你一笑，\n\n你只覺流光溢彩，眩目動人。\n面前多了一杯白煙騰騰的茶，清香撲鼻。')
  pi('「我......很久沒收到你的信，想說來看看......」\n你到最後幾近沒了聲音，實在是太羞人了，\n你面上已紅成了秋柿。\n\n還好他看不到，你心想。')
  pi('「能得閣下掛念，是原某三生有幸。」他低笑出聲，\n「不知原某能否再貪一些，求朝朝暮暮與良人伴？」')

def ysy52():
  pi('不急，人家可是無爭公子，\n日理萬機，忙得很，還是別去打擾人家了吧。')
  pi('就這樣日復一日，你逐漸淡忘這事。')
  pi('許久許久之後的某日，\n那些信紙不小心被闖進屋裡的野貓撕碎，\n\n牠有墨一樣黑的漂亮皮毛。')
  pi('可惜是隻瞎貓。')
  pi('你沒說什麼，把紙片全丟進灶裡。')

def ysy61():
  pi('彈什麼鬼〈鳳求凰〉。')
  pi('你才不是灰燼裡爬出來的鳥。')
  pi('當隻安穩過日子的麻雀也很好，不是嗎。')
  pi('「走啦！沒興致了哎呀哎呀！」\n「你別跑那麼快！人家跟你又沒仇！喂！」\n「我跟他八字不對！」')
  pi('啪地一聲。\n原隨雲的琴弦斷得很不優雅。')

def ysy62():
  pi('你輕功一躍，三兩下便跳上平台。')
  pi('「見過無爭公子。」\n你恭恭敬敬朝他抱拳，\n他抱著琴回以一禮。')
  pi('「聽聞閣下性喜雲遊，卻不知在此也能相遇。」\n他信手撫琴，唇角微勾，\n竟是動人的美，更勝遼闊景致。')
  pi('「聽聞公子性喜平淡，卻不知琴聲中繾綣纏綿是為何？」\n你笑嘻嘻地說道。')
  pi('「參差荇菜，左右采之。」\n原隨雲淡淡說道，若有所思。')
  pi('這句話就把你打懵了。')
  pi('「荇菜？是什麼蔬菜嗎？」\n你發誓，你是打從心底困惑。\n此問一出，原隨雲笑得倒是開懷。')
  pi('你丈二金剛模不著腦袋。')
  pi('原隨雲一笑，「原某先行告退，來日方長，望少俠能博覽群書，充實自我。」\n「......你什麼意思！」')
  pi('*註  詩曰：「參差荇菜，左右采之。窈窕淑女，琴瑟友之。」')

def endA():
  pi('【結局甲】 一生至交，相見恨晚。')
  pi('經此一事，你倆情誼更堅，\n成為交心好友。')
  pi('他時不時寫信給你，還是不許回信的那種——\n「雙目有疾，亦不願假手他人」')
  pi('藉口，都是藉口。')
  pi('但你還是接受這個拙劣的藉口，\n經常赴無爭山莊拜訪，\n每回都盡興而歸。')
  pi('\n然而你不知道。')
  pi('許久許久以前，上元燈節，\n原隨雲心血來潮，去金陵城內感受下節日氛圍，\n他想看看愚昧者究竟能多愚昧。')
  pi('燈火闌珊處，\n衣著華貴的青年靜靜聽著嘈雜人聲。')
  pi('「哎，這位公子，你迷路啦？」\n\n那人的聲音實在是純粹乾淨，\n天真，天真的過頭了，\n想來是未見過江湖的險惡醜陋。')
  pi('原隨雲朝對方微微一笑，感受到眼前人兒一愣。\n\n「在下本與家僕來這城內過節，不料卻被人潮沖散......」他狀似苦惱，\n「本來是約在北城門，現下失了方向，正愁該如何是好。」')
  pi('一隻香軟小手滑入他手中，\n「你......眼睛不方便吧，我帶你去！」\n\n人兒小心翼翼地，一路牽他走到城門，\n同時呱啦呱啦地同他說燈節的精彩，\n那掌心的溫度，他始終難忘。')
  pi('他明明是討厭被觸碰的，卻不忍掙脫。\n不忍放手。')
  pi('原隨雲要她一輩子在他懷裡天真無邪。')
  pi('至死。')
  final()

def endB():
  pi('【結局乙】 時有往來，情淡如水。')
  pi('日子依然平淡。\n你還是那個浪蕩江湖，結交四方名俠的江湖新秀。\n\n偶爾會收到原隨雲的信，\n不過你鮮少回覆。')
  pi('你有時會遇到原隨雲，\n煙雨朦朧的日子，喧嚷紛擾的茶館，\n他靜靜坐在那，凡塵出世。')
  pi('「訪友。」他說。')
  pi('訪的不是你。')
  final()

def endC():
  pi('【結局丙】 曲終人散，有緣無份。')
  pi('你是初出茅廬的江湖新秀，\n也和大家一樣，喜歡在茶館嘮嗑打哈哈。')
  pi('「哎聽說了沒，聽說啊那無爭公子......」')
  pi('「......是蝙蝠公子？無惡不作的那位？」')
  pi('「不可能吧......那麼風度翩翩的一個人......」')
  pi('「真的啊，香帥可是親自......」')
  pi('流言碎語傳入你耳中，你不甚在意。\n茶有些涼。')
  final()

def ysy6():
  pi('\n許久之後。\n\n風和日麗的好日子。\n該去四處浪蕩。')
  pi('你同好友出遊，沿途好山好水，\n你兩人吱吱喳喳不停話家常，\n不亦樂乎。')
  pi('馬車最終停在中原一處山谷旁。\n映入眼簾是寬不知幾尺流水瀑布，\n十幾人高的水車嘎嘎轉動。')
  pi('中原多磐石草原，不似江南水鄉澤國，\n所見之景遼闊壯麗，\n一番嶄新氣象。')
  pi('遙遙高台上卻見一頎長身影，\n獨自站在那，格外惹人注目。\n\n你沒忍住多瞧幾眼。')
  pi('等等。')
  pi('有點眼熟。')
  pi('好像是那什麼公子......')
  pi('「原隨雲？」\n你朋友順著你的視線看過去，\n我覺得你跟他挺有緣的，到哪都能遇到。」')
  pi('悠悠琴聲似乎順風飄來，若有似無，\n你聽不大清楚，\n卻知其中情意繾綣，溫柔纏綿。')
  pi('一曲畢，\n你仍仰頭看著對方。')
  pi('他緩緩轉過來，\n明明相隔頗遠，明明隔著眼罩，\n你卻能感受到他是對著你。\n\n恍然之間，他臉上似乎有淡淡一笑。')
  pi('這時，你————\n\n壹.不予置理\n貳.輕功上前')
  while True :
    choice6 = input()
    if choice6 == '1' :
      ysy61()
      endC()
      break
    elif choice6 == '2' :
      ysy62()
      endB()
      break
    else :
      pi('請少俠重新選擇')

def ysy5():
  pi('之後的幾個月，\n你漸漸習慣每隔一段時間就會收到飛鴿傳書，\n雪白信紙上陳著瀟灑飄逸字跡。')
  pi('信裡有時僅是雜言碎語，不知所云；\n有時字裡行間透著蒼涼與黑暗，\n更多的是自命不凡的驕傲。')
  pi('你偶爾會回信，\n也不知道他究竟會不會讀，\n總有人唸給他聽的吧，你想。')
  pi('然而近來，你卻沒收到他的信。\n從上回收到信已過了四個月餘。')
  pi('你有點焦躁不安，\n某種習慣的事物突然消失。\n\n縱容知道原隨雲武功高強，\n心中難免擔心。')
  pi('你決定......\n\n壹.前往無爭山莊一探\n貳.再等等吧，莫急')
  while True :
    choice5 = input()
    if choice5 == '1' :
      ysy51()
      endA()
      break
    elif choice5 == '2' :
      ysy52()
      endC()
      break
    else :
      pi('請少俠重新選擇')

def ysy4():
  pi('\n無爭山莊一宴後，你與原隨雲魚雁往來，\n你感受得到他在字裡行間的情緒，\n真真切切吐露他的感受。')
  pi('「心似浮雲常自在，意如流水任東西。」\n「你看到的原隨雲是我父親想要的原隨雲。」\n「很多人嘴上稱讚我，心中卻在可憐我。可是，我需要麼？」\n\n你對他的了解不再僅限於「溫文爾雅的無爭公子」，\n而得以窺探他心中那一塊鮮為人知的黑暗面。')
  pi('但那黑暗究竟有多深，\n你不得而知。')
  pi('某日，你又接到了一封信。\n鴿子依然啪嗒啪嗒的迅速飛走了。\n捉鴿子失敗。')
  pi('「近日欲至中原雲遊，敬邀摯友與原某同行。」\n\n再熟悉不過的俊逸瀟灑字跡，\n只簡簡單單兩句話。')
  pi('走吧。')
  pi('\n原隨雲的馬車低調不奢靡，\n雖說如此，細節卻處處用心，\n座椅鋪上了軟墊，手爐已暖好，\n車上有淡淡的清冷檀香味。')
  pi('你與他有說有笑，一路好不開心，\n外頭的初雪悄悄落下。\n\n「今日正是初雪，能與你度過，實是原某之幸。」\n他帶笑說道，興致看起來頗是不錯。')
  pi('然，馬車卻突然一個顛簸。\n \n茶盞滑至桌緣，你眼明手快捉著，\n熱茶卻是潑了你滿手。\n「嘶————」你疼的叫出聲。')
  pi('原隨雲伸手捧住你的手，\n他的手冰涼涼的，\n絲毫不像方才抱手爐暖了許久。')
  pi('「你沒事吧？今日怕是路況不佳......」\n他聲音裡滿是關切，指尖撫過你手背。')
  pi('有點癢。')
  pi('你面上微紅，驀地把手抽走。\n原隨雲一僵。')
  pi('他低笑一聲，幽幽道：\n「是原某心急了，如有冒犯還請閣下原諒。」\n\n他坐回原本的位置，與你隔著茶几。\n你摩挲著被燙得發紅的手。')
  pi('有點疼。')
  pi('片刻，馬車又是一震，\n伴隨輪子吱吱的聲音停了下來。')
  pi('外頭有吆喝聲，隨即是馬匹嘶鳴。\n你臉色微變，原隨雲卻是紋風不動。')
  pi('「裡面的，還不快點給爺出來！」\n\n山賊。')
  pi('原隨雲冷冷推了門出去，你跟在他身後。\n\n「身上金銀財寶放著，人快滾。不過你這馬車簡陋成這樣，怕是也沒什麼，哈哈哈哈！」\n眾山賊大笑，他依然淡漠。')
  pi('「呦，小妹妹倒是長的挺不錯，過來給爺看看！」\n為首的山賊油膩膩的，輕蔑地說道。')
  pi('你眼角餘光看到原隨雲眉頭一皺。\n你瞪向山賊。')
  pi('「瞅啥瞅？不過來？哼，那爺過去！」\n他踏出幾步，伸手欲把你抓過來，\n\n然而未及你身前一尺，\n又踉踉蹌蹌後退，\n捂著軟趴趴的右手腕，顯是已被折斷。')
  pi('你還一臉懵逼，\n原隨雲已擋到你身前。')
  pi('「玩什麼英雄救美？小的們還不把他打死！」\n山賊面目猙獰，蜂擁而上。')
  pi('原隨雲一手輕柔覆上你的右手，\n冰冷冷的觸感緩解了疼痛。\n\n你的視野被他的身子擋去一半，\n只知道勁風陣陣，慘叫連連，\n不消片刻，\n面前屍體已躺得七橫八豎。')
  pi('原隨雲慢慢轉過身來，\n手上動作輕柔，\n「你還好吧？」\n\n還未待你回話，\n你看到他背後的土匪站了起來，\n驀地往前衝來，\n大刀舉起，銀光一閃！')
  pi('這時你————\n\n壹.側身閃避\n貳.上前阻擋')
  while True :
    choice4 = input()
    if choice4 == '1' :
      ysy41()
      endB()
      break
    elif choice4 == '2' :
      ysy42()
      endA()
      break
    else :
      pi('請少俠重新選擇')

def ysy3():
  pi('\n你想了想，這其中會不會有詐？\n你一個剛起步的江湖小萌新，\n哪有可能收到邀請......肯定是寄錯了。\n那隻笨鴿子，就該煮來吃！')
  pi('沒把此事放在心上，就這麼過了數月。')
  pi('是日，你前往中原赴舊友之宴。\n\n許久未見，自是有滿腹心事可聊，\n你正聊得開心，享受醇酒佳餚，\n遠遠的卻見一人長得特別好看，\n忍不住多瞧幾眼。')
  pi('那皮相生得極好，青年更是氣度出眾，\n五官端正，彎眉朱唇，噙著淺淺的笑，\n穿著整齊乾淨，衣料顯為上品，\n卻不是當今公子哥兒們間流行的俗氣款式，\n\n唯一美中不足的是矇住眼眸的黑綢，\n\n不過，此人不露雙眸卻已令人神魂顛倒，\n拿下絲綢怕是人神共憤！')
  pi('似乎感覺到你的目光，那人轉了過來，\n分明沒被實際上注視，你卻覺得被赤裸裸地盯著看。')
  pi('這時，你......\n\n壹.愣在原地\n貳.轉身就跑')
  while True :
    choice3 = input()
    if choice3 == '1' :
      ysy31()
      ysy5()
      break
    elif choice3 == '2' :
      ysy32()
      ysy6()
      break
    else :
      pi('請少俠重新選擇')

def ysy2():
  pi('\n你想了想，\n這無爭山莊宴會可是難得一見，\n去了開開眼界、結交朋友也好，\n何況，這無爭公子可是難得一見。')
  pi('宴會當日。\n\n走進無爭山莊，\n江湖傳言的雕梁畫棟、金碧輝煌果真不假！\n莊內大宴四方賓客名士，\n許多人過來向你敬酒，\n看來你「江湖新秀」的聲名早已遠播。')
  pi('等到幾盞酒下肚，眾人正聊得開懷，\n一名風度翩翩的男子緩緩走來，\n你還在納悶是誰，周圍的人已紛紛舉起杯盞敬酒。')
  pi('「久聞閣下大名，今日得一見風采，真乃原某有幸。」\n\n他也不搭理旁人，只朝你舉杯，\n你忙地回禮————竟是無爭公子本人！')
  pi('等到抬頭，你方有機會細看對方模樣。\n\n那皮相生得極好，原隨雲人更是氣度出眾，\n五官端正，彎眉朱唇，噙著淺淺的笑，\n穿著整齊乾淨，衣料顯為上品，\n卻不是當今公子哥兒們間流行的俗氣款式，\n\n唯一美中不足的是矇住眼眸的黑綢，\n\n不過，此人不露雙眸卻已令人神魂顛倒，\n拿下絲綢怕是人神共憤！')
  pi('或許上天就是不願有人十全十美。')
  pi('「在下初入江湖，待人處事仍有不足，才是要向無爭公子學習。」\n你恭恭敬敬地回道，他微微一笑，一飲而盡杯中醇酒。')
  pi('縱然目不可視，\n原隨雲動作卻與常人無絲毫不同，\n這點你可是驗證了。')
  pi('原隨雲上通天文下知地理，\n詩書禮樂無不熟稔，\n言談又幽默風趣，\n你忍不住與他聊了起來，\n兩人意外地投機，相談甚歡。')
  pi('「恕原某還需主持宴會，無法繼續奉陪，先行告辭。」聊了許久，他這麼說，\n「若是閣下不嫌棄，原某數月後將至中原遊歷，若有意同行，可以飛鴿告之。」\n\n你想起了那隻你意圖煮來吃的鴿子。')
  pi('這次無爭山莊一宴，你結識了不少江湖豪傑，\n其中，原隨雲更是......令人印象深刻。')
  pi('那麼，是否要與他同遊中原呢？\n\n壹.頗有興趣，與原隨雲同遊可是難得的機會！\n貳.算了吧，去了怕是要被人說話，不可高攀。')
  while True :
    choice2 = input()
    if choice2 == '1' :
      ysy4()
      break
    elif choice2 == '2' :
      ysy5()
      break
    else :
      pi('請少俠重新選擇')

def ysy1():
  pi('\n叩叩叩。\n你是被鴿子啄窗的聲音吵醒的。\n好想抓來煮鴿子湯。')
  pi('你取下鴿子腳上的信，\n啪嗒啪嗒，牠馬上飛走了，\n可能感覺到鴿身安全受到威脅吧。')
  pi('那是張白底藍紋的請柬，\n\n「無爭山莊」\n\n紙上字跡瘦勁清峻，瀟灑飄逸。\n三月後，恰逢無爭山莊原老莊主生辰，\n將在莊內大宴賓客，\n信末「原隨雲  恭候」二字倒是寫得端莊嚴謹。')
  pi('「無爭」二字，\n乃江湖眾人予「無與爭鋒」之名號，\n在此任莊主手上硬是成了「與世無爭」。')
  pi('但，無爭山莊少莊主————原隨雲\n在江湖上可是大名鼎鼎，\n年紀輕輕便精通三十三種武功，\n個性溫文爾雅，彈得一手好琴————')
  pi('可惜是個瞎子！')
  pi('你早有耳聞他的大名，卻是未曾見過其人，\n你心中奇怪，\n無爭公子怎麼會邀請你一個江湖新秀？')
  pi('這宴，是去還是不去？\n\n壹.前往赴宴，見見「無爭公子」究竟是何許人。\n貳.推辭邀請，萬一有詐怎麼辦......')
  while True :
    choice1 = input()
    if choice1 == '1' :
      ysy2()
      break
    elif choice1 == '2' :
      ysy3()
      break
    else :
      pi('請少俠重新選擇')


showGameMessege()
game()
start()
ysy1()