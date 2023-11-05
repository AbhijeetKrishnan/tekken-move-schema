# Tekken Frame Data UI

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier) 

An attempt to create a better frontend for viewing Tekken frame data. Built using [SvelteKit](https://kit.svelte.dev/) and deployed using [Vercel](https://vercel.com/).

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
# start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

## TODO

- [ ] "Advanced" data toggle
- [ ] Improved design based on Tekken 8's visual identity
- [ ] Color coding for block frames based on safe/unsafe, and magnitude
- [ ] Icons for move properties (homing, tail spin, power crush, wall bounce, heat burst, heat smash etc.)
- [ ] Search functionality for moves
- [ ] Filters based on move properties

## Motivation

Tekken movelists are famously long, and require a lot of experience and study to fully grasp their individual properties
to use effectively. 
The in-game information provided for these moves is sparse, and in Tekken 7, required a paid DLC to access. 
The availability of accurate, up-to-date, well-structured and easily searchable information on these movelists, such as their
frame data and tracking, has historically been vital for accelerating the learning process for a player.
The fact that Tekken 8 provides this frame data in-game in the base product is a good step forward.

The Tekken community uses the following sources for frame data

- [RBNorway](https://rbnorway.org/tekken-frame-data/): Minimalist and fast, this site offers frame data for all characters in a spartan layout. Provides good search features. Lacks some advanced move information, such as wall crush properties, range, recovery, string information and tracking.
- [Geppopotamus](https://geppopotamus.info/game/tekken7fr/index_en.htm): The Japanese counterpart to RBNorway (an EN version is available). It is more comprehensive and detailed than RBNorway, and is authoritative enough to usually be the seed for other frame data services. However, the layout leaves something to be desired. The choice to use button notation instead of the community [Tekken input notation](https://wavu.wiki/t/Notation) is unorthodox.
- [Mokujin](https://github.com/TLNBS2405/mokujin): A Discord bot that serves up frame data when queried in a server. It includes links to move gifs compiled by the[T7Chicken](https://github.com/TekkenChicken) project. Relies on data from RBNorway and Geppopotamus.
- [Wavu Wiki](https://wavu.wiki/t/Main_Page): An *extremely* comprehensive collection of frame data which includes almost anything you'd want to know about a move. It does a valiant job of trying to present this data in a stylized table, but it falls short on readability. Being a MediaWiki, it is easy to contribute to it, and as such, has the potential for being *the* most authoritative source of Tekken frame data.

I'd like to experiment with a different layout that incorporates the same data as Wavu Wiki but provides a frontend that is easier to read and more intuitive.