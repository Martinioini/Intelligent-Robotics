# Coverage audit — version 0.2

Checked 2026-10-09 against all 89 supplied slide pages (text and visual diagrams), the available Murphy introduction and Chapters 1–3, and the current LaTeX notes. This is a **conceptual coverage audit**, not a transcription of every figure, historical story, end note or exercise solution. Source originals are unchanged.

## Slide-to-notes map

All references below use **PDF page numbers**. Covers, divider slides and repeated diagrams are accounted for but do not require duplicate paragraphs.

| Source pages | Content | Destination / result |
| --- | --- | --- |
| S02 1, 4–5 | Cover and definition prompts | Scope; foundations introduction |
| S02 2–3 | Robotics, perception/action, historical development | Foundations; evolution |
| S02 6–7 | Robot etymology and course ISO definition | Robot, robotics and intelligent robot |
| S02 8–9 | Sensors, information processing, actuators and disciplines | Fundamental elements |
| S02 10–14 | Field/service robotics; rover, rescue, domestic and medical examples | Taxonomy, field/service distinction and examples |
| S02 15–19 | Education/domestic/personal robots, humanoids/androids and transport | Applications condensed; form distinguished from autonomy |
| S02 20–23 | Mobile/manipulation and autonomous/teleoperated taxonomy | Independent taxonomy dimensions |
| S02 24–29 | One loop across domains; sensing, localization, mapping, motion | Sense–Plan–Act; diagram/function examples |
| S02 30–31 | Classical AI versus embodied intelligent behavior | Intelligent robot and paradigm distinctions |
| S02 32 | Human in the loop; interpret versus execute commands | Shared intelligence; collaboration versus hybrid architecture |
| S03 1–3, 10 | Cover, divider and collaborative paradigm repeat | Scope; evolution/collaboration |
| S03 4–6 | Industrial revolutions; enabling Industry 4.0 technologies | Industrial revolutions and six technology groups |
| S03 7–9, 13–14 | Dark factories versus human–robot work | Collaboration and social/organizational implications |
| S03 11–12 | Collaborative manufacturing; Industry 5.0 | Shared task; human-centric/sustainable/resilient distinction |
| S03 15–16, 21–22, 25 | Historical branches, Unimation/Unimate, AI and Shakey | Historical pressures and milestone table |
| S03 17–20, 24 | Performance demonstration and industrial/service market plots | Examples condensed; market counts intentionally omitted |
| S03 23, 26–27 | Autonomous example, cobots, humanoid interest and barriers | Collaboration/autonomy/form distinction; application limitations |
| S04 1–4 | Autonomy prompts, self-governing, bounded rationality | Automation versus autonomy; scope and limits |
| S04 5–7 | Tool versus agent; examples; CWA | Definitions, comparisons and CWA examples |
| S04 8 | Greenfield/brownfield | Dedicated comparison |
| S04 9–12 | Monkey/banana toy world; open world | Model assumptions and toy planning example |
| S04 13–18 | Plans/actions/models/representation balances | Comparison table and continuum explanation |
| S04 19–25 | Architecture prompt; deliberative/reflex analogy; hierarchical/reactive | Architecture distinctions and Sense–Plan–Act/Sense–Act |
| S04 26–28 | Perception to symbols; interfacing; time horizons; BDI/common ground | Hybrid layers, interface difficulties and interaction |
| S04 29–30 | Hybrid diagrams and Plan, Sense–Act behavior activation | Hybrid organization and execution/replanning example |

## Book-to-notes map

References below use **printed book pages**, not PDF indices. In the body, add 21 to obtain the PDF index.

| Available material | Essential content checked | Result after audit |
| --- | --- | --- |
| Part I pp. 2–11 | Intelligent robot, paradigm/primitives, sensing organization, architectures and four evaluation criteria | All concepts represented. Evaluation criteria added. |
| Ch. 1 §§1.1–1.3, pp. 13–19 | AI versus engineering emphasis, seven AI contributions, applications, three D's, social implications | Foundations/evolution expanded with three D's and adoption context. |
| Ch. 1 §1.4, pp. 19–28 | Telemanipulation; manipulators/AGVs; DOF, control, kinematics/dynamics, teach pendant; industrial/space branches | Concise introductory definitions added; anecdotes/obsolete performance numbers condensed. |
| Ch. 1 §1.5, pp. 28–34 | Telesystem components, delays/fatigue, telepresence, suitability conditions, shared/traded control | Six suitability conditions and predictive-display role added. |
| Ch. 1 §§1.6–1.7, pp. 34–37 | Seven AI areas and chapter synthesis | Represented in AI table and revision. |
| Ch. 2 §§2.1–2.2, pp. 41–52 | Hierarchical organization, world model, STRIPS/MEA, difference table/evaluator, predicates, recursive subgoals and state updates | Expanded with source-aligned two-room worked reasoning. |
| Ch. 2 §2.3, p. 53 | CWA, open world, frame problem and tractability | Covered; narrow frame formulation distinguished from Murphy's broad discussion. |
| Ch. 2 §§2.4–2.7, pp. 54–63 | NHC/RCS/NASREM, interleaving, architecture criteria, latency, uncertainty and programming implications | Roles and conditional replanning expanded; reuse/latency/uncertainty preserved. Historical language/tool anecdotes condensed. |
| Ch. 3 §§3.1–3.3, pp. 67–83 | Computational theory, behavior types/acquisition, IRM, releasers, internal state, chaining, concurrency/inhibition | Previously missing foundations added in a clearly labeled book supplement. |
| Ch. 3 §3.4, pp. 83–91 | Action–perception cycle, releaser versus guide, active perception, affordances, optic flow, recognition | Existing architecture explanation expanded; active perception distinguished from hardware classification. |
| Ch. 3 §§3.5–3.7, pp. 91–100 | Schema/instantiation, motor/perceptual schema, composition, rana computatrix, emergence and transfer limitations | Added with compact definitions, a composition example and failure case. |
| Exercises/end notes, pp. 37–40, 63–65, 100–103 | Prompts, historical notes, references | Used to check concept readiness. No claim to reproduce every exercise, programming task or historical note. |
| Front matter and later TOC entries | Book identification and unavailable chapters | Scope recorded; chapter titles alone do not count as available content. |

## What the audit changed

The original version covered the supplied slides at a conceptual level, but selected too little from available book Chapter 3 and compressed some Chapter 2 mechanisms excessively. Version 0.2 closes those **available-source** gaps. Twenty-one revision questions cover the included foundations. Mixed automation/autonomy balances are now explicit.

The source map in the PDF differentiates slide coverage from book-only integration. Product catalogues, repeated imagery, market counts and tangential historical details remain condensed rather than omitted silently as missing technical coverage.

## Exam scope

There are 13 supplied exam prompts/cues, recorded individually in `CONTINUE.md`, with the five screenshot originals stored under `exam-examples/`. **No detailed later-topic answer is marked complete.** Sensor physics, tactile construction, C-space, SLAM, subsumption architecture, ROS communication, synchro drive, Kalman filtering, event cameras, bumpers and IMUs require subsequent material. The current PDF explicitly states this boundary.

“Reactive paradigm” is not a complete answer to “subsumption architecture”; “localization and mapping” is not a complete SLAM answer; “sensor” or “active perception” is not a complete active-sensor definition.

## Validation

The PDF is rebuilt from the LaTeX source with the repository build script. Version 0.2 produces **20 pages**, with **21 revision questions**. Compilation completed with zero warnings. All final pages were rendered and visually inspected; source-map rows, terminology, question count and handoff links were verified. Coverage claims here concern the source scope above, not the entire final-exam syllabus.
