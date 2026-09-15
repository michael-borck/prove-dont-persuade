# Prove, Don't Persuade

A Quarto book by Michael Borck about evaluating applied AI: whether it works, for whom, and under which conditions.

The free source and online edition are the primary versions. Tessera is a fictional teaching company, not a real client engagement.

## Reading and exercises

Start with the proof brief in `index.qmd`. Build one cumulative evidence dossier using Appendix C, then use Appendix D's prototype, pilot, and production gates to defend your decision.

- **Core route:** all twelve chapters have timed activities that can be completed without an AI account. Appendix G prints the synthetic lab inputs and answer checks; `resources/lab-v1/` supplies matching downloads.
- **Build-along route:** tool-based labs may require external Tessera datasets/documents, suitable hardware, and setup help. The full CSVs, policy collection, and router photographs are not bundled.
- **Evidence:** illustrative case results are not measurements of your build. Preserve actual inputs, outputs, versions, and failures; label unexecuted work honestly.

Appendices E and F explain external resources and setup limits; Appendix G supplies the self-contained lab. Source filenames retain their original numeric prefixes for URL stability; `_quarto.yml` defines the reading order.

## Build

Install Quarto and use:

```sh
quarto render --to html
quarto preview
```

The shared publisher prepares the separate print source and copies canonical PDF/EPUB downloads back into the HTML output. From the parent books workspace:

```sh
python book-publisher/publish.py --book prove --llm --preprocess --render
```

This builds locally; it does not push commits, publish GitHub Pages, or upload to KDP. PDF rendering also requires the configured TeX toolchain. `print-config.yml` preserves the 6 × 9 inch print layout.

Do not edit generated `_print_source/`, `_book/`, or `llm.txt` as manuscript sources.

## Checks and editorial status

```sh
python scripts/check_manuscript.py
```

These checks cover configured source files, explicit local chapter links, reading-order dependencies, and the arithmetic and printed/downloadable consistency of the supplied evaluation and lab cases. They do not certify factual accuracy, legal compliance, external lab reproducibility, or print layout.

See [EDITORIAL-REVISION.md](EDITORIAL-REVISION.md) for completed changes, validation results, and remaining audit work.

## Links

- [Online book](https://michael-borck.github.io/prove-dont-persuade/)
- [Tessera companion](https://tessera.locoensayo.org)
- [DeepWiki](https://deepwiki.com/michael-borck/prove-dont-persuade)
- [Conversation, Not Delegation](https://michael-borck.github.io/conversation-not-delegation/)
- [All books](https://books.borck.education)

Corrections and reproducible issue reports are welcome through this repository. The book metadata currently declares a CC BY licence.
