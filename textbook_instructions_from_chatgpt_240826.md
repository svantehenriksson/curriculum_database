Prototype Math Textbook — Cursor Instructions

Build a simple HTML/JavaScript prototype math textbook from:

read_with_chatgpt/ops_math_7_9_S1_S6_matrix.json

The JSON is the source of truth. One row = one mini-chapter = one new idea.

Audience and principle

Write for almost everyone, including pupils who do not naturally “get” mathematics.

Assume the reader is intelligent but may be confused, uninterested, or missing the intuition that makes the formal rule seem obvious.

The main design rule is:

Question/need → words → image → concrete example → symbol/rule

Never begin with a formula when the idea can be understood first.

Every mini-chapter

1. Why / Words

Start with the question the concept answers or the problem it solves.

Explain the idea in a few plain sentences. Give the reader a mental hook. Use the Finnish mathematical term, but do not hide the idea behind terminology.

2. Illustration

Add one square-bracket placeholder that makes the idea visible:

[Illustration: ...]

The picture should explain something, not merely decorate the page.

3. Concrete example → theory

Use a natural concrete example, preferably based on the row's application and example.

Work through it simply. Only after the idea is visible and understandable, state the general mathematical rule/symbolism from theory.

If there is no honest everyday application, use a clear mathematical or geometric example instead. Never invent fake teenage relatability.

Writing rules

One new idea at a time.

Why before how.

Language before image before symbol.

Keep cognitive load low.

Short, precise prose; no waffle.

Explain symbols when they first appear.

Prefer ordinary situations where the mathematics genuinely matters.

Do not manufacture stories, characters, slang, jokes, “challenges”, or fake enthusiasm to sound young.

Write like a patient person thinking alongside the pupil, not lecturing.

Anticipate the most tempting misunderstanding when it genuinely helps, and explain why it is tempting.

Each mini-chapter should leave one memorable mental hook.

Do not introduce harder mathematics than the row requires.

Preserve the Finnish mathematical term as the title/key term.

Write the explanations in clear Finnish.

Example of desired reasoning style

For percentage change, do not start with a formula.

Start with something like:

“A price rises from €50 to €60. The change is €10. But is €10 a big increase? That depends on what the price was to begin with.”

Then make the comparison visible, work through 10/50 = 1/5 = 20%, and only then generalize:

percentage change = change / original value × 100%

The example should create the need for the mathematics rather than being bolted onto a rule afterward.

Interface

Plain HTML, CSS and JavaScript.

Load the JSON dynamically.

Group chapters under S1–S6 and show the content-area name.

Simple previous/next navigation.

Spacious, highly readable typography.

Make illustration placeholders visually distinct.

Content clarity matters more than visual polish.

Not yet

Do not add exercises, quizzes, answer fields, gamification, teacher material, assessment criteria, T1–T20 mappings, or extra curriculum interpretation.

First make the 90 ideas exceptionally clear.