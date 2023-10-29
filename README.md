# tekken-move-schema: a JSON schema for Tekken moves

This JSON file defines a schema for JSON objects representing Tekken moves following the specification outlined in the
[2020-12 draft](https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-01) of the [JSON
Schema](https://json-schema.org/) published by the Internet Engineering Task Force (IETF).

## Motivation

Tekken movelists are famously long, and require a lot of experience and study to fully grasp their individual properties
to use effectively. The in-game information provided for these moves is sparse, and as of Tekken 7, requires a paid DLC
to access. The availability of accurate, up-to-date, well-structured and easily searchable information on these movelists, such as their
frame data and tracking, has historically been vital for accelerating the learning process for a player. 

This JSON file outlines a schema for representing Tekken moves as JSON objects in a flexible yet complete way to capture
all relevant information about a move. It is based on the movelist layout used by
[wavu.wiki](https://wavu.wiki/t/Movelist). Moves created as JSON objects following this schema will be able to be
ingested by third-party applications such as Discord bots (e.g., [Mokujin](https://github.com/TLNBS2405/mokujin)) or
websites (e.g., [Tekken 7 Pretty Movelist](https://mspkvp.github.io/tk7movespretty/)) to display.

## TODOs

- [ ] Include `"lead"` move information like `"inputs"`, `"target"` and `"damage"` in the object itself as an array to
  avoid having to iteratively search for the lead move ID
- [x] Represent `"target"` and `"damage"` as arrays to account for multi-hit moves e.g., Marduk qcf+1+2 (do block frames of intermediate hits of multi-hit moves matter?)
- [ ] Account for frame advantage [recovery states](https://wavu.wiki/t/Notation#Frame_advantage)
- [ ] Account for various properties typically provided as notes
  - [ ] homing
  - [ ] tailspin
  - [ ] spike
  - [ ] floor break
  - [ ] balcony break
  - [ ] having a clean hit property (effects with/without it)
  - [ ] throw break (and frame window)
  - [ ] delayable strings
  - [ ] natural hit combos, CH combos (from $n^{th}$ hit)
  - [ ] jailing from $n^{th}$ hit/block with $f$ frames of delay
  - [ ] requiring rage