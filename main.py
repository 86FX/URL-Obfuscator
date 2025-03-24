import random, string

strings = ["www.", "ftp.", "cpanel.", "webmail.", "api.", "cdn.",
    ".com", ".net", ".org", ".de", ".icu", ".uk", ".ru",
    "gravity", "giraffe", "remember", "topple", "minor", "element", "skull", "best", "design", "royal", "fashion", "hub", "curve", "extra", "visit", "strategy", "tomato", "enforce", "wire", "journey", "mercy", "artist", "catalog", "brush", "impulse", "drink", "blur", "claim", "nasty", "again", "guide", "garlic", "future", "small", "fever", "east", "table", "junior", "female", "express", "banana", "plastic", "pioneer", "vacuum", "primary", "usual", "fatigue", "history", "spend", "tent", "skate", "absurd", "analyst", "screen", "acquire", "fee", "perfect", "clinic", "treat", "merit",
    "bit.ly", "ip-api.com", "discord.com", "webhooks", "api.telegram.org", "sendDocument",
    "!", "$", "%", "^", "&", "*", "(", ")", "-", "=", "_",
    "+", ",", ".", ";", ":", "'", '"', "\\", "|", "/", "[",
    "]", "{", "}"]
random.shuffle(strings)

def do(url, times=random.randrange(25, 125)):
    return url.split(chr(47))[0]+chr(47)*2+"".join([("".join([(random.choice([chr(i) for i in range(97, 123)]+[(chr(i)) for i in range(48, 58)])) for i in range(times)])+"."+"".join([(random.choice([chr(i) for i in range(97, 123)]+[chr(i) for i in range(48, 58)]+strings)) for i in range(times)])+"@") for i in range(3)])+url.lower().replace(chr(119)*3+chr(ord("".join([chr(int(i)) for i in b"776597651006510165326598651216532656665108659765110651076532".decode().replace(str(65), chr(32)).split()])[::-1][11])-ord(str(6))), '').replace(url.split(chr(47))[0]+chr(47)*2, '', 1)+chr(35)+"".join([(random.choice([chr(i) for i in range(33, 127)]+[url.lower().replace(chr(119)*3+chr(ord("".join([chr(int(i)) for i in b"776597651006510165326598651216532656665108659765110651076532".decode().replace(str(65), chr(32)).split()])[::-1][11])-ord(str(6))), '').replace(url.split(chr(47))[0]+chr(47)*2, '', 1).split('/')[0]]*5+["discord.com/api/webhooks/"+"".join([random.choice(string.digits) for i in range(18)])+"/"+"".join([random.choice(string.ascii_letters) for i in range(68)])for i in range(15)])) for i in range(times)])

at = input('[?] enter url | ')
print("\n[+] " + do(at))
