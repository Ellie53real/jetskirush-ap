from __future__ import annotations
from BaseClasses import Item, ItemClassification

class JetskiRushItem(Item):
    game = "Jetski Rush"

class ItemDict(TypedDict):
    name: str

ITEM_TABLE = {
    "Seaside Factory": 200,
    "Arctic Iceway": 201,
    "Kabuki Peaks": 202,
    "Fungal Forest": 203,
    "Crossbone Cove": 204,
    "Aquatic Arena": 205,
    "Temple Ravine": 206,
    "Candy Canyon": 207,
    "Hollow Castle": 208,
    "Retro Rush": 209,
    "Cosmic Circuit": 210,
    "Pyro Peak": 211,
    "Trophy": 212,
}

ITEM_CLASSIFICATIONS = {
    "Seaside Factory": ItemClassification.progression,
    "Arctice Iceway": ItemClassification.progression,
    "Kabuki Peaks": ItemClassification.progression,
    "Fungal Forest": ItemClassification.progression,
    "Crossbone Cove": ItemClassification.progression,
    "Aquatic Arena": ItemClassification.progression,
    "Temple Ravine": ItemClassification.progression,
    "Candy Canyon": ItemClassification.progression,
    "Hollow Castle": ItemClassification.progression,
    "Retro Rush": ItemClassification.progression,
    "Cosmic Circuit": ItemClassification.progression,
    "Pyro Peak": ItemClassification.progression,
    "Trophy": ItemClassification.progression,
}

def create_item_with_classification(world: JetskiRushWorld, name: str) -> JetskiRushItem:
    classification = ITEM_CLASSIFICATIONS[name]
    return JetskiRushItem(name, classification, ITEM_TABLE[name], world.player)

def create_all_items(world: JetskiRushWorld) -> None:
    # To do: create the items
    pass