#! python3

import sys
import os

sys.path.append(os.path.join(os.getcwd(), "Stuff"))

from gui import GUI

from dishonesty import Dishonesty, DishonestyInstructions, DishonestyInstructions2, DishonestyInstructions3
from dishonesty import DishonestyInstructions4, DishonestyInstructions5
from intros import Intro, DilemmasIntro, ending
from demo import Demographics
from comments import Comments
from hexaco import Hexaco, HexacoInstructions
from debrief import Debriefing

frames = [Intro,
          DishonestyInstructions,
          DishonestyInstructions2,
          DishonestyInstructions3,
          DishonestyInstructions4,
          DishonestyInstructions5,
          Dishonesty,
          HexacoInstructions,
          Hexaco,        
          Debriefing,
          Demographics,
          Comments,
          ending
          ]


GUI(frames)
