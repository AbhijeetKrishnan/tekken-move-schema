from typing import Union, List, Tuple, Optional

import jsonschema
from pydantic import BaseModel, Field, HttpUrl

from .t7_enums import T7CharEnum, HitLevelEnum, StanceEnum, StateEnum, LimbEnum, HitStateEnum, ComboPropEnum


class WhiffRecovery(BaseModel):
    """How the character recovers after a whiffed move"""

    frames: int = Field(
        None,
        title="Recovery Frames",
        description="The number of frames of recovery",
        ge=0
    )
    stance: StanceEnum = Field(
        None,
        title="Recovery Stance",
        description="The stance the character recovers into",
    )

class State(BaseModel):
    """A state in Tekken 7

    A state is something that alters the way in which a player is hit by attacks.
    """
    # TODO: parry state (ps) should also communicate info about which moves (limbs) it parries

    state: StateEnum = Field(
        ...,
        title="State",
        description="The state abbreviation",
    )
    frames: Union[int, Tuple[int, int]] = Field(
        ...,
        title="Frames",
        description="The start frame of the state, or a tuple of the start and end frames",
    )

class AtkProp(BaseModel):
    """Properties of an attack upon its active frames connecting with an opponent"""

    onHitState: HitStateEnum = Field(
        None,
        title="On Hit State",
        description="The state in which the move hit",
    )
    damage: int = Field( # TODO: handle multi-hit moves
        None,
        title="Damage",
        description="The damage dealt by the move",
        ge=0
    )
    frameAdvantage: int = Field(
        None,
        title="Frame Advantage",
        description="The frame advantage for the attacker",
    )
    attackerRecoveryStance: StanceEnum = Field(
        None,
        title="Attacker Recovery",
        description="The stance in which the attacker recovers",
    )
    defenderRecoveryStates: List[State] = Field(
        None,
        title="Defender Recovery States",
        description="The states the defender is in after being hit",
    )
    comboProperties: ComboPropEnum = Field(
        None,
        title="Combo Properties",
        description="The combo properties of the move",
    )

class CleanHit(BaseModel):
    cleanHitRange: float = Field(
        None,
        title="Clean Hit Range",
        description="The clean hit range of the move",
    )
    onCleanHit: AtkProp = Field(
        None,
        title="On Clean Hit",
        description="The move's properties on clean hit",
    )

class T7Attack(BaseModel):
    """An attack move in Tekken 7 that has active frames"""
    # TODO: handle multi-hit moves

    hitLevel: HitLevelEnum = Field(
        None,
        title="Hit Level",
        description="The hit level of the attack",
    )
    range: float = Field(
        None,
        title="Range",
        description="The maximum range recorded of the attack hitting a Heihachi on-axis, using the \
            value from the in-game frame display. Full details here: https://wavu.wiki/t/Movelist#Range"
    )
    tracksLeft: int = Field(
        None,
        title="Left Tracking Score",
        description="The tracking score of the attack with the opponent stepping right (https://wavu.wiki/t/Tracking#Measurement)",
        ge=-6,
        le=17
    )
    tracksRight: int = Field(
        None,
        title="Right Tracking Score",
        description="The tracking score of the attack with the opponent stepping left (https://wavu.wiki/t/Tracking#Measurement)",
        ge=-6,
        le=17
    )
    startup: Union[int, Tuple[int, int]] = Field(
        ...,
        title="Startup Frames",
        description="The active frames of the attack",
        ge=1
    )
    startupStates: List[State] = Field(
        None,
        title="Startup States",
        description="The states the character is in during startup",
    )
    isHoming: bool = Field(
        None,
        title="Homing",
        description="Whether the attack is homing",
    )
    limb: LimbEnum = Field(
        None,
        title="Limb",
        description="The limb the attack hits with",
    )
    onHit: AtkProp = Field(
        ...,
        title="On Hit",
        description="The attack's properties on hit"
    )
    onBlock: AtkProp = Field(
        ...,
        description="The attack's properties on block"
    )
    onCh: AtkProp = Field(
        ...,
        description="The attack's properties on counterhit"
    )
    onCleanHit: Optional[CleanHit] = Field(
        None,
        title="Clean Hit",
        description="The attack's properties on clean hit, if any"
    )

class T7Throw(BaseModel):
    """A Tekken 7 throw"""

    hitLevel: HitLevelEnum = Field(
        None,
        title="Hit Level",
        description="The hit level of the throw",
    )
    range: float = Field(
        None,
        title="Range",
        description="The maximum range recorded of the throw hitting a Heihachi on-axis, using the \
            value from the in-game frame display. Full details here: https://wavu.wiki/t/Movelist#Range"
    )
    tracksLeft: int = Field(
        None,
        title="Left Tracking Score",
        description="The tracking score of the throw with the opponent stepping right (https://wavu.wiki/t/Tracking#Measurement)",
        ge=-6,
        le=17
    )
    tracksRight: int = Field(
        None,
        title="Right Tracking Score",
        description="The tracking score of the throw with the opponent stepping left (https://wavu.wiki/t/Tracking#Measurement)",
        ge=-6,
        le=17
    )
    startup: Union[int, Tuple[int, int]] = Field(
        ...,
        title="Startup Frames",
        description="The active frames of the throw",
        ge=1
    )
    throwBreak: str = Field( # TODO: consider making this an enum
        None,
        title="Throw Break",
        description="The throw break input",
    )
    breakWindow: int = Field(
        None,
        title="Break Window",
        description="The frames of the throw break window",
    )

class T7Unblockable(BaseModel):
    """An unblockable attack in Tekken 7"""

    hitLevel: HitLevelEnum = Field(
        None,
        title="Hit Level",
        description="The hit level of the unblockable",
    )
    range: float = Field(
        None,
        title="Range",
        description="The maximum range recorded of the unblockable hitting a Heihachi on-axis, using the \
            value from the in-game frame display. Full details here: https://wavu.wiki/t/Movelist#Range"
    )
    tracksLeft: int = Field(
        None,
        title="Left Tracking Score",
        description="The tracking score of the unblockable with the opponent stepping right (https://wavu.wiki/t/Tracking#Measurement)",
        ge=-6,
        le=17
    )
    tracksRight: int = Field(
        None,
        title="Right Tracking Score",
        description="The tracking score of the unblockable with the opponent stepping left (https://wavu.wiki/t/Tracking#Measurement)",
        ge=-6,
        le=17
    )
    startup: Union[int, Tuple[int, int]] = Field(
        ...,
        title="Startup Frames",
        description="The active frames of the unblockable",
        ge=1
    )
    startupStates: List[State] = Field(
        None,
        title="Startup States",
        description="The states the character is in during startup",
    )
    onHit: AtkProp = Field(
        ...,
        title="On Hit",
        description="The attack's properties on hit"
    )
    onCh: AtkProp = Field(
        ...,
        description="The attack's properties on counterhit"
    )

class T7Other(BaseModel):
    """Any other move that doesn't fit into the other categories"""

    startupStates: List[State] = Field( # TODO: startupStates common to all moves, so move to T7Move?
        None,
        title="Startup States",
        description="The states the character is in during startup",
    )

class T7Move(BaseModel):
    """A character's move in Tekken 7"""

    id: str = Field(
        ...,
        title="Move ID",
        description="A unique identifier for the move, typically of the form {character fullname}-{move input}"
        # TODO: include pattern validation?
    )
    character: T7CharEnum = Field(
        None,
        title="Character Name",
        description="The character's name to which this move belongs",
    )
    name: str = Field(
        None,
        title="Move Name",
        description="The move's name in the movelist"
    )
    # TODO: how to handle strings?
    # lead: 'T7Move' = Field(
    #     None,
    #     title="Lead Move",
    #     description="The ID of the lead move which precedes this move, if any",
    # )
    requiredState: StateEnum = Field(
        None,
        title="Required State",
        description="The state required for the character to be in to perform the move",
    )
    input: str = Field(
        ...,
        title="Move Input",
        description="The move's input using the style of wavu.wiki (https://wavu.wiki/t/Notation#Style)"
    )
    data: Union[T7Attack, T7Throw, T7Unblockable, T7Other] = Field(
        None,
        title="Move Data",
        description="The data associated with the move",
    )
    notes: List[str] = Field(
        None,
        title="Notes",
        description="Additional notes about the move",
    )
    animation: HttpUrl = Field(
        None,
        title="Animation URL",
        description="A URL to the move's animation",
    )
    recovery: WhiffRecovery = Field(
        None,
        title="Recovery",
        description="The move's recovery details. For attacks, throws and unblockables, it is the \
            number of frames after the last active frame. For other moves, it is the total recovery frames",
    )