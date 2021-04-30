# coding=utf-8
from flask import Flask, render_template, request
from flask import jsonify
import random
# from flask_cors import CORS
from flask_cors import *
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORS(app, supports_credentials=True)

@app.route('/products/', methods=['GET', 'POST'])
def products():
    lt=[{
     {
     	"data": [
     		  {
     			"id": 1,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，饼干",
     			"defaultimg": "p1.jpg",
     			"name": "亿滋奥利奥夹心饼干原味349g独立装12小包装零食",
     			"yprice": 13.9,
     			"xprice": 12.9,
     			"origin": "中国",
     			"quantity": 1000,
     			"sales":9,
     			"time": 1539519963,
     			"explain": "净含量：349g,保质期：12个月",
     			"remark": "存放于阴凉干燥处，避免阳光直射。",
     			"hot": 1
     		}
     		,
     		  {
     			"id": 2,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，肉类",
     			"defaultimg": "p2.jpg",
     			"name": "牛肉片 手撕风干牛肉干五香辣牛肉片500g1斤内蒙特产散装零食包邮",
     			"yprice": 98,
     			"xprice": 88,
     			"origin": "中国",
     			"quantity": 1000,
     			"sales":9,
     			"time": 1539520185,
     			"explain": "净含量：500g,保质期：12个月",
     			"remark": "存放于阴凉干燥处，避免阳光直射。",
     			"hot": 1
     		}
     		,
     			  {
     			"id": 3,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，豆制品",
     			"defaultimg": "p3.jpg",
     			"name": "陕西风味 锅巴 孜然麻辣",
     			"yprice": 24.8,
     			"xprice": 21.9,
     			"origin": "中国",
     			"quantity": 800,
     			"sales":45,
     			"time": 1539520184,
     			"explain": "净含量：500g,保质期：6个月",
     			"remark": "存放于阴凉干燥通风处，避免阳光直射。",
     			"hot": 1
     		}
     		,
     		 {
     			"id": 4,
     			"sort": 1,
     			"status": 0,
     			"bid":1,
     			"Keyword": "休闲零食，肉类",
     			"defaultimg": "p4.jpg",
     			"name": "来伊份鸭肫500g卤味原味真空鸭胗肝鸭肉熟食",
     			"yprice": 56.9,
     			"xprice": 55.9,
     			"origin": "中国",
     			"quantity": 500,
     			"sales":2,
     			"time": 1539520194,
     			"explain": "净含量：500g,保质期：9个月",
     			"remark": "存常温、阴凉、通风、干燥",
     			"hot": 1
     		}
     		 ,   
     		{
     			"id": 5,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，肉类",
     			"defaultimg": "p5.jpg",
     			"name": "新多味烘烤五香花生米5斤装一斤装蒜香花生小包装熟休闲散装零食",
     			"yprice": 56.9,
     			"xprice": 55.9,
     			"origin": "中国",
     			"quantity": 500,
     			"sales":41,
     			"time": 1539520194,
     			"explain": "净含量：500g,保质期：9个月",
     			"remark": "存常温、阴凉、通风、干燥",
     			"hot": 1
     		}
     		,
     		
     		 {
     			"id": 6,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，糕点",
     			"defaultimg": "p6.jpg",
     			"name": "知味观艾草青团网红鲜奶蛋黄肉松糯米果团子杭州特产糕点零食小吃",
     			"yprice": 34.2,
     			"xprice": 32.2,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：500g,保质期：12天",
     			"remark": "存常温、阴凉、通风、干燥",
     			"hot": 1
     		}
     		,
     			 {
     			"id": 7,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，肉类",
     			"defaultimg": "p7.jpg",
     			"name": "知川味素腊肠 齐善素食素食素肉佛家仿荤斋菜食品蛋白肠素肠素零食",
     			"yprice": 15.5,
     			"xprice": 15,
     			"origin": "中国",
     			"quantity": 300,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：200g,保质期：1年",
     			"remark": "常温储存",
     			"hot": 1
     		}
     		,
     	   {
     			"id": 8,
     			"sort": 1,
     			"status": 1,
     			"bid":1,
     			"Keyword": "休闲零食，干果类",
     			"defaultimg": "p8.jpg",
     			"name": "新疆特产吐鲁番特级绿香妃葡萄干500g超大颗粒免洗青提子干果零食",
     			"yprice": 55,
     			"xprice": 55,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：500g,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		}
     		,
     		{
     			"id": 9,
     			"sort": 2,
     			"status": 1,
     			"bid":1,
     			"Keyword": "酒水饮料，鸡尾酒",
     			"defaultimg": "p9.jpg",
     			"name": "  RIO锐澳鸡尾酒套装洋酒女士网红预调酒3度微醺330ml*10罐正品整箱 ",
     			"yprice": 59,
     			"xprice": 55,
     			"origin": "中国",
     			"quantity": 1000,
     			"sales":59,
     			"time": 1539520183,
     			"explain": "净含量：500ml,保质期：36个月",
     			"remark": "存放于阴凉干燥处，避免阳光直射。",
     			"hot": 1
     		}
     		,
     		  {
     			"id": 10,
     			"sort": 2,
     			"status": 1,
     			"bid":1,
     			"Keyword": "酒水饮料，白酒",
     			"defaultimg": "p10.jpg",
     			"name": " 牛栏山二锅头 陈酿42度500ml*12瓶浓香型白牛二白酒  ",
     			"yprice": 78,
     			"xprice": 78,
     			"origin": "中国",
     			"quantity": 180,
     			"sales":20,
     			"time": 1539520185,
     			"explain": "净含量：500ml,保质期：9999个月",
     			"remark": "常温",
     			"hot": 1
     		}
     		,
     			  {
     			"id": 11,
     			"sort": 2,
     			"status": 1,
     			"bid":1,
     			"Keyword": "酒水饮料，果酒",
     			"defaultimg": "p11.jpg",
     			"name": "山谷春 【礼盒装】桑椹果酒13.5度 (干型)桑椹干红桑果酒 750mlx2",
     			"yprice": 24.8,
     			"xprice": 21.9,
     			"origin": "中国",
     			"quantity": 800,
     			"sales":451,
     			"time": 1539520194,
     			"explain": "净含量：750ml,保质期：800个月",
     			"remark": "存放于阴凉干燥通风处，避免阳光直射。",
     			"hot": 1
     		}
     		,
     		 {
     			"id": 12,
     			"sort": 2,
     			"status": 0,
     			"bid":1,
     			"Keyword": "酒水饮料，饮料",
     			"defaultimg": "p12.jpg",
     			"name": "蓝色可乐*5巴厘岛百事蓝可乐印尼进口blue网红碳酸饮料可乐",
     			"yprice": 19.9,
     			"xprice": 18.9,
     			"origin": "中国",
     			"quantity": 500,
     			"sales":42,
     			"time": 1539520194,
     			"explain": "净含量：500ml,保质期：9个月",
     			"remark": "存常温、阴凉、通风、干燥",
     			"hot": 1
     		}
     		 ,   
     		{
     			"id": 13,
     			"sort": 2,
     			"status": 1,
     			"bid":1,
     			"Keyword": "酒水饮料，饮料",
     			"defaultimg": "p13.jpg",
     			"name": "【健力宝官方旗舰店】健力宝经典纪念罐运动饮料330ml*24罐整箱",
     			"yprice": 53.9,
     			"xprice": 52.9,
     			"origin": "中国",
     			"quantity": 500,
     			"sales":45,
     			"time": 1539520194,
     			"explain": "净含量：330ml,保质期：9个月",
     			"remark": "存常温、阴凉、通风、干燥",
     			"hot": 1
     		}
     		
     		,
     		 {
     			"id": 14,
     			"sort": 2,
     			"status": 1,
     			"bid":1,
     			"Keyword": "酒水饮料，饮料",
     			"defaultimg": "p14.jpg",
     			"name": "望山楂山楂汁饮料原果熬制微气泡果饮解辣解腻开胃伴侣300ml*6瓶",
     			"yprice": 91,
     			"xprice": 90,
     			"origin": "中国",
     			"quantity": 100,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：300ml,保质期：200天",
     			"remark": "存常温、阴凉、通风、干燥",
     			"hot": 1
     			}
     		,
     		
     	   {
     			"id": 16,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，食用油",
     			"defaultimg": "p16.jpg",
     			"name": "金龙鱼油5升包邮区域金龙鱼大豆油维生素AE营养食用油炒菜5l桶装",
     			"yprice": 55,
     			"xprice": 49,
     			"origin": "中国",
     			"quantity": 400,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：5L,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 17,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，食用油",
     			"defaultimg": "p17.jpg",
     			"name": "特级初榨纯橄榄油食用油非转基因 500ml凉拌沙拉低脂孕妇护肤压榨",
     			"yprice": 108,
     			"xprice": 107,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":5,
     			"time": 1539520195,
     			"explain": "净含量：500gml,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 18,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，食用油",
     			"defaultimg": "p18.jpg",
     			"name": "四川压榨新菜籽油农家自榨非转基因纯菜籽油粮油食用油5L包邮纯正",
     			"yprice": 55,
     			"xprice": 54,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：5L,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 19,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，调味品",
     			"defaultimg": "p19.jpg",
     			"name": "雅盐 内蒙古雅布赖低钠天然湖盐加碘食用盐350g*4袋无抗结剂家用",
     			"yprice": 17.9,
     			"xprice": 16.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：350g,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 20,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，食用油",
     			"defaultimg": "p20.jpg",
     			"name": "刀唛玉米亚麻籽油4.68L胡麻仁油孕妇宝宝月子油调和油植物油",
     			"yprice": 84.9,
     			"xprice": 82.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：4.68L,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 21,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，面食",
     			"defaultimg": "p21.jpg",
     			"name": "贵州盘县特产手工挂面 碱水面苦荞面 干面条 待煮面条凉面5斤",
     			"yprice": 32.9,
     			"xprice": 31.2,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：5kg,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 22,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，面食",
     			"defaultimg": "p22.jpg",
     			"name": "江西米粉大米米粉 五谷鱼粉花甲米线粗粮渔粉专用粉条20kg袋装",
     			"yprice": 145,
     			"xprice": 140,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：20kg,保质期：3年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 23,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，面食",
     			"defaultimg": "p23.jpg",
     			"name": "8.2斤鹅肠刀削面鱼肠面手工手擀面非油炸爽滑宽面粗面整箱面条",
     			"yprice": 45,
     			"xprice": 45,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：8.2kg,保质期：2年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		},
     		 {
     			"id": 24,
     			"sort": 3,
     			"status": 1,
     			"bid":1,
     			"Keyword": "粮油副食，大米",
     			"defaultimg": "p24.jpg",
     			"name": "江西特产皇阳牌万年贡米大米10斤装真空包装晚稻长粒大米籼米",
     			"yprice": 85,
     			"xprice": 75,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "净含量：10kg,保质期：1年",
     			"remark": "置阴凉处，冷藏保存",
     			"hot": 1
     		}
     		,
     	   {
     			"id": 25,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p25.jpg",
     			"name": "修剪指甲刀套装家用不锈钢耳勺指甲钳修甲工具修脚指甲剪",
     			"yprice": 35.9,
     			"xprice": 32.9,
     			"origin": "德国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "8件套",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 26,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p26.jpg",
     			"name": "萌果宝宝沐浴球沐浴海绵洗澡海绵蜂窝海绵超萌水果造型卡通可爱",
     			"yprice": 16,
     			"xprice": 15,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "3不同水果图案",
     			"remark": "买二赠一",
     			"hot": 1
     		},
     		 {
     			"id": 27,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p27.jpg",
     			"name": "DL/的力洗漱包手提式化妆包便携女防水大容量收纳包健身洗浴包男",
     			"yprice": 55,
     			"xprice": 54,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "小号时尚简约款",
     			"remark": "送钥匙扣一个",
     			"hot": 1
     		},
     		 {
     			"id": 28,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p28.jpg",
     			"name": "圆形加厚松木菜板实木家用砧板厨房切菜板剁肉板菜墩砍大骨头砧板",
     			"yprice": 68,
     			"xprice": 68,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "直径38CM厚度",
     			"remark": "送抹布",
     			"hot": 1
     		},
     		 {
     			"id": 29,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p29.jpg",
     			"name": "加厚大号火锅汤勺漏勺304不锈钢长柄厨房用具厨具套装",
     			"yprice": 21.9,
     			"xprice": 20.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "304不锈钢",
     			"remark": "无赠品", 
     			"hot": 1
     		},
     		 {
     			"id": 30,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p30.jpg",
     			"name": "水龙头防溅头嘴 增压家用厨房定型延伸长器 通用花洒节水过滤喷头",
     			"yprice": 32.9,
     			"xprice": 31.2,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "3档全铜接口防溅头---短",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 31,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p31.jpg",
     			"name": "围裙 防水PVC厨房简约工作服 韩版时尚防水防油厨师围裙男女20020",
     			"yprice": 14,
     			"xprice": 14,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "桔色 白色 银灰色 大红色",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 32,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p32.jpg",
     			"name": "腹肌轮健腹轮家用女士男收腹健身器材自动初学者锻炼卷腹滚轮回弹",
     			"yprice": 18.8,
     			"xprice": 18.8,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "红黑 欧式健腹轮",
     			"remark": "送弹力带一根",
     			"hot": 1
     		},
     		 {
     			"id": 33,
     			"sort": 4,
     			"status": 1,
     			"bid":1,
     			"Keyword": "个人用品，",
     			"defaultimg": "p33.jpg",
     			"name": "奥义tpe瑜伽垫女加宽加厚初学者运动瑜珈毯子加长防滑健身三件套",
     			"yprice": 85,
     			"xprice": 75,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "加宽66cm/荧光紫",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		{
     			"id": 34,
     			"sort": 5,
     			"status": 1,
     			"bid":1,
     			"Keyword": "家居用品，卧室用具",
     			"defaultimg": "p34.jpg",
     			"name": "牛皮拼接圆形地毯客厅茶几毯ins风网红卧室床边圆毯电脑椅垫定制",
     			"yprice": 2100,
     			"xprice": 2098,
     			"origin": "中国",
     			"quantity": 10000,
     			"sales":9999,
     			"time": 1539519963,
     			"explain": "直径1.2米 直径1.6米",
     			"remark": "适用空间: 书房 衣帽间 客厅 门厅",
     			"hot": 1
     		},
     	   {
     			"id": 35,
     			"sort": 5,
     			"status": 1,
     			"bid":1,
     			"Keyword": "家居用品，装饰品",
     			"defaultimg": "p35.jpg",
     			"name": "百家姓玉石平安扣摆件玄关客厅酒柜博古架摆设创意家居装饰品包邮",
     			"yprice": 435.9,
     			"xprice": 432.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "工艺: 半手工",
     			"remark": "适用空间: 客厅",
     			"hot": 1
     		},
     		 {
     			"id": 36,
     			"sort": 5,
     			"status": 1,
     			"bid":1,
     			"Keyword": "家居用品，卫生间用具",
     			"defaultimg": "p36.jpg",
     			"name": "家居样板间装饰品摆件别墅卫生间摆设漱口杯托盘卫浴套装洗漱用品",
     			"yprice": 216,
     			"xprice": 215,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "五件套 托盘 八件套",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 37,
     			"sort": 5,
     			"status": 1,
     			"bid":1,
     			"Keyword": "家居用品，卧室用具",
     			"defaultimg": "p37.jpg",
     			"name": "欧式双耳花瓶陶瓷复古家居饰品古典美式摆件新中式博古架瓷器奢华",
     			"yprice": 155,
     			"xprice": 154,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "适用场景: 玄关 客厅 卧室 桌面 床头",
     			"remark": "送景德镇瓷碗一个",
     			"hot": 1
     		},
     		 {
     			"id": 38,
     			"sort": 5,
     			"status": 1,
     			"bid":1,
     			"Keyword": "家居用品，卧室用具",
     			"defaultimg": "p38.jpg",
     			"name": "加密毛绒雪尼尔飘窗垫定做榻榻米垫毯子阳台垫窗台垫防滑坐垫特价",
     			"yprice": 68,
     			"xprice": 68,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "70*180cm 70*200cm 80*150",
     			"remark": "送抹布",
     			"hot": 1
     		},
     		 {
     			"id": 39,
     			"sort": 5,
     			"status": 1,
     			"bid":1,
     			"Keyword": "家居用品，卧室用具",
     			"defaultimg": "p39.jpg",
     			"name": "",
     			"yprice": 21.9,
     			"xprice": 20.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "304不锈钢",
     			"remark": "无赠品", 
     			"hot": 1
     		},
     		{
     			"id": 40,
     			"sort": 6,
     			"status": 1,
     			"bid":1,
     			"Keyword": "医疗保健，紧急用品",
     			"defaultimg": "p40.jpg",
     			"name": "家用医药箱多层药品收纳箱铝合金急救箱套装儿童药箱应急医疗箱",
     			"yprice": 132.9,
     			"xprice": 131.2,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "材质: 金属",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 41,
     			"sort": 6,
     			"status": 1,
     			"bid":1,
     			"Keyword": "医疗保健，",
     			"defaultimg": "p41.jpg",
     			"name": "测血压心率心电图彩屏智能手环男运动多功能计手表女老人医疗级",
     			"yprice": 414,
     			"xprice": 414,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "桔色 白色 银灰色 大红色",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 42,
     			"sort": 6,
     			"status": 1,
     			"bid":1,
     			"Keyword": "医疗保健，运动健身",
     			"defaultimg": "p42.jpg",
     			"name": "30天续航 TicWatch Pro4G智能手表 成人电话运动GPS防水NFC支付安卓IOS手环 多功能黑科技",
     			"yprice": 1418.8,
     			"xprice": 1318.8,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "幻影黑蓝牙版（150-210毫米腕）",
     			"remark": "保修期: 12个月",
     			"hot": 1
     		},
     		 {
     			"id": 43,
     			"sort": 6,
     			"status": 1,
     			"bid":1,
     			"Keyword": "医疗保健，养生",
     			"defaultimg": "p43.jpg",
     			"name": "养生堂牌B族维生素片 0.5g/片*60片",
     			"yprice": 185,
     			"xprice": 175,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "功能:补充B族维生素",
     			"remark": "保质期：730 天",
     			"hot": 1
     		},	 
     		{ 
     			"id": 44,
     			"sort": 6,
     			"status": 1,
     			"bid":1,
     			"Keyword": "医疗保健，保健品",
     			"defaultimg": "p44.jpg",
     			"name": "通惠牌灵芝孢子虫草菌丝体粉 20g/盒袍子粉",
     			"yprice": 300,
     			"xprice": 298,
     			"origin": "中国",
     			"quantity": 10000,
     			"sales":9999,
     			"time": 1539519963,
     			"explain": "功能:辅助抑制肿瘤",
     			"remark": "保质期：540 天",
     			"hot": 1
     		},
     	   {
     			"id": 45,
     			"sort": 6,
     			"status": 1,
     			"bid":1,
     			"Keyword": "医疗保健，蛋白粉",
     			"defaultimg": "p45.jpg",
     			"name": "姿美堂鱼胶原蛋白粉水解粉液态饮正品口服液肽精华质粉男女非片",
     			"yprice": 435.9,
     			"xprice": 432.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "系列: 胶原蛋白粉",
     			"remark": "保质期: 24个月",
     			"hot": 1
     		},
     		{
     			"id": 46,
     			"sort": 7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，美妆",
     			"defaultimg": "p46.jpg",
     			"name": "美素无瑕光感裸妆BB霜保湿自然裸妆遮瑕隔离防晒护肤化妆品",
     			"yprice": 216,
     			"xprice": 215,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "功效: 防晒 遮瑕 提亮肤色 隔离套",
     			"remark": "化妆品保质期: 36个月，无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 47,
     			"sort": 7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，美妆",
     			"defaultimg": "p47.jpg",
     			"name": "纪梵希明星彩妆套装 小粉唇+小羊皮 口红女唇膏 正品",
     			"yprice": 655,
     			"xprice": 654,
     			"origin": "法国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "彩妆套装: “薄荷绿”限量版唇膏套装",
     			"remark": "保质期：1年",
     			"hot": 1
     		},
     		 {
     			"id": 48,
     			"sort": 7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，美妆工具",
     			"defaultimg": "p48.jpg",
     			"name": "RT多功能焕肤魔法多合一美妆蛋组合6只装",
     			"yprice": 108,
     			"xprice": 99,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "美容工具分类: 化妆海绵",
     			"remark": "无",
     			"hot": 1
     		},
     		 {
     			"id": 49,
     			"sort": 7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，美妆工具",
     			"defaultimg": "p49.jpg",
     			"name": "爱柔纯棉一次性洗脸巾女生卸妆巾洗面巾洁面巾无纺布美容院面巾纸",
     			"yprice": 71.9,
     			"xprice": 60.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "美妆工具分类: 脸部美容化妆用具",
     			"remark": "保质期: 3年", 
     			"hot": 1
     		},
     		 {
     			"id": 50,
     			"sort":7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，护肤",
     			"defaultimg": "p50.jpg",
     			"name": "倩碧面霜 水磁场深层水嫩保湿润肤霜50ml补水保湿乳液",
     			"yprice": 532.9,
     			"xprice": 531.2,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "倩碧单品: 水磁场润肤霜",
     			"remark": "无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 51,
     			"sort": 7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，护肤",
     			"defaultimg": "p51.jpg",
     			"name": "杰威尔男士洗面奶控油祛痘美白去黑头淡痘印洁面乳护肤品套装专用",
     			"yprice":74,
     			"xprice": 64,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "功效: 控油 去黑头 深层清洁",
     			"remark": "化妆品保质期: 36个月",
     			"hot": 1
     		},
     		 {
     			"id": 52,
     			"sort": 7,
     			"status": 1,
     			"bid":1,
     			"Keyword": "美妆护肤，护肤",
     			"defaultimg": "p52.jpg",
     			"name": "薇诺娜洗面奶极润保湿洁面乳深层清洁不含皂基15*3支温和不刺激",
     			"yprice": 1418.8,
     			"xprice": 1318.8,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "幻影黑蓝牙版（150-210毫米腕）",
     			"remark": "保修期: 12个月",
     			"hot": 1
     		},
     		{
     			"id": 53,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，球鞋",
     			"defaultimg": "p53.jpg",
     			"name": "安踏KT4灭霸鸳鸯套装 兰州拉面早茶全明星配色 汤普森4代限量战靴",
     			"yprice": 1185,
     			"xprice": 1175,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "颜色分类: 限量版鸳鸯迷彩",
     			"remark": "适合场地: 室外水泥地，篮球专业比赛鞋",
     			"hot": 1
     		},
     			{ 
     			"id": 54,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，衣服",
     			"defaultimg": "p54.jpg",
     			"name": "李宁羽毛球服ATSK549 553训练轻弹力棉文化衫速干汤尤杯林丹正品",
     			"yprice": 79,
     			"xprice": 75,
     			"origin": "中国",
     			"quantity": 10000,
     			"sales":9999,
     			"time": 1539519963,
     			"explain": "尺码: S M L XL XXL XXXL 更大码",
     			"remark": "颜色分类: ATSK553-2绿 ATSK553-10",
     			"hot": 1
     		},
     	   {
     			"id": 55,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，篮球",
     			"defaultimg": "p55.jpg",
     			"name": "李宁篮球正品7号5头盔哥同款军成人儿童青少年水泥地耐磨室外训练",
     			"yprice": 435.9,
     			"xprice": 432.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "篮球规格: 七号篮球(标准球)",
     			"remark": "颜色分类: 7号黑金送网袋+球袋",
     			"hot": 1
     		},
     		 {
     			"id": 56,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，游泳",
     			"defaultimg": "p56.jpg",
     			"name": "VIZEHO泳镜男女高清防水防雾大框舒适专业 成人儿童游泳眼镜装备",
     			"yprice": 26,
     			"xprice": 25,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "泳镜类型: 休闲泳镜",
     			"remark": "颜色分类: 白色 黑色 紫红色  无赠品",
     			"hot": 1
     		},
     		 {
     			"id": 57,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，户外旅行",
     			"defaultimg": "p57.jpg",
     			"name": "户外6-8人家庭3-4人野外全自动露营大帐篷野营加厚防雨二室一厅",
     			"yprice": 555,
     			"xprice": 554,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "帐篷大小: 5人-8人 帐篷结构: 双层帐",
     			"remark": "支架材质: 铝合金  外帐材质: 190T涤纶布  帐底材质: 210D牛津布防雨5000MM",
     			"hot": 1
     		},
     		 {
     			"id": 58,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，钓具",
     			"defaultimg": "p58.jpg",
     			"name": "日本进口正品DAIWA 达亿瓦 波纹鲤K三代目鲤鱼竿振出竿钓杆台钓竿",
     			"yprice": 3468,
     			"xprice": 3368,
     			"origin": "日本",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "钓竿长度: 3.6m 4.5M 5.4m 6.3m",
     			"remark": "收缩后长度: 104~112cm 先经: 1.0mm  钓竿调性: 硬钓",
     			"hot": 1
     		},
     		 {
     			"id": 59,
     			"sort": 8,
     			"status": 1,
     			"bid":1,
     			"Keyword": "户外运动，钓具",
     			"defaultimg": "p59.jpg",
     			"name": "DAIWA达瓦 REVROS A 2500 2506 路亚轮渔线轮 浅线杯纺车轮矶钓轮",
     			"yprice": 321.9,
     			"xprice": 320.9,
     			"origin": "中国",
     			"quantity": 200,
     			"sales":53,
     			"time": 1539520195,
     			"explain": "304不锈钢",
     			"remark": "轴承数: 5轴", 
     			"hot": 1
     		}
     		
     	],
     	"sort": [
     		{
     			"id": 1,
     			"status": 1,
     			"grade":1,
     			"classify":"",
     			"name": "休闲零食",
     			"quantity": 10000,
     			"sales":"187",
     			"color":"#87CEEB",
     			"img": ""
     		}, {
     			"id": 2,
     			"status": 1,
     			"grade":1,
     			"classify": "",
     			"name": "酒水饮料",
     			"quantity": 10000,
     			"sales":"867",
     			"color":"#87B87F",
     			"img": ""
     		}, {
     			"id": 3,
     			"status":1,
     			"grade":1,
     			"classify": "",
     			"name": "粮油副食",
     			"quantity": 1345,
     			"sales":"867",
     			"color":"#2ab023",
     			"img": ""
     		}, {
     			"id": 4,
     			"status": 1,
     			"grade":1,
     			"classify": "",
     			"name": "个人用品",
     			"quantity": 345,
     			"sales":"267",
     			"color":"#1e3ae6",
     			"img": ""
     		}, {
     			"id": 5,
     			"status": 1,
     			"grade":1,
     			"classify": "",
     			"name": "家居用品",
     			"quantity": 425,
     			"sales":"167",
     			"color":"#87B87F",
     			"img": ""
     		}, {
     			"id": 6,
     			"status": 1,
     			"grade":1,
     			"classify": "",
     			"name": "医疗保健",
     			"quantity": 3312,
     			"sales":"920",
     			"color":"#13a9e1",
     			"img": ""
     		},  {
     			"id": 7,
     			"status": 1,
     			"grade":1,
     			"classify": "",
     			"name": "美妆护肤",
     			"quantity": 145,
     			"sales":"110",
     			"color":"#ff6600",
     			"img": ""
     		}, {
     			"id": 8,
     			"status": 1,
     			"grade":1,
     			"classify": "",
     			"name": "户外运动",
     			"quantity": 11145,
     			"sales":"1100",
     			"color":"#d63116",
     			"img": ""
     		}
     	],"orderstatus":[
     	{
     	 "id":1,
     	 "name":"待发货"	
     	},{
     	 "id":2,
     	 "name":"待收货"	
     	},{
     	 "id":3,
     	 "name":"待付款"	
     	},{
     	 "id":4,
     	 "name":"退货中"	
     	},{
     	 "id":5,
     	 "name":"已完成"	
     	},{
     	 "id":6,
     	 "name":"已退款"	
     	}
     	],"address":[
     	{
     		"id":1,
     		"name":"张小泉",
     		"phone":18934545676,
     		"detailsaddress":"江苏南京市雨花台区郁金香软件大厦3懂3单元302室",
     		"Postalcode":345678		
     	},{
     		"id":2,
     		"name":"黄天师",
     		"phone":13934545342,
     		"detailsaddress":"江苏南京市建邺区相册科技园软件大厦3懂3单元302室",
     		"Postalcode":345678		
     	}
     	
     	],"brandlist": [
     		{
     			"id": 1,
     			"Numbering":"H3432",
     			"sort": 1,
     			"status": 0,
     			"logoImg": "156.jpg",
     			"quantity": 14,
     			"name": "玉兰油OLAY",
     			"area":"法国",
     			"pid":1,
     			"addtime":1539747700,
     			"content":"玉兰油OLAY，是宝洁公司全球著名的护肤品牌，是中国区最大护肤品牌，在大陆已持续十年呈两位数增长。OLAY以全球高科技护肤研发技术为后盾，在深入了解中国女性对护肤和美的需要的基础上，不断扩大产品范围，目前已经涵盖了护肤和沐浴系列，真正帮助女性全面周到地呵护自己的肌肤。玉兰油全球销售额近十亿美金，成为世界上最大、最著名的护肤品牌之一。卓越的护肤功效获得世界爱美女性肯定，迅速畅销150多个国家。玉兰油OLAY，是宝洁公司全球著名的护肤品牌，是中国区最大护肤品牌，在大陆已持续十年呈两位数增长。OLAY以全球高科技护肤研发技术为后盾，在深入了解中国女性对护肤和美的需要的基础上，不断扩大产品范围，目前已经涵盖了护肤和沐浴系列，真正帮助女性全面周到地呵护自己的肌肤。玉兰油全球销售额近十亿美金，成为世界上最大、最著名的护肤品牌之一。卓越的护肤功效获得世界爱美女性肯定，迅速畅销150多个国家。"
     		}, {
     			"id": 2,
     			"Numbering":"H3434",
     			"sort": 1,
     			"status": 1,
     			"logoImg": "34.jpg",
     			"quantity": 21,
     			"name": "比克度",
     			"area":"中国",
     			"pid":2,
     			"addtime":1539748700,
     			"content":"比度克是广州市中通生化制品有限公司旗下品牌。国际知名药妆品牌，针对痘痘、痘印、粉刺、黑头等普遍出现的皮肤问题，专门解决问题肌肤的品牌。"
     		}, {
     			"id": 3,
     			"Numbering":"H346",
     			"sort": 1,
     			"status": 0,
     			"logoImg": "42.jpg",
     			"quantity": 11,
     			"name": "欧莱雅",
     			"area":"法国",
     			"pid":3,
     			"addtime":1539754700,
     			"content":"巴黎欧莱雅（L'OREAL PARIS）是欧莱雅集团里知名度最高、历史最悠久的大众化妆品品牌之一，主要生产染发护发、彩妆及护肤产品，其出众的品质一直倍受全球爱美女性的青睐。巴黎欧莱雅拥有一流的药学试验室和皮肤学中心，还有遍布全球的研究..."
     		}, {
     			"id": 4,
     			"Numbering":"H3437",
     			"sort": 1,
     			"status": 1,
     			"pid":4,
     			"logoImg": "152.jpg",
     			"quantity": 21,
     			"name": "丝塔芙"
     		}, {
     			"id": 5,
     			"Numbering":"H3438",
     			"sort": 4,
     			"status": 1,
     			"logoImg": "1.jpg",
     			"quantity": 66,
     			"name": "华为"
     		}, {
     			"id": 6,
     			"Numbering":"H3439",
     			"sort": 3,
     			"status": 1,
     			"logoImg": "199.jpg",
     			"quantity": 124,
     			"name": "辉子"
     		}, {
     			"id": 7,
     			"Numbering":"H3442",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "245.jpg",
     			"quantity": 24,
     			"name": "御泥坊"
     		}, {
     			"id": 10,
     			"Numbering":"H3444",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "644.jpg",
     			"quantity": 24,
     			"name": "凡茜"
     		}, {
     			"id": 11,
     			"Numbering":"H3447",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "740.jpg",
     			"quantity": 24,
     			"name": "麦秀雷顿"
     		}, {
     			"id": 12,
     			"Numbering":"H3445",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "741.png",
     			"quantity": 24,
     			"name": "水密码"
     		}, {
     			"id": 13,
     			"Numbering":"H3472",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "1396.jpg",
     			"quantity": 24,
     			"name": "美肤宝"
     		}, {
     			"id": 14,
     			"Numbering":"H3482",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "1663.jpg",
     			"quantity": 24,
     			"name": "雪肤晶"
     		}, {
     			"id": 15,
     			"Numbering":"H3492",
     			"sort": 2,
     			"status": 1,
     			"logoImg": "1309.jpg",
     			"quantity": 24,
     			"name": "水密码"
     		}, {
     			"id": 16,
     			"Numbering":"H3232",
     			"sort": 4,
     			"status": 1,
     			"logoImg": "618.jpg",
     			"quantity": 24,
     			"name": "高夫"
     		}, {
     			"id": 17,
     			"Numbering":"H3132",
     			"sort": 4,
     			"status": 1,
     			"logoImg": "1089.jpg",
     			"quantity": 24,
     			"name": "高夫"
     		}, {
     			"id": 18,
     			"Numbering":"H3233",
     			"sort": 4,
     			"status": 1,
     			"logoImg": "2.jpg",
     			"quantity": 24,
     			"name": "小米"
     		}
     	],"kuaidi":[
     {
       "id":1,
       "name":"中通",
       "code":456,
       "rzma":"zt4566765655454343",
       "logoimg":"kd_logo_14.png",
       "content":"中通中通中通中通中通中通中通中通中通中通中通中通中通",
       "status":1	
     },{
       "id":2,
       "name":"圆通",
       "code":236,
       "rzma":"yt4566765655454343",
       "logoimg":"kd_logo_12.png",
       "content":"",
       "status":1	
     },{
       "id":3,
       "name":"申通",
       "rzma":"st4566765655454343",
       "code":346,
       "logoimg":"kd_logo_10.png",
       "content":"申通快递品牌初创于1993年，公司致力于民族品牌的建设和发展，不断完善终端网络、中转运输网络和信息网络三网一体的立体运行体系，立足传统快递业务，全面进入电子商务领域，以专业的服务和严格的质量管理推动中国快递行业的发展。",
       "status":1	
     },{
       "id":4,
       "name":"天天快递",
       "rzma":"tt4566765655454343",
       "code":216,
       "logoimg":"kd_logo_16.png",
       "content":"",
       "status":0	
     },{
       "id":5,
       "name":"韵达快递",
       "rzma":"yd4566765655454343",
       "code":563,
       "logoimg":"kd_logo_07.png",
       "content":"",
       "status":1	
     },{
       "id":6,
       "name":"顺丰",
       "code":225,
       "rzma":"sf4566765655454343",
       "logoimg":"kd_logo_03.png",
       "content":"",
       "status":1	
     },{
       "id":7,
       "name":"百世汇通",
       "rzma":"bsht4566765655454343",
       "code":564,
       "logoimg":"kd_logo_05.png",
       "content":"",
       "status":1	
     },{
       "id":8,
       "name":"优速物流",
       "rzma":"bsht4566765655454343",
       "code":112,
       "logoimg":"kd_logo_04.png",
       "content":"",
       "status":1	
     },{
       "id":9,
       "name":"邮政EMS",
       "rzma":"bsht4566765655454343",
       "code":116,
       "logoimg":"kd_logo_06.png",
       "content":"EMS（即“Express Mail Service”）是邮政特快专递服务，由万国邮联管理下的国际邮件快递服务，在中国境内是由中国邮政提供的一种快递服务。该业务在海关、航空等部门均享有优先处理权，它以高质量为用户传递国际、国内紧急信函、文件资料、金融票据、商品货样等各类文件资料和物品。",
       "status":1	
     }
     ]
     }
     
    ]
    return jsonify(lt)

@app.route('/member/', methods=['GET', 'POST'])
def member():
    lt =[ {
	"data": [
		{
			"id": 1,
			"status": 1,
			"grade": 1,
			"integral": 3456,
			"number": 4565,
			"Headimg":"1.jpg",
			"growthvalue":100,
			"name": "张小民",
			"nickname": "张小小",
			"sex": 2,
			"age": 27,
			"province": "江苏",
			"city": "南京",
			"county": "浦口区",
			"address": "江东中国南路2号将普大厦204号",
			"password": 123456789,
			"phone": "028-56434567",
			"mobilephone": 13845678981,
			"mailbox": "123456789@qq.com",
			"into": "开开心心过每一天的生活！",
			"regtime": 1516603876
		},{
			"id": 2,
			"status": 1,
			"grade": 2,
			"integral": 2590,
			"number": 4565,
			"Headimg":"2.jpg",
			"growthvalue":1000,
			"name": "李明",
			"nickname": "李师师",
			"sex":1,
			"age": 27,
			"province": "江苏",
			"city": "南京",
			"county": "建邺区",
			"address": "江东中国南路2号将普大厦204号",
			"password": 123456789,
			"phone": "028-56434567",
			"mobilephone": 18945678900,
			"mailbox": "123456789@qq.com",
			"into": "开开心心过每一天的生活！",
			"regtime": 1519282276
		},{
			"id": 3,
			"status": 0,
			"grade": 3,
			"integral": 15000,
			"Headimg":"3.jpg",
			"growthvalue":2500,
			"number": 4565,
			"name": "华国锋",
			"nickname": "天下无贼",
			"sex":1,
			"age": 27,
			"province": "江苏",
			"city": "连云港",
			"county": "开发新区",
			"address": "江东中国南路2号将普大厦204号",
			"password": 123456789,
			"phone": "028-56434567",
			"mobilephone": 18945678900,
			"mailbox": "123456789@qq.com",
			"into": "开开心心过每一天的生活！",
			"regtime": 1518418276
		},{
			"id": 4,
			"status": 0,
			"grade": 4,
			"integral": 15000,
			"Headimg":"4.jpg",
			"growthvalue":6000,
			"number": 4565,
			"name": "张雯",
			"nickname": "小宝贝",
			"sex":0,
			"age": 27,
			"province": "",
			"city": "上海",
			"county": "普陀区",
			"address": "江东中国南路2号将普大厦204号",
			"password": 123456789,
			"phone": "028-56434567",
			"mobilephone": 18945678900,
			"mailbox": "123456789@qq.com",
			"into": "开开心心过每一天的生活！",
			"regtime": 1514789476
		},{
			"id": 5,
			"status":1,
			"grade": 3,
			"integral": 15000,
			"Headimg":"5.jpg",
			"growthvalue":6000,
			"number": 4565,
			"name": "胡小兵",
			"nickname": "天师大侠",
			"sex":1,
			"age": 21,
			"province": "",
			"city": "北京",
			"county": "朝阳区",
			"address": "江东中国南路2号将普大厦204号",
			"password": 123456789,
			"phone": "028-56434567",
			"mobilephone": 18945678900,
			"mailbox": "123456789@qq.com",
			"into": "开开心心过每一天的生活！",
			"regtime": 1514789476
		},{
			"id": 6,
			"status":1,
			"grade": 1,
			"integral": 15000,
			"Headimg":"5.jpg",
			"growthvalue":50,
			"number": 4565,
			"name": "黄磊",
			"nickname": "磊磊宝贝",
			"sex":1,
			"age": 21,
			"province": "河北",
			"city": "保定",
			"county": "朝阳区",
			"address": "江东中国南路2号将普大厦204号",
			"password": 123456789,
			"phone": "028-56434567",
			"mobilephone": 18945678900,
			"mailbox": "123456789@qq.com",
			"into": "开开心心过每一天的生活！",
			"regtime": 1514799476
		}
	],"grade":[{
		 "id":1,
		 "name":"注册会员",
		 "quantity":2,
		 "growthvalue":0	
	},{
		 "id":2,
		 "name":"铜牌会员",
		 "quantity":1,
		 "growthvalue":100	
	},{
		 "id":3,
		 "name":"银牌会员",
		  "quantity":2,
		 "growthvalue":2500	
	},{
		 "id":4,
		 "name":"金牌会员",
		  "quantity":1,
		 "growthvalue":5000	
	},{
		 "id":5,
		 "name":"金钻会员",
		 "quantity":0,
		 "growthvalue":10000	
	}]}]return jsonify(lt)

@app.route('/userData/', methods=['GET', 'POST'])
def userData():
    lt = [
        {
        	"data": [
        		{
        			"id": 0,
        			"ip": "66.183.254.66",
        			"address": "绵阳",
        			"status": 0,
        			"starttime": 1556092463,
        			"name": "明方",
        			"endtime": "",
        			"grade": "超级管理员"
        		}, {
        			"id": 1,
        			"ip": "66.183.254.66",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1555092463,
        			"name": "明方",
        			"endtime": 1555192463,
        			"grade": "超级管理员"
        		}, {
        			"id": 2,
        			"ip": "66.183.254.66",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1554092463,
        			"name": "明方",
        			"endtime": 1554096463,
        			"grade": "超级管理员"
        		}, {
        			"id": 3,
        			"ip": "192.168.0.223",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1554082463,
        			"name": "明方",
        			"endtime": 1554072463,
        			"grade": "超级管理员"
        		}, {
        			"id": 4,
        			"ip": "42.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1554042463,
        			"name": "花海",
        			"endtime": 1554052463,
        			"grade": "普通管理员"
        		}, {
        			"id": 5,
        			"ip": "42.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1554032463,
        			"name": "花海",
        			"endtime": 1554032963,
        			"grade": "普通管理员"
        		}, {
        			"id": 6,
        			"ip": "42.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1554002463,
        			"name": "花海",
        			"endtime": 1553992463,
        			"grade": "普通管理员"
        		}, {
        			"id": 7,
        			"ip": "42.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1553952463,
        			"name": "飞羽",
        			"endtime": 1553972463,
        			"grade": "普通管理员"
        		}, {
        			"id": 8,
        			"ip": "42.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1553892463,
        			"name": "飞羽",
        			"endtime": 1553922463,
        			"grade": "普通管理员"
        		}, {
        			"id": 9,
        			"ip": "42.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1553702463,
        			"name": "飞羽",
        			"endtime": 1553792463 ,
        			"grade": "普通管理员"
        		}
        		, {
        			"id": 10,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"starttime": 1553092463,
        			"name": "飞羽",
        			"endtime": 1553162463,
        			"grade": "普通管理员"
        		}
        	],
        	"user": [
        		{
        			"id": 0,
        			"ip": "66.183.254.66",
        			"address": "绵阳",
        			"status": 0,
        			"starttime": 1556092463,
        			"name": "明方",
        			"endtime":"",
        			"grade": 3,
        			"sex":"男",
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"管理部",
        			"position":"经理",
        			"password":123456789
        		}
        	],"grade":[
        	{
        		"id":1,
        		"name":"店长"			
        	},{
        		"id":2,
        		"name":"管理员"			
        	}],"administrator":[
        	{
        		    "id": 0,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 0,
        			"statushut": 1,
        			"starttime": 1539211963,
        			"name": "惊鸿",
        			"registeredtime":1519111963,
        			"endtime":"",
        			"grade": 1,
        			"sex":1,
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"技术部",
        			"position":"经理",
        			"password":123456789
        		
        	},{
        		    "id": 1,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 0,
        			"statushut": 1,
        			"starttime": 1539211963,
        			"name": "明方",
        			"registeredtime":1536111963,
        			"endtime":"",
        			"grade": 2,
        			"sex":1,
        			"age":18,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"管理部",
        			"position":"经理",
        			"password":123456789
        		
        	},{
        		    "id": 2,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 0,
        			"statushut": 1,
        			"starttime": 1539211963,
        			"name": "飞羽",
        			"registeredtime":1519234963,
        			"endtime":"",
        			"grade": 2,
        			"sex":1,
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"管理部",
        			"position":"经理",
        			"password":123456789
        		
        	},{
        		    "id": 3,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 0,
        			"statushut": 1,
        			"starttime": 1539211963,
        			"name": "花海",
        			"registeredtime":1519234963,
        			"endtime":"",
        			"grade": 2,
        			"sex":1,
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"技术部",
        			"position":"技术",
        			"password":123456789
        		
        	},{
        		    "id": 4,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 0,
        			"statushut": 1,
        			"starttime": 1539211963,
        			"name": "雪舞",
        			"registeredtime":1519234963,
        			"endtime":"",
        			"grade": 2,
        			"sex":1,
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"技术部",
        			"position":"技术",
        			"password":123456789
        		
        	},{
        		    "id": 5,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 0,
        			"statushut": 1,
        			"starttime": 1539611963,
        			"name": "云烟",
        			"registeredtime":1549234963,
        			"endtime":"",
        			"grade": 2,
        			"sex":1,
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"技术部",
        			"position":"技术",
        			"password":123456789
        		
        	},{
        		    "id": 6,
        			"ip": "48.168.6.56",
        			"address": "绵阳",
        			"status": 1,
        			"statushut": 0,
        			"starttime": 1545511963,
        			"name": "紫月",
        			"registeredtime":1515534963,
        			"endtime":"",
        			"grade": 1,
        			"sex":1,
        			"age":28,
        			"Avatar":"",
        			"Phone":"18923456789",
        			"mailbox":"1915668836@qq.com",
        			"content":"注意安全操作",
        			"department":"技术部",
        			"position":"技术",
        			"password":123456789
        		
        	}
        	]
        }
        ]

    return jsonify(lt)

@app.route('/defray/', methods=['GET', 'POST'])
def defray():
    lt = [
       {"data":[
       {
       	"id":0,
       	"status": 1,
       	"type":1,
       	"name":"支付宝",
       	"Settlement":"人民币",
       	"img":"zhifb.jpg",
       	"country":"中华人民共和国",
       	"content":"支付宝 （中国）网络技术有限公司是国内的第三方支付平台，致力于提供“简单、安全、快速”的支付解决方案。 支付宝公司从2004年建立开始，始终以“信任”作为产品和服务的核心。旗下有“支付宝”与“支付宝钱包”两个独立品牌。自2014年第二季度开始成为当前全球最大的移动支付厂商。支付宝与国内外180多家银行以及VISA、MasterCard国际组织等机构建立战略合作关系，成为金融机构在电子支付领域最为信任的合作伙伴。2018年4月1日起，支付宝、微信静态条码支付，每天限额500元。 [2-3]  2018年8月21日，支付宝官方微博、蚂蚁金服安全中心官方微博消息，支付宝发布延时到账功能全面升级，被骗资金有望追回。",
       	"illustrate":"支付宝（中国）网络技术有限公司是国内领先的第三方支付平台，致力于提供“简单、安全、快速”的支付解决方案",
       	"bank":[{
       		"id":0,
       		"img":"black4.png",
       		"name":"中国银行"
       	},{
       		"id":1,
       		"img":"black1.png",
       		"name":"中信银行"
       	},{
       		"id":2,
       		"img":"black2.png",
       		"name":"中国工商银行"
       	},{
       		"id":3,
       		"img":"black3.png",
       		"name":"中国农业银行"
       	},{
       		"id":5,
       		"img":"black5.png",
       		"name":"中国建设银行"
       	},{
       		"id":6,
       		"img":"black6.png",
       		"name":"交通银行"
       	},{
       		"id":7,
       		"img":"black7.png",
       		"name":"深圳发展银行"
       	},{
       		"id":8,
       		"img":"black8.png",
       		"name":"广东发展银行"
       	},{
       		"id":9,
       		"img":"black9.png",
       		"name":"中国民生银行"
       	},{
       		"id":10,
       		"img":"black10.png",
       		"name":"招商银行"
       	}
       	],
       	"time":1539619513,
       	"endtime":1594619513
       	
       },{
       	"id":1,
       	"status": 1,
       	"type":1,
       	"name":"微信",
       	"Settlement":"人民币",
       	"img":"weixin.jpg",
       	"country":"中华人民共和国",
       	"content":"微信 （中国）网络技术有限公司是国内的第三方支付平台，致力于提供“简单、安全、快速”的支付解决方案。 支付宝公司从2004年建立开始，始终以“信任”作为产品和服务的核心。旗下有“支付宝”与“支付宝钱包”两个独立品牌。自2014年第二季度开始成为当前全球最大的移动支付厂商。支付宝与国内外180多家银行以及VISA、MasterCard国际组织等机构建立战略合作关系，成为金融机构在电子支付领域最为信任的合作伙伴。2018年4月1日起，支付宝、微信静态条码支付，每天限额500元。 [2-3]  2018年8月21日，支付宝官方微博、蚂蚁金服安全中心官方微博消息，支付宝发布延时到账功能全面升级，被骗资金有望追回。",
       	"illustrate":"微信支付是集成在微信客户端的支付功能，用户可以通过手机完成快速的支付流程。",
       	"bank":[{
       		"id":0,
       		"img":"black4.png",
       		"name":"中国银行"
       	},{
       		"id":1,
       		"img":"black1.png",
       		"name":"中信银行"
       	},{
       		"id":2,
       		"img":"black2.png",
       		"name":"中国工商银行"
       	},{
       		"id":3,
       		"img":"black3.png",
       		"name":"中国农业银行"
       	},{
       		"id":5,
       		"img":"black5.png",
       		"name":"中国建设银行"
       	},{
       		"id":6,
       		"img":"black6.png",
       		"name":"交通银行"
       	},{
       		"id":7,
       		"img":"black7.png",
       		"name":"深圳发展银行"
       	},{
       		"id":8,
       		"img":"black8.png",
       		"name":"广东发展银行"
       	},{
       		"id":9,
       		"img":"black9.png",
       		"name":"中国民生银行"
       	},{
       		"id":10,
       		"img":"black10.png",
       		"name":"招商银行"
       	},{
       		"id":11,
       		"img":"black11.png",
       		"name":"华夏银行"
       	},{
       		"id":12,
       		"img":"black12.png",
       		"name":"中国光大银行"
       	},{
       		"id":13,
       		"img":"black13.png",
       		"name":"北京银行"
       	},{
       		"id":14,
       		"img":"black14.png",
       		"name":"上海银行"
       	},{
       		"id":15,
       		"img":"black15.png",
       		"name":"厦门国际银行"
       	}
       	],
       	"time":1539622513,
       	"endtime":1594619513
       	
       },{
       	"id":2,
       	"status": 0,
       	"type":1,
       	"name":"银联支付",
       	"img":"yinglian.jpg",
       	"Settlement":"人民币",
       	"country":"中华人民共和国",
       	"content":"作为中国的银行卡联合组织，中国银联处于我国银行卡产业的核心和枢纽地位，对我国银行卡产业发展发挥着基础性作用，各银行通过银联跨行交易清算系统，实现了系统间的互联互通，进而使银行卡得以跨银行、跨地区和跨境使用。在建设和运营银联跨行交易清算系统、实现银行卡联网通用的基础上，中国银联积极联合商业银行等产业各方推广统一的银联卡标准规范，创建银行卡自主品牌；推动银行卡的发展和应用；维护银行卡受理市场秩序，防范银行卡风险。通过银联跨行交易清算系统，实现商业银行系统间的互联互通和资源共享，保证银行卡跨行、跨地区和跨境的使用。",
       	"illustrate":"作为中国的银行卡联合组织，实现了系统间的互联互通，进而使银行卡得以跨银行、跨地区和跨境使用",
       	"bank":[{
       		"id":0,
       		"img":"black4.png",
       		"name":"中国银行"
       	},{
       		"id":1,
       		"img":"black1.png",
       		"name":"中信银行"
       	},{
       		"id":2,
       		"img":"black2.png",
       		"name":"中国工商银行"
       	},{
       		"id":3,
       		"img":"black3.png",
       		"name":"中国农业银行"
       	},{
       		"id":5,
       		"img":"black5.png",
       		"name":"中国建设银行"
       	},{
       		"id":6,
       		"img":"black6.png",
       		"name":"交通银行"
       	},{
       		"id":7,
       		"img":"black7.png",
       		"name":"深圳发展银行"
       	},{
       		"id":8,
       		"img":"black8.png",
       		"name":"广东发展银行"
       	},{
       		"id":9,
       		"img":"black9.png",
       		"name":"中国民生银行"
       	},{
       		"id":10,
       		"img":"black10.png",
       		"name":"招商银行"
       	}
       	],
       	"time":1539622513,
       	"endtime":1594619513
       	
       },{
       	"id":3,
       	"status": 0,
       	"type":1,
       	"name":"易宝支付（预存）",
       	"img":"yozhif.jpg",
       	"Settlement":"人民币",
       	"country":"中华人民共和国",
       	"content":"易宝支付易宝支付易宝支付易宝支付易宝支付易宝支付易宝支付易宝支付易宝支付",
       	"illustrate":"易宝支付",
       	"bank":[{
       		"id":1,
       		"img":"black1.png",
       		"name":"中信银行"
       	},{
       		"id":2,
       		"img":"black2.png",
       		"name":"中国工商银行"
       	},{
       		"id":3,
       		"img":"black3.png",
       		"name":"中国农业银行"
       	},{
       		"id":5,
       		"img":"black5.png",
       		"name":"中国建设银行"
       	},{
       		"id":6,
       		"img":"black6.png",
       		"name":"交通银行"
       	},{
       		"id":7,
       		"img":"black7.png",
       		"name":"深圳发展银行"
       	},{
       		"id":8,
       		"img":"black8.png",
       		"name":"广东发展银行"
       	},{
       		"id":9,
       		"img":"black9.png",
       		"name":"中国民生银行"
       	}
       	],
       	"time":1539623513,
       	"endtime":1584619513
       	
       }
       ],"type":[
       {
       	"id":0,
       	"status":0,
       	"name":"银联支付",
       	"content":"作为中国的银行卡联合组织，实现了系统间的互联互通，进而使银行卡得以跨银行、跨地区和跨境使用"
       },{
       	"id":1,
       	"status":1,
       	"name":"在线预存",
       	"content":"作为中国的银行卡联合组织，实现了系统间的互联互通，进而使银行卡得以跨银行、跨地区和跨境使用"
       },{
       	"id":2,
       	"status":1,
       	"name":"第三方支付（支付宝）平台",
       	"content":"在线支付（第三方支付平台）支付宝，微信，财付通等"
       },{
       	"id":3,
       	"status":1,
       	"name":"信用卡、储蓄卡",
       	"content":"直接使用开通的信用卡支付"
       },{
       	"id":4,
       	"status":1,
       	"name":"货到付款",
       	"content":"在线支付是指卖方与买方通过因特网上的电子商务网站进行交易时，银行为其提供网上资金结算服务的一种业务。它为企业和个人提供了一个安全、快捷、方便的电"
       },{
       	"id":5,
       	"status":1,
       	"name":"红包抵扣",
       	"content":"支持红包付款的才能使用，红包直接抵扣相应的金额"
       },{
       	"id":6,
       	"status":0,
       	"name":"积分抵扣",
       	"content":"支持用户积分抵扣相应的订单金额"
       }
       ]}
       
        ]

    return jsonify(lt)

if __name__ == '__main__':
    app.run(debug=True)

# app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行。
