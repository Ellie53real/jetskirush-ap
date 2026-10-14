from dataclasses import dataclass
from Options import *

class TrackRequirement(Range):
    """How many tracks you need to complete in order to goal."""
    display_name = "Track Requirement"
    range_start = 1
    range_end = 12
    default = 8

@dataclass
class JetskiRushOptions(PerGameCommonOptions):
    track_requirement: TrackRequirement