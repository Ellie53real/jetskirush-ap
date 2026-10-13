from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
from . import items, regions, rules
from .options import JetskiRushOptions
from .data.location_ids import LOCATION_IDS
from .data.item_ids import ITEM_IDS

class JetskiRushWebWorld(WebWorld):
    game = "Jetski Rush"
    theme = "racing"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Jetski Rush for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        [""]
    )

    tutorials = [setup_en]

class JetskiRushWorld(World):
    """
    """

    game = "Jetski Rush"
    web = JetskiRushWebWorld()
    options_dataclass = JetskiRushOptions
    options: JetskiRushOptions
    location_name_to_id = LOCATION_IDS
    item_name_to_id = ITEM_IDS
    origin_region_name = "Course Select"

    def create_regions(self):
        return regions.create_regions_and_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
    
    def create_items(self) -> None:
        items.create_all_items(self)
    
    def create_item(self, name: str) -> items.JetskiRushItem:
        return items.create_item_with_classification(self, name)

    def get_filler_item_name(self) -> str:
        return "VRChat Credits"