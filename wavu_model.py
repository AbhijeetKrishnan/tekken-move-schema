from pydantic import BaseModel


class WavuMove:
    id: str
    name: str
    input: str
    parent: str
    damage: int
    target: str
    reach: float
    tracksLeft: int
    tracksRight: int
    startup: int
    recv: int
    tot: int
    crush: str
    block: int
    hit: str
    ch: str
    notes: str