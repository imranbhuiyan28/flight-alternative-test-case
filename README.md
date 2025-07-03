# 🧪 UI Test Automation Suite (Behave + Selenium)

This repository contains a collection of automated UI test scenarios written using **Behave** (BDD) and **Selenium WebDriver**, focused on verifying the **responsiveness**, **layout integrity**, **navigation**, and **UX** of a web application across devices.

---

## 📁 Features Covered

### ✅ UI Responsiveness
- Validates mobile and desktop layouts
- Ensures no horizontal scroll or layout breakage
- Confirms hamburger menu on mobile

### ✅ UI/UX Verification
- Visibility of key homepage elements: logo, navbar, hero section, footer

### ✅ Error Feedback
- Tests user-facing error messages when submitting incomplete forms

### ✅ Navigation
- Validates footer and header navigation (e.g. About Us, header links)

### ✅ Performance
- Page load time for homepage
- Search response time within acceptable limits

### ✅ Header Elements
- Verifies correct number of header links are present

---

## 🚀 Getting Started

### 📦 Prerequisites
- Python 3.8+
- Chrome (or another supported browser)
- ChromeDriver or relevant WebDriver installed and added to PATH
- Virtual environment (recommended)

### 🔧 Installation

```bash
git clone https://github.com/yourusername/ui-test-suite.git
cd ui-test-suite
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

