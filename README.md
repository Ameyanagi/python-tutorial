# Python Tutorial =

A comprehensive, multi-language Python tutorial built with Quarto, featuring multiple output formats and modern development practices.

## =� Available Formats

- **=� Interactive HTML Book** - Web-based tutorial with code execution
- **=� PDF Book** - Downloadable printable version  
- **<� RevealJS Slides** - Presentation format for teaching
- **< Multi-Language** - English and Japanese (�,�) versions

## <� Project Structure

```
python-tutorial/
   en/                     # English content
      book/              # Tutorial chapters (.qmd)
      slides/            # Slide presentations (.qmd)
   ja/                     # Japanese content (�,�)
      book/              # Tutorial chapters (.qmd)
      slides/            # Slide presentations (.qmd)
   shared/                 # Shared resources
      code/              # Working code examples
      data/              # Sample datasets
      images/            # Images and diagrams
   .github/workflows/      # CI/CD automation
   .vscode/               # VS Code configuration
   plans/                 # Project planning docs
   .states/               # Implementation tracking
   docs/                  # Generated output (GitHub Pages)
```

## =� Quick Start

### Prerequisites

1. **Python 3.12+** - For best type hinting support
2. **Quarto** - For rendering the tutorial
3. **uv** - Recommended package manager (or use Poetry/Conda)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/python-tutorial.git
   cd python-tutorial
   ```

2. **Install Quarto:**
   - Download from [quarto.org](https://quarto.org/docs/get-started/)
   - Or use package manager:
     ```bash
     # macOS
     brew install quarto
     
     # Windows
     winget install Posit.Quarto
     
     # Linux
     # Download .deb/.rpm from quarto.org
     ```

3. **Set up Python environment:**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

### Development Commands

```bash
# Preview English content
uv run quarto preview en/

# Preview Japanese content  
uv run quarto preview ja/

# Render English book + slides
uv run quarto render en/

# Render Japanese book + slides
uv run quarto render ja/

# Render entire project
uv run quarto render

# Code quality checks
uv run ruff check .          # Linting
uv run ruff format .         # Formatting
uv run pyright shared/code/  # Type checking
```

## =� Tutorial Content

### Foundation
1. **Environment Setup** - uv, VS Code, Git/GitHub
2. **Git and GitHub** - Version control essentials
3. **Python Syntax** - Variables, operators, basic I/O

### Python Basics  
4. **Data Types** - Lists, tuples, dictionaries, sets
5. **Control Flow** - Conditions, loops, logic
6. **Functions** - Organization, scope, advanced concepts

### Object-Oriented Programming
7. **Classes and Objects** - OOP fundamentals
8. **Inheritance** - Code reuse and polymorphism  
9. **Advanced OOP** - Magic methods, decorators

### Advanced Topics
10. **Type Hints** - Static typing and mypy
11. **Async Programming** - Concurrency with asyncio
12. **Multiprocessing** - Parallel computing

### Applications
13. **Data Science** - pandas, numpy, matplotlib
14. **Automation** - File handling, APIs, scheduling
15. **General Programming** - Testing, debugging, packaging
16. **Web Development** - Streamlit frontend, FastAPI backend

### Self-Review Sections
- Interactive exercises and quizzes
- Coding challenges with solutions
- Logic puzzles and performance comparisons
- Comprehensive projects

## =� Development Environment

### Recommended Setup

1. **VS Code** with extensions:
   - Python
   - Ruff (linting & formatting)
   - Pyright (type checking)
   - Error Lens (debugging)
   - Quarto (tutorial editing)

2. **Environment Management:**
   - Primary: **uv** (fastest, modern)
   - Alternative: Poetry, Miniforge

3. **Code Quality:**
   - **Ruff** for linting and formatting
   - **Pyright** for type checking
   - **pytest** for testing

### Configuration Files

- `.vscode/settings.json` - VS Code preferences
- `pyproject.toml` - Python project config
- `_quarto.yml` - Tutorial configuration
- `custom.scss` - Modern styling theme

## =� Deployment

### GitHub Pages (Automatic)

The tutorial automatically deploys to GitHub Pages via GitHub Actions:

1. **Push to main branch** triggers the workflow
2. **Quarto renders** all content (EN + JP)
3. **GitHub Pages** serves the static site
4. **Available at** `https://your-username.github.io/python-tutorial/`

### Manual Deployment

```bash
# Build all content
quarto render

# Deploy to GitHub Pages manually
gh-pages -d docs
```

## < Multi-Language Support

### English Version
- Complete tutorial chapters
- Interactive code examples
- Comprehensive exercises
- Modern presentation slides

### Japanese Version (�,�)
- Parallel content structure
- Culturally appropriate examples
- Japanese programming conventions
- Native language explanations

### Adding New Languages

1. Create new language directory (e.g., `fr/`, `es/`)
2. Copy `en/_quarto.yml` and translate metadata
3. Translate content files from `en/book/`
4. Update main `_quarto.yml` navigation
5. Add language selector links

## <� Learning Objectives

By completing this tutorial, you will:

-  Master Python syntax and core concepts
-  Understand data structures and algorithms
-  Write clean, maintainable functions
-  Apply object-oriented programming principles
-  Handle advanced topics like async programming
-  Build real-world applications
-  Use modern development tools and practices
-  Follow Python best practices and conventions

## > Contributing

We welcome contributions! Here's how to help:

### Content Contributions
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/new-chapter`)
3. **Add your content** following existing patterns
4. **Test rendering** with `quarto preview`
5. **Submit a pull request**

### Translation Contributions
1. **Choose a target language**
2. **Create language directory structure**
3. **Translate existing chapters**
4. **Test with native speakers**
5. **Submit for review**

### Bug Reports and Suggestions
- Use **GitHub Issues** for feedback
- Include specific chapter/section references
- Provide clear reproduction steps
- Suggest improvements or corrections

## =� Requirements

### System Requirements
- **OS:** Windows, macOS, or Linux
- **Python:** 3.12 or higher
- **Memory:** 4GB RAM minimum
- **Storage:** 2GB for full development setup

### Dependencies
- **Quarto:** Tutorial rendering
- **Python packages:** See `pyproject.toml`
- **VS Code:** Recommended editor
- **Git:** Version control

## =� License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## =O Acknowledgments

- **Quarto** - Amazing publishing system
- **Python Software Foundation** - The Python language
- **VS Code** team - Excellent development environment
- **Ruff** - Lightning-fast Python linting
- **Community contributors** - Feedback and improvements

## =� Support

- **Documentation:** See individual chapter README files
- **Issues:** Use GitHub Issues for bugs/suggestions
- **Discussions:** GitHub Discussions for questions
- **Email:** [your-email@example.com] for private inquiries

---

**Happy Learning! =(**

Start your Python journey: [English Tutorial](en/index.html) | [�,�������](ja/index.html)