# Developmental revision record

Date: 2026-09-14. Status: **first revision pass complete; editorial review remains open**.

## Changes in this pass

- Reordered privacy before deployment, and model comparison before agents. Source
  filenames remain stable; numbered references and transitions follow reading order.
- Added an upfront proof brief and one cumulative dossier, with eight capstone
  acceptance criteria and explicit prototype/pilot/production decision gates.
- Focused the bias chapter and moved prompt injection to the retrieval chapter,
  with a synthetic, tool-free test and an independent paper option.
- Added self-contained bias, privacy, evaluation, agent-design, and capstone
  activities with inputs, time estimates, outputs, and success criteria.
- Replaced the router example's incompatible sample sizes/percentages with an
  explicitly fictional six-row count table; checked all reported calculations.
  The failed test no longer justifies deployment. Reviewing only predictions
  labelled fault no longer passes as protection against missed faults.
- Distinguished low-renewal-label distributions from measured prediction errors
  in the fairness case. Introduced the proxy-label limitation in the data chapter.
- Removed mandatory Glitch deployment. Browser preview is the optional build
  route, and the complete paper evaluation needs no account or hosting.
- Corrected the resource promise: full Tessera CSVs, policies, and photographs
  are external dependencies, not bundled/reproducible assets in this edition.
- Distinguished readable instructions from executable agent infrastructure;
  corrected the cited agent token-cost comparison and limited claims about
  NotebookLM internals to observable behaviour and explicit hypotheses.
- Shortened the introduction and replaced three full RTCF endings with independent
  work. This is not yet a complete prose/cadence pass.
- Added a 6 × 9 inch print configuration, matching the existing source PDF layout
  instead of accepting the shared preprocessor's 7 × 10 inch default.

## Verification

- `python scripts/check_manuscript.py`: four checks passed (configured sources,
  order, explicit local QMD links/anchors, worked evaluation arithmetic).
- Shared publisher `--book prove --llm --preprocess --render`: HTML, PDF, and EPUB
  completed successfully; canonical downloads and fresh `llm.txt` copied.
- Publisher `--book prove --audit`: zero errors and zero warnings. This checks
  build/publishing metadata, not editorial quality or actual KDP publication status.
- EPUB ZIP integrity and the reordered navigation entries checked.
- PDF: 160 pages, 432 × 648 points (6 × 9 inches). Sampled physical pages 7, 8,
  94, 139, and 141: proof brief, evaluation table, dossier, and stage-gate layout
  readable. This was not a sequential proofread of all pages or KDP validation.
- Content scan: 44,037 approximate prose words, down from 46,260 (about 4.8%).
  Introduction: 2,294 versus 2,616. Counts are diagnostics, not quality scores.
- `git diff --check`: clean.

## Still required, in order

1. **Evidence and terminology pass.** Verify the source/version behind the customer
   data's quoted percentages; consistently distinguish a proxy renewal label from
   actual churn throughout Chapters 4, 10, and 12. Check claims about learning,
   interpretability, model collapse, privacy law, sovereignty, labour, and future
   capability against primary sources. Removing overclaims in selected passages
   does not establish the rest of the manuscript's accuracy.
2. **Lab reproducibility pass.** Obtain and version external exercise inputs with
   provenance, or replace additional labs with self-contained alternatives. Test
   the actual browser interactions, local setup, and source-based activities on a
   clean machine. Documentation checks and a successful book render are not a
   successful lab run. Convert the remaining retrospective activity descriptions
   into runnable instructions.
3. **Prose pass.** Nine chapters still have full RTCF endings. Reduce repeated
   thesis statements, vary more openings and exercises, and shorten remaining
   categorical/performative contrasts without losing the author's voice.
4. **Reader and production review.** Have a reader unfamiliar with the case attempt
   the dossier and capstone. Read the full PDF/EPUB sequentially, check the remaining
   external links, and resolve typography/navigation issues before release.

At the end of the revision pass, the changes were local. Source-control commits
and pushes are separate from publication: this pass did not publish GitHub Pages,
update a hosted chatbot, or upload anything to KDP.
