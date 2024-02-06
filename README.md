# Fourthsmaster 
This learning app is intended to teach broadly three musical concepts as they apply to the guitar: the Circle of Fourths, the seven positions of the major scale on the fretboard, and more precisely the notes on the fretboard.

The app is a work in progress and it is used as a scaffolding to increasing complexity.

## Learning concepts in this app
The primary motivation for creating this version of the app, was to limit the development to the simplest terms and tools.

Tools used for this version of the app:
- FastAPI
- Jinja2 templating
- TailwindCSS
- HTML
- JavaScript (minimally)

Algorithms used in this app:
The notes on the fretboard are not a single image ...
- The "/shapes" path selects a shape randomly
- Each note has three states: fretted (black), random selection (green), random root selections (concentric circle green)
- Each "shape" is created using a list of note indexes for that shape
- All notes on the entire fretboard are indexed by constructing a **matrix**
- Likewise, "/keys" builds a shapes depending on the user's selection of musical note
- The "Draw" button generates a new random note in that key
- The "Flip" button reveals the answer to the random note highlighted

## To Do:
- Connect to a SQL server
- Add authentication
- create spaced repetition algorithm