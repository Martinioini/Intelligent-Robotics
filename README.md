# Intelligent Robotics

A single, concise study PDF in **English**, based on the supplied course slides and the corresponding available sections of Robin R. Murphy, *Introduction to AI Robotics* (2000). Terminology follows the slides and book.

**Read:** [Consolidated study notes](output/pdf/intelligent-robotics-notes.pdf)

Current coverage: slide sets **02, 03 and 04**. Definitions and examples are organized by topic; repeated slides and product/market catalogues are condensed. Each topic has source reading anchors. Revision questions include concise model answers. Version 0.3 also includes a clearly labeled supplement for the available book Chapter 3 foundations and the slide-specific terminology, examples and Murphy objectives added in the third audit.

## Get the repository

```sh
git clone https://github.com/Martinioini/Intelligent-Robotics.git
```

## Build

```sh
cd Intelligent-Robotics
python3 scripts/build.py
```

Or run `make pdf`. The stable output is `output/pdf/intelligent-robotics-notes.pdf`.

On a fresh Linux x86_64 checkout, download the pinned Tectonic 0.17.0 compiler and build:

```sh
python3 scripts/build.py --install-compiler
```

This downloads the pinned compiler from the official Tectonic GitHub release and builds the document. The first build needs network access for TeX resources. `.tools/`, `.cache/` and `.tmp/` stay **inside this repository**, avoiding a large TeX installation on the internal disk. They are ignored by Git. On other platforms, install Tectonic on PATH, then run the normal build command. The LaTeX source can also be compiled with a standard TeX distribution. The included PDF can be rebuilt without the original slide/book PDFs, because the notes do not import source pages.

## Structure

- `Material/`: local reference PDFs, excluded from Git; the versioned [inventory](Material/README.md) identifies the source files.
- `latex/main.tex`: typography, scope, table of contents and chapter inclusion.
- `latex/chapters/`: editable English notes grouped by topic.
- `scripts/build.py`: reproducible build with compiler cache and temporary files on the repository disk.
- `output/pdf/`: one current consolidated PDF, intended to be versioned.
- `LESSONS.md`: coverage and source map.
- `COVERAGE_AUDIT.md`: double-check of all supplied slide groups and available book concepts.
- `CONTINUE.md`: persistent handoff with all 13 old-exam prompts, their pending status and the next-session procedure.
- `exam-examples/`: preserved screenshots supplied by the user.

Read [the continuation handoff](CONTINUE.md) and [the coverage audit](COVERAGE_AUDIT.md) before adding future lessons. The old-exam checklist includes later topics that are not yet taught in the supplied material.

## Add the next lesson

1. Place the new slides in `Material/slides/` and any additional book extract in `Material/Books/`.
2. Read the lesson and the corresponding available book passages. Extend an existing topic or add a numbered `.tex` chapter under `latex/chapters/`.
3. Preserve English source terminology. Merge repeated definitions, explain missing links and label any added examples. Do not summarize unavailable textbook chapters from their titles alone.
4. Add reading anchors using one-based PDF page numbers for slides and printed page numbers for the book. Update `LESSONS.md`, the scope/version/date in `latex/main.tex`, and the source map chapter.
5. If adding a chapter, insert its `\input{chapters/...}` in `latex/main.tex`.
6. Run `make pdf`, check the compiler log and visually inspect the updated pages. Keep the PDF filename stable.

## Source limits

The supplied Murphy extract ends at printed p. 103; it is not the complete book. The 2019 second edition cited in one slide is not supplied. Slide sets 03 and 04 carry older cover labels. References in the notes identify the exact supplied sets. No unseen lessons or exam syllabus have been inferred.

The original reference PDFs remain local. The repository versions the LaTeX source, build script, study PDF, documentation and supplied exam screenshots.
