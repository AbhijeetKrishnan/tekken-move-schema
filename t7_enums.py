from typing import List
import enum


class T7CharEnum(enum.StrEnum):
    # TODO: alternate names to call the enum? e.g., maven instead of master_raven
    akuma = "Akuma"
    alisa = "Alisa"
    anna = "Anna"
    armor_king = "Armor King"
    asuka = "Asuka"
    bob = "Bob"
    bryan = "Bryan"
    claudio = "Claudio"
    devil_jin = "Devil Jin"
    dragunov = "Dragunov"
    eddy = "Eddy"
    eliza = "Eliza"
    fahkumram = "Fahkumram"
    feng = "Feng"
    ganryu = "Ganryu"
    geese = "Geese"
    gigas = "Gigas"
    heihachi = "Heihachi"
    hwoarang = "Hwoarang"
    jack_7 = "Jack-7"
    jin = "Jin"
    josie = "Josie"
    julia = "Julia"
    katarina = "Katarina"
    kazumi = "Kazumi"
    kazuya = "Kazuya"
    king = "King"
    kuma = "Kuma"
    kunimitsu = "Kunimitsu"
    lars = "Lars"
    law = "Law"
    lee = "Lee"
    lei = "Lei"
    leo = "Leo"
    leroy = "Leroy"
    lidia = "Lidia"
    lili = "Lili"
    lucky_chloe = "Lucky Chloe"
    marduk = "Marduk"
    master_raven = "Master Raven"
    miguel = "Miguel"
    negan = "Negan"
    nina = "Nina"
    noctis = "Noctis"
    paul = "Paul"
    shaheen = "Shaheen"
    steve = "Steve"
    xiaoyu = "Xiaoyu"
    yoshimitsu = "Yoshimitsu"
    zafina = "Zafina"

class HitLevelEnum(enum.StrEnum):
    high = "h"
    mid = "m"
    low = "l"
    special_mid = "sm"

class StanceEnum(enum.StrEnum):
    """A stance is anything that changes which moves can be done"""

    n = "n" # neutral

    ss = "SS" # side step
    r = "R" # rage
    wr = "WR" # while running
    fc = "FC" # full crouch
    ws = "WS" # while standing
    bt = "BT" # back turned
    j = "J" # jumping
    otg = "OTG" # on the ground

    fuft = "FUFT" # face up feet towards
    fufa = "FUFA" # face up feet away
    fdft = "FDFT" # face down feet towards
    fdfa = "FDFA" # face down feet away

    cd = "CD" # crouch dash
    har = "HAR" # Harrier
    hmt = "HMT" # Hermit

    # TODO: character-specific stances

class StateEnum(enum.IntEnum):
    hc   = enum.auto() # high crush
    lc   = enum.auto() # low crush
    a    = enum.auto() # airborne (floating)
    pc   = enum.auto() # power crush
    ps   = enum.auto() # parry state TODO: this needs to include more details
    ra   = enum.auto() # rage armor
    ar   = enum.auto() # armor
    s    = enum.auto() # standing
    i    = enum.auto() # invulnerable
    tech = enum.auto() # can tech (tech window)

class LimbEnum(enum.IntEnum):
    la = enum.auto()  # "left arm"
    ra = enum.auto()  # "right arm"
    ll = enum.auto()  # "left leg"
    rl = enum.auto()  # "right leg"
    k = enum.auto()   # "knee"
    h = enum.auto()   # "head"
    s = enum.auto()   # "shoulder"
    b = enum.auto()   # "belly"
    e = enum.auto()   # "elbow"
    w = enum.auto()   # "weapon"

class HitStateEnum(enum.StrEnum):
    n = "n" # normal hit
    ch = "CH" # counter hit
    cl = "CL" # clean hit (but not CH)

class ComboPropEnum(enum.IntFlag):
    splat = enum.auto() # wall splat
    screw = enum.auto() # tailspin
    tornado = enum.auto()
    spike = enum.auto()
    fb = enum.auto() # floor break
    bb = enum.auto() # wall/balcony break