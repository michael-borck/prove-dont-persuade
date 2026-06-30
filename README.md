# prove-dont-persuade

A comprehensive Quarto book exploring why proof and evidence beat persuasion and demos in applied AI projects.

## About

"Prove, Don't Persuade" is a technical book that challenges conventional approaches to demonstrating AI value. Instead of relying on impressive demos and persuasive narratives, this book advocates for building concrete proof through practical, measurable implementations. It provides frameworks, case studies, and actionable guidance for data scientists, AI practitioners, and business leaders seeking to validate AI initiatives effectively.

This repository contains the complete source code for the book, written in Quarto format, enabling reproducible research and transparent documentation of concepts and examples.

## Features

- Comprehensive framework for validating AI projects through proof rather than persuasion
- Practical case studies and real-world applications
- Reproducible examples and implementation guides
- Trust-building tools and conversation logs for stakeholder engagement
- From prototype to production guidance
- Appendices covering specialized topics (Trust Tool, Tessera Case Study, etc.)

## Prerequisites

- [Quarto](https://quarto.org/) (version 1.3 or later)
- [R](https://www.r-project.org/) (recommended for executing code examples)
- A text editor or IDE (VS Code, RStudio, or similar)
- Git (for cloning the repository)

## Installation

### Clone the Repository

```bash
git clone https://github.com/michael-borck/prove-dont-persuade.git
cd prove-dont-persuade
```

### Install Quarto

If you haven't already installed Quarto, download it from [quarto.org](https://quarto.org/docs/get-started/):

```bash
# macOS
brew install quarto

# Ubuntu/Debian
sudo apt-get install quarto

# Windows
choco install quarto
```

### Install R Dependencies (Optional)

If running code examples, install required R packages:

```bash
Rscript -e "install.packages(c('tidyverse', 'ggplot2', 'knitr'))"
```

## Usage

### Rendering the Book

To render the entire book in HTML format:

```bash
quarto render
```

To render as PDF:

```bash
quarto render --to pdf
```

To render in a specific format:

```bash
quarto render --to html
quarto render --to docx
quarto render --to epub
```

### Development Mode

For interactive development with live preview:

```bash
quarto preview
```

This command starts a local server and automatically reloads the preview whenever you save changes to the source files.

### Building Specific Chapters

To render an individual chapter:

```bash
quarto render chapters/01-introduction.qmd
```

### Viewing the Output

After rendering, open the generated files:

```bash
# HTML output
open _book/index.html

# PDF output
open _book/prove-dont-persuade.pdf
```

## Project Structure

```
prove-dont-persuade/
├── _quarto.yml                 # Quarto configuration file
├── index.qmd                   # Book introduction/cover
├── about-author.qmd            # Author biography
├── acknowledgments.qmd         # Acknowledgments section
├── chapters/                   # Main book chapters
│   └── [chapter files]
├── appendices/                 # Book appendices
│   ├── a-the-trust-tool.qmd
│   ├── b-conversation-log-format.qmd
│   ├── c-what-you-build.qmd
│   ├── d-prototype-to-production.qmd
│   └── e-the-tessera-case.qmd
├── images/                     # Figures, diagrams, and images
├── CHAPTER_OUTLINE.md          # Detailed chapter outline
├── .gitignore                  # Git ignore patterns
└── README.md                   # This file
```

## Key Sections

### Chapters

The main narrative is organized into sequential chapters covering foundational concepts through advanced implementation strategies for applied AI projects.

### Appendices

- **Appendix A**: The Trust Tool — A framework for building stakeholder trust
- **Appendix B**: Conversation Log Format — Templates for documenting discussions
- **Appendix C**: What You Build — Guidance on building proof of concepts
- **Appendix D**: Prototype to Production — Transitioning from proof to deployment
- **Appendix E**: The Tessera Case — A detailed real-world case study

## Configuration

The book configuration is managed in `_quarto.yml`. Key settings include:

- Output formats (HTML, PDF, ePub)
- Table of contents structure
- Theme and styling preferences
- Code execution options

To customize rendering, edit `_quarto.yml` according to [Quarto documentation](https://quarto.org/docs/books/).

## Contributing

While this is a published work by Michael Borck, corrections and suggestions are welcome. Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b fix/correction`)
3. Commit your changes (`git commit -m 'Fix typo in chapter 3'`)
4. Push to the branch (`git push origin fix/correction`)
5. Open a Pull Request

## License

This work is licensed under a custom license. Please see the LICENSE file for details.

## Author

**Michael Borck** — Data Science and AI thought leader focused on practical, evidence-based approaches to implementing AI in organizations.

## Resources

- [Quarto Documentation](https://quarto.org/)
- [Quarto Books Guide](https://quarto.org/docs/books/)
- [R Markdown Cookbook](https://bookdown.org/yihui/rmarkdown-cookbook/)

## Support

For questions, issues, or suggestions regarding this book:

- Open an issue on [GitHub Issues](https://github.com/michael-borck/prove-dont-persuade/issues)
- Contact the author for specific inquiries

## Acknowledgments

See `acknowledgments.qmd` for a complete list of individuals and organizations that contributed to this work.