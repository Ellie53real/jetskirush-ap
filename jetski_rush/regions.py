from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region, Location
from .data.location_ids import LOCATION_IDS

if TYPE_CHECKING:
    from .__init__ import JetskiRushWorld

class JetskiRushLocation(Location):
    game = "Jetski Rush"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_IDS[location_name] for location_name in location_names}

def create_regions_and_locations(world: JetskiRushWorld) -> None:
    regions = ["Track Select", "Seaside Factory", "Arctic Iceway", "Kabuki Peaks", "Fungal Forest", "Crossbone Cove", "Aquatic Arena", "Temple Ravine", "Candy Canyon", "Hollow Castle", "Retro Rush", "Cosmic Circuit", "Pyro Peak"]
    track_select = Region("Track Select", world.player, world.multiworld)
    regions.append(track_select)

    seaside_factory = Region("Seaside Factory", world.player, world.multiworld)
    seaside_factory.add_locations(get_location_names_with_ids([
        "Seaside Factory - Finish",
        "Seaside Factory - Finish (Trophy)",
        "Seaside Factory - Time Trial in 2:00"
    ]))
    regions.append(seaside_factory)

    arctic_iceway = Region("Arctic Iceway", world.player, world.multiworld)
    arctic_iceway.add_locations(get_location_names_with_ids([
        "Arctic Iceway - Finish",
        "Arctic Iceway - Finish (Trophy)",
        "Arctic Iceway - Time Trial in 3:30"
    ]))
    regions.append(arctic_iceway)

    kabuki_peaks = Region("Kabuki Peaks", world.player, world.multiworld)
    kabuki_peaks.add_locations(get_location_names_with_ids([
        "Kabuki Peaks - Finish",
        "Kabuki Peaks - Finish (Trophy)",
        "Kabuki Peaks - Time Trial in 3:00"
    ]))
    regions.append(kabuki_peaks)

    fungal_forest = Region("Fungal Forest", world.player, world.multiworld)
    fungal_forest.add_locations(get_location_names_with_ids([
        "Fungal Forest - Finish",
        "Fungal Forest - Finish (Trophy)",
        "Fungal Forest - Time Trial in 4:00"
    ]))
    regions.append(fungal_forest)

    crossbone_cove = Region("Crossbone Cove", world.player, world.multiworld)
    crossbone_cove.add_locations(get_location_names_with_ids([
        "Crossbone Cove - Finish",
        "Crossbone Cove - Finish (Trophy)",
        "Crossbone Cove - Time Trial in 2:00"
    ]))
    regions.append(crossbone_cove)

    aquatic_arena = Region("Aquatic Arena", world.player, world.multiworld)
    aquatic_arena.add_locations(get_location_names_with_ids([
        "Aquatic Arena - Finish",
        "Aquatic Arena - Finish (Trophy)",
        "Aquatic Arena - Time Trial in 3:00"
    ]))
    regions.append(aquatic_arena)

    temple_ravine = Region("Temple Ravine", world.player, world.multiworld)
    temple_ravine.add_locations(get_location_names_with_ids([
        "Temple Ravine - Finish",
        "Temple Ravine - Finish (Trophy)",
        "Temple Ravine - Time Trial in 3:45"
    ]))
    regions.append(temple_ravine)

    candy_canyon = Region("Candy Canyon", world.player, world.multiworld)
    candy_canyon.add_locations(get_location_names_with_ids([
        "Candy Canyon - Finish",
        "Candy Canyon - Finish (Trophy)",
        "Candy Canyon - Time Trial in 3:30"
    ]))
    regions.append(candy_canyon)

    hollow_castle = Region("Hollow Castle", world.player, world.multiworld)
    hollow_castle.add_locations(get_location_names_with_ids([
        "Hollow Castle - Finish",
        "Hollow Castle - Finish (Trophy)",
        "Hollow Castle - Time Trial in 3:45"
    ]))
    regions.append(hollow_castle)

    retro_rush = Region("Retro Rush", world.player, world.multiworld)
    retro_rush.add_locations(get_location_names_with_ids([
        "Retro Rush - Finish",
        "Retro Rush - Finish (Trophy)",
        "Retro Rush - Time Trial in 2:00"
    ]))
    regions.append(retro_rush)

    cosmic_circuit = Region("Cosmic Circuit", world.player, world.multiworld)
    cosmic_circuit.add_locations(get_location_names_with_ids([
        "Cosmic Circuit - Finish",
        "Cosmic Circuit - Finish (Trophy)",
        "Cosmic Circuit - Time Trial in 3:00"
    ]))
    regions.append(cosmic_circuit)

    pyro_peak = Region("Pyro Peak", world.player, world.multiworld)
    pyro_peak.add_locations(get_location_names_with_ids([
        "Pyro Peak - Finish",
        "Pyro Peak - Finish (Trophy)",
        "Pyro Peak - Time Trial in 3:45"
    ]))
    regions.append(pyro_peak)

    track_select.connect(seaside_factory)
    track_select.connect(arctic_iceway)
    track_select.connect(kabuki_peaks)
    track_select.connect(fungal_forest)
    track_select.connect(crossbone_cove)
    track_select.connect(aquatic_arena)
    track_select.connect(temple_ravine)
    track_select.connect(candy_canyon)
    track_select.connect(hollow_castle)
    track_select.connect(retro_rush)
    track_select.connect(cosmic_circuit)
    track_select.connect(pyro_peak)
