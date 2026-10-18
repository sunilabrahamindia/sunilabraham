---
layout: default
title: "Simulation (Documentation)"
description: "Documentation of the background, design, development history, revisions, and future possibilities of the three simulations in The Sunil Abraham Project."
categories: [TSAP Documentation]
permalink: /tsap/simulation-documentation/
created: 2026-10-19
---

{% include documentation-notice.html %}

The **simulations** published under the Tito Dutta section of The Sunil Abraham Project (TSAP) are interactive experiments exploring artificial life, collective behaviour, and internet governance. Simulation #1 examines autonomous organisms, ecological interactions, resource competition, and emergent behaviour; Simulation #2 explores ant trail-following, pheromone feedback, and the emergence of circular movement; and Simulation #3 presents a fictional internet governance crisis in which competing public interests, technical risks, and rights must be considered.

The individual simulation pages focus on the interactive experience. This documentation provides a more detailed account of what each experiment explores and preserves the background, design decisions, and revisions that may otherwise be difficult to reconstruct later. The simulations may be revisited and modified in the future, so this page should be maintained as an evolving historical record rather than treated as a description of three permanently finished projects.

The record should distinguish confirmed facts from interpretation. Source files, Git commits, earlier versions, and related discussions should be used to establish the chronology wherever possible. If the reason for a past decision cannot be verified, it should be identified as undocumented rather than guessed.

## Overview {#overview}

### Simulation #1: Artificial Life {#s1}

[Open Simulation #1: Artificial Life](/tito/s1/)

Simulation #1 is an artificial-life experiment exploring autonomous organisms, ecology, evolution, resource competition, and emergent behaviour. Its interactive environment represents entities whose behaviour follows programmed rules, allowing their interactions to affect the wider system over time.

The experiment provides a way to observe how individual behaviour and environmental conditions can combine to produce patterns at the level of a population. Resource availability, competition, reproduction, and other modelled processes influence what happens within the simulated environment. The results depend on the rules and assumptions implemented in the model; they should not be read as a complete representation of biological life.

The development record should explain the original concept, the behaviour assigned to organisms, the role of environmental resources, and the important design choices visible in the source. It should also preserve significant future changes, including changes to the model itself and changes made only to its controls or presentation.

### Simulation #2: Ant Mill {#s2}

[Open Simulation #2: Ant Mill](/tito/s2/)

Simulation #2 is an agent-based experiment exploring ant trail-following, pheromone feedback, food sources, and the emergence of circular movement. Individual ants follow local movement rules, sense nearby trail pheromone, deposit pheromone, respond to neighbouring ants, and search for food. Under some conditions, positive feedback can reinforce a circular procession.

The experiment makes it possible to explore how group-level patterns can emerge from local interactions rather than from a central controller directing every ant. Its controls include population, randomness, pheromone evaporation, presets, and obstacles, allowing visitors to examine how the model responds to different conditions.

The model is illustrative. It does not claim that every natural ant mill forms through precisely the same mechanisms. Its results depend on the rules and simplifications used in the implementation. The development history should record the model's assumptions and mechanics, as well as later changes to behaviour, controls, explanation, or accessibility.

### Simulation #3: Internet Governance in a Crisis {#s3}

[Open Simulation #3: Internet Governance in a Crisis](/tito/s3/)

Simulation #3 is a fictional internet governance negotiation. A government asks a major online platform to restrict access to material it says could trigger violence. The evidence is incomplete, and a broad restriction could affect lawful speech, people outside the country, and access to information.

The participant facilitates a fictional multistakeholder process. Across three rounds, the participant responds to the initial request, negotiates safeguards, and makes a final decision. The available choices lead to different stakeholder responses and consequences determined by the simulation's rules.

The scenario explores tensions among public safety, freedom of expression, procedural fairness, technical risks, and accountability. It is a rule-based teaching scenario, not a prediction of a real case. Its outcomes should not be interpreted as measured probabilities or as evidence that actual governments, platforms, or civil society organisations would necessarily respond in the same way.

Simulation #3 has a particularly important development history because an earlier version used a questionnaire and scoring approach, while the current version presents a three-round negotiation. The transition should be recorded as a change in design, with the reasons and chronology supported by earlier source versions, commits, or contemporaneous discussion wherever available.

## Simulation #1: Development History {#s1-history}

### Concept and initial implementation {#s1-concept}

The current page describes Simulation #1 as an artificial-life experiment involving autonomous organisms, ecology, evolution, resource competition, and emergent behaviour. Its source page was created on 6 September 2026.

The detailed motivation behind the original design, the sequence in which its mechanics were introduced, and the reasoning behind individual choices should be added from verifiable development records. This documentation does not assume a more specific origin story than the available evidence supports.

### Design and mechanics {#s1-design}

The simulation's rules, organism behaviour, environmental interactions, and controls are part of the model and should be documented from the implementation. Future updates to this section should explain the mechanics in sufficient detail for a reader to understand what the simulation actually represents, rather than relying only on its visual appearance.

It is also important to distinguish programmed rules from emergent outcomes. A pattern observed during a run may result from interactions among rules; it should not be described as a separately programmed feature unless the source supports that description.

### Revisions and future development {#s1-revisions}

Simulation #1 may be revisited to improve its mechanics, controls, presentation, accessibility, or explanatory material. Its current version should not be treated as final.

When a substantial revision occurs, record the date, the previous behaviour or design, what changed, the reason if documented, and the outcome observed during testing. Link to the relevant commit or issue where available. If the change introduces a substantially different model, retain a clear account of the earlier approach.

## Simulation #2: Development History {#s2-history}

### Concept and initial implementation {#s2-concept}

Simulation #2 explores ant trail-following, pheromone feedback, food-seeking, and circular movement. Its source page was created on 18 October 2026.

The current page describes the central mechanisms and cautions that the model does not claim to explain every natural ant mill. More detailed statements about the original motivation or the order in which individual features were developed should be added only after checking the source history or other records.

### Movement and pheromone mechanisms {#s2-mechanics}

The current implementation describes ants sensing nearby pheromone, depositing trails, responding to neighbours, and searching for food. It includes controls for population, randomness, pheromone evaporation, presets, and obstacles.

These are substantive elements of the experiment, not merely interface decoration. When any mechanism or parameter changes, the documentation should explain what was changed and, where verifiable, how that change affects the model. It should also preserve the distinction between the simplified model and the behaviour of real ants.

### Revisions and future development {#s2-revisions}

Simulation #2 may be revised as experience with the current model suggests improvements. A revision could affect the underlying movement rules, pheromone behaviour, environmental conditions, controls, or explanatory text. The documentation should identify which part changed rather than describing every update as a general improvement.

Any future claim that a revision produces more realistic or more understandable behaviour should be supported by testing or a clearly stated rationale. Intended improvements and demonstrated outcomes are not the same thing.

## Simulation #3: Development History {#s3-history}

### Earlier questionnaire and scoring approach {#s3-questionnaire}

An earlier version of Simulation #3 used a questionnaire and scoring approach. The participant answered questions, and the responses were processed through a structured set of rules to produce an outcome.

This earlier approach is part of the experiment's history and should remain documented even though the current page uses a different interaction model. The exact details of the former questionnaire, its scoring rules, and its results should be recorded from an archived version or Git history rather than reconstructed from memory.

### Transition to a negotiation scenario {#s3-negotiation}

The current version presents the fictional internet governance dispute as a three-round negotiation.

**Round 1: Responding to the request.** The participant selects an initial response to the government's demand. The choices differ in how they address the scope of the restriction, the specificity of the order, and the need for independent review.

**Round 2: Negotiating safeguards.** The participant considers safeguards such as evidence requirements, time limits, notice, reasons, appeal mechanisms, independent oversight, and reporting.

**Round 3: Making the final decision.** The participant chooses a final course of action. The simulation then presents consequences generated by its programmed rules and records the decision.

This design makes the sequence of choices and negotiations central to the experience. The transition from questionnaire and scoring to a staged negotiation is confirmed by the development history, including the commit that introduced the current design on 19 October 2026. The precise reasoning behind every design choice should be recorded only where supported by the original discussions or other evidence.

### Further revisions {#s3-revisions}

The three-round negotiation is the current implementation, not necessarily the final one. Future revisions may change the scenario, choices, stakeholder responses, safeguards, consequences, or explanatory material.

A later redesign should be added as a new stage in the history. It should not erase the questionnaire version or the transition to the current format. The record should identify what changed, why where known, and how the new implementation differs from the previous one.

Because this is a teaching scenario, changes to the underlying rules may alter the interpretation of the experience, not just its interface. Significant changes to the model and its assumptions therefore deserve explicit documentation.

## Development Methodology {#methodology}

The three simulations address different subjects, but each translates an idea into an interactive model. Their development can involve conceptual framing, model design, implementation, presentation, testing, and revision. These activities may overlap, and testing may lead to a reconsideration of the original concept rather than merely a technical fix.

### Model design and implementation {#model-design}

The documentation should distinguish the question a simulation is intended to explore from the rules used to represent it. It should describe the entities, variables, choices, and relationships that actually appear in the implementation, without assuming that a visually plausible result is necessarily an accurate representation of the real world.

When the implementation changes, the record should make clear whether the change affects the model's rules, the user interface, the explanatory material, or more than one of these.

### AI assistance and human decisions {#ai-assistance}

Where development records establish that AI tools were used, the documentation may describe their role in drafting code, exploring alternative designs, explaining technical approaches, or assisting with revisions. It should not assume that AI was involved in every stage or attribute a particular decision to an AI tool without evidence.

A suggestion, an experimental draft, and a change adopted in the published implementation are different things. The historical record should distinguish them where relevant.

### Testing and interpretation {#testing}

A simulation can run successfully without representing every aspect of the real-world phenomenon that inspired it. Technical correctness, usefulness as an illustration, and empirical validity are separate questions.

Testing should consider whether the page behaves as intended, whether controls are understandable, whether the model's assumptions are explained, and whether visitors might mistake illustrative outcomes for predictions or factual claims. The appropriate criteria differ between artificial life, ant movement, and internet governance.

## Recording Revisions {#revision-record}

This page should be updated when a simulation undergoes a significant change to its concept, rules, interaction model, explanatory approach, or intended use. Minor maintenance changes can remain traceable through Git history without necessarily requiring a long entry here.

For each substantial revision, record the following where information is available:

- **Date:** When the change was made or committed.
- **Simulation:** Which experiment was affected.
- **Previous state:** The relevant design or behaviour before the change.
- **Change:** What was modified.
- **Reason:** Why the change was made, if documented.
- **Outcome:** What testing or observation established, distinguishing it from the intended outcome.
- **References:** Links to commits, source files, earlier versions, or related issues.

### Initial chronology {#chronology}

#### 6 September 2026: Simulation #1 {#chronology-1}

The Simulation #1 page records this creation date. It presents an artificial-life experiment exploring autonomous organisms, ecology, evolution, resource competition, and emergent behaviour.

Source: [Simulation #1](/tito/s1/).

#### 18 October 2026: Simulation #2 {#chronology-2}

The Simulation #2 page records this creation date. It presents an ant-mill experiment involving local ant movement, pheromone feedback, food sources, and circular procession behaviour.

Source: [Simulation #2: Ant Mill](/tito/s2/).

#### 19 October 2026: Simulation #3 {#chronology-3}

The current Simulation #3 page records this creation date. The Git history records a commit introducing the current three-round internet governance negotiation on 19 October 2026. An earlier questionnaire and scoring approach preceded it.

Source: [Simulation #3: Internet Governance in a Crisis](/tito/s3/).

This initial chronology records page creation and a verifiable design transition. It is not a complete history of every edit or experiment.

## Limitations and Historical Accuracy {#limitations}

This page describes the current simulations and records the development details that can be established with confidence. It does not yet provide a complete chronology of every implementation change.

The source files and creation dates provide a starting point. Earlier versions, Git commits, issue discussions, and other contemporaneous records should be consulted when adding a more detailed history.

The following principles should guide future additions:

- Do not describe an inferred reason for a change as a documented fact.
- Do not treat the current implementation as the only version that ever existed.
- Do not interpret a simulation's output as evidence about the real world beyond what its design and validation support.
- Distinguish a planned improvement from a change that has been implemented and tested.

Where the history is incomplete, the documentation should say so. A transparent record of uncertainty is more useful than a confident but unsupported explanation.

## Future Development {#future}

All three simulations may be revisited. Simulation #1 and Simulation #2 may receive new features, revised rules, or improvements to their explanatory and interactive elements. Simulation #3 may undergo another substantial redesign as experience with the current negotiation format develops.

Future work may also reveal connections between the experiments, including the relationship between local rules and collective behaviour, the importance of feedback, the role of assumptions in model design, and the difficulty of interpreting complex outcomes. These connections can support reflection without obscuring the different purposes and limitations of the three simulations.

This section should be updated when concrete development plans emerge. Potential ideas should remain distinct from work that has actually begun or been completed.

## Conclusion {#conclusion}

The simulations are interactive experiments whose present forms reflect conceptual and technical decisions. Their value lies not only in what visitors can do on the published pages, but also in the questions they make possible and the design choices through which those questions are explored.

Preserving their development history will make future maintenance and revision easier. It will help explain how earlier implementations relate to current ones, which assumptions remain in place, what was learned from testing, and which questions remain unresolved.

The purpose of this document is both practical and historical: to preserve the reasoning and evolution behind the simulations while leaving room for them to change.

{% include navbox-tsap.html %}
