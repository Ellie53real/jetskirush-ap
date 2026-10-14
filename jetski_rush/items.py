from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from worlds.generic.Rules import CollectionState
if TYPE_CHECKING:
    from .__init__ import JetskiRushWorld

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

class JetskiRushItem(Item):
    game = "Jetski Rush"

def create_item_with_classification(world: JetskiRushWorld, item_name: str, classification: ItemClassification) -> JetskiRushItem:
    return JetskiRushItem(item_name, classification, ITEM_TABLE[item_name], world.player)

def create_all_items(world: JetskiRushWorld) -> None:

    pass