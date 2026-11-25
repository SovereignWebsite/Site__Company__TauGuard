# Learnings

1. Read the pages, and say how much you read. Downloading is not reading. /sources/ states it per page.
2. Two of TauGuard's own pages disagree (three decision outcomes against four). Say so; do not pick silently.
3. A stylesheet changed in place at a fixed address is served from old caches: it showed Dinis a broken picker my fresh-browser checks could not show. Version every stylesheet link (?v=hash), and give SVG thumbnails fixed width and height.
4. Before showing a design to anyone, compare its palette with the other party's own site. My first dark design echoed TauGuard's.
5. Run axe in dark mode and at 390px as well as the default; the default misses contrast and phone-layout faults.
6. The mandatory notice is a 115-character sentence: three lines at a readable phone size is the floor.
7. A generated site: edit docs/build/*.py, never the generated HTML. The SVG helper checks text widths and fails the build rather than letting text overflow.
8. A script that makes a new signing key for a name that already has a published key overwrites the published file. Read before running seeded scripts.
