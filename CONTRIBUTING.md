# Contributing to 1TamilMV

Thank you for your interest in contributing to **1TamilMV**! We welcome contributions from developers, movie enthusiasts, and Tamil cinema fans worldwide.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Community](#community)

---

## 🤝 Code of Conduct

This project is committed to being welcoming and inclusive. We expect all contributors to:

- Be respectful and constructive in all interactions
- Welcome feedback and diverse perspectives
- Show empathy towards other community members
- Respect differing opinions
- Keep discussions about Tamil cinema and movies friendly

**Unacceptable behavior:**
- Harassment or discrimination
- Disrespectful comments
- Personal attacks
- Sharing pirated content links

---

## 🚀 Getting Started

### 1. Fork the Repository

Visit GitHub and click the "Fork" button.

### 2. Clone Your Fork

```bash
git clone https://github.com/YourUsername/1TamilMV.git
cd 1TamilMV
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/Original/1TamilMV.git
```

---

## 💻 Development Setup

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git
- Telegram Bot Token (from @BotFather)

### Setup Steps

1. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Copy Configuration**

```bash
cp config.example.yaml config.yaml
# Edit config.yaml with your Bot Token
```

4. **Run Bot**

```bash
python main.py
```

---

## ✏️ Making Changes

### Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Commit Guidelines

Write meaningful commit messages:

```bash
git commit -m "feat: Add movie rating system

- Implement 5-star rating
- Store ratings in database
- Show average rating in search results

Closes #123"
```

**Format:** `Type: Description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

---

## 🔄 Submitting Changes

### 1. Keep Your Fork Updated

```bash
git fetch upstream
git rebase upstream/main
```

### 2. Push Your Changes

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill in PR title and description

### PR Title Format

`[Type] Brief description`

Example: `[Feature] Add movie rating system`

---

## 🎬 Areas Needing Help

1. **Feature Development**
   - AI recommendations
   - Voice search
   - Web dashboard
   - Mobile app

2. **Movie Data**
   - Collecting new movies
   - Updating movie information
   - OTT platform data

3. **Documentation**
   - Tutorial writing
   - API documentation
   - Translation support

4. **Bug Fixes**
   - Search improvements
   - Performance optimization
   - Stability fixes

5. **Translation**
   - Tamil language support
   - Telugu support
   - Kannada support
   - Malayalam support

---

## 📚 Documentation Standards

- Write clear commit messages
- Add docstrings to functions
- Comment complex logic
- Update README if adding features
- Include usage examples

---

## 🧪 Testing

Run tests before submitting:

```bash
pytest tests/
pytest --cov=src  # with coverage
```

---

## 📞 Questions?

- **Discord:** [Join Server](https://discord.gg/1tamilmv)
- **Telegram:** [@1TamilMVSupport](https://t.me/1TamilMVSupport)
- **GitHub Issues:** [Ask a Question](https://github.com/YourUsername/1TamilMV/issues)
- **Email:** support@1tamilmv.dev

---

## 🎉 Thank You!

We appreciate your contributions! Every bit helps make 1TamilMV better for Tamil cinema lovers worldwide.

**Happy coding!** 🚀
