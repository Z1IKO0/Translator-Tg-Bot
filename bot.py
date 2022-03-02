 
 ​# @mrlokaman ©️ shyan 
 ​#lntechnical 
 ​import​ ​os 
 ​from​ ​pyrogram​ ​import​ ​Client​, ​filters 
 ​from​ ​pyrogram​.​types​ ​import​ ( 
 ​    ​InlineKeyboardButton​, 
 ​    ​InlineKeyboardMarkup 
 ​) 
 ​from​ ​googletrans​ ​import​ ​Translator 
 ​TOKEN​ ​=​ ​os​.​environ​.​get​(​"TOKEN"​, ​""​) 
  
 ​API_ID​ ​=​ ​int​(​os​.​environ​.​get​(​"API_ID"​, ​12345​)) 
  
 ​API_HASH​ ​=​ ​os​.​environ​.​get​(​"API_HASH"​, ​""​) 
 ​app​ ​=​ ​Client​( 
 ​        ​"Gtt"​, 
 ​        ​bot_token​=​TOKEN​,​api_hash​=​API_HASH​, 
 ​            ​api_id​=​API_ID 
 ​    ) 
  
 ​@​app​.​on_message​(​filters​.​private​ ​&​ ​filters​.​command​([​'start'​])) 
 ​async​ ​def​ ​start​(​client​, ​message​): 
 ​        ​await​ ​message​.​reply_text​(​text​ ​=​f"Salam **​{​message​.​from_user​.​first_name​ ​}​** ​\n​\n​ __Mən Dilmanc Bot'am​\n​ Mən göndərdiyin mesajı seçdiyin dilə tərcümə etmək üçün kodlaşdırılmışam​\n​ Başlamaq üçün mənə 1 mesaj göndər__"​,​reply_to_message_id​ ​=​ ​message​.​message_id​ ,​parse_mode​=​"markdown"​, ​reply_markup​=​InlineKeyboardMarkup​([ [                    ​InlineKeyboardButton​(​"··>Epic Projects <··"​ ,​url​=​"t.me/EpicProjects"​) ],               [​InlineKeyboardButton​(​"Kömək 🆘"​, ​url​=​"t.me/LuxeSUP"​) ]   ]  ) ) 
 ​                   
  
  
  
 ​@​app​.​on_message​(​filters​.​private​ ​&​ ​filters​.​text​  ) 
 ​async​ ​def​ ​echo​(​client​, ​message​): 
  
 ​  
 ​ ​keybord1​=​ ​InlineKeyboardMarkup​( [ 
 ​        [  
 ​            ​InlineKeyboardButton​(​"Azərbaycanca"​,​callback_data​ ​=​ ​'az'​), 
 ​             ​InlineKeyboardButton​(​"Almanca"​, ​callback_data​=​'de'​), 
 ​            ​InlineKeyboardButton​(​"Fransızca"​,​callback_data​ ​=​'fr'​), 
 ​        ], 
 ​        [   ​InlineKeyboardButton​(​"Koreya dili"​, ​callback_data​=​'ko'​), 
 ​        ​InlineKeyboardButton​(​"İngilscə"​, ​callback_data​=​'en'​),       
 ​        ​InlineKeyboardButton​(​"Türkcə"​,​callback_data​ ​=​ ​'tr'​),         
 ​        ], 
 ​        [​InlineKeyboardButton​(​"Yunanca"​,​callback_data​ ​=​"el"​), 
 ​                 ​InlineKeyboardButton​(​"Belarusca"​,​callback_data​ ​=​"be"​),                
 ​        ​InlineKeyboardButton​(​"Rusca"​,​callback_data​=​"ru"​)], 
 ​         
 ​        [​InlineKeyboardButton​(​"Portuqalca"​,​callback_data​ ​=​ ​"pt"​), 
 ​        ​InlineKeyboardButton​(​"Bolqarca"​,​callback_data​ ​=​"bg"​), 
 ​        ​InlineKeyboardButton​(​"İspanca"​,​callback_data​ ​=​ ​"es"​) 
 ​        ], 
 ​        [  
 ​        ​InlineKeyboardButton​(​"Farsca"​,​callback_data​ ​=​"fa"​), 
 ​        ​InlineKeyboardButton​(​"Xorvatca"​,​callback_data​ ​=​ ​"hr"​), 
 ​        ​InlineKeyboardButton​(​"Çexcə"​, ​callback_data​ ​=​ ​"cs"​), 
 ​        ], 
 ​        [ ​InlineKeyboardButton​(​"Danimarkaca"​,​callback_data​ ​=​ ​"da"​), 
 ​        ​InlineKeyboardButton​(​"İtalyanca"​,​callback_data​ ​=​ ​"it"​), 
 ​        ​InlineKeyboardButton​(​"Ukraynaca"​,​callback_data​ ​=​ ​"uk"​),          
 ​        ], 
 ​        [​InlineKeyboardButton​(​"Burada sizin reklamınız ola bilər ✔ "​ ,​url​=​"https://t.me/epicreklam"​) 
 ​        ], 
 ​        [​InlineKeyboardButton​(​" Növbəti »»»"​,​callback_data​ ​=​ ​"page2"​) 
 ​        ] 
 ​        ] ) 
 ​         
 ​ ​await​  ​message​.​reply_text​(​"👇"​,​reply_to_message_id​ ​=​ ​message​.​message_id​, ​reply_markup​ ​=​ ​keybord1​)  
  
  
 ​@​app​.​on_callback_query​() 
 ​async​ ​def​ ​translate_text​(​bot​,​update​): 
 ​  ​keybord6​ ​=​  ​InlineKeyboardMarkup​([ 
 ​       [​InlineKeyboardButton​(​"Tayca"​,​callback_data​ ​=​ ​"th"​), 
 ​       ​InlineKeyboardButton​(​"Afrikanca"​, ​callback_data​=​"af"​), 
 ​       ​InlineKeyboardButton​(​"Türkməncə"​,​callback_data​ ​=​"tk"​)      
 ​       ], 
 ​       [​InlineKeyboardButton​(​"Esperantoca"​,​callback_data​ ​=​ ​"eo"​), 
 ​       ​InlineKeyboardButton​(​"Urdu dili"​,​callback_data​ ​=​ ​"ur"​), 
 ​       ​InlineKeyboardButton​(​"Uyğurca"​,​callback_data​ ​=​"ug"​) 
 ​        
 ​       ], 
 ​       [​InlineKeyboardButton​(​"Özbəkcə"​,​callback_data​ ​=​ ​"uz"​), 
 ​       ​InlineKeyboardButton​(​"Vyetnam dili"​,​callback_data​ ​=​"vi"​), 
 ​       ​InlineKeyboardButton​(​"Qaller dili"​,​callback_data​ ​=​ ​"cy"​) 
 ​        
 ​       ], 
 ​       [​InlineKeyboardButton​(​"Xosa dili"​,​callback_data​ ​=​ ​"xh"​), 
 ​       ​InlineKeyboardButton​(​"Yəhudi dili"​,​callback_data​ ​=​ ​"yi"​), 
 ​       ​InlineKeyboardButton​(​"Yoruba dili"​,​callback_data​ ​=​ ​"yo"​) 
 ​       ], 
 ​       [​InlineKeyboardButton​(​"Burada sizin reklamınız ola bilər ✔ "​ ,​url​=​"https://t.me/zikointime"​) 
 ​       ], 
 ​       [​InlineKeyboardButton​(​" ««« Geri"​,​callback_data​ ​=​ ​"page5"​) 
 ​        
 ​       ] 
 ​ ]) 
 ​   
 ​  ​keybord5​ ​=​ ​InlineKeyboardMarkup​([ 
 ​         [​InlineKeyboardButton​(​"Şotlandca"​,​callback_data​ ​=​ ​"gd"​), 
 ​         ​InlineKeyboardButton​(​"Serbcə"​,​callback_data​ ​=​ ​"sr"​), 
 ​         ​InlineKeyboardButton​(​"Şesoto dili"​,​callback_data​ ​=​ ​"st"​) 
 ​         ], 
 ​         [​InlineKeyboardButton​(​"Şona dili"​,​callback_data​ ​=​"sn"​), 
 ​         ​InlineKeyboardButton​(​"Sindcə"​,​callback_data​ ​=​"sd"​), 
 ​         ​InlineKeyboardButton​(​"Sinhala dili"​,​callback_data​ ​=​ ​"si"​) 
 ​         ], 
 ​         [​InlineKeyboardButton​(​"Slovakca"​,​callback_data​ ​=​ ​"sk"​), 
 ​         ​InlineKeyboardButton​(​"Slovenya dili"​,​callback_data​ ​=​ ​"sl"​), 
 ​         ​InlineKeyboardButton​(​"Somali dili"​,​callback_data​ ​=​ ​"so"​) 
 ​         ], 
 ​         [​InlineKeyboardButton​(​"Katalanca"​,​callback_data​ ​=​ ​"ca"​), 
 ​         ​InlineKeyboardButton​(​"Sundan dili"​,​callback_data​ ​=​"su"​), 
 ​         ​InlineKeyboardButton​(​"Suahili dili"​,​callback_data​ ​=​"sw"​) 
 ​         ], 
 ​         [​InlineKeyboardButton​(​"İsveç dili"​,​callback_data​ ​=​ ​"sv"​), 
 ​         ​InlineKeyboardButton​(​"Filipin dili"​,​callback_data​ ​=​'tl'​), 
 ​         ​InlineKeyboardButton​(​"Tacikcə"​,​callback_data​ ​=​ ​"tg"​) 
 ​         ], 
 ​         [​InlineKeyboardButton​(​"Tamil dili"​,​callback_data​ ​=​ ​"ta"​), 
 ​         ​InlineKeyboardButton​(​"Tatarca"​,​callback_data​ ​=​ ​"tt"​), 
 ​         ​InlineKeyboardButton​(​"Telugu dili"​,​callback_data​ ​=​ ​"te"​) 
 ​         ], 
 ​         [​InlineKeyboardButton​(​" ««« Geri"​,​callback_data​ ​=​ ​"page4"​), 
 ​         ​InlineKeyboardButton​(​" Növbəti »»»"​,​callback_data​ ​=​ ​"page6"​) 
 ​         ]  ]) 
 ​    
 ​  
 ​  ​keybord4​ ​=​ ​InlineKeyboardMarkup​([ 
 ​          [​InlineKeyboardButton​(​"Malayya dili"​,​callback_data​ ​=​ ​"ml"​), 
 ​          ​InlineKeyboardButton​(​"Malta dili"​,​callback_data​ ​=​ ​"mt"​), 
 ​          ​InlineKeyboardButton​(​"Maori dili"​,​callback_data​ ​=​ ​"mi"​) 
 ​          ], 
 ​          [​InlineKeyboardButton​(​"Marathi dili"​,​callback_data​ ​=​ ​"mr"​), 
 ​          ​InlineKeyboardButton​(​"Monqolca"​,​callback_data​ ​=​ ​"mn"​), 
 ​          ​InlineKeyboardButton​(​"Myamma dili"​,​callback_data​ ​=​ ​"my"​) 
 ​          ], 
 ​          [​InlineKeyboardButton​(​"Nepalca"​,​callback_data​ ​=​"ne"​), 
 ​          ​InlineKeyboardButton​(​"Norveç dili"​,​callback_data​ ​=​ ​"no"​), 
 ​          ​InlineKeyboardButton​(​"Nyanja dili"​,​callback_data​ ​=​ ​"ny"​) 
 ​          ], 
 ​          [​InlineKeyboardButton​(​"Odia dili"​,​callback_data​ ​=​ ​"or"​), 
 ​          ​InlineKeyboardButton​(​"Puştu dili "​,​callback_data​ ​=​ ​"ps"​), 
 ​          ​InlineKeyboardButton​(​"Korsikanca"​,​callback_data​ ​=​ ​"co"​), 
 ​          ], 
 ​          [​InlineKeyboardButton​(​"Polyakca"​,​callback_data​ ​=​ ​"pl"​), 
 ​          ​InlineKeyboardButton​(​"Bosnakca"​,​callback_data​ ​=​ ​"bs"​), 
 ​          ​InlineKeyboardButton​(​"Pəncab dili"​,​callback_data​ ​=​ ​"pa"​), 
 ​          ], 
 ​          [​InlineKeyboardButton​(​"Romanca"​,​callback_data​ ​=​ ​"ro"​), 
 ​          ​InlineKeyboardButton​(​"Benqalca"​,​callback_data​ ​=​ ​"bn"​), 
 ​          ​InlineKeyboardButton​(​"Samoa dili"​,​callback_data​=​ ​"sm"​), 
 ​          ], 
 ​          [​InlineKeyboardButton​(​" ««« Geri"​,​callback_data​ ​=​ ​"page3"​), 
 ​          ​InlineKeyboardButton​(​" Növbəti »»»"​,​callback_data​ ​=​ ​"page5"​) 
 ​          ] 
 ​           
 ​  
 ​  
 ​  
 ​ ]) 
 ​   
 ​   
 ​  ​keybord3​ ​=​ ​InlineKeyboardMarkup​([ 
 ​                [ ​InlineKeyboardButton​(​"Hollandca"​,​callback_data​ ​=​ ​"nl"​), 
 ​                ​InlineKeyboardButton​(​"Yaponca"​,​callback_data​ ​=​ ​"ja"​), 
 ​                ​InlineKeyboardButton​(​"Yava dili"​,​callback_data​ ​=​ ​"jv"​) 
 ​                ], 
 ​                [​InlineKeyboardButton​(​"Kanada dili"​,​callback_data​ ​=​ ​"kn"​), 
 ​                ​InlineKeyboardButton​(​"Qazax dili"​,​callback_data​ ​=​ ​"kk"​), 
 ​                ​InlineKeyboardButton​(​"Kxmer dili"​,​callback_data​ ​=​ ​"km"​) 
 ​                ], 
 ​                [​InlineKeyboardButton​(​"Kinyarvan dili"​,​callback_data​ ​=​ ​"rw"​), 
 ​                ​InlineKeyboardButton​(​"Ərəbcə"​,​callback_data​ ​=​"ar"​), 
 ​                ​InlineKeyboardButton​(​"Kürdcə"​,​callback_data​ ​=​ ​"ku"​) 
 ​                ], 
 ​                [ ​InlineKeyboardButton​(​"Qırğızca"​,​callback_data​ ​=​"ky"​), 
 ​                ​InlineKeyboardButton​(​"Lao dili"​,​callback_data​ ​=​ ​"lo"​), 
 ​                ​InlineKeyboardButton​(​"Latınca"​,​callback_data​ ​=​ ​"la"​) 
 ​                ], 
 ​                [​InlineKeyboardButton​(​"Latviyanca"​,​callback_data​ ​=​ ​"lv"​), 
 ​                ​InlineKeyboardButton​(​'Litvaca'​,​callback_data​ ​=​"lt"​), 
 ​                ​InlineKeyboardButton​(​"Lüksemburq dili"​,​callback_data​ ​=​ ​"lb"​) 
 ​                ], 
 ​                [​InlineKeyboardButton​(​"Makedonca"​,​callback_data​ ​=​ ​"mk"​), 
 ​                ​InlineKeyboardButton​(​"Malaqas dili"​,​callback_data​ ​=​"mg"​), 
 ​                ​InlineKeyboardButton​(​"Malay dili"​,​callback_data​ ​=​"ms"​) 
 ​                ], 
 ​                [​InlineKeyboardButton​(​" ««« Geri"​,​callback_data​ ​=​ ​"page2"​), 
 ​                ​InlineKeyboardButton​(​" Növbəti »»»"​,​callback_data​ ​=​ ​"page4"​) 
 ​                ] 
 ​               
 ​  
 ​ ]) 
 ​   
 ​   
 ​  ​keybord1​=​ ​InlineKeyboardMarkup​( [ 
 ​        [  
 ​            ​InlineKeyboardButton​(​"Azərbaycanca"​,​callback_data​ ​=​ ​'az'​), 
 ​             ​InlineKeyboardButton​(​"Almanca"​, ​callback_data​=​'de'​), 
 ​            ​InlineKeyboardButton​(​"Fransızca"​,​callback_data​ ​=​'fr'​), 
 ​        ], 
 ​        [   ​InlineKeyboardButton​(​"Koreya dili"​, ​callback_data​=​'ko'​), 
 ​        ​InlineKeyboardButton​(​"İngilscə"​, ​callback_data​=​'en'​),       
 ​        ​InlineKeyboardButton​(​"Türkcə"​,​callback_data​ ​=​ ​'tr'​),         
 ​        ], 
 ​        [​InlineKeyboardButton​(​"Yunanca"​,​callback_data​ ​=​"el"​), 
 ​                 ​InlineKeyboardButton​(​"Belarusca"​,​callback_data​ ​=​"be"​),                
 ​        ​InlineKeyboardButton​(​"Rusca"​,​callback_data​=​"ru"​)], 
 ​         
 ​        [​InlineKeyboardButton​(​"Portuqalca"​,​callback_data​ ​=​ ​"pt"​), 
 ​        ​InlineKeyboardButton​(​"Bolqarca"​,​callback_data​ ​=​"bg"​), 
 ​        ​InlineKeyboardButton​(​"İspanca"​,​callback_data​ ​=​ ​"es"​) 
 ​        ], 
 ​        [  
 ​        ​InlineKeyboardButton​(​"Farsca"​,​callback_data​ ​=​"fa"​), 
 ​        ​InlineKeyboardButton​(​"Xorvatca"​,​callback_data​ ​=​ ​"hr"​), 
 ​        ​InlineKeyboardButton​(​"Çexcə"​, ​callback_data​ ​=​ ​"cs"​), 
 ​        ], 
 ​        [ ​InlineKeyboardButton​(​"Danimarkaca"​,​callback_data​ ​=​ ​"da"​), 
 ​        ​InlineKeyboardButton​(​"İtalyanca"​,​callback_data​ ​=​ ​"it"​), 
 ​        ​InlineKeyboardButton​(​"Ukraynaca"​,​callback_data​ ​=​ ​"uk"​),          
 ​        ], 
 ​        [​InlineKeyboardButton​(​"Burada sizin reklamınız ola bilər ✔"​ ,​url​=​"https://t.me/zikointime"​) 
 ​        ], 
 ​        [​InlineKeyboardButton​(​" Növbəti »»»"​,​callback_data​ ​=​ ​"page2"​) 
 ​        ] 
 ​        ] ) 
 ​   
 ​   
 ​  ​keybord2​=​ ​InlineKeyboardMarkup​([ 
 ​           [​InlineKeyboardButton​(​"Ermənicə"​,​callback_data​ ​=​ ​"hy"​), 
 ​           ​InlineKeyboardButton​(​"Eston dili"​,​callback_data​ ​=​ ​"et"​), 
 ​           ​InlineKeyboardButton​(​"Finlandca"​,​callback_data​ ​=​ ​"fi"​) 
 ​           ], 
 ​           [​InlineKeyboardButton​(​"Amharca"​,​callback_data​ ​=​ ​"am"​), 
 ​           ​InlineKeyboardButton​(​"Friz dili"​,​callback_data​ ​=​ ​"fy"​), 
 ​           ​InlineKeyboardButton​(​"Qalisiya dili"​,​callback_data​ ​=​ ​"gl"​) 
 ​           ], 
 ​           [​InlineKeyboardButton​(​"Gürcü dili"​,​callback_data​ ​=​ ​"ka"​), 
 ​           ​InlineKeyboardButton​(​"Albanca"​,​callback_data​ ​=​ ​"sq"​), 
 ​           ​InlineKeyboardButton​(​"Baskca"​,​callback_data​ ​=​ ​"em"​) 
 ​           ], 
 ​           [​InlineKeyboardButton​(​"Qucarati dili"​,​callback_data​ ​=​ ​"gu"​), 
 ​           ​InlineKeyboardButton​(​"Haiti dili"​,​callback_data​ ​=​ ​"ht"​), 
 ​           ​InlineKeyboardButton​(​"Hausa dili"​,​callback_data​ ​=​"ha"​) 
 ​           ], 
 ​           [​InlineKeyboardButton​(​"Hindicə"​,​callback_data​ ​=​ ​"hi"​), 
 ​           ​InlineKeyboardButton​(​"Macar dili"​,​callback_data​ ​=​ ​"hu"​), 
 ​           ​InlineKeyboardButton​(​"İslandiya dili"​,​callback_data​ ​=​ ​"is"​) 
 ​           ], 
 ​           [​InlineKeyboardButton​(​"Iqboca"​,​callback_data​ ​=​ ​"ig"​), 
 ​           ​InlineKeyboardButton​(​"İndoneziya dili"​,​callback_data​ ​=​ ​"id"​), 
 ​           ​InlineKeyboardButton​(​"Irland dili"​,​callback_data​ ​=​ ​"ga"​) 
 ​           ], 
 ​           [​InlineKeyboardButton​(​" ««« Geri"​,​callback_data​ ​=​ ​"page1"​), 
 ​           ​InlineKeyboardButton​(​" Növbəti »»»"​,​callback_data​ ​=​ ​"page3"​), 
 ​           ] 
 ​            ]) 
 ​                                                 
 ​   
 ​   
 ​   
 ​  ​tr_text​ ​=​ ​update​.​message​.​reply_to_message​.​text 
 ​  ​cb_data​ ​=​ ​update​.​data 
 ​  ​if​ ​cb_data​==​ ​"page2"​: 
 ​          ​await​ ​update​.​message​.​edit​(​"Dili seç ☟"​,​reply_markup​ ​=​ ​keybord2​) 
 ​  ​elif​ ​cb_data​ ​==​ ​"page1"​: 
 ​          ​await​ ​update​.​message​.​edit​(​"Dili seç ☟"​,​reply_markup​ ​=​keybord1​) 
 ​  ​elif​ ​cb_data​ ​==​"page3"​: 
 ​          ​await​ ​update​.​message​.​edit​(​"Dili seç ☟"​,​reply_markup​ ​=​keybord3​) 
 ​  ​elif​ ​cb_data​ ​==​ ​"page4"​: 
 ​          ​await​ ​update​.​message​.​edit​(​"Dili seç ☟"​,​reply_markup​ ​=​keybord4​) 
 ​  ​elif​ ​cb_data​ ​==​"page5"​: 
 ​          ​await​ ​update​.​message​.​edit​(​"Dili seç ☟"​,​reply_markup​ ​=​keybord5​) 
 ​  ​elif​ ​cb_data​ ​==​"page6"​: 
 ​          ​await​ ​update​.​message​.​edit​(​"Dili seç ☟"​,​reply_markup​ ​=​keybord6​) 
 ​  ​else​ : 
 ​       ​translator​ ​=​ ​Translator​()   
 ​       ​translation​ ​=​ ​translator​.​translate​(​tr_text​,​dest​=​cb_data​)  
 ​       ​await​ ​update​.​message​.​edit​(​translation​.​text​) 
  
 ​app​.​run​()
	 
