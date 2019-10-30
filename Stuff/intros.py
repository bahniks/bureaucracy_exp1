from common import InstructionsFrame
from math import ceil
import random
import os

from gui import GUI


intro = """
Vítejte na výzkumné studii pořádané ve spolupráci s Fakultou podnikohospodářskou Vysoké školy ekonomické v Praze. Tato studie se skládá z několika různých úkolů a otázek. Níže je uveden přehled toho, co vás čeká:

1) Třídění obrázků: vaším úkolem bude třídit obrázky podle barvy. V tomto úkolu můžete vydělat peníze pro sebe a vámi vybranou charitu.
2) Loterie: můžete se rozhodnout zúčastnit se loterie s několika koly a získat další peníze (0-1280 Kč) v závislosti na vašich rozhodnutích a výsledcích loterie.
3) Odhady hodnot: budete odhadovat a porovnávat různé hodnoty týkající se všeobecných znalostí.
4) Odhady pravděpodobností: budete odhadovat pravděpodobnosti různých jevů.
5) Hodnocení lidí: budete hodnotit lidi a jejich činy dle poskytnutých popisů.
6) Dotazníky: budete odpovídat na otázky ohledně vašich vlastností a postojů.
7) Konec studie a platba: poté, co skončíte, půjdete do vedlejší místnosti, kde podepíšete pokladní dokument, na základě kterého obdržíte vydělané peníze v hotovosti. Jelikož v dokumentu bude uvedena pouze celková suma, nikdo se nedoví, kolik jste vydělali v jednotlivých částech studie.

Děkujeme, že jste vypnuli své mobilní telefony, a že nebudete s nikým komunikovat v průběhu studie. Pokud s někým budete komunikovat, nebo pokud budete nějakým jiným způsobem narušovat průběh studie, budete požádáni, abyste opustili laboratoř, bez nároku na vyplacení peněz.

V případě, že máte otázky nebo narazíte na technický problém během úkolů, zvedněte ruku a tiše vyčkejte příchodu výzkumného asistenta.

Nepokračujte prosím dokud vám výzkumný asistent nedá pokyn.
"""



endingtext = """
{}  V loterii jste vydělali {} Kč. Za účast na studii je odměna 100 Kč. Vaše celková odměna za tuto studii je tedy {} Kč, zaokrouhleno na desítky korun nahoru získáváte {} Kč. Napište prosím tuto (zaokrouhlenou) částku společně s číslem vašeho místa – {} na papír na stole před vámi.

Výsledky experimentu budou volně dostupné na stránkách PLESS a CEBEX, krátce po vyhodnocení dat a publikaci výsledků. Žádáme vás, abyste nesdělovali detaily této studie možným účastníkům, aby jejich volby a odpovědi nebyly ovlivněny a znehodnoceny.
  
Zvedněte prosím ruku a některý z výzkumných asistentů přijde a ukončí experiment. Poté si můžete vzít všechny svoje věci, papír s číslem vašeho místa a uvedenou odměnou, a bez toho, aniž byste rušili ostatní účastníky, se odeberte do vedlejší místnosti, kde obdržíte svoji odměnu. 

Toto je konec experimentu. Děkujeme za vaši účast!
 
Laboratoř CEBEX/PLESS
"""

winending = "V losování v souvislosti s úlohou s tříděním obrázků jste byl(a) vybrán(a). V úloze jste získal(a) {} Kč pro sebe a {} Kč pro charitu {}."
lostending = "V losování v souvislosti s úlohou s tříděním obrázků jste nebyl(a) vybrán(a)."


Intro =(InstructionsFrame, {"text": intro, "height": 28, "proceed": False, "keys": ["g", "G"]})


class Ending(InstructionsFrame):
    def __init__(self):
        pass
    
    def __call__(self, root):
        if not "won" in root.texts:
            win = random.random() < 1/4
        else:
            win = root.texts["won"]
        if win:
            reward = ceil(root.texts["reward"] / 10)
            charity = ceil(root.texts["charityReward"] / 10)
            ruffle = winending.format(reward, charity, root.texts["charity"])
        else:
            reward = 0
            ruffle = lostending
        lottery = root.texts["lottery_win"]
        sumReward = reward + lottery + 100
        roundedReward = int(ceil(sumReward/10)*10)
        seat = root.texts["station"]
        text = endingtext.format(ruffle, lottery, sumReward, roundedReward, seat)
        super().__init__(root, text, height = 30, font = 15, proceed = False)
        return self

ending = Ending()



if __name__ == "__main__":
    os.chdir(os.path.dirname(os.getcwd()))
    GUI([Intro,
         ending])
