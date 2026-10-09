# Continue next time — Intelligent Robotics

Last updated: 2026-10-09. Document version: **0.2**.

## Goal and user preferences

Maintain **one concise study PDF in English**, written in LaTeX, progressively integrating new lectures with the corresponding available Murphy passages. Keep the terminology from the course. Condense repeated slides and catalogues while preserving definitions, physical principles, distinctions, reasoning and worked examples needed for exam answers.

The user supplied old-exam questions as a coverage checklist. These include later topics; **do not present the current first-lecture notes as preparation for the whole exam**. A screenshot labeled “GOOD” is an example of the assessment style, not an authoritative source or a guarantee that its answer is complete.

## Repository and build

- Actual location: `/mnt/ssd/Intelligent Robotics`, on the drive labeled `ssd ale`.
- Desktop location: `/home/marti/Desktop/Intelligent Robotics`, a symlink to the SSD repository.
- Stable deliverable: `output/pdf/intelligent-robotics-notes.pdf`.
- Main source: `latex/main.tex`; topics: `latex/chapters/`.
- Build: `python3 scripts/build.py` (or `make pdf`).
- Tectonic 0.17.0 is in `.tools/`. Compiler downloads, cache, temporary files and previews must remain inside the SSD repository. Do not install a large TeX distribution on the internal disk.
- Read `AGENTS.md`, `README.md`, `LESSONS.md` and `COVERAGE_AUDIT.md` before changing coverage.
- A local commit is prepared for pushing to `origin` (`git@github.com:Martinioini/Intelligent-Robotics.git`), branch `main`. No remote push has been performed.
- Git includes the LaTeX/build sources, notes PDF, documentation and exam screenshots. Original slide/book PDFs remain local and ignored; `Material/README.md` is the versioned input inventory.

## Material currently available

Only three slide sets: S02 (32 PDF pages), S03 (27), S04 (30), totaling 89 slides. The Murphy PDF is **the 2000 edition, first 124 PDF pages**, ending at printed p. 103. Its body contains the Part I overview and Chapters 1–3. Later chapter titles occur in the table of contents but their bodies are absent. The 2019 edition credited by a slide is not supplied.

Slide references use one-based PDF pages. Book references use printed pages; for the numbered body in this extract, PDF page = printed page + 21. S03 and S04 have older A.Y. 2024–25 cover labels; identify them by the supplied filenames.

No separate lecture-note file has been found in `Material/`; the available supplementary notes are the Murphy extract and the generated LaTeX study notes.

## Work completed in the second audit

- Rechecked all slide text and visually reviewed all 89 slides, including diagrams containing text absent from extraction.
- Compared the notes with book objectives, explanations, summaries and relevant exercises in the available introduction and Chapters 1–3.
- Added missing introductory book material: Murphy's intelligent-robot wording; DOF, kinematics/dynamics, teach pendant, AGV; teleoperation suitability and predictive displays; three D's and adoption issues.
- Strengthened STRIPS with means–ends analysis, difference table/evaluator, failed preconditions, subgoals and a two-room example.
- Expanded NHC/RCS and the four architecture evaluation criteria; clarified that NHC need not repeat all planning after each sensor update.
- Added a clearly labeled book supplement for computational theory, behavior categories/acquisition, IRMs/releasers, inhibition and concurrency, action–perception cycle, schema theory, and limitations of biological transfer. It is available book material, not a claim that these details were all in S04.
- Added revision questions for those foundations. There are now 21 model-answer questions.
- Preserved all five supplied screenshots in `exam-examples/` so that future sessions do not depend on `/tmp` clipboard files.
- Recorded pending exam topics below and the exact source-to-notes audit in `COVERAGE_AUDIT.md`.

## Final verification of version 0.2

The regenerated PDF has **20 pages** and **21 revision questions**. Tectonic compilation completed with no warnings, including no overfull/underfull boxes. All 20 final pages were rendered and visually inspected. English terminology, source-map rows, question count and persistent screenshot links were checked. Generated review images and extracted text were removed after verification.

## Old-exam checklist — all detailed answers still pending

| ID | Question supplied by user | Current status / what to add |
| --- | --- | --- |
| EX01 | Explain commonalities and differences between sonar, lidar and radar. Start with their physical principles. | Sensor vocabulary only. Need emitted signals, ranging principle, equation/assumptions, differences, limitations and use cases. [Screenshot](exam-examples/01-sonar-lidar-radar.png). |
| EX02 | Define an active sensor. Give four examples used in mobile robotics. | Active **perception** is explained; active sensor hardware is not. Need active/passive classification with four unambiguous examples. [Screenshot](exam-examples/02-active-sensors.png). |
| EX03 | Explain construction of tactile skins; illustrate basic elements and their connections. | Absent. Need the specific taught sensing mechanism, layered structure, sensing cells and electrical/readout connections. [Screenshot](exam-examples/03-tactile-skins.png). |
| EX04 | Define configuration space (C-Space) and explain how it is calculated. | DOF terminology is only a prerequisite. Need configuration variables, C-free/C-obstacle, collision test and a worked construction. [Screenshot](exam-examples/04-configuration-space.png). |
| EX05 | Explain SLAM and describe fundamental concepts and algorithms. | Localization/mapping mentioned only. Need joint estimation, uncertainty, data association, algorithm families and worked explanation. [Screenshot](exam-examples/05-slam.png). |
| EX06 | Explain subsumption architecture. | Reactive paradigm, inhibition and behavior composition covered. **Subsumption itself is not**; need layers, suppression/inhibition wiring, example and tradeoffs. Murphy Ch. 4 is outside this extract. |
| EX07 | Messages, services, actions. | Absent. Confirm which ROS version is taught; add communication patterns, examples, feedback/cancellation and selection criteria from course material. |
| EX08 | Observation model and action model in SLAM. | Absent in detail. Need variable definitions, probabilistic/equation forms, noise and prediction/update roles. |
| EX09 | Synchro drive. | Absent. Need wheel layout, coordinated steering/driving, body orientation and kinematic consequences. Preserve course spelling. |
| EX10 | “Kalman filter is for linear stochastic equations.” | User's closed-question cue, not a fully checked answer. Need exact model assumptions, noise assumptions, predict/update equations and distinctions from EKF/other variants. |
| EX11 | Event cameras. | Absent. Need what an event records, acquisition timing, differences from frame cameras and limitations. |
| EX12 | Collision-detection sensor: bumper. | User's expected closed-answer cue saved. Need sourced bumper/contact explanation and distinction from pre-contact obstacle detection. |
| EX13 | What is an IMU used for? | Absent. Need measured quantities, orientation/motion estimation role, limitations and relation to localization. |

The current material does **not** justify marking any of these 13 detailed exam topics complete. Do not convert “term mentioned” into “exam answer covered”.

## Checks when adding the pending topics

- Treat screenshot answers as student examples; some images are cropped and no complete answer should be reconstructed from hidden text.
- For ranging sensors, check which measurement method the lecture actually teaches rather than assuming every device measures a returned pulse time in exactly the same way. Explain the relevant wave propagation speed and units.
- For active-sensor examples, check infrared motion-sensor classification rather than copying the screenshot's example without qualification.
- For tactile skins, identify the transduction mechanism before presenting one layer construction as universal.
- For C-space, the screenshot gives a partition but the question also asks **how to calculate it**. Provide the taught collision-space construction, not just a definition.
- For SLAM, cover algorithms and both models; the visible definition in the screenshot does not satisfy the whole question.
- For closed questions, save both the correct choice and a one-sentence explanation, with any necessary assumptions.

## Next-session procedure

1. Inventory `Material/` for new PDFs or notes and read their contents, including diagrams.
2. Read the corresponding **available** book sections. If the user supplies new course slides but no corresponding book chapter, use the slides and make the source limit explicit.
3. Extend existing topics or create a new chapter. Maintain English and course terminology. Add physical principles, equations/variable definitions, comparisons and a worked example when the question requires them.
4. Resolve the matching EX IDs only after a complete sourced answer is in the PDF; record section and reading anchors. Keep unaddressed topics pending.
5. Update `LESSONS.md`, `COVERAGE_AUDIT.md`, this file, the PDF scope/version/date and source map. Check the “How to study” section references after adding a chapter.
6. Run `python3 scripts/build.py`, inspect `output/pdf/main.log`, render the changed PDF pages with `pdftoppm` into `tmp/pdfs/`, and visually inspect tables, equations, diagrams, headers and page breaks. Remove generated previews after verification.
7. Deliver the same PDF path and briefly report additions and remaining gaps. Do not claim future exam completeness or invent missing course content.
