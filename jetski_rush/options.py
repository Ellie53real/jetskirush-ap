from dataclasses import dataclass
from Options import *

class TrackRequirement(Range):
    """How many tracks you need to complete in order to goal."""
    display_name = "Track Requirement"
    range_start = 1
    range_end = 12
    default = 8

class TimeTrials(Toggle):
    """Whether or not to enable checks for finishing tracks with certain time limits."""
    display_name = "Time Trials"
    default = 0

@dataclass
class JetskiRushOptions(PerGameCommonOptions):
    track_requirement: TrackRequirement
    time_trials: TimeTrials