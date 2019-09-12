from common import InstructionsFrame
from math import ceil
import random


intro = """
Dobrý den,

děkujeme, že se účastníte našeho výzkumu. Studie sestává z několika samostatných částí, v jejichž průběhu budete na počítači řešit různé třídící úlohy a odpovídat na otázky. Celá studie trvá asi 50 minut.

Vaše účast na výzkumu je zcela dobrovolná a můžete ji kdykoliv ukončit. Pokud se budete chtít na něco zeptat, přivolejte prosím experimentátora zvednutím ruky.

Kliknutím na tlačítko Pokračovat vyjadřujete svůj souhlas s účastí a anonymním využitím Vašich dat.

Pro začátek klikněte na tlačítko Pokračovat.
"""

dilemmasintro = """
Nyní budete číst krátké popisy několika situací a činů, jež různé osoby v těchto situacích vykonají nebo mohou vykonat.

Při čtení můžete mít někdy pocit, že situace, tak jak jsou popsané, nejsou realistické. Například můžete číst, že když osoba udělá X, stane se Y, a můžete si myslet, že to není realistické – tedy že nemusí nutně dojít k Y, pokud osoba udělá X. V případě, že budete mít takovéto pochybnosti, prosíme potlačte je, jako byste to udělal(a) například u ne zcela realistického filmu a předpokládejte, že situace se odehrají tak, jak jsou popsány.

Čtěte prosím pozorně popisy všech situací a odpovězte na otázky, jež budou po každé situaci následovat.
"""

endingtext = """
Děkujeme za Vaši účast! 
Dnešní výzkum sestával z několika samostatných studií: Jedna skupina zkoumala vliv tzv. plynulosti (angl. fluency) na hodnocení slov a obrázků. Zajímalo nás například, jestli budou lidé hodnotit aditiva s hůře vyslovitelnými názvy jako nebezpečnější nebo jestli se hodnocení obrázků koček liší v závislosti na kontrastu a straně obrazovky, na níž se kočka zobrazí.
Další skupina studií byla z oblasti morální psychologie – četli jste různé scenáře, jejichž detaily se mezi náhodně vybranými účastníky lišily. Vliv těchto detailů na hodnocení popsaných činů nebo na rozhodnutí o výši přiznané náhrady škody nám umožní identifikovat faktory důležité pro tvorbu morálních soudů a rozhodnutí.
Úloha s tříděním barevných obrázků měla simulovat práci zaměstnance, jenž dostává za svoji práci relativně malou fixní odměnu bez ohledu na to, jak svoji práci vykonává. Pokud ji však vykonává špatně (zde když netřídí dle barvy), společnosti vzniká škoda, ačkoliv úředník tím sám netrpí. Naopak má někdy možnost přivydělat si, když je k obrázku přidán “úplatek”, jenž získá, když provede zatřídění dle požadavku uplácejícího. Tato úloha vznikla originálně v laboratoři PLESS a pokud se osvědčí, umožní v budoucnosti zkoumat náchylnost ke korupci či nepoctivému chování.

Podrobnější popis jednotlivých studií a jejich hypotéz Vám bude zaslán v průběhu nejbližších dní e-mailem. Prosíme, abyste tyto informace během sběru dat nešířili, zejména ne mezi potenciální účastníky. O ukončení sběru dat budete informováni rovněž e-mailem.

Pod klávesnicí naleznete potvrzení o převzetí odměny. Toto potvrzení je pro Würzburgskou univerzitu, jež přispívá 4 € pro každého účastníka dnešní studie. Prosím čitelně vyplňte potvrzení.

{}

Nyní si můžete vzít své věci, vyplněné potvrzení a přejít do vedlejší místnosti, kde Vám bude odměna vyplacena. 
Tím Vaše účast na dnešní studii končí. Ještě jednou děkujeme!
"""

winending = "V losování v souvislosti s úlohou s tříděním obrázků jste byl(a) vybrán(a). V úloze jste získal(a) {} Kč pro sebe a {} Kč pro charitu Člověk v tísni. Vaše celková odměna je tedy {} Kč – zapište prosím tuto částku na papírek, jenž odevzdáte spolu s vyplněným potvrzením."
lostending = "V losování v souvislosti s úlohou s tříděním obrázků jste nebyl(a) vybrán(a). Vaše odměna za dnešní experiment je tedy 100 Kč."

Intro =(InstructionsFrame, {"text": intro})
DilemmasIntro = (InstructionsFrame, {"text": dilemmasintro})


class Ending(InstructionsFrame):
    def __init__(self):
        pass
    
    def __call__(self, root):
        win = random.random() < 1/13
        if win:
            reward = ceil(root.reward / 10)
            charity = ceil(root.charity / 10)
            text = endingtext.format(winending.format(reward, charity, reward + 100))
        else:
            text = endingtext.format(lostending)
        super().__init__(root, text, height = 30, font = 15, proceed = False)
        return self

ending = Ending()
