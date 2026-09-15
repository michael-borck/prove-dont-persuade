# Developmental revision record

Revision completed: 2026-09-15. **Editorial revision closed; reader and release sign-off remain separate.**

This supersedes the “still required” list from the first revision in `ed1a83a`.
The earlier evidence is preserved in the publisher's 2026-09-14 audit snapshot.

## Disposition of the remaining work

| Area | Completed revision |
|---|---|
| Structure | Privacy precedes deployment choice; model comparison precedes agents. Reading order is configured independently of stable source filenames. |
| Proof workflow | Upfront brief, cumulative dossier, original acceptance rules, and prototype/pilot/production gates remain. Added a complete worked decision memo. |
| Data evidence | Replaced unverifiable customer percentages with a small synthetic versioned lab. Distinguished renewal-risk labels from actual churn, label prevalence from errors, and prediction from causal explanation. |
| Reproducibility | New Appendix G prints every core lab input. Matching customer/support CSVs and source excerpts are bundled with provenance and SHA-256 checksums. All twelve chapters have timed, tool-free core activities and success criteria. |
| Evaluation | Reproduced both customer rules, baseline and failed acceptance criterion; six-message toy scorer; router class/lighting counts. No failed test earns deployment approval. |
| Sources and terminology | Qualified privacy, residency/jurisdiction, costs, interpretability, quantisation, model collapse, MCP, labour, and rebound claims. Corrected a misattributed language-evaluation paper, GDPR link, and VET to Verify–Explain–Test. |
| Retrieval and agents | Separated paper design, source-grounded generation, automated retrieval, and executable runtime. Source checking and permission enforcement are not reduced to prompt wording. |
| Trust grid | Clarified that precision, consequences, measured accuracy, and controls are different. Citations or improved scores do not automatically lower the consequences of error. |
| Prose | Reduced repeated manifestos and chapter machinery; only 3/12 chapters retain the full RTCF closing exercise. Focused data, privacy, deployment, language, model-comparison, and conclusion chapters. |
| Resources and production | Corrected core/optional resource promises and chapter-level PDF/EPUB links. Replaced failing author-site destinations with working project/book links. Rebuilt all formats and corrected an orphaned lab-table continuation header. |

The original external Tessera exports and optional tool installations have not
been obtained or executed as part of this revision. They are **extensions**, not
dependencies of the core route. Lab-v1 is expressly not an original Tessera
export or real customer evidence.

## Length and style review

Approximate configured prose: **29,884 words**, versus 46,260 in the initial
scan and 44,037 after the first pass. The book now has 22 configured QMD files,
including seven appendices, and twelve core chapters.

Core chapters range from roughly 1,042 to 2,688 words. The shorter chapters
share complete inputs and answer checks in Appendix G rather than repeating
datasets, setup instructions, and a full series of callouts. This is a deliberate
compact learning path, not a claim that a word-count threshold proves quality.
Reader pacing remains a question for the fresh-reader gate.

The scan reports 12 callouts across configured files, eight in core chapters,
and no cross-file repeated sentences meeting its threshold. Shared terminology,
reference components, and selected practice scaffolds intentionally remain.

## Verification

- `python scripts/check_manuscript.py`: **9 tests passed** for configured files,
  order, explicit local QMD links/anchors, customer and support fixture/table
  agreement, source-excerpt agreement, checksum manifest, practice variation,
  and router evaluation arithmetic.
- The same tests passed in an isolated source copy without generated book files.
- Shared publisher `--book prove --llm --preprocess --render`: HTML, PDF, EPUB,
  fresh llm.txt, and canonical downloads completed.
- Rendered validator: **22 HTML pages; 1,432 local targets/anchors; zero errors**.
  EPUB ZIP integrity, XHTML well-formedness, internal links, and configured
  chapter sequence in its 24-entry spine checked.
- PDF: **130 pages, 6 × 9 inches**. All chapter boundaries reviewed in reading
  order from extracted PDF text; final physical pages 120–123 visually checked
  for the complete customer table, support table, source excerpts, and worked
  decision memo. The orphaned customer-table header was repaired.
- Joint external-reference scan: 53/54 URLs reachable; the one automated-access
  restriction concerns CND's PNAS reference, with an accessible author copy.
- Publisher metadata audit: zero errors and zero warnings. The registry still
  says not yet published; no ISBN has been invented or assigned here.
- `git diff --check`: checked at handoff.

These checks validate the supplied teaching arithmetic and local publishing
outputs. They do not establish legal compliance, production model performance,
successful optional browser interactions, or a human proofread of every page.

## Reader and release gates—not completed by this revision

1. Give an unfamiliar reader Appendix G and the dossier criteria. Have them
   calculate both rules and the baseline, explain why neither meets the whole
   brief, preserve the proxy-label limitation, and write their own decision memo.
   Then check their source-bounded answers, including the absent refund amount.
2. If offering a facilitated build-along course, execute the selected optional
   Orange, Teachable Machine, Ollama/Open WebUI, or NotebookLM route in the
   actual teaching environment. Record versions, hardware, access, failures,
   and setup time. No optional run is marked tested here.
3. Complete page-by-page human proofreading and an EPUB-reader check, then
   approve the cover/print proof and release metadata separately.

No commit/push, website deployment, hosted chatbot refresh, or KDP upload was
performed in this closing revision. The rebuilt local free-edition files are
not a claim that hosted or purchased editions have changed.
