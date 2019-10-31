#! python3

import sys
import os

sys.path.append(os.path.join(os.getcwd(), "Stuff"))

from gui import GUI

from dishonesty import Dishonesty, DishonestyInstructions, DishonestyInstructions2, DishonestyInstructions3
from dishonesty import DishonestyInstructions4, DishonestyInstructions5, DishonestyInstructions6, DishonestyInstructions7
from intros import Intro, ending
from demo import Demographics
from comments import Comments
from hexaco import Hexaco, HexacoInstructions
from debrief import Debriefing
from charity import Charity
from anchoring import AnchoringInstructions1, Comparison, AnchoringInstructions2, Absolute
from wee import WeakEvidenceInstructions, WeakEvidence
from lottery import Lottery, LotteryInstructions

frames = [Intro,
          Charity,
          DishonestyInstructions,
          DishonestyInstructions2,
          DishonestyInstructions3,
          DishonestyInstructions4,
          DishonestyInstructions5,
          DishonestyInstructions6,
          DishonestyInstructions7,
          Dishonesty,
          LotteryInstructions,
          Lottery,
          AnchoringInstructions1,
          Comparison,
          AnchoringInstructions2,
          Absolute,
          WeakEvidenceInstructions,
          WeakEvidence,
          HexacoInstructions,
          Hexaco,
          Debriefing,
          Demographics,
          Comments,
          ending
          ]


GUI(frames)
