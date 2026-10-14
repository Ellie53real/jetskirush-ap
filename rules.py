from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import *
from .tracks import TRACK_NAMES

if TYPE_CHECKING:
    from .__init__ import JetskiRushWorld

def set_all_rules(world: JetskiRushWorld) -> None:
    for location in LOCATION_IDS.keys():
        for track in TRACK_NAMES.keys():
            if track in location:
                world.set_rule(location, Has(track))

world.set_completion_rule(Has("Trophy", count=world.options.track_requirement))