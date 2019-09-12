#! python3

import sys
import os

sys.path.append(os.path.join(os.getcwd(), "Stuff"))

from gui import GUI

from dishonesty import Dishonesty, DishonestyInstructions, DishonestyInstructions2, DishonestyInstructions3
from dishonesty import DishonestyInstructions4, DishonestyInstructions5
from cats import Cats, CatsInstructions
from richman import RichMan
from ambiguity import Ambiguity
from responsibility import Responsibility
from enabling import Enabling
from letter import Letter
from fluencyrisk import FluencyRisk, FluencyRiskInstructions
from fluency import Fluency, FluencyPresentation, FluencyIntro1, FluencyIntro2, FluencyIntro3
from fluency import FluencyIntro4, FluencyIntro5, FluencyPractice1, FluencyPractice2
from fluency import PronounceabilityIntro, fluencyProunceability, fluencyLanguage
from intros import Intro, DilemmasIntro, ending
from demo import Demographics
from comments import Comments
from hexaco import Hexaco, HexacoInstructions
from debrief import Debriefing

frames = [Intro,
          FluencyIntro1,
          FluencyIntro2,
          FluencyPractice1,
          FluencyIntro3,
          FluencyPractice2,
          FluencyIntro4,
          FluencyPresentation,
          FluencyIntro5,                
          Fluency,
          DishonestyInstructions,
          DishonestyInstructions2,
          DishonestyInstructions3,
          DishonestyInstructions4,
          DishonestyInstructions5,
          Dishonesty,
          CatsInstructions,
          Cats,
          DilemmasIntro,
          Ambiguity,
          Enabling,
          RichMan,
          Letter,
          Responsibility,
          FluencyRiskInstructions,
          FluencyRisk,
          PronounceabilityIntro,
          fluencyProunceability,
          fluencyLanguage,
          HexacoInstructions,
          Hexaco,        
          Debriefing,
          Demographics,
          Comments,
          ending
          ]


GUI(frames)
