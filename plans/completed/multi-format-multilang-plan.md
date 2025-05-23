# Multi-Format Multi-Language Python Tutorial Plan

## Output Formats
- **Book**: Web (HTML) + PDF versions
- **Slides**: RevealJS presentations for each chapter
- **Languages**: English and Japanese versions

## Repository Structure
```
python-tutorial/
├── en/                     # English content
│   ├── book/              # Book chapters (.qmd)
│   ├── slides/            # Slide presentations (.qmd)
│   └── _quarto.yml        # English Quarto config
├── ja/                     # Japanese content  
│   ├── book/              # Book chapters (.qmd)
│   ├── slides/            # Slide presentations (.qmd)
│   └── _quarto.yml        # Japanese Quarto config
├── shared/                 # Shared resources
│   ├── code/              # Code examples
│   ├── data/              # Sample datasets
│   └── images/            # Images and diagrams
├── _quarto.yml            # Main project config
└── plans/, .states/       # Project tracking
```

## Quarto Configuration Strategy

### Main Project (_quarto.yml)
- Define global settings
- Multi-language book project
- Output to docs/ for GitHub Pages

### Language-Specific Configs
- **en/_quarto.yml**: English book + slides
- **ja/_quarto.yml**: Japanese book + slides

### Output Targets
1. **HTML Book**: Interactive web version
2. **PDF Book**: Printable/downloadable version  
3. **RevealJS Slides**: Chapter-by-chapter presentations
4. **GitHub Pages**: Host all formats

## Content Synchronization
- Maintain parallel EN/JP content structure
- Shared code examples and datasets
- Consistent chapter numbering and exercises
- Cross-language navigation links

## Build Process
1. Build English book + slides
2. Build Japanese book + slides  
3. Deploy to GitHub Pages with language selector
4. Generate PDFs for both languages

## Technical Implementation
- Quarto book project with multiple languages
- RevealJS for interactive slides
- Custom CSS for modern design
- GitHub Actions for automated builds
- GitHub Pages for hosting all formats