import psutil as ps
import json
from psutil import virtual_memory
from bcolor import colors


path = 'config.json'
with open(path, 'r') as f:
    data = json.load(f)

settings = data['settings']
other = data['other']
links = data['links']

defcl = colors['default']
errcl = colors['error']
exacl = colors['example']
logcl = colors['logs']

prefix = settings['prefix']

quick_messages = {
	'UNKNOWN ERROR LOG': '[Logs:error] Произошла неизвестная ошибка! |',
	'UNKNOWN ERROR': 'Произошла неизвестная ошибка!',
	'UNKNOWN ERROR EN': 'An unknown error has occurred!',
	'BOT STATUS LOG': '[Logs:owner] Статус бота был успешно сменен на:',
	'THIRD PARTY SYM ERROR': 'Ошибка! Были найдены сторонние символы!',
	'THIRD PARTY SYM ERROR EN': 'Mistake! Third party symbols were found!',
	'THIRD PARTY SYM ERROR LOG': '[Logs:error] Ошибка! Были найдены сторонние символы! |',

	'COPYRIGHT RU': 'Copyright © 2020 Aki | Все права защищены.',
	'COPYRIGHT EN': 'Copyright © 2020 Aki | All rights reserved.',
}

copyright_ru = quick_messages['COPYRIGHT RU']
copyright_en = quick_messages['COPYRIGHT EN']

fucku_en = [
        "You are a fucking fucktard {}! ~{}",
        "Fuck you, {}. ~{}",
        "Fucking fuck off, {}. ~{}",
        "Fuck off, {}. ~{}",
        "Fuck this, {}. ~{}",
        "Fuck that, {}. ~{}",
        "You are a fucking faggot, {}. ~{}",
        "{}, Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch! ~{}",
        "Oh fuck off, just really fuck off you total dickface. Christ {}, you are fucking thick. ~{}",
        "{}, why don't you go outside and play hide-and-go-fuck-yourself? ~{} ",
        "Hey {}, what a fascinating story, in what chapter do you shut the fuck up?\n\nSincerly,\n{}",
        "What you've just said is one of the most insanely idiotic things I have ever heard, {}. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points :name, and may God have mercy on your soul. ~{}"
        ]

fucku_ru = [
        "Ты гребаный ублюдок {}! ~{}",
        "Пошёл ты, {}. ~{}",
        "Отвали, {}. ~{}",
        "Отъебись, {}. ~{}",
        "К черту тебя, {}. ~{}",
        "Пошёл к чёрту, {}. ~{}",
        "Ты гребаный пидор, {}. ~{}",
        "{}, Ты, кишка с глиняным мозгом, глупый дурак, сукин сын, непристойный жирный подлец!! ~{}",
        "Ой, отвали, просто отвали, полное хуйло. Господи {}, ты чертовски тупой. ~{}",
        "{}, почему бы вам не выйти на улицу и не пойти нахуй? ~{} ",
        "Хей {}, какая увлекательная история, в какой главе ты заткнёшься?\n\nИскренне,\n{}",
        "То, что вы только что сказали, - одна из самых безумных идиотских вещей, которые я когда-либо слышал, {}. В своем бессвязном, бестолковом ответе вы ни разу не приблизились к чему-либо, что можно было бы считать рациональной мыслью. Все в этой комнате теперь глупы из-за того, что послушали это. Я не буду вас оскорблять, и да помилует Господь твою душу. ~{}"
        ]

uwutalk_en = [
        'S-Sorry onii-chan p-please d-do me harder ;w;\n{}',
        'Y-You got me all wet now senpai!\n{}',
        'D-Dont t-touch me there senpai\n{}',
        'P-Please l-love me harder oniichan ohh grrh aahhhh~!\n{}',
        'Give me all your cum senpai ahhhhh~\n{}',
        'F-Fuck me harder chan!','Oh my god I hate you so much senpai but please k-keep fucking me harder! ahhh~\n{}',
        'D-do you like my stripped panties getting soaked by you and your hard cock? ehhh master your so lewd ^_^\n{}',
        'kun your cute little dick between my pussy lips looks really cute, Im blushing\n{}',
        'Master does it feel good when I slide by tits up and down on your cute manly part?\n{}',
        'oniichan my t-toes are so warm with your cum all over them uwu~\n{}',
        'Lets take this swimsuit off already <3 ill drink your unknown melty juice\n{}',
        'S-stop senpai if we keep making these lewd sounds im going to cum\n{}',
        'Your such a pervert for filling me up with your baby batter senpai\n{}',
        'Fill up my baby chamber with your semen kun (＞ｍ＜)\n{}',
        'M-master d-dont spank my petite butt so hard ahhhH~~~ your getting me so w-wet~\n{}',
        'Senpai your cock is already throbbing from my huge tits~\n{}',
        'Hey kun, Can I have some semen?\n{}',
        'Senpai shove deeper your penis in m-my pussy (>ω<) please\n{}'
]

uwutalk_ru = [
        'П-прости, онии-чан, п-пожалуйста, делай это посильнее ;w;\n{}',
        'Т-ты сделал меня всю мокрой, сэмпай!\n{}',
        'Н-не т-трогай меня там, сэмпай\n{}',
        'П-пожалуйста, люби меня сильнее онии-чан ооо гррх аахххх ~!\n{}',
        'Дай мне всю свою сперму, сэмпай аххххх ~\n{}',
        'Т-трахни меня сильнее, чан!\n{}',
        'Боже мой, я так сильно тебя ненавижу, сэмпай, но, пожалуйста, продолжай трахать меня сильнее! ааа ~\n{}',
        'Т-тебе нравится, когда ты и твой твердый член пропитали мои мокрые трусики? эххх мастер ты такой развратный ^_^\n{}',
        'Кун, твой милый маленький член между губами моей киски выглядит очень мило, я краснею\n{}',
        'Хозяин, тебе хорошо, когда я скольжу грудью вверх и вниз по твоей милой мужской части?\n{}',
        'Онии-чан, моя грудь очень тёплая от твоей спермы на ней uwu~\n{}',
        'Давай уже снимем этот купальник <3 я выпью твой таинственный жидкий сок\n{}',
        'П-Прекрати сэмпай, если мы продолжим издавать эти непристойные звуки, я кончу\n{}',
        'Ты такой извращенец, что наполнил меня своим детским кляром-сэмпай\n{}',
        'Наполни мою детскую комнатку своей спермой-кун (＞ｍ＜)\n{}',
        'М-мастер, н-не шлепай мою маленькую задницу так сильно ахххХ~~~ ты делаешь меня такой м-мокрой~\n{}',
        'Сэмпай, твой член уже пульсирует от моих огромных сисек~\n{}',
        'Эй, кун, можно мне немного спермы?\n{}',
        'Сэмпай засуньте свой пенис глубже в мою киску (> ω <), пожалуйста\n{}'
]

ping_list = [ # ПЕРЕНЕСИ МЕНЯ В ЮЗЕФУЛ.ПУ
            {'ping': 0.00000000000000000, 'emoji': '🟩🔳🔳🔳🔳'},
            {'ping': 0.10000000000000000, 'emoji': '🟧🟩🔳🔳🔳'},
            {'ping': 0.15000000000000000, 'emoji': '🟥🟧🟩🔳🔳'},
            {'ping': 0.20000000000000000, 'emoji': '🟥🟥🟧🟩🔳'},
            {'ping': 0.25000000000000000, 'emoji': '🟥🟥🟥🟧🟩'},
            {'ping': 0.30000000000000000, 'emoji': '🟥🟥🟥🟥🟧'},
            {'ping': 0.35000000000000000, 'emoji': '🟥🟥🟥🟥🟥'}
]

async def bytes2human(number, typer = None): # Thanks Fsoky community
        # Пример Работы Этой Функции перевода чисел:
        # >> bytes2human(10000)
        # >> '9.8K'
        # >> bytes2human(100001221)
        # >> '95.4M'

        if typer == "system":
            symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')  # Для перевода в Килобайты, Мегабайты, Гигобайты, Террабайты, Петабайты, Петабайты, Эксабайты, Зеттабайты, Йоттабайты
        else:
            symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')  # Для перевода в обычные цифры (10k, 10MM)

        prefix = {}

        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10

        for s in reversed(symbols):
            if number >= prefix[s]:
                value = float(number) / prefix[s]
                return '%.1f%s' % (value, s)

        return f"{number}B"

def bytes2human(number, typer = None): # Thanks Fsoky community
        if typer == "system":
            symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')  # Для перевода в Килобайты, Мегабайты, Гигобайты, Террабайты, Петабайты, Петабайты, Эксабайты, Зеттабайты, Йоттабайты
        else:
            symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')  # Для перевода в обычные цифры (10k, 10MM)

        prefix = {}

        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10

        for s in reversed(symbols):
            if number >= prefix[s]:
                value = float(number) / prefix[s]
                return '%.1f%s' % (value, s)

        return f"{number}B"

diff = {
    00.00 : "https://media.discordapp.net/attachments/720644512510378004/721619905358725150/time00.00.png",
    00.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721627416384110602/time00.05.png",
    00.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721627464207695922/time00.10.png",
    00.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721683678526439434/time00.15.png",
    00.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721683730044813363/time00.20.png",
    00.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721683805273849886/time00.25.png",
    00.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721683846063718410/time00.30.png",
    00.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721683889260855417/time00.35.png",
    00.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721683929631031296/time00.40.png",
    00.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721684011444994118/time00.45.png",
    00.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721684056844009482/time00.50.png",
    00.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721684095481937960/time00.55.png",
    01.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721684158807539732/time01.00.png",
    01.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721684192164970596/time01.05.png",
    01.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721684228680450108/time01.10.png",
    01.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721684266106486834/time01.15.png",
    01.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721684328320598086/time01.20.png",
    01.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721684367939993640/time01.25.png",
    01.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721684419622076456/time01.30.png",
    01.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721684486105858098/time01.35.png",
    01.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721684519077281842/time01.40.png",
    01.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721684553374105630/time01.45.png",
    01.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721684586194796554/time01.50.png",
    01.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721684620592152677/time01.55.png",
    02.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721684670454038550/time02.00.png",
    02.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721684699080163338/time02.05.png",
    02.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721684730080395294/time02.10.png",
    02.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721684758064791573/time02.15.png",
    02.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721684794265829516/time02.20.png",
    02.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721684824821334046/time02.25.png",
    02.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721684852155482112/time02.30.png",
    02.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721684901648138240/time02.35.png",
    02.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721684942852980746/time02.40.png",
    02.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721684995038642216/time02.45.png",
    02.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721685032007237642/time02.50.png",
    02.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721685067033739354/time02.55.png",
    03.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721685118917541918/time03.00.png",
    03.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721685159262421012/time03.05.png",
    03.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721685191944568832/time03.10.png",
    03.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721685225641345064/time03.15.png",
    03.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721685261976862780/time03.20.png",
    03.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721685294268678255/time03.25.png",
    03.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721685335569989692/time03.30.png",
    03.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721685368176509018/time03.35.png",
    03.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721685401508773918/time03.40.png",
    03.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721685433628753950/time03.45.png",
    03.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721685467891761204/time03.50.png",
    03.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721685501194666024/time03.55.png",
    04.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721685552402923578/time04.00.png",
    04.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721685582098595930/time04.05.png",
    04.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721685610317873175/time04.10.png",
    04.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721685645742833674/time04.15.png",
    04.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721685681596006500/time04.20.png",
    04.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721685709441990656/time04.25.png",
    04.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721685762583691334/time04.30.png",
    04.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721685796775788564/time04.35.png",
    04.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721685827117252668/time04.40.png",
    04.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721685861116280903/time04.45.png",
    04.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721685895450722374/time04.50.png",
    04.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721685937540562985/time04.55.png",
    05.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721685980406349844/time05.00.png",
    05.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721686010131382302/time05.05.png",
    05.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721686041370689607/time05.10.png",
    05.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721686080486768700/time05.15.png",
    05.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721686110408933466/time05.20.png",
    05.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721686138015711258/time05.25.png",
    05.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721686169204817920/time05.30.png",
    05.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721686204533440542/time05.35.png",
    05.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721686239920783500/time05.40.png",
    05.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721686274351693834/time05.45.png",
    05.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721686302763778098/time05.50.png",
    05.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721686330924597338/time05.55.png",
    06.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721686430744576020/time06.00.png",
    06.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721686462633869364/time06.05.png",
    06.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721686489339002900/time06.10.png",
    06.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721686521341542400/time06.15.png",
    06.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721686554430668822/time06.20.png",
    06.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721686587746025472/time06.25.png",
    06.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721686618812973186/time06.30.png",
    06.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721686656163381358/time06.35.png",
    06.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721686719203770378/time06.40.png",
    06.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721686756977672292/time06.45.png",
    06.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721686825244295278/time06.50.png",
    06.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721686856395259924/time06.55.png",
    07.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721686888192147537/time07.00.png",
    07.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721686914285174794/time07.05.png",
    07.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721686948594450473/time07.10.png",
    07.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721686984854339624/time07.15.png",
    07.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721687014214205500/time07.20.png",
    07.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721687046648889364/time07.25.png",
    07.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721687077024038994/time07.30.png",
    07.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721687106891546755/time07.35.png",
    07.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721687142522421318/time07.40.png",
    07.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721687179461525544/time07.45.png",
    07.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721687212273434634/time07.50.png",
    07.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721687245160972288/time07.55.png",
    08.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721687333216190494/time08.00.png",
    08.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721687371309121576/time08.05.png",
    08.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721687407937716324/time08.10.png",
    08.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721687439227224124/time08.15.png",
    08.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721687469124354048/time08.20.png",
    08.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721687510303899658/time08.25.png",
    08.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721687559142375454/time08.30.png",
    08.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721687600758259762/time08.35.png",
    08.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721687635243827210/time08.40.png",
    08.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721687670937485322/time08.45.png",
    08.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721687702138912778/time08.50.png",
    08.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721687732727840919/time08.55.png",
    09.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721687769839173672/time09.00.png",
    09.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721687804001779722/time09.05.png",
    09.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721687833508708432/time09.10.png",
    09.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721687864651284620/time09.15.png",
    09.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721687903847186472/time09.20.png",
    09.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721687943722434651/time09.25.png",
    09.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721687980791824444/time09.30.png",
    09.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721688014689927208/time09.35.png",
    09.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721688052212301884/time09.40.png",
    09.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721688085229731960/time09.45.png",
    09.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721688119631675462/time09.50.png",
    09.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721688151805919302/time09.55.png",
    10.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721688212963328050/time10.00.png",
    10.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721688238577680494/time10.05.png",
    10.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721688268680331334/time10.10.png",
    10.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721688299428904970/time10.15.png",
    10.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721688333880786974/time10.20.png",
    10.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721688367770894437/time10.25.png",
    10.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721688404403945512/time10.30.png",
    10.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721688435332743188/time10.35.png",
    10.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721688466219335712/time10.40.png",
    10.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721688504073060412/time10.45.png",
    10.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721688534481633360/time10.50.png",
    10.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721688562470486027/time10.55.png",
    11.00 : "https://cdn.discordapp.com/attachments/720644512510378004/721688593382244352/time11.00.png",
    11.05 : "https://cdn.discordapp.com/attachments/720644512510378004/721688630254501928/time11.05.png",
    11.10 : "https://cdn.discordapp.com/attachments/720644512510378004/721688657848696862/time11.10.png",
    11.15 : "https://cdn.discordapp.com/attachments/720644512510378004/721688717647020072/time11.15.png",
    11.20 : "https://cdn.discordapp.com/attachments/720644512510378004/721688750056407040/time11.20.png",
    11.25 : "https://cdn.discordapp.com/attachments/720644512510378004/721688787528187934/time11.25.png",
    11.30 : "https://cdn.discordapp.com/attachments/720644512510378004/721688815806185472/time11.30.png",
    11.35 : "https://cdn.discordapp.com/attachments/720644512510378004/721688844587630602/time11.35.png",
    11.40 : "https://cdn.discordapp.com/attachments/720644512510378004/721688889697370173/time11.40.png",
    11.45 : "https://cdn.discordapp.com/attachments/720644512510378004/721688922165346354/time11.45.png",
    11.50 : "https://cdn.discordapp.com/attachments/720644512510378004/721688957095772230/time11.50.png",
    11.55 : "https://cdn.discordapp.com/attachments/720644512510378004/721688988376760340/time11.55.png",
}

translit_abc = {
    'q':'ку',
    'w':'в',
    'e':'е',
    'r':'р',
    't':'т',
    'y':'й',
    'u':'у',
    'i':'и',
    'o':'о',
    'p':'п',
    'a':'а',
    's':'с',
    'd':'д',
    'f':'ф',
    'g':'г',
    'h':'х',
    'j':'ж',
    'k':'к',
    'l':'л',
    'z':'з',
    'x':'х',
    'c':'с',
    'v':'в',
    'b':'б',
    'n':'н',
    'm':'м',
    ',':',',
    ' ':' ',
    '!':'!'
}

ru_layout = {
    'q':'й',
    'w':'ц',
    'e':'у',
    'r':'к',
    't':'е',
    'y':'н',
    'u':'г',
    'i':'ш',
    'o':'щ',
    'p':'з',
    '[':'х',
    '{':'х',
    '}':'ъ',
    ']':'ъ',
    'a':'ф',
    's':'ы',
    'd':'в',
    'f':'а',
    'g':'п',
    'h':'р',
    'j':'о',
    'k':'л',
    'l':'д',
    ':':'ж',
    ';':'ж',
    '"':'э',
    "'":'э',
    'z':'я',
    'x':'ч',
    'c':'с',
    'v':'м',
    'b':'и',
    'n':'т',
    'm':'ь',
    '<':'б',
    ',':'б',
    '>':'ю',
    '.':'ю',
    '?':',',
    '/':'.',
    '`':'ё',
    '~':'ё',
    ' ':' ',
    '!':'!'
}
