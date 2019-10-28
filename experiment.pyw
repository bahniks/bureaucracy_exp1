#! python3

import sys
import os

sys.path.append(os.path.join(os.getcwd(), "Stuff"))

from gui import GUI

from dishonesty import Dishonesty, DishonestyInstructions, DishonestyInstructions2, DishonestyInstructions3
from dishonesty import DishonestyInstructions4, DishonestyInstructions5
from intros import Intro, ending
from demo import Demographics
from comments import Comments
from hexaco import Hexaco, HexacoInstructions
from debrief import Debriefing
from charity import Charity
from anchoring import AnchoringInstructions1, Comparison, AnchoringInstructions2, Absolute
from wee import WeakEvidenceInstructions, WeakEvidence
from lottery import Lottery, LotteryInstructions
from character import CharacterIntro, Character1, CharacterIntro2, Character2

frames = [Intro, #
          Charity, #
          DishonestyInstructions, #
          DishonestyInstructions2, #
          DishonestyInstructions3, #
          DishonestyInstructions4, #
          DishonestyInstructions5, #
          Dishonesty, #
          LotteryInstructions, #
          Lottery, #
          AnchoringInstructions1, #
          Comparison, #
          AnchoringInstructions2, #
          Absolute, #
          WeakEvidenceInstructions, #
          WeakEvidence, #
          CharacterIntro,
          Character1,
          CharacterIntro2,
          Character2,
          HexacoInstructions, #
          Hexaco, #
          Debriefing, #
          Demographics, #
          Comments, #
          ending #
          ]

#frames = [Charity, Dishonesty, Lottery, Demographics, ending]

GUI(frames)
