Prototype Math Textbook — Cursor Instructions

Build a simple HTML/JavaScript prototype math textbook from:

read_with_chatgpt/ops_math_7_9_S1_S6_matrix.json

Use the JSON as the source of truth. Each row becomes exactly one mini-chapter.

Goal

Create a textbook for almost everyone, especially pupils who are not naturally confident or interested in mathematics.

Each mini-chapter should explain one idea only, as clearly, concretely, and briefly as possible.

Do not add exercises yet.

Mini-chapter structure

For every JSON row, present content in this exact order:

WordsExplain the idea in plain everyday language. Avoid curriculum jargon unless the term itself must be learned. Keep this short.

Illustration

Insert a placeholder description in square brackets, e.g.[Illustration: a thermometer showing +5 °C and -7 °C, with the distance to zero highlighted.]

Example + theoryStart from a concrete, relatable example and use it to reveal the mathematical rule or theory.Prefer the row's application and example fields. Use theory only to explain what is genuinely needed.

Writing rules

One row = one mini-chapter.

One main idea per mini-chapter.

Make every explanation understandable without assuming mathematical enthusiasm.

Prefer concrete situations before abstraction.

Use short sentences and ordinary words.

Explain symbols when they first appear.

Never hide a simple idea behind formal terminology.

Avoid excessive background, history, side notes, caveats, or motivational waffle.

Do not introduce concepts that belong to another row unless absolutely necessary.

Do not invent harder mathematics than the JSON row requires.

Preserve the Finnish mathematical term as the chapter title or visible key term.

The explanatory prose may be in clear Finnish unless otherwise specified.

Interface

Create a lightweight browser-based textbook using plain HTML, CSS, and JavaScript.

Requirements:

Read the JSON file dynamically.

Group mini-chapters under S1–S6.

Show the content area name.

Provide simple navigation between mini-chapters.

Keep typography spacious and highly readable.

Keep visual design simple; content clarity matters more than polish.

Illustration placeholders should be visually distinct so they can later be replaced by generated or drawn artwork.

Important

This is a content prototype, not a complete textbook.

Do not add:

exercises

quizzes

answer fields

gamification

teacher material

assessment criteria

T1–T20 mappings

extra curriculum interpretation

First make the 90 mini-chapters clear, concise, relatable, and internally consistent.