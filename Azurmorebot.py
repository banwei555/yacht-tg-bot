# 新增：导入保活函数
from keep_alive import keep_alive

ADMIN_ID = 8655639490



YACHTS = [
    {
        "size": 33.5,
        "types": ["钓鱼", "运动", "专业", "单体", "巡航"],
        "name_zh": "美国波士顿捕鲸者350英尺军警版专业豪华钓鱼艇",
        "name_en": "Military Police Version American Boston Whaler 350 Professional Luxury Fishing Boat",
        "name_ru": "Профессиональная роскошная рыбацкая лодка Boston Whaler 350 футов версия для военной полиции США",
        "desc_zh": "美式专业军警级工艺，顶级钓鱼配置，超强抗风浪性能，专业海钓与远海作业的全能之选",
        "desc_en": "American professional military police-grade craftsmanship, top-level fishing configuration, super strong wind and wave resistance, all-round choice for professional sea fishing and offshore operations",
        "desc_ru": "Американское профессиональное мастерство уровня военной полиции, топовая комплектация для рыбалки, сверхпрочная устойчивость к ветру и волнам, универсальное решение для профессиональной морской рыбалки и морских операций",
        "url": "https://www.azurmore.com/productinfo/3607122.html",
        "price": 168
    },
    {
        "size": 55,
        "types": ["飞桥", "硬顶", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利法拉帝Ferretti 550硬顶飞桥游艇",
        "name_en": "Ferretti 550 Hardtop Flybridge Yacht",
        "name_ru": "Яхта Ferretti 550 с флайбриджем и хардтопом",
        "desc_zh": "意式经典奢华设计，硬顶飞桥双布局，宽敞商务空间，稳定巡航性能，高端商务接待与休闲巡航的标杆之选",
        "desc_en": "Italian classic luxury design, dual layout of hardtop and flybridge, spacious business space, stable cruising performance, benchmark choice for high-end business hosting and leisure cruising",
        "desc_ru": "Классический итальянский роскошный дизайн, двойная планировка с хардтопом и флайбриджем, просторное деловое пространство, стабильные ходовые характеристики, эталонный выбор для высококлассных деловых приёмов и прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607120.html",
        "price": 480
    },
    {
        "size": 42,
        "types": ["钓鱼", "运动", "专业", "单体", "巡航"],
        "name_zh": "途达Tuda 42英尺二类专业钓鱼艇",
        "name_en": "Tuda 42-foot Class II Professional Fishing Boat",
        "name_ru": "Профессиональная рыбацкая лодка Tuda 42 фута, класс II",
        "desc_zh": "国产专业二类钓鱼艇，专业海钓配置，灵活操控性能，高性价比，近海海钓与休闲出海的实用之选",
        "desc_en": "Domestic professional Class II fishing boat, professional sea fishing configuration, flexible handling performance, cost-effective, practical choice for offshore sea fishing and leisure sailing",
        "desc_ru": "Отечественная профессиональная рыбацкая лодка класса II, профессиональная комплектация для морской рыбалки, гибкое управление, выгодное соотношение цена-качество, практичный выбор для прибрежной морской рыбалки и отдыха в море",
        "url": "https://www.azurmore.com/productinfo/3607121.html",
        "price": 168
    },
    {
        "size": 62,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 62英尺飞桥游艇",
        "name_en": "Azimut 62-foot flybridge yacht from Italy",
        "name_ru": "Итальянская яхта Azimut 62 фута с флайбриджем",
        "desc_zh": "意式轻奢设计，飞桥全景视野，精致内饰布局，强劲动力性能，商务接待与近海休闲巡航的优选",
        "desc_en": "Italian light luxury design, panoramic view of flybridge, exquisite interior layout, powerful dynamic performance, ideal choice for business hosting and offshore leisure cruising",
        "desc_ru": "Итальянский дизайн в стиле легкой роскоши, панорамный обзор с флайбриджа, изысканная планировка интерьера, мощные динамические характеристики, идеальный выбор для деловых приёмов и прибрежных прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607119.html",
        "price": 260
    },
    {
        "size": 66,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "美国侯爵Marquis 660豪华飞桥游艇",
        "name_en": "American Marquis 660 Luxury Flybridge Yacht",
        "name_ru": "Американская роскошная яхта Marquis 660 с флайбриджем",
        "desc_zh": "美式硬核豪华工艺，大尺寸飞桥空间，强劲动力系统，舒适内饰布局，商务接待与远海巡航的品质之选",
        "desc_en": "American hardcore luxury craftsmanship, large-size flybridge space, powerful power system, comfortable interior layout, high-quality choice for business hosting and offshore cruising",
        "desc_ru": "Американская высококачественная роскошная мастерская работа, просторный флайбридж, мощная силовая установка, комфортная планировка интерьера, высококачественный выбор для деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3607118.html",
        "price": 660
    },
    {
        "size": 95,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "2010款意大利阿兹慕Azimut 95旗舰游艇",
        "name_en": "2010 Italian Azimut 95 flagship yacht",
        "name_ru": "Флагманская итальянская яхта Azimut 95, 2010 года выпуска",
        "desc_zh": "阿兹慕经典旗舰款，超大奢华空间，顶级定制配置，超长续航能力，高端圈层商务接待与跨洋巡航的臻选",
        "desc_en": "Azimut classic flagship model, super large luxury space, top-level custom configuration, ultra-long endurance, perfect choice for high-end circle business hosting and transoceanic cruising",
        "desc_ru": "Классическая флагманская модель Azimut, просторное роскошное пространство, топовая комплектация на заказ, сверхдальний запас хода, идеальный выбор для деловых приёмов в высших кругах и трансокеанских круизов",
        "url": "https://www.azurmore.com/productinfo/3596570.html",
        "price": 2000
    },
    {
        "size": 112,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "意大利法拉帝Ferretti 112英尺超级游艇",
        "name_en": "Ferretti 112-foot Superyacht",
        "name_ru": "Суперяхта Ferretti 112 футов, Италия",
        "desc_zh": "法拉帝顶级超级游艇，全手工奢华工艺，全场景定制化配置，超大私密起居空间，环球航行与顶级商务社交的旗舰之选",
        "desc_en": "Ferretti top-level superyacht, fully handcrafted luxury craftsmanship, full-scene customized configuration, super large private living space, flagship choice for world sailing and top business socializing",
        "desc_ru": "Топовая суперяхта Ferretti, полностью ручная роскошная мастерская работа, полная персонализированная комплектация для любых сценариев, просторное приватное жилое пространство, флагманский выбор для кругосветных плаваний и делового общения высочайшего уровня",
        "url": "https://www.azurmore.com/productinfo/3595372.html",
        "price": 1088
    },
    {
        "size": 112,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "星瑞Asteria 112英尺超级游艇",
        "name_en": "Asteria 112-foot Superyacht",
        "name_ru": "Суперяхта Asteria 112 футов",
        "desc_zh": "国产高端定制超级游艇，国际化豪华配置，超大空间布局，优秀续航性能，高端商务接待与远海巡航的旗舰之选",
        "desc_en": "Domestic high-end custom superyacht, international luxury configuration, super large space layout, excellent endurance performance, flagship choice for high-end business hosting and offshore cruising",
        "desc_ru": "Отечественная высококлассная суперяхта на заказ, международная роскошная комплектация, просторная планировка пространства, отличный запас хода, флагманский выбор для высококлассных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3595351.html",
        "price": 1680
    },
    {
        "size": 110,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "中国台湾嘉鸿Horizon 110英尺超级游艇",
        "name_en": "Horizon 110 Foot Superyacht",
        "name_ru": "Суперяхта Horizon 110 футов, Тайвань, Китай",
        "desc_zh": "亚洲顶级定制游艇品牌，全手工奢华工艺，全场景个性化定制，超长跨洋续航能力，顶级商务社交与环球航行的臻选",
        "desc_en": "Asia's top custom yacht brand, fully handcrafted luxury craftsmanship, full-scene personalized customization, ultra-long transoceanic endurance, perfect choice for top business socializing and world sailing",
        "desc_ru": "Лучший азиатский бренд яхт на заказ, полностью ручная роскошная мастерская работа, полная персонализация для любых сценариев, сверхдальний запас хода для трансокеанских плаваний, идеальный выбор для делового общения высочайшего уровня и кругосветных путешествий",
        "url": "https://www.azurmore.com/productinfo/3584817.html",
        "price": 1980
    },
    {
        "size": 60,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 60英尺豪华飞桥游艇",
        "name_en": "Azimut 60 Foot Luxury Flying Bridge Yacht from Italy",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Azimut 60 футов",
        "desc_zh": "阿兹慕经典畅销款，意式精致奢华设计，飞桥全景视野，灵活操控性能，商务接待与近海休闲巡航的优选",
        "desc_en": "Azimut classic best-selling model, Italian exquisite luxury design, panoramic view of flybridge, flexible handling performance, ideal choice for business hosting and offshore leisure cruising",
        "desc_ru": "Классическая бестселлерная модель Azimut, изысканный итальянский роскошный дизайн, панорамный обзор с флайбриджа, гибкое управление, идеальный выбор для деловых приёмов и прибрежных прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3584805.html",
        "price": 970
    },
    {
        "size": 55,
        "types": ["飞桥", "硬顶", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利法拉帝Ferretti 550硬顶飞桥游艇",
        "name_en": "Italian Ferretti 550 Hard Top Flybridge Yacht",
        "name_ru": "Итальянская яхта Ferretti 550 с флайбриджем и жёстким верхом",
        "desc_zh": "意大利法拉帝经典豪华款，全封闭硬顶飞桥双布局设计，意式手工奢华内饰，宽敞商务会客空间，稳定强劲的动力系统，是高端商务接待与近海休闲远航的标杆之选",
        "desc_en": "Classic luxury model from Italian Ferretti, fully enclosed hardtop and flybridge dual layout design, Italian handcrafted luxury interior, spacious business reception space, stable and powerful power system, a benchmark choice for high-end business hosting and offshore leisure long-distance sailing",
        "desc_ru": "Классическая роскошная модель итальянского бренда Ferretti, конструкция с полностью закрытым хардтопом и флайбриджем, роскошный итальянский интерьер ручной работы, просторное пространство для деловых приёмов, стабильная и мощная силовая установка, эталонный выбор для высококлассных деловых приёмов и дальних прогулочных плаваний в прибрежной зоне",
        "url": "https://www.azurmore.com/productinfo/3583364.html",
        "price": 960
    },
    {
        "size": 80,
        "types": ["飞桥", "豪华", "商务", "巡航", "双体", "接待"],
        "name_zh": "波兰Sunreef 80英尺超豪华双体游艇",
        "name_en": "Polish Sunreef 80 foot ultra luxury catamaran yacht",
        "name_ru": "Ультрароскошный катамаран Sunreef 80 футов, Польша",
        "desc_zh": "双体游艇标杆品牌，超大宽体空间设计，可跨洋航行能力，全定制奢华配置，商务接待与长途航海的理想之选",
        "desc_en": "Benchmark brand of catamaran yachts, super large wide-body space design, ocean-crossing capability, fully customized luxury configuration, ideal choice for business hosting and long-distance sailing",
        "desc_ru": "Эталонный бренд катамаранов, просторная ширококорпусная конструкция, возможность трансокеанских переходов, полностью настраиваемая роскошная комплектация, идеальный выбор для деловых приёмов и дальних морских плаваний",
        "url": "https://www.azurmore.com/productinfo/3579536.html",
        "price": 7960
    },
    {
        "size": 50,
        "types": ["帆船", "双体", "豪华", "巡航", "休闲"],
        "name_zh": "法国蓝高LAGOON 50英尺双体豪华帆船",
        "name_en": "France LAGOON 50-foot twin-hull luxury sailboat",
        "name_ru": "Двухкорпусная роскошная парусная лодка LAGOON 50 футов, Франция",
        "desc_zh": "全球双体帆船标杆品牌，超大舒适空间，专业航海性能，稳定易操控，休闲航海旅行与远洋巡航的经典之选",
        "desc_en": "Global benchmark brand of catamaran sailboats, super large comfortable space, professional sailing performance, stable and easy to handle, classic choice for leisure sailing trips and ocean cruising",
        "desc_ru": "Эталонный мировой бренд парусных катамаранов, просторное комфортное пространство, профессиональные ходовые характеристики под парусом, стабильная и простая в управлении, классический выбор для отдыха под парусом и океанских круизов",
        "url": "https://www.azurmore.com/productinfo/3607236.html",
        "price": 680
    },
    {
        "size": 56,
        "types": ["帆船", "单体", "豪华", "巡航", "休闲"],
        "name_zh": "法国丹枫Dufour 56英尺豪华帆船",
        "name_en": "France DUFOUR 56-foot luxury sailboat",
        "name_ru": "Роскошная парусная лодка DUFOUR 56 футов, Франция",
        "desc_zh": "法国顶级帆船品牌，专业远洋航海性能，舒适奢华内饰，灵活操控设计，环球航海与高端休闲航海的品质之选",
        "desc_en": "France's top sailboat brand, professional ocean sailing performance, comfortable and luxurious interior, flexible handling design, high-quality choice for world sailing and high-end leisure sailing",
        "desc_ru": "Лучший французский бренд парусных лодок, профессиональные характеристики для океанских плаваний под парусом, комфортный роскошный интерьер, гибкая конструкция управления, высококачественный выбор для кругосветных плаваний и высококлассного отдыха под парусом",
        "url": "https://www.azurmore.com/productinfo/3607231.html",
        "price": 650
    },
    {
        "size": 42,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "波兰卡帝尔GALEON 42英尺豪华飞桥游艇",
        "name_en": "Poland GALEON 42-foot luxury flybridge yacht",
        "name_ru": "Роскошная яхта с флайбриджем GALEON 42 фута, Польша",
        "desc_zh": "欧洲新锐豪华游艇品牌，创新变形空间设计，精致内饰布局，强劲动力性能，商务接待与休闲巡航的优选",
        "desc_en": "Europe's cutting-edge luxury yacht brand, innovative transformable space design, exquisite interior layout, powerful dynamic performance, ideal choice for business hosting and leisure cruising",
        "desc_ru": "Передовой европейский бренд роскошных яхт, инновационная трансформируемая планировка пространства, изысканный интерьер, мощные динамические характеристики, идеальный выбор для деловых приёмов и прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607218.html",
        "price": 228
    },
    {
        "size": 54,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "英国公主PRINCESS 54英尺豪华飞桥游艇",
        "name_en": "UK PRINCESS 54-foot luxury flybridge yacht",
        "name_ru": "Роскошная яхта с флайбриджем PRINCESS 54 фута, Великобритания",
        "desc_zh": "英伦皇室级豪华游艇品牌，经典优雅设计，精湛手工工艺，静谧舒适航行体验，高端商务接待与休闲远航的臻选",
        "desc_en": "British royal-class luxury yacht brand, classic and elegant design, exquisite handcraftsmanship, quiet and comfortable sailing experience, perfect choice for high-end business hosting and leisure long-distance sailing",
        "desc_ru": "Британский бренд роскошных яхт королевского класса, классический элегантный дизайн, безупречная ручная работа, тихая и комфортная ходовая характеристика, идеальный выбор для высококлассных деловых приёмов и дальних прогулочных плаваний",
        "url": "https://www.azurmore.com/productinfo/3607213.html",
        "price": 360
    },
    {
        "size": 50,
        "types": ["运动", "豪华", "商务", "巡航", "单体"],
        "name_zh": "法国亚诺Jeanneau旗下PRESTIGE 50英尺豪华运动游艇",
        "name_en": "French PRESTIGE 50-foot Luxury Sports Yacht (Jeanneau)",
        "name_ru": "Роскошная спортивная яхта PRESTIGE 50 футов от Jeanneau, Франция",
        "desc_zh": "法国顶级游艇品牌，运动流线型设计，精致法式内饰，强劲运动性能，兼顾商务接待与休闲运动巡航",
        "desc_en": "France's top yacht brand, sporty streamlined design, exquisite French interior, powerful sport performance, balancing business hosting and leisure sport cruising",
        "desc_ru": "Лучший французский бренд яхт, спортивный обтекаемый дизайн, изысканный французский интерьер, мощные спортивные характеристики, сбалансированное решение для деловых приёмов и спортивных прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607202.html",
        "price": 300
    },
    {
        "size": 42,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "英国公主PRINCESS 42英尺飞桥游艇",
        "name_en": "UK PRINCESS 42-foot flybridge yacht",
        "name_ru": "Яхта с флайбриджем PRINCESS 42 фута, Великобритания",
        "desc_zh": "公主游艇经典入门款，英伦精致奢华工艺，紧凑实用空间布局，灵活操控性能，小型商务接待与近海休闲巡航的优选",
        "desc_en": "Princess Yachts classic entry-level model, British exquisite luxury craftsmanship, compact and practical space layout, flexible handling performance, ideal choice for small business hosting and offshore leisure cruising",
        "desc_ru": "Классическая начальная модель Princess Yachts, британская изысканная роскошная мастерская работа, компактная и практичная планировка пространства, гибкое управление, идеальный выбор для небольших деловых приёмов и прибрежных прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607189.html",
        "price": 195
    },
    {
        "size": 68,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利SESSA 68英尺豪华飞桥游艇",
        "name_en": "Italy SESSE 68-foot luxury flybridge yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем SESSA 68 футов",
        "desc_zh": "意大利新锐豪华游艇品牌，意式运动奢华设计，超大飞桥空间，强劲动力性能，商务接待与远海巡航的品质之选",
        "desc_en": "Italy's cutting-edge luxury yacht brand, Italian sport luxury design, super large flybridge space, powerful dynamic performance, high-quality choice for business hosting and offshore cruising",
        "desc_ru": "Передовой итальянский бренд роскошных яхт, итальянский дизайн спортивной роскоши, просторный флайбридж, мощные динамические характеристики, высококачественный выбор для деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3607183.html",
        "price": 980
    },
    {
        "size": 45,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利CNC AZ45英尺豪华飞桥游艇",
        "name_en": "Italian CNC AZ45-foot flybridge luxury yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем CNC AZ45 футов",
        "desc_zh": "意大利专业游艇品牌，紧凑实用飞桥设计，意式精致内饰，灵活操控性能，小型商务接待与近海休闲巡航的优选",
        "desc_en": "Italian professional yacht brand, compact and practical flybridge design, Italian exquisite interior, flexible handling performance, ideal choice for small business hosting and offshore leisure cruising",
        "desc_ru": "Итальянский профессиональный бренд яхт, компактная и практичная конструкция флайбриджа, изысканный итальянский интерьер, гибкое управление, идеальный выбор для небольших деловых приёмов и прибрежных прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607161.html",
        "price": 220
    },
    {
        "size": 60,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 60英尺豪华飞桥游艇",
        "name_en": "Italy Azimut 60-foot luxury flybridge yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Azimut 60 футов",
        "desc_zh": "阿兹慕经典畅销款，意式轻奢设计，飞桥全景视野，宽敞商务空间，稳定巡航性能，商务接待与近海休闲的标杆之选",
        "desc_en": "Azimut classic best-selling model, Italian light luxury design, panoramic view of flybridge, spacious business space, stable cruising performance, benchmark choice for business hosting and offshore leisure",
        "desc_ru": "Классическая бестселлерная модель Azimut, итальянский дизайн в стиле легкой роскоши, панорамный обзор с флайбриджа, просторное деловое пространство, стабильные ходовые характеристики, эталонный выбор для деловых приёмов и прибрежного отдыха",
        "url": "https://www.azurmore.com/productinfo/3607154.html",
        "price": 485
    },
    {
        "size": 43,
        "types": ["巡航", "豪华", "商务", "单体", "探险"],
        "name_zh": "意大利阿兹慕Azimut 43英尺麦哲伦系列豪华游艇",
        "name_en": "Italy Azimut 43-foot Magellan luxury yacht",
        "name_ru": "Итальянская роскошная яхта серии Magellan Azimut 43 фута",
        "desc_zh": "阿兹慕探险巡航系列，长续航设计，坚固船体结构，舒适居家内饰，兼顾近海休闲与远海探险巡航",
        "desc_en": "Azimut expedition cruising series, long endurance design, solid hull structure, comfortable home-style interior, balancing offshore leisure and offshore expedition cruising",
        "desc_ru": "Серия экспедиционных круизных яхт Azimut, конструкция с большим запасом хода, прочная структура корпуса, комфортный домашний интерьер, сбалансированное решение для прибрежного отдыха и дальних экспедиционных круизов",
        "url": "https://www.azurmore.com/productinfo/3607152.html",
        "price": 398
    },
    {
        "size": 45,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "法国ANTHONY PRESTIGE 45英尺豪华飞桥游艇",
        "name_en": "France Yacht ANTHONY PRESTIGE 45-foot luxury flybridge yacht",
        "name_ru": "Французская роскошная яхта с флайбриджем ANTHONY PRESTIGE 45 футов",
        "desc_zh": "法国豪华游艇品牌，法式优雅设计，飞桥全景视野，精致内饰布局，稳定动力性能，商务接待与休闲巡航的优选",
        "desc_en": "French luxury yacht brand, French elegant design, panoramic view of flybridge, exquisite interior layout, stable power performance, ideal choice for business hosting and leisure cruising",
        "desc_ru": "Французский бренд роскошных яхт, французский элегантный дизайн, панорамный обзор с флайбриджа, изысканная планировка интерьера, стабильные характеристики силовой установки, идеальный выбор для деловых приёмов и прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3607150.html",
        "price": 218
    },
    {
        "size": 68,
        "types": ["飞桥", "豪华", "商务", "巡航", "运动", "单体"],
        "name_zh": "意大利SESSA 68英尺飞桥游艇",
        "name_en": "Italian Sessa 68ft Flybridge Yacht",
        "name_ru": "Итальянская яхта с флайбриджем Sessa 68 футов",
        "desc_zh": "意大利运动豪华游艇标杆，意式动感设计，超大飞桥休闲空间，强劲动力性能，商务接待与运动巡航的品质之选",
        "desc_en": "Italian benchmark of sport luxury yachts, Italian dynamic design, super large flybridge leisure space, powerful dynamic performance, high-quality choice for business hosting and sport cruising",
        "desc_ru": "Итальянский эталон спортивных роскошных яхт, итальянский динамичный дизайн, просторное прогулочное пространство на флайбридже, мощные динамические характеристики, высококачественный выбор для деловых приёмов и спортивных круизов",
        "url": "https://www.azurmore.com/productinfo/3630009.html",
        "price": 478
    },
    {
        "size": 46,
        "types": ["双体", "豪华", "巡航", "休闲", "帆船"],
        "name_zh": "法国蓝高Lagoon 46英尺豪华双体帆船",
        "name_en": "French Lagoon 46ft Luxury Catamaran",
        "name_ru": "Роскошный парусный катамаран Lagoon 46 футов, Франция",
        "desc_zh": "蓝高经典双体帆船，宽体稳定设计，超大舒适起居空间，专业航海性能，家庭休闲航海与近海巡航的经典之选",
        "desc_en": "Lagoon classic catamaran sailboat, wide-body stable design, super large comfortable living space, professional sailing performance, classic choice for family leisure sailing and offshore cruising",
        "desc_ru": "Классический парусный катамаран Lagoon, устойчивая ширококорпусная конструкция, просторное комфортное жилое пространство, профессиональные ходовые характеристики под парусом, классический выбор для семейного отдыха под парусом и прибрежных круизов",
        "url": "https://www.azurmore.com/productinfo/3628992.html",
        "price": 498
    },
    {
        "size": 70,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 70英尺豪华飞桥游艇",
        "name_en": "Italian Azimut 70ft Luxury Flybridge Yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Azimut 70 футов",
        "desc_zh": "阿兹慕旗舰级飞桥游艇，意式奢华设计，超大飞桥全景空间，顶级内饰配置，强劲动力性能，高端商务接待与远海巡航的臻选",
        "desc_en": "Azimut flagship flybridge yacht, Italian luxury design, super large flybridge panoramic space, top-level interior configuration, powerful dynamic performance, perfect choice for high-end business hosting and offshore cruising",
        "desc_ru": "Флагманская яхта с флайбриджем Azimut, итальянский роскошный дизайн, просторное панорамное пространство на флайбридже, топовая комплектация интерьера, мощные динамические характеристики, идеальный выбор для высококлассных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3628984.html",
        "price": 1300
    },
    {
        "size": 65,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利蒙特卡洛Monte Carlo 65英尺二类豪华飞桥游艇",
        "name_en": "Italian Monte Carlo 65ft Luxury Flybridge Yacht Class II",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Monte Carlo 65 футов, класс II",
        "desc_zh": "蒙特卡洛经典豪华游艇，二类游艇资质，法式优雅设计，超大飞桥空间，稳定远航性能，商务接待与远海巡航的品质之选",
        "desc_en": "Monte Carlo classic luxury yacht, Class II yacht qualification, French elegant design, super large flybridge space, stable long-distance sailing performance, high-quality choice for business hosting and offshore cruising",
        "desc_ru": "Классическая роскошная яхта Monte Carlo, квалификация яхты класса II, французский элегантный дизайн, просторный флайбридж, стабильные характеристики для дальних плаваний, высококачественный выбор для деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3628967.html",
        "price": 1000
    },
    {
        "size": 59,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "英法合资亚诺Jeanneau Prestige 590豪华飞桥游艇",
        "name_en": "British-French Jeanneau Prestige 590 Luxury Flybridge Yacht",
        "name_ru": "Роскошная яхта с флайбриджем Jeanneau Prestige 590, британско-французское производство",
        "desc_zh": "全球知名游艇品牌，英法联合设计，经典飞桥布局，奢华居家内饰，优秀续航能力，商务接待与家庭休闲远航的优选",
        "desc_en": "World-renowned yacht brand, British-French joint design, classic flybridge layout, luxury home-style interior, excellent endurance, ideal choice for business hosting and family leisure long-distance sailing",
        "desc_ru": "Всемирно известный бренд яхт, совместный британско-французский дизайн, классическая планировка с флайбриджем, роскошный домашний интерьер, отличный запас хода, идеальный выбор для деловых приёмов и семейного отдыха в дальних плаваниях",
        "url": "https://www.azurmore.com/productinfo/3628962.html",
        "price": 700
    },
    {
        "size": 88,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "英国圣汐克Sunseeker 88英尺豪华飞桥游艇",
        "name_en": "UK Sunseeker 88-foot luxury flybridge yacht",
        "name_ru": "Роскошная яхта с флайбриджем Sunseeker 88 футов, Великобритания",
        "desc_zh": "英伦顶级豪华游艇品牌，皇室御用工艺，流线型动感设计，超大奢华空间，澎湃动力性能，高端商务接待与跨洋巡航的臻选",
        "desc_en": "UK's top luxury yacht brand, royal craftsmanship, streamlined dynamic design, super large luxury space, surging power performance, perfect choice for high-end business hosting and transoceanic cruising",
        "desc_ru": "Лучший британский бренд роскошных яхт, мастерская работа для королевского двора, обтекаемый динамичный дизайн, просторное роскошное пространство, мощные динамические характеристики, идеальный выбор для высококлассных деловых приёмов и трансокеанских круизов",
        "url": "https://www.azurmore.com/productinfo/3628942.html",
        "price": 1888
    },
    {
        "size": 45.5,
        "types": ["帆船", "单体", "豪华", "巡航", "休闲"],
        "name_zh": "德国汉斯Hansa 455豪华巡航帆船",
        "name_en": "Germany Hansa 455 Luxury Sailing Yacht",
        "name_ru": "Роскошная круизная парусная яхта Hansa 455, Германия",
        "desc_zh": "德国经典帆船品牌，德式精密工艺，专业航海性能，易操控设计，休闲航海旅行与近海巡航的经典之选",
        "desc_en": "German classic sailboat brand, German precision craftsmanship, professional sailing performance, easy-to-handle design, classic choice for leisure sailing trips and offshore cruising",
        "desc_ru": "Классический немецкий бренд парусных лодок, немецкая прецизионная мастерская работа, профессиональные ходовые характеристики под парусом, простая в управлении конструкция, классический выбор для отдыха под парусом и прибрежных круизов",
        "url": "https://www.azurmore.com/productinfo/3607252.html",
        "price": 168
    },
    {
        "size": 57,
        "types": ["帆船", "单体", "豪华", "巡航", "休闲"],
        "name_zh": "法国亚诺Jeanneau 57英尺二类豪华帆船",
        "name_en": "France Jeanneau 57-foot Class II luxury sailboat",
        "name_ru": "Роскошная парусная лодка Jeanneau 57 футов, класс II, Франция",
        "desc_zh": "全球帆船标杆品牌，二类游艇资质，专业远洋航海性能，舒适奢华内饰，灵活易操控，环球航海与高端休闲航海的品质之选",
        "desc_en": "Global sailboat benchmark brand, Class II yacht qualification, professional ocean sailing performance, comfortable and luxurious interior, flexible and easy to handle, high-quality choice for world sailing and high-end leisure sailing",
        "desc_ru": "Эталонный мировой бренд парусных лодок, квалификация яхты класса II, профессиональные характеристики для океанских плаваний под парусом, комфортный роскошный интерьер, гибкая и простая в управлении, высококачественный выбор для кругосветных плаваний и высококлассного отдыха под парусом",
        "url": "https://www.azurmore.com/productinfo/3607242.html",
        "price": 220
    },
    {
        "size": 70,
        "types": ["全新游艇", "豪华", "商务", "巡航", "飞桥", "单体"],
        "name_zh": "珠海定制70英尺全新豪华游艇",
        "name_en": "Brand New Custom Zhuhai 70ft Luxury Yacht",
        "name_ru": "Абсолютно новая заказная роскошная яхта 70 футов, Чжухай",
        "desc_zh": "国产全新定制豪华游艇，国际化设计标准，全场景个性化定制，超大奢华空间，高端商务接待与远海巡航的高性价比之选",
        "desc_en": "Domestic brand new custom luxury yacht, international design standard, full-scene personalized customization, super large luxury space, cost-effective choice for high-end business hosting and offshore cruising",
        "desc_ru": "Отечественная абсолютно новая заказная роскошная яхта, международные стандарты дизайна, полная персонализация для любых сценариев, просторное роскошное пространство, выгодное решение по соотношению цена-качество для высококлассных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3679732.html",
        "price": 0
    },
    {
        "size": 68,
        "types": ["全新游艇", "豪华", "双体", "巡航", "商务", "动力艇"],
        "name_zh": "全新定制格丽特Glitter 68（海珠68英尺）豪华动力双体游艇",
        "name_en": "Brand New Custom Glitter 68 (Haizhu 68ft) Luxury Power Catamaran",
        "name_ru": "Абсолютно новый заказной роскошный силовой катамаран Glitter 68 (Haizhu 68 футов)",
        "desc_zh": "国产全新定制豪华动力双体艇，宽体稳定设计，超大空间布局，定制化奢华配置，商务接待与休闲远航的理想之选",
        "desc_en": "Domestic brand new custom luxury power catamaran, wide-body stable design, super large space layout, customized luxury configuration, ideal choice for business hosting and leisure long-distance sailing",
        "desc_ru": "Отечественный абсолютно новый заказной роскошный силовой катамаран, устойчивая ширококорпусная конструкция, просторная планировка пространства, настраиваемая роскошная комплектация, идеальный выбор для деловых приёмов и дальних прогулочных плаваний",
        "url": "https://www.azurmore.com/productinfo/3679703.html",
        "price": 0
    },
    {
        "size": 46,
        "types": ["全新游艇", "豪华", "双体", "巡航", "休闲", "动力艇"],
        "name_zh": "全新定制格丽特Glitter 46英尺豪华动力双体游艇",
        "name_en": "Brand New Custom Glitter 46ft Luxury Power Catamaran",
        "name_ru": "Абсолютно новый заказной роскошный силовой катамаран Glitter 46 футов",
        "desc_zh": "国产全新定制豪华动力双体艇，紧凑实用宽体设计，稳定航行性能，舒适休闲空间，家庭休闲出海与小型商务接待的优选",
        "desc_en": "Domestic brand new custom luxury power catamaran, compact and practical wide-body design, stable sailing performance, comfortable leisure space, ideal choice for family leisure sailing and small business hosting",
        "desc_ru": "Отечественный абсолютно новый заказной роскошный силовой катамаран, компактная и практичная ширококорпусная конструкция, стабильные ходовые характеристики, комфортное прогулочное пространство, идеальный выбор для семейного отдыха в море и небольших деловых приёмов",
        "url": "https://www.azurmore.com/productinfo/3679682.html",
        "price": 0
    },
    {
        "size": 28,
        "types": ["全新游艇", "观光艇", "敞篷", "接待", "巡航", "单体"],
        "name_zh": "全新定制海珠Haizhu 8.6米观光艇",
        "name_en": "Brand New Custom Haizhu 8.6m Sightseeing Boat",
        "name_ru": "Абсолютно новая заказная экскурсионная лодка Haizhu 8,6 метра",
        "desc_zh": "国产全新定制观光艇，轻量化灵活设计，宽敞载客空间，360°全景视野，滨海景区观光与小型团队接待的实用之选",
        "desc_en": "Domestic brand new custom sightseeing boat, lightweight and flexible design, spacious passenger space, 360° panoramic view, practical choice for coastal scenic sightseeing and small group reception",
        "desc_ru": "Отечественная абсолютно новая заказная экскурсионная лодка, легкая гибкая конструкция, просторное пространство для пассажиров, панорамный обзор 360°, практичный выбор для экскурсий в прибрежных зонах и приёма небольших групп",
        "url": "https://www.azurmore.com/productinfo/3679670.html",
        "price": 0
    },
    {
        "size": 50,
        "types": ["全新游艇", "钓鱼", "专业", "运动", "单体", "巡航"],
        "name_zh": "全新定制海珠Haizhu 50英尺畅销专业钓鱼艇",
        "name_en": "Brand New Custom Haizhu 50ft Bestselling Professional Fishing Boat",
        "name_ru": "Абсолютно новая заказная профессиональная рыбацкая лодка Haizhu 50 футов, бестселлер",
        "desc_zh": "国产全新专业钓鱼艇，畅销经典款，专业海钓配置，强劲动力性能，宽敞作业空间，专业海钓与远海作业的高性价比之选",
        "desc_en": "Domestic brand new professional fishing boat, bestselling classic model, professional sea fishing configuration, powerful dynamic performance, spacious working space, cost-effective choice for professional sea fishing and offshore operations",
        "desc_ru": "Отечественная абсолютно новая профессиональная рыбацкая лодка, бестселлерная классическая модель, профессиональная комплектация для морской рыбалки, мощные динамические характеристики, просторное рабочее пространство, выгодное решение по соотношению цена-качество для профессиональной морской рыбалки и морских операций",
        "url": "https://www.azurmore.com/productinfo/3679659.html",
        "price": 0
    },
    {
        "size": 38,
        "types": ["全新游艇", "钓鱼", "专业", "运动", "单体", "巡航"],
        "name_zh": "全新定制海珠Haizhu 38英尺专业钓鱼艇",
        "name_en": "Brand New Custom Haizhu 36ft Professional Fishing Boat",
        "name_ru": "Абсолютно новая заказная профессиональная рыбацкая лодка Haizhu 36 футов",
        "desc_zh": "国产全新专业钓鱼艇，紧凑实用设计，专业海钓配置，灵活操控性能，近海海钓与休闲出海的入门优选",
        "desc_en": "Domestic brand new professional fishing boat, compact and practical design, professional sea fishing configuration, flexible handling performance, ideal entry-level choice for offshore sea fishing and leisure sailing",
        "desc_ru": "Отечественная абсолютно новая профессиональная рыбацкая лодка, компактная и практичная конструкция, профессиональная комплектация для морской рыбалки, гибкое управление, идеальный выбор для начинающих любителей прибрежной морской рыбалки и отдыха в море",
        "url": "https://www.azurmore.com/productinfo/3679648.html",
        "price": 0
    },
    {
        "size": 64,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 64英尺豪华飞桥游艇",
        "name_en": "Italian Azimut 64ft Luxury Flybridge Yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Azimut 64 фута",
        "desc_zh": "阿兹慕经典豪华飞桥游艇，意式轻奢设计，全景飞桥视野，宽敞商务空间，强劲稳定动力，高端商务接待与远海巡航的优选",
        "desc_en": "Azimut classic luxury flybridge yacht, Italian light luxury design, panoramic flybridge view, spacious business space, powerful and stable power, ideal choice for high-end business hosting and offshore cruising",
        "desc_ru": "Классическая роскошная яхта с флайбриджем Azimut, итальянский дизайн в стиле легкой роскоши, панорамный обзор с флайбриджа, просторное деловое пространство, мощная и стабильная силовая установка, идеальный выбор для высококлассных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3679631.html",
        "price": 498
    },
    {
        "size": 112,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "意大利法拉帝Ferretti 112英尺超级游艇",
        "name_en": "Italian Ferretti 112ft Superyacht",
        "name_ru": "Итальянская суперяхта Ferretti 112 футов",
        "desc_zh": "法拉帝顶级超级游艇，全手工奢华工艺，全场景定制化配置，超大私密起居空间，环球航行与顶级商务社交的旗舰之选",
        "desc_en": "Ferretti top-level superyacht, fully handcrafted luxury craftsmanship, full-scene customized configuration, super large private living space, flagship choice for world sailing and top business socializing",
        "desc_ru": "Топовая суперяхта Ferretti, полностью ручная роскошная мастерская работа, полная персонализированная комплектация для любых сценариев, просторное приватное жилое пространство, флагманский выбор для кругосветных плаваний и делового общения высочайшего уровня",
        "url": "https://www.azurmore.com/productinfo/3679624.html",
        "price": 4200
    },
    {
        "size": 46,
        "types": ["全新游艇", "豪华", "动力艇", "巡航", "商务", "单体"],
        "name_zh": "全新定制格丽特Glitter 46英尺豪华动力单体游艇",
        "name_en": "Brand new custom Glitter 46-foot luxury power monohull yacht",
        "name_ru": "Абсолютно новая заказная роскошная силовая однокорпусная яхта Glitter 46 футов",
        "desc_zh": "国产全新定制豪华动力单体艇，紧凑精致设计，稳定航行性能，舒适休闲空间，家庭休闲出海与小型商务接待的优选",
        "desc_en": "Domestic brand new custom luxury power monohull yacht, compact and exquisite design, stable sailing performance, comfortable leisure space, ideal choice for family leisure sailing and small business hosting",
        "desc_ru": "Отечественная абсолютно новая заказная роскошная силовая однокорпусная яхта, компактная и изысканная конструкция, стабильные ходовые характеристики, комфортное прогулочное пространство, идеальный выбор для семейного отдыха в море и небольших деловых приёмов",
        "url": "https://www.azurmore.com/productinfo/3679550.html",
        "price": 0
    },
    {
        "size": 31,
        "types": ["全新游艇", "帆船", "单体", "巡航", "休闲"],
        "name_zh": "法国丹枫Dufour 310帆船-全新展船从未下水",
        "name_en": "French Dufour 310 Sailing Boat – Brand New Display Boat Never Launched",
        "name_ru": "Парусная лодка Dufour 310, Франция – абсолютно новая выставочная лодка, никогда не спущенная на воду",
        "desc_zh": "法国经典入门帆船品牌，全新未下水展船，专业航海性能，易操控设计，休闲航海旅行与帆船入门的经典之选",
        "desc_en": "French classic entry-level sailboat brand, brand new never-launched display boat, professional sailing performance, easy-to-handle design, classic choice for leisure sailing trips and entry-level sailing",
        "desc_ru": "Классический французский бренд парусных лодок начального уровня, абсолютно новая выставочная лодка, никогда не спущенная на воду, профессиональные ходовые характеристики под парусом, простая в управлении конструкция, классический выбор для отдыха под парусом и начинающих яхтсменов",
        "url": "https://www.azurmore.com/productinfo/3679274.html",
        "price": 38
    },
    {
        "size": 18,
        "types": ["全新游艇", "运动", "休闲", "敞篷", "单体"],
        "name_zh": "全新美国蒙特利MONTEREY 184运动艇",
        "name_en": "Brand New American MONTEREY 184 Sport Boat",
        "name_ru": "Абсолютно новая американская спортивная лодка MONTEREY 184",
        "desc_zh": "美国经典运动艇品牌，全新进口，轻量化灵活设计，强劲运动性能，近海休闲娱乐与水上运动的入门优选",
        "desc_en": "American classic sport boat brand, brand new imported, lightweight and flexible design, powerful sport performance, ideal entry-level choice for offshore leisure entertainment and water sports",
        "desc_ru": "Классический американский бренд спортивных лодок, абсолютно новая импортная модель, легкая гибкая конструкция, мощные спортивные характеристики, идеальный выбор для начинающих любителей прибрежного отдыха и водных видов спорта",
        "url": "https://www.azurmore.com/productinfo/3679262.html",
        "price": 0
    },
    {
        "size": 20,
        "types": ["全新游艇", "运动", "休闲", "敞篷", "单体"],
        "name_zh": "全新美国蒙特利MONTEREY 197运动艇",
        "name_en": "Brand New American MONTEREY 197 Sport Boat",
        "name_ru": "Абсолютно новая американская спортивная лодка MONTEREY 197",
        "desc_zh": "美国经典运动艇品牌，全新进口，大尺寸运动空间，强劲动力性能，近海休闲娱乐与水上运动的品质之选",
        "desc_en": "American classic sport boat brand, brand new imported, large-size sport space, powerful dynamic performance, high-quality choice for offshore leisure entertainment and water sports",
        "desc_ru": "Классический американский бренд спортивных лодок, абсолютно новая импортная модель, просторное спортивное пространство, мощные динамические характеристики, высококачественный выбор для прибрежного отдыха и водных видов спорта",
        "url": "https://www.azurmore.com/productinfo/3679241.html",
        "price": 0
    },
    {
        "size": 66,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利蒙地卡洛Monte Carlo MC6豪华飞桥游艇",
        "name_en": "Italian Monte Carlo MC6 Luxury Flybridge Yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Monte Carlo MC6",
        "desc_zh": "蒙地卡洛旗舰级飞桥游艇，法式意式融合设计，超大奢华空间，顶级内饰配置，强劲动力性能，高端商务接待与远海巡航的臻选",
        "desc_en": "Monte Carlo flagship flybridge yacht, French-Italian fusion design, super large luxury space, top-level interior configuration, powerful dynamic performance, perfect choice for high-end business hosting and offshore cruising",
        "desc_ru": "Флагманская яхта с флайбриджем Monte Carlo, дизайн в стиле слияния французских и итальянских традиций, просторное роскошное пространство, топовая комплектация интерьера, мощные динамические характеристики, идеальный выбор для высококлассных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3678040.html",
        "price": 700
    },
    {
        "size": 72,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 72英尺豪华飞桥游艇",
        "name_en": "Italian Azimut 72ft Luxury Flybridge Yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Azimut 72 фута",
        "desc_zh": "阿兹慕旗舰级飞桥游艇，意式奢华设计，超大飞桥全景空间，顶级内饰配置，强劲动力性能，高端商务接待与远海巡航的臻选",
        "desc_en": "Azimut flagship flybridge yacht, Italian luxury design, super large flybridge panoramic space, top-level interior configuration, powerful dynamic performance, perfect choice for high-end business hosting and offshore cruising",
        "desc_ru": "Флагманская яхта с флайбриджем Azimut, итальянский роскошный дизайн, просторное панорамное пространство на флайбридже, топовая комплектация интерьера, мощные динамические характеристики, идеальный выбор для высококлассных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3678027.html",
        "price": 3000
    },
    {
        "size": 76,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "意大利圣劳伦佐Sanlorenzo SX76飞桥豪华游艇",
        "name_en": "Italian Sanlorenzo SX76 Flybridge Luxury Yacht",
        "name_ru": "Итальянская роскошная яхта с флайбриджем Sanlorenzo SX76",
        "desc_zh": "意大利顶级定制游艇品牌，全手工奢华工艺，创新跨界设计，超大私密起居空间，高端商务社交与远海巡航的旗舰之选",
        "desc_en": "Italy's top custom yacht brand, fully handcrafted luxury craftsmanship, innovative crossover design, super large private living space, flagship choice for high-end business socializing and offshore cruising",
        "desc_ru": "Лучший итальянский бренд яхт на заказ, полностью ручная роскошная мастерская работа, инновационный кроссоверный дизайн, просторное приватное жилое пространство, флагманский выбор для делового общения высочайшего уровня и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3678014.html",
        "price": 3500
    },
    {
        "size": 77,
        "types": ["飞桥", "豪华", "商务", "巡航", "出口版", "单体"],
        "name_zh": "兰萨罗特LANZAROTE 77英尺豪华飞桥游艇（出口版）",
        "name_en": "LANZAROTE 77ft Luxury Flybridge Yacht (Export Version)",
        "name_ru": "Роскошная яхта с флайбриджем LANZAROTE 77 футов (экспортная версия)",
        "desc_zh": "西班牙经典游艇品牌，出口专属配置，宽体稳定设计，超大飞桥空间，国际化豪华配置，跨境商务接待与远海巡航的品质之选",
        "desc_en": "Spanish classic yacht brand, export exclusive configuration, wide-body stable design, super large flybridge space, international luxury configuration, high-quality choice for cross-border business hosting and offshore cruising",
        "desc_ru": "Классический испанский бренд яхт, эксклюзивная экспортная комплектация, устойчивая ширококорпусная конструкция, просторный флайбридж, международная роскошная комплектация, высококачественный выбор для трансграничных деловых приёмов и дальних морских круизов",
        "url": "https://www.azurmore.com/productinfo/3677992.html",
        "price": 238
    },
    {
        "size": 46,
        "types": ["飞桥", "豪华", "商务", "巡航", "动力艇", "单体"],
        "name_zh": "英国西莱Sealine F46飞桥动力游艇",
        "name_en": "British Sealine F46 Flybridge Motor Yacht",
        "name_ru": "Британская силовая яхта с флайбриджем Sealine F46",
        "desc_zh": "英国经典动力游艇品牌，英伦精致工艺，飞桥全景视野，舒适居家内饰，稳定动力性能，家庭休闲远航与小型商务接待的优选",
        "desc_en": "British classic motor yacht brand, British exquisite craftsmanship, panoramic flybridge view, comfortable home-style interior, stable power performance, ideal choice for family leisure long-distance sailing and small business hosting",
        "desc_ru": "Классический британский бренд силовых яхт, британская изысканная мастерская работа, панорамный обзор с флайбриджа, комфортный домашний интерьер, стабильные характеристики силовой установки, идеальный выбор для семейного отдыха в дальних плаваниях и небольших деловых приёмов",
        "url": "https://www.azurmore.com/productinfo/3672194.html",
        "price": 98
    },
    {
        "size": 42,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "法国博纳多BENETEAU Antares系列42英尺豪华飞桥游艇",
        "name_en": "BENETEAU Antares Series 42ft Luxury Flybridge Yacht",
        "name_ru": "Роскошная яхта с флайбриджем серии Antares BENETEAU 42 фута, Франция",
        "desc_zh": "全球游艇标杆品牌，博纳多经典巡航系列，法式实用设计，宽敞空间布局，稳定航行性能，家庭休闲巡航与小型商务接待的经典之选",
        "desc_en": "Global yacht benchmark brand, Beneteau classic cruising series, French practical design, spacious space layout, stable sailing performance, classic choice for family leisure cruising and small business hosting",
        "desc_ru": "Эталонный мировой бренд яхт, классическая круизная серия Beneteau, французский практичный дизайн, просторная планировка пространства, стабильные ходовые характеристики, классический выбор для семейных прогулочных круизов и небольших деловых приёмов",
        "url": "https://www.azurmore.com/productinfo/3635348.html",
        "price": 138
    },
    {
        "size": 53,
        "types": ["飞桥", "豪华", "商务", "巡航", "单体"],
        "name_zh": "意大利阿兹慕Azimut 50 Fly 52.9英尺飞桥游艇",
        "name_en": "Azimut 50 Fly 52.9ft Flybridge Yacht",
        "name_ru": "Яхта с флайбриджем Azimut 50 Fly 52,9 фута, Италия",
        "desc_zh": "阿兹慕经典飞桥游艇，意式轻奢设计，紧凑实用飞桥布局，精致内饰，灵活操控性能，小型商务接待与近海休闲巡航的优选",
        "desc_en": "Azimut classic flybridge yacht, Italian light luxury design, compact and practical flybridge layout, exquisite interior, flexible handling performance, ideal choice for small business hosting and offshore leisure cruising",
        "desc_ru": "Классическая яхта с флайбриджем Azimut, итальянский дизайн в стиле легкой роскоши, компактная и практичная планировка флайбриджа, изысканный интерьер, гибкое управление, идеальный выбор для небольших деловых приёмов и прибрежных прогулочных круизов",
        "url": "https://www.azurmore.com/productinfo/3630037.html",
        "price": 720
    },
    {
        "size": 85,
        "types": ["飞桥", "豪华", "商务", "巡航", "超级游艇", "单体"],
        "name_zh": "意大利法拉帝Ferretti Yachts 850飞桥游艇",
        "name_en": "Ferretti Yachts 850 Flybridge Yacht",
        "name_ru": "Яхта с флайбриджем Ferretti Yachts 850, Италия",
        "desc_zh": "法拉帝旗舰级飞桥游艇，全手工意式奢华工艺，超大奢华空间，顶级定制配置，澎湃动力性能，高端商务接待与跨洋巡航的臻选",
        "desc_en": "Ferretti flagship flybridge yacht, fully handcrafted Italian luxury craftsmanship, super large luxury space, top-level custom configuration, surging power performance, perfect choice for high-end business hosting and transoceanic cruising",
        "desc_ru": "Флагманская яхта с флайбриджем Ferretti, полностью ручная итальянская роскошная мастерская работа, просторное роскошное пространство, топовая комплектация на заказ, мощные динамические характеристики, идеальный выбор для высококлассных деловых приёмов и трансокеанских круизов",
        "url": "https://www.azurmore.com/productinfo/3630015.html",
        "price": 0
    }
]

# 代理配置：本地用就开，云服务器就关（把PROXY_HOST改成空字符串即可）
PROXY_HOST = ""
PROXY_PORT = 7897  # 这里是整数也完全没问题，已经做了兼容
PRICE_UNIT = {
    "zh": "万元",
    "en": "Million CNY",
    "ru": "млн КНР"
}
# ======================== 【2. 核心代码（已修复所有问题）】========================
import re
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton, ChatMemberUpdated,
    ReplyKeyboardRemove
)
from aiogram.filters import Command, ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.exceptions import TelegramForbiddenError, TelegramNetworkError
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# 🔧 修复核心：统一类型判断，彻底解决int.strip()报错
# 先把端口转成字符串再判断，兼容整数/字符串两种写法
proxy_host_str = str(PROXY_HOST).strip() if PROXY_HOST else ""
proxy_port_str = str(PROXY_PORT).strip() if PROXY_PORT else ""

# 自动兼容有无代理（修复后的判断逻辑，100%不报错）
if proxy_host_str and proxy_port_str:
    os.environ["HTTP_PROXY"] = f"http://{PROXY_HOST}:{PROXY_PORT}"
    os.environ["HTTPS_PROXY"] = f"http://{PROXY_HOST}:{PROXY_PORT}"
    session = AiohttpSession(proxy=f"http://{PROXY_HOST}:{PROXY_PORT}")
else:
    session = AiohttpSession()

# 初始化Bot（明确指定ParseMode，提升兼容性）
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    session=session
)
dp = Dispatcher()
user_language = {}

LANG = {
    "zh": {
        "welcome": "🎉 欢迎使用游艇查询机器人！\n请选择语言：\n【中文 / English / Русский】",
        "sent": "✅ 资料已私聊发送",
        "need_private": "⚠️ 请先私聊我才能接收资料",
        "result": "🔹 为您找到以下游艇：",
        "recommend": "🔍 未找到完全匹配，为您推荐：",
        "lang_saved": "✅ 语言已保存！\n\n📌 搜索格式指南：\n▪️ 500万以上 / 500W以上\n▪️ 全新游艇 / 超级游艇\n▪️ 游艇品牌：Azimut / Ferretti\n▪️ 50尺商务游艇推荐",
        "no_result": "😥 未找到匹配游艇\n\n✅ 正确格式示例：\n▪️ 500万以上\n▪️ 全新游艇\n▪️ 游艇品牌：Azimut / Ferretti\n▪️ 50尺商务游艇推荐",
        "new_user_welcome": """
👋 欢迎加入游艇群！
📌 使用指南：
直接发送你想要的【尺寸 + 类型】或【价格筛选】，我会私聊发资料给你！
例如：
• 40尺飞桥 | 50尺双体 | 钓鱼艇
• 豪华商务 | 家庭度假 | 派对娱乐
• 500万以下 | 40尺 300万以下 | 500-600万
所有资料均私密发送，群内不可见 😊
"""
    },
    "en": {
        "welcome": "🎉 Welcome to Yacht Bot!\nChoose Language: 【中文 / English / Русский】",
        "sent": "✅ Info sent privately",
        "need_private": "⚠️ Message me privately first",
        "result": "🔹 Found Yachts:",
        "recommend": "🔍 No exact match, recommendations:",
        "lang_saved": "✅ Language saved!\n\n📌 Search Guide:\n▪️ above 5m CNY / 5m\n▪️ Brand New Yachts / Superyachts\n▪️ Yacht brand：Azimut / Ferretti\n▪️ Recommended 50-foot catamaran business yachts",
        "no_result": "😥 No matching yachts\n\n✅ Correct format:\n▪️ above 5m CNY / 5m\n▪️ Brand New Yachts / Superyachts\n▪️ 5-6m CNY\n▪️ Recommended 50-foot catamaran business yachts",
        "new_user_welcome": """
👋 Welcome to the Yacht Group!
📌 How to use:
Send your query directly, and I'll send you info privately!
Examples:
• 40ft flybridge | 50ft catamaran
• Above 5m CNY | Below 6m CNY
All info is sent privately, not visible in the group 😊
"""
    },
    "ru": {
        "welcome": "🎉 Добро пожаловать!\nВыберите язык: 【中文 / English / Русский】",
        "sent": "✅ Информация отправлена",
        "need_private": "⚠️ Напишите мне в личные сообщения",
        "result": "🔹 Найденные яхты:",
        "recommend": "🔍 Нет совпадений, рекомендации:",
        "lang_saved": "✅ Язык сохранен!\n\n📌 Формат поиска:\n▪️ выше 5млн КНР / 5млн\n▪️ Новые яхты / Суперяхты\n▪️ Яхтенный бренд：Azimut / Ferretti\n▪️ Рекомендуемые 50-футовые катамаранные бизнес-яхты",
        "no_result": "😥 Яхты не найдены\n\n✅ Правильный формат:\n▪️ выше 5млн\n▪️ Новые яхты\n▪️ Яхтенный бренд：Azimut / Ferretti\n▪️ Рекомендуемые 50-футовые катамаранные бизнес-яхты",
        "new_user_welcome": """
👋 Добро пожаловать в группу яхт!
📌 Как пользоваться:
Отправьте запрос, и я отправлю информацию лично!
Примеры:
• 40 футов флайбридж | 50 футов катамаран
• выше 5 млн КНР | ниже 6 млн КНР
Вся информация отправляется лично, не видна в группе 😊
"""
    }
}

TYPE_MAP = {
    # --- 船体结构 ---
    "单体": [
        "单体", "monohull", "monohull yacht", "motorboat", "single hull",
        "однокорпусный"
    ],
    "双体": [
        "双体", "catamaran", "power catamaran", "twin hull",
        "катамаран"
    ],

    # --- 甲板形式 ---
    "飞桥": [
        "飞桥", "flybridge", "fly bridge", "flying bridge", "flybridge yacht",
        "летный мост", "флайбридж"
    ],
    "硬顶": [
        "硬顶", "hardtop", "hard top", "hardtop yacht",
        "хардтоп"
    ],
    "敞篷": [
        "敞篷", "open", "open yacht", "convertible",
        "открытый"
    ],

    # --- 功能/类型 ---
    "钓鱼": [
        "钓鱼", "fishing", "fishing boat", "fishing yacht", "professional fishing", "海钓",
        "рыбацкая"
    ],
    "运动": [
        "运动", "sport", "sport boat", "sports yacht", "sport motorboat", "speed",
        "спортивная"
    ],
    "商务": [
        "商务", "business", "business yacht", "corporate", "executive",
        "бизнес", "деловая"
    ],
    "巡航": [
        "巡航", "cruise", "cruising", "cruiser", "motor cruiser",
        "круиз"
    ],
    "超级游艇": [
        "超级游艇", "superyacht", "super yacht", "flagship yacht", "大型游艇",
        "суперяхта"
    ],
    "全新游艇": [
        "全新", "brand new", "new", "new yacht", "custom built", "custom glitter",
        "новый"
    ],
    "帆船": [
        "帆船", "sailing boat", "sailboat", "sailing yacht",
        "парусная лодка"
    ],
    "观光艇": [
        "观光", "sightseeing", "sightseeing boat", "tour boat",
        "экскурсионная лодка"
    ],

    # --- 品牌（已清理：无任何尺寸、无任何型号）---
    "Ferretti": [
        "Ferretti", "法拉帝"
    ],
    "Azimut": [
        "Azimut", "阿兹慕"
    ],
    "Sunseeker": [
        "Sunseeker", "圣汐"
    ],
    "Sunreef": [
        "Sunreef", "波兰Sunreef"
    ],
    "Marquis": [
        "Marquis", "American Marquis"
    ],
    "Asteria": [
        "Asteria"
    ],
    "Horizon": [
        "Horizon"
    ],
    "Monterey": [
        "MONTEREY"
    ],
    "Monte Carlo": [
        "Monte Carlo"
    ],
    "Sanlorenzo": [
        "Sanlorenzo"
    ],
    "Lanzarote": [
        "LANZAROTE"
    ],
    "Sealine": [
        "Sealine", "British Sealine"
    ],
    "Beneteau": [
        "BENETEAU"
    ],
    "Dufour": [
        "Dufour", "French Dufour"
    ],
    "Haizhu": [
        "Haizhu", "海珠"
    ],
    "Glitter": [
        "Glitter"
    ],
    "Tuda": [
        "Tuda"
    ]
}


# -------------------------- 工具函数 --------------------------
def get_size(text):
    match = re.search(r'(\d+)\s*(尺|ft|футов)', text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def get_types(text):
    t = text.lower()
    matched = []
    for k, v in TYPE_MAP.items():
        for w in v:
            if w.lower() in t:
                matched.append(k)
                break
    return matched


def get_price_range(text, lang="zh"):
    txt = text.lower().replace(" ", "").replace("w", "m").replace("млн", "m")
    min_p = None
    max_p = None
    if lang == "en":
        sole = re.match(r'^(\d+)m$', txt)
        if sole:
            min_p = int(sole.group(1)) * 100
            return (min_p, max_p)
        above = re.search(r'above(\d+)m', txt)
        if above:
            min_p = int(above.group(1)) * 100
        below = re.search(r'below(\d+)m', txt)
        if below:
            max_p = int(below.group(1)) * 100
        between = re.search(r'(\d+)-(\d+)m', txt)
        if between:
            min_p = int(between.group(1)) * 100
            max_p = int(between.group(2)) * 100
        return (min_p, max_p)
    if lang == "zh":
        txt = txt.replace("m", "万")
        sole = re.match(r'^(\d+)万$', txt)
        if sole:
            min_p = int(sole.group(1))
            return (min_p, max_p)
        above = re.search(r'(\d+)万以上', txt)
        if above:
            min_p = int(above.group(1))
        below = re.search(r'(\d+)万以下', txt)
        if below:
            max_p = int(below.group(1))
        between = re.search(r'(\d+)-(\d+)万', txt)
        if between:
            min_p = int(between.group(1))
            max_p = int(between.group(2))
        return (min_p, max_p)
    if lang == "ru":
        sole = re.match(r'^(\d+)m$', txt)
        if sole:
            min_p = int(sole.group(1)) * 100
            return (min_p, max_p)
        above = re.search(r'выше(\d+)m', txt)
        if above:
            min_p = int(above.group(1)) * 100
        below = re.search(r'ниже(\d+)m', txt)
        if below:
            max_p = int(below.group(1)) * 100
        between = re.search(r'(\d+)-(\d +)m', txt)
        if between:
            min_p = int(between.group(1)) * 100
            max_p = int(between.group(2)) * 100
        return (min_p, max_p)
    return (None, None)


def get_size_range(text, lang="zh"):
    txt = text.lower().replace(" ", "")
    min_s = None
    max_s = None
    if lang == "zh":
        sole = re.match(r'^(\d+)尺$', txt)
        if sole:
            min_s = int(sole.group(1))
            return (min_s, max_s)
        above = re.search(r'(\d+)尺以上', txt)
        if above:
            min_s = int(above.group(1))
        below = re.search(r'(\d+)尺以下', txt)
        if below:
            max_s = int(below.group(1))
        between = re.search(r'(\d+)-(\d+)尺', txt)
        if between:
            min_s = int(between.group(1))
            max_s = int(between.group(2))
    elif lang == "en":
        txt = txt.replace("ft", "")
        sole = re.match(r'^(\d+)$', txt)
        if sole:
            min_s = int(sole.group(1))
            return (min_s, max_s)
        above = re.search(r'above(\d+)', txt)
        if above:
            min_s = int(above.group(1))
        below = re.search(r'below(\d+)', txt)
        if below:
            max_s = int(below.group(1))
        between = re.search(r'(\d+)-(\d+)', txt)
        if between:
            min_s = int(between.group(1))
            max_s = int(between.group(2))
    elif lang == "ru":
        txt = txt.replace("футов", "")
        sole = re.match(r'^(\d+)$', txt)
        if sole:
            min_s = int(sole.group(1))
            return (min_s, max_s)
        above = re.search(r'выше(\d+)', txt)
        if above:
            min_s = int(above.group(1))
        below = re.search(r'ниже(\d+)', txt)
        if below:
            max_s = int(below.group(1))
        between = re.search(r'(\d+)-(\d+)', txt)
        if between:
            min_s = int(between.group(1))
            max_s = int(between.group(2))
    return (min_s, max_s)


def filter_by_size(yachts, min_s, max_s):
    out = []
    for y in yachts:
        s = y["size"]
        if min_s is not None and s < min_s:
            continue
        if max_s is not None and s > max_s:
            continue
        out.append(y)
    return out


def filter_by_price(yachts, min_p, max_p):
    out = []
    for y in yachts:
        p = y["price"]
        if min_p is not None and p < min_p: continue
        if max_p is not None and p > max_p: continue
        out.append(y)
    return out


# -------------------------- 搜索 --------------------------
def search(size=None, types=None, min_p=None, max_p=None):
    res = []
    seen = set()
    for y in YACHTS:
        if size is not None and y["size"] != size: continue
        if types and not any(t in y["types"] for t in types): continue
        if y["name_zh"] in seen: continue
        seen.add(y["name_zh"])
        res.append(y)
    return filter_by_price(res, min_p, max_p)


# -------------------------- 新用户欢迎 --------------------------
@dp.chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def welcome_new_user(event: ChatMemberUpdated):
    user = event.new_chat_member.user
    if user.is_bot:
        return
    try:
        await event.answer(LANG["zh"]["new_user_welcome"].strip())
    except Exception as e:
        print(f"欢迎消息发送失败: {e}")
        try:
            await bot.send_message(user.id, LANG["zh"]["new_user_welcome"].strip())
        except Exception as e2:
            print(f"私聊发送欢迎消息失败: {e2}")


# -------------------------- 指令处理器 --------------------------
@dp.message(Command("start", ignore_case=True))  # 兼容大小写，确保/START也能触发
async def start(msg: Message):
    # 修复：完善键盘配置，添加占位符和持久化按钮（确保显示）
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="中文"),
                KeyboardButton(text="English"),
                KeyboardButton(text="Русский")
            ]
        ],
        resize_keyboard=True,  # 自适应键盘大小
        one_time_keyboard=False,  # 按钮不自动消失
        input_field_placeholder="请选择语言 / Please select language / Пожалуйста, выберите язык"  # 输入框提示
    )
    # 优先用用户已选语言发送欢迎语，无则用中文
    lang = user_language.get(msg.from_user.id, "zh")
    await msg.answer(LANG[lang]["welcome"], reply_markup=kb)


@dp.message(lambda m: m.text.strip() in ["中文", "English", "Русский"])
async def set_lang(msg: Message):
    uid = msg.from_user.id
    t = msg.text.strip()
    if t == "中文":
        user_language[uid] = "zh"
    elif t == "English":
        user_language[uid] = "en"
    elif t == "Русский":
        user_language[uid] = "ru"

    lang = user_language[uid]
    # 保存语言后移除键盘，避免干扰后续操作
    await msg.answer(LANG[lang]["lang_saved"], reply_markup=ReplyKeyboardRemove())


@dp.message()
async def handler(msg: Message):
    try:
        text = msg.text.strip()
        if len(text) < 1: return
        uid = msg.from_user.id
        lang = user_language.get(uid, "zh")

        # 提取搜索条件
        size = get_size(text)
        types = get_types(text)
        min_p, max_p = get_price_range(text, lang)
        min_s, max_s = get_size_range(text, lang)

        # 筛选游艇：尺寸 + 价格 + 类型 联合筛选
        yachts = search(size=size, types=types)
        yachts = filter_by_size(yachts, min_s, max_s)  # 新增：尺寸筛选
        yachts = filter_by_price(yachts, min_p, max_p)  # 价格筛选

        # 无匹配结果时推荐同类
        if not yachts:
            if size:
                yachts = [y for y in YACHTS if y["size"] == size]
            else:
                yachts = YACHTS[:2]

        # 仍无结果则提示
        if not yachts:
            await msg.answer(LANG[lang]["no_result"])
            return

        # 拼接结果文本
        res_text = LANG[lang]["result"] + "\n\n"
        for y in yachts:
            p = y["price"]
            if lang == "zh":
                price_str = f"{p}万元"
                res_text += f"📌 {y['size']}尺 | {y['name_zh']}\n💰 {price_str}\n💡 {y['desc_zh']}\n🔗 {y['url']}\n\n"
            elif lang == "en":
                price_str = f"{p / 100} Million CNY"
                res_text += f"📌 {y['size']}ft | {y['name_en']}\n💰 {price_str}\n💡 {y['desc_en']}\n🔗 {y['url']}\n\n"
            else:
                price_str = f"{p / 100} млн КНР"
                res_text += f"📌 {y['size']} футов | {y['name_ru']}\n💰 {price_str}\n💡 {y['desc_ru']}\n🔗 {y['url']}\n\n"

        # 发送结果（私聊/群聊区分）
        if msg.chat.type == "private":
            await msg.answer(res_text, disable_web_page_preview=True)
        else:
            try:
                await bot.send_message(uid, res_text, disable_web_page_preview=True)
                await msg.answer(LANG[lang]["sent"])
            except TelegramForbiddenError:
                bot_me = await bot.get_me()
                await msg.answer(f"{LANG[lang]['need_private']}\nhttps://t.me/{bot_me.username}")
    except Exception as e:
        print(f"处理消息时出错: {e}")
        import traceback
        traceback.print_exc()
        # 给用户友好提示
        await msg.answer("😵 处理请求时出错，请稍后重试！")


# -------------------------- 启动入口 --------------------------
async def main():
    try:
        me = await bot.get_me()
        print(f"✅ 机器人 @{me.username} 启动成功！")
        print(f"📊 游艇总数：{len(YACHTS)}")
        print(f"🌐 支持语言：中 / 英 / 俄")
        print(f"👋 新用户欢迎：已开启")
        await dp.start_polling(bot, skip_updates=True)
    except TelegramNetworkError:
        print("❌ 代理连接失败！请检查代理软件，或者把PROXY_HOST改成空关闭代理")
    except TelegramForbiddenError:
        print("❌ BOT_TOKEN无效，请检查你的机器人Token")
    except Exception as e:
        print(f"❌ 启动失败：{e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    keep_alive()
    try:
        # Windows系统异步兼容
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        print("✅ 机器人已安全停止")
    except Exception as e:
        print(f"❌ 运行出错：{e}")