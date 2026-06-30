# Prove, Don't Persuade
## Why Proof Beats the Demo in Applied AI

**Author:** Michael Borck
**Status:** Chapter outline / proposal (working title)
**Planned format:** Open-access Quarto book, Markdown sources, renders to HTML + PDF + EPUB.

**Tagline:** *Anyone can demo AI. The edge is proving it works.*

**Companion case site:** Tessera — a fictional Australian managed-cloud company, presented as a living site at **tessera.locoensayo.org**.

---

## 1. Why this book

This is a readable, opinionated spine for applied AI. Its premise is that in an age of polished AI demos, the practitioner's edge is no longer *building* something that looks impressive; it is **proving, with evidence, that a solution actually works**, and knowing where it breaks. The book is where that discipline lives.

The book is **standalone**. It is built around one case company — **Tessera** — that the reader builds for and evaluates across twelve chapters. Where the book's path happens to align with a classroom or a course, that is a happy coincidence: the methods a reader learns here transfer to any applied-AI setting, including formal study.

---

## 2. The premise: evidence is the moat

The book takes a deliberately pragmatic stance on AI (neither alarmist nor utopian) and lands it on the practitioner's desk.

**The commoditisation argument.** Building a demo (a classifier, a RAG chatbot, an agent) is exactly the kind of work generative AI is rapidly commoditising. If the only thing you do is *produce* the demo, you have no edge.

**The variation argument (the human moat).** The edge comes from variation: human judgement about *whether it works, for whom, and under what conditions*. That judgement shows up as **evaluation**: stating a threshold, measuring against it honestly, naming who it fails for, and deciding how much a human must stay in the loop. The machine produces the demo; the practitioner supplies the proof.

**From builder to evaluator.** As AI shifts from chatbots to agentic systems that act on their own, the practitioner's job changes: from maker of slick prototypes to **expert evaluator** of AI-generated work.

**Augmentation, not automation.** Use these tools for human augmentation, not passive automation that atrophies the judgement the profession depends on. Efficiency is not the goal; *defensible, evidence-based confidence* is.

This premise is the thread that runs through every chapter. The book's spine is stated up front: **prove, don't persuade.**

---

## 3. Design principles

1. **"Prove, don't persuade" as the spine.** Stated in the introduction and enacted in every chapter: every claim about an AI solution is an assertion until evidence supports it.
2. **One case company throughout.** **Tessera** (Australian managed cloud + multi-tenant SaaS) runs through the book: every concept lands on a concrete artefact. Tessera is fictional but exists as a living companion site, so readers who learn by exploring can go deeper (Appendix E).
3. **AI as a first-class topic, integrated not appended.** Every chapter carries recurring features (below): one on *using* AI as a thinking partner, one on the **trust-tool placement** that is the book's spine.
4. **No-code floor, power-user ceiling.** Every hands-on activity has a no-code **Core** path (equity — same capability for every reader) and an optional **🔬 Power-user extension** (depth for readers who want it). Appendix F is the toolkit quick-start.

---

## 4. Recurring features

Every chapter includes:

- **🤖 Conversation Log**: AI used as a thinking partner for *this* chapter's task, with a worked example against Tessera. Crucially, where the AI got it wrong and the practitioner corrected it.
- **📍 Trust-tool placement**: where this chapter's output sits on the Average/Precise × Small/Large grid, and what that means for human oversight.
- **🌐 Tessera Case**: the concrete Tessera artefact that anchors the chapter (the no-code **Core** hands-on).
- **🔬 Power-user extension**: an optional deeper take on the chapter's hands-on work (measurement, a second model, self-hosting, a touch of code).
- **🔍 Go deeper**: one to three curated external resources (paper, podcast, video) for currency and breadth.

Plus standard callouts: **Watch out** (yellow) for traps that look right but aren't; occasional **Key idea** and **Try this**.

---

## 5. Chapter outline

Two acts: **Foundation** (build the base) and **Build and Prove** (does it actually work?).

### Front matter

**Introduction: The Proof Mindset**
What "applied AI that works" actually means; why "does it work?" is a different question from "is it impressive?"; the trust tool introduced; the *prove, don't persuade* principle stated; the book's AI stance laid out in full; the no-code-floor / power-user-ceiling explained; the Tessera case site introduced.

### Part I: Foundation: what changed, and for whom

**Chapter 1: What changed?** The three AI paradigms (narrow / general / agentic); multimodality; the direction of change; first contact with the local stack; the trust tool introduced.
**Chapter 2: For whom?** Cultural and regional variation in AI; who the average optimises for; first-mover pressure; the equity argument for local AI.
**Chapter 3: Can you tell?** Detecting bias and shadow systems; the Delegation Trap; rubber-stamping as failure; prompt injection and adversarial inputs.
**Chapter 4: What's in the data?** Pattern recognition; clustering; classical ML in Orange; when analysis is average vs precise. *(Grounded in `tessera-customer-data.csv`: satisfaction and tenure dominate churn; a split is a correlation, not a cause.)*
**Chapter 5: What are you giving up?** Deployment models (cloud / VPS / local); tokens vs subscriptions; data sovereignty; model selection. *(Tessera's third-party model vendor is the cross-border tension.)*
**Chapter 6: Whose data is it?** Privacy-by-design; PII and re-identification; the Privacy Act and international frameworks. *(Grounded in Tessera's quasi-identifier collapse and its own breach.)*

### Part II: Build and Prove: does it actually work?

**Chapter 7: Are you asking well?** RTCF; prompt chaining; the harness (prompt / retrieval / tool / inference layers); the folder-based architecture; building rough RAG before meeting the polished version.
**Chapter 8: What is it saying?** Clustering and sentiment; NLP on customer feedback; where the lexicon silently fails. *(Grounded in `tessera-support-data.csv`: Analytics Pro / SecureLink skew negative; cross-validates the churn model.)*
**Chapter 9: Does it actually work?** Build and evaluate; the three-lens rubric (accuracy / fairness / explainability); the good-enough threshold; adversarial testing. Built in Google Teachable Machine. *(The chapter that earns the book its title.)*
**Chapter 10: Can it do the whole job?** Agentic AI; tool-calling; skills folders as sub-agents; the large/precise danger zone; human-in-the-loop.
**Chapter 11: How does it decide?** Inside classical models; quantisation; jagged intelligence; NotebookLM as production RAG to deconstruct.
**Chapter 12: What comes next?** Collaborative AI; Jevons Paradox; the workforce question; the political economy of AI at scale; AGI as a planning assumption. Closes by returning to the premise: in a world of demos, the proof is the point.

### Appendices

- **A. The Trust Tool** — the placement grid in full.
- **B. The Conversation Log Format** — the record that turns a build into something defensible.
- **C. What You Build** — the inventory of artefacts across the twelve chapters.
- **D. From Prototype to Production** — the honest boundary between a proved prototype and a live system.
- **E. The Tessera Case — A Living Example** — map of the companion site's artefacts to the chapters.
- **F. The No-Code Toolkit — Getting Started** — quick-start for Orange, Teachable Machine, NotebookLM, Ollama, Open WebUI.

---

## 6. Relationship to the companion book

***Conversation, Not Delegation* is the companion on method.** Where *Prove, Don't Persuade* teaches the build-and-evaluate discipline (the *what we prove*), *Conversation, Not Delegation* teaches *how to work with the machine well* (the trust tool, the conversation loop, staying in the loop). The two are complementary. *Substantiate, Don't Assume* is the audit sibling of the same instinct.

---

## 7. Build and deployment

- **Format:** Quarto book, Markdown sources, renders to HTML + PDF + EPUB.
- **Hosting:** GitHub Pages.
- **Licence:** Creative Commons BY (open access, attribution).
- **Case site:** tessera.locoensayo.org (fictional company, real artefacts for exploration).
