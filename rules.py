from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import *
from .tracks import TRACK_NAMES

if TYPE_CHECKING:
    from .__init__ import JetskiRushWorld

def set_all_rules(world: JetskiRushWorld) -> None:
    for location in LOCATION_IDS.keys():
        if "Seaside Factory" in location:
            world.set_rule(location, Has("Seaside Factory"))
        elif "Arctic Iceway" in location:
            world.set_rule(location, Has("Arctic Iceway"))
        elif "Kabuki Peaks" in location:
            world.set_rule(location, Has("Kabuki Peaks"))
        elif "Fungal Forest" in location:
            world.set_rule(location, Has("Fungal Forest"))
        elif "Crossbone Cove" in location:
            world.set_rule(location, Has("Crossbone Cove"))
        elif "Aquatic Arena" in location:
            world.set_rule(location, Has("Aquatic Arena"))
        elif "Temple Ravine" in location:
            world.set_rule(location, Has("Temple Ravine"))
        elif "Candy Canyon" in location:
            world.set_rule(location, Has("Candy Canyon"))
        elif "Hollow Castle" in location:
            world.set_rule(location, Has("Hollow Castle"))
        elif "Retro Rush" in location:
            world.set_rule(location, Has("Retro Rush"))
        elif "Cosmic Circuit" in location:
            world.set_rule(location, Has("Cosmic Circuit"))
        elif "Pyro Peak" in location:
            world.set_rule(location, Has("Pyro Peak"))

world.set_completion_rule(Has("Trophy", count=world.options.track_requirement))