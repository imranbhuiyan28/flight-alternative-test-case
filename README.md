# 🧪 UI Test Automation Suite (Behave + Selenium)

This repository contains a comprehensive collection of automated UI test scenarios written using **Behave** (BDD) and **Selenium WebDriver**. The suite focuses on verifying the **responsiveness**, **layout integrity**, **navigation**, and **user experience (UX)** of a web application across various devices and screen sizes.

---

## 📁 Features Covered

### ✅ UI Responsiveness
- Validate mobile and desktop layouts
- Ensure no horizontal scroll or layout breakage
- Confirm hamburger menu presence on mobile view

### ✅ UI/UX Verification
- Check visibility of key homepage elements: logo, navigation bar, hero section, and footer

### ✅ Error Feedback
- Test user-facing error messages on incomplete form submissions

### ✅ Navigation
- Validate footer and header navigation links (e.g., About Us, header links)

### ✅ Performance
- Verify homepage loads within acceptable time
- Ensure search responses appear promptly

### ✅ Header Elements
- Confirm correct number of header links are present

---

## 🚀 Getting Started

### 📦 Prerequisites
- Python 3.8 or higher
- Chrome browser (or other supported browsers)
- Corresponding WebDriver installed and added to system PATH (e.g., ChromeDriver)
- Recommended: Python virtual environment

### 🔧 Installation

```bash
git clone https://github.com/yourusername/ui-test-suite.git
cd ui-test-suite
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt



🎥 Demo Video
For a quick overview and demo of the test suite in action, watch the video below:

click here to watch on Loom:https://www.loom.com/share/69e0b84963ec4d7090be75853274c617?sid=a00a9e7b-fddd-4f64-8ec3-e6792e3a1a02