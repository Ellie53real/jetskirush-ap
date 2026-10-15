from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import *
from .data.location_ids import LOCATION_IDS

if TYPE_CHECKING:
    from .__init__ import JetskiRushWorld

def set_all_rules(world: JetskiRushWorld) -> None:
    seaside_factory_access = world.get_entrance("Seaside Factory Access")
    arctic_iceway_access = world.get_entrance("Arctic Iceway Access")
    kabuki_peaks_access = world.get_entrance("Kabuki Peaks Access")
    fungal_forest_access = world.get_entrance("Fungal Forest Access")
    crossbone_cove_access = world.get_entrance("Crossbone Cove Access")
    aquatic_arena_access = world.get_entrance("Aquatic Arena Access")
    temple_ravine_access = world.get_entrance("Temple Ravine Access")
    candy_canyon_access = world.get_entrance("Candy Canyon Access")
    hollow_castle_access = world.get_entrance("Hollow Castle Access")
    retro_rush_access = world.get_entrance("Retro Rush Access")
    cosmic_circuit_access = world.get_entrance("Cosmic Circuit Access")
    pyro_peak_access = world.get_entrance("Pyro Peak Access")

world.set_completion_rule(Has("Trophy", count=world.options.track_requirement))