# 新增：导入保活函数
from keep_alive import keep_alive

ADMIN_ID = 8655639490

YACHTS = [
    {
        "size": 40,
        "types": ["飞桥", "豪华", "商务", "巡航", "接待"],
        "name_zh": "40尺飞桥豪华游艇",
        "name_en": "40ft Flybridge Luxury Yacht",
        "name_ru": "Яхта 40 футов Летный мост",
        "desc_zh": "空间舒适，适合商务接待、小型聚会，平稳舒适，性价比极高",
        "desc_en": "Comfortable space, perfect for business meetings & small parties, stable & cost-effective",
        "desc_ru": "Комфортное пространство, идеально для деловых встреч, стабильно и экономично",
        "url": "https://www.azurmore.com/productinfo/3595372.html",
        "price": 380
    },
    {
        "size": 40,
        "types": ["钓鱼", "专业", "实用", "出海", "作业"],
        "name_zh": "40尺专业钓鱼艇",
        "name_en": "40ft Professional Fishing Boat",
        "name_ru": "Рыбацкая лодка 40 футов",
        "desc_zh": "专业钓鱼配置，出海稳定，工具齐全，适合海钓爱好者",
        "desc_en": "Professional fishing equipment, stable at sea, full tools, perfect for fishing lovers",
        "desc_ru": "Профессиональное оборудование, стабильно в море, идеально для рыбалки",
        "url": "https://www.azurmore.com/productinfo/3595351.html",
        "price": 260
    },
    {
        "size": 50,
        "types": ["飞桥", "豪华", "商务", "派对", "娱乐", "大空间"],
        "name_zh": "50尺豪华飞桥游艇",
        "name_en": "50ft Luxury Flybridge Yacht",
        "name_ru": "Яхта 50 футов Летный мост",
        "desc_zh": "超大豪华空间，适合高端商务、派对娱乐，体验一流",
        "desc_en": "Super large luxury space, great for VIP business & parties, first-class experience",
        "desc_ru": "Огромное роскошное пространство, для ВИП-встреч и вечеринок",
        "url": "https://www.azurmore.com/productinfo/3584817.html",
        "price": 680
    },
    {
        "size": 50,
        "types": ["双体", "豪华", "家庭", "休闲", "度假", "巡航"],
        "name_zh": "50尺豪华双体船",
        "name_en": "50ft Luxury Catamaran",
        "name_ru": "Катамаран 50 футов",
        "desc_zh": "超平稳不晕船，适合家庭度假、长途巡航，舒适安全",
        "desc_en": "Super stable no seasickness, perfect for family vacations & long cruises",
        "desc_ru": "Стабильно без укачивания, идеально для семейного отдыха",
        "url": "https://www.azurmore.com/productinfo/3579540.html",
        "price": 520
    },
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
        "lang_saved": "✅ 语言已保存！\n\n📌 搜索格式指南：\n▪️ 500万以上 / 500W以上\n▪️ 家庭用游艇 / 限量版游艇\n▪️ 游艇品牌：Azimut / Ferretti\n▪️ 50尺双体商务游艇推荐",
        "no_result": "😥 未找到匹配游艇\n\n✅ 正确格式示例：\n▪️ 500万以上\n▪️ 家庭用游艇\n▪️ 游艇品牌：Azimut / Ferretti\n▪️ 50尺商务游艇推荐",
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
        "lang_saved": "✅ Language saved!\n\n📌 Search Guide:\n▪️ above 5m CNY / 5m\n▪️ Family Yacht / Limited Edition Yacht\n▪️ Yacht brand：Azimut / Ferretti\n▪️ Recommended 50-foot catamaran business yachts",
        "no_result": "😥 No matching yachts\n\n✅ Correct format:\n▪️ above 5m CNY / 5m\n▪️ Family Yacht / Limited Edition Yacht\n▪️ 5-6m CNY\n▪️ Recommended 50-foot catamaran business yachts",
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
        "lang_saved": "✅ Язык сохранен!\n\n📌 Формат поиска:\n▪️ выше 5млн КНР / 5млн\n▪️ Семейная яхта / Яхта ограниченной серии\n▪️ Яхтенный бренд：Azimut / Ferretti\n▪️ Рекомендуемые 50-футовые катамаранные бизнес-яхты",
        "no_result": "😥 Яхты не найдены\n\n✅ Правильный формат:\n▪️ выше 5млн\n▪️ Семейная яхта\n▪️ Яхтенный бренд：Azimut / Ferretti\n▪️ Рекомендуемые 50-футовые катамаранные бизнес-яхты",
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
    "飞桥": [
        "飞桥", "飞桥类", "飞桥型", "飞桥式", "飞桥艇", "飞桥游艇", "飞桥款",
        "flybridge", "fly bridge", "fly-bridge", "flybridge yacht",
        "летный мост", "летный", "флайбридж"
    ],
    "钓鱼": [
        "钓鱼", "钓鱼类", "钓鱼艇", "钓鱼游艇", "海钓", "海钓船", "海钓艇",
        "профессиональная", "коммерческая"
    ],
    "家庭": [
        "家庭", "家庭类", "家庭型", "亲子", "休闲", "度假", "旅游",
        "family", "leisure", "vacation",
        "семейная", "досуг", "отпуск"
    ],
    "实用": [
        "实用", "性价比", "经济", "实惠", "基础款",
        "practical", "economic", "affordable",
        "практичная", "экономичная"
    ],
    "商务": [
        "商务", "商务类", "商务型", "商务款", "商务接待", "商务艇", "洽谈", "会议",
        "business", "corporate", "executive",
        "бизнес", "деловая", "корпоративная"
    ],
    "派对": [
        "派对", "聚会", "娱乐", "轰趴", "party", "celebration",
        "вечеринка", "встреча"
    ],
    "巡航": [
        "巡航", "远航", "长途", "海上巡航", "远洋",
        "cruise", "cruising", "long distance",
        "круиз", "дальнее плавание"
    ],
    "高端": [
        "高端", "顶级", "旗舰", "限量", "exclusive", "top",
        "премиум", "топ", "флагман"
    ],
    "限量": [
        "限量", "限定", "限量版", "典藏", "limited", "exclusive",
        "ограниченная", "эксклюзивная"
    ],
    "休闲": [
        "休闲", "放松", "观光", "游玩", "leisure", "relax",
        "отдых", "расслабление"
    ],
    "度假": [
        "度假", "旅游", "海岛", "海景", "vacation", "holiday",
        "отпуск", "путешествие"
    ],
    "大空间": [
        "大空间", "宽敞", "空间大", "大容量", "spacious", "roomy",
        "просторная", "большое пространство"
    ],
    "私人": [
        "私人", "私家", "个人", "private", "personal",
        "приватная", "личная"
    ],
    "接待": [
        "接待", "会客", "宴请", "VIP接待", "reception",
        "прием", "встреча"
    ],
    "娱乐": [
        "娱乐", "游玩", "K歌", "影音", "entertainment", "fun",
        "развлечение"
    ],
    "出海": [
        "出海", "海上", "深海", "近海", "sea", "ocean",
        "море", "океан"
    ],
    "经典": [
        "经典", "复古", "传统", "classic", "traditional",
        "классика", "традиционная"
    ],
    "现代": [
        "现代", "时尚", "新款", "modern", "fashion",
        "современная", "модная"
    ]
}


# -------------------------- 工具函数 --------------------------
def get_size(text):
    match = re.search(r'(\d+)', text)
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
        between = re.search(r'(\d+)-(\d+)m', txt)
        if between:
            min_p = int(between.group(1)) * 100
            max_p = int(between.group(2)) * 100
        return (min_p, max_p)
    return (None, None)


# -------------------------- 新增：尺寸范围筛选工具函数（移到这里了！） --------------------------
def get_size_range(text, lang="zh"):
    txt = text.lower().replace(" ", "")
    min_s = None
    max_s = None
    # 中文尺寸解析
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
    # 英文尺寸解析
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
    # 俄语尺寸解析
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

# 原来的价格筛选函数，现在里面没有那两个小函数了
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