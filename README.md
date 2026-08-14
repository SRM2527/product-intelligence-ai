# Product Intelligence AI

An AI-powered product research and enrichment system that transforms basic manufacturer information into structured product intelligence.

## 🚀 Overview

Product information is often scattered across different websites and sources. Manually researching specifications, features, applications, and other product details can be time-consuming.

**Product Intelligence AI** automates this process.

The user provides:

* Brand
* Manufacturer Part Number (MPN)
* Product Description

The system researches relevant web sources, extracts useful product information, and presents the results through a professional dashboard.

## ✨ Features

* 🔎 Automated product web research
* 🏷️ Product identification using brand and MPN
* 📂 Product category classification
* ⚙️ Specification extraction
* ✨ Feature extraction
* 🏭 Application identification
* 🔑 Keyword generation
* 📊 Confidence and completeness scoring
* 🔗 Research source references
* 🖥️ Interactive web dashboard

## 🏗️ Architecture

```text
User
  ↓
Frontend
HTML + CSS + JavaScript
  ↓
FastAPI REST API
  ↓
Web Research
Tavily
  ↓
Source Processing
  ↓
Fact & Specification Extraction
  ↓
Product Enrichment
  ↓
Structured Product Intelligence
  ↓
Dashboard
```

## 🛠️ Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI

### Research

* Tavily Search API

### Data Processing

* Python
* Regular expressions
* Rule-based enrichment

## 📁 Project Structure

```text
product-intelligence-ai/
│
├── .gitignore
├── .env.example
├── README.md
│
├── backend/
│   ├── main.py
│   ├── ai_service.py
│   └── research_service.py
│
└── frontend/
    └── index.html
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd product-intelligence-ai
```

### 2. Create a virtual environment

```bash
cd backend
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn tavily-python python-dotenv
```

### 5. Configure API keys

Create:

```text
backend/.env
```

Add your own API keys:

```text
TAVILY_API_KEY=your_actual_tavily_key
OPENAI_API_KEY=your_actual_openai_key
```

**Never upload `.env` to GitHub.**

## ▶️ Running the Backend

From the `backend` directory:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## 🖥️ Running the Frontend

Open:

```text
frontend/index.html
```

using VS Code Live Server.

Enter a product's:

* Brand
* MPN
* Description

Then click:

**Generate Product Intelligence**

## 🧪 Example

### Input

```text
Brand: Bosch
MPN: GSR 120-LI
Description: Cordless drill driver
```

### Output

The system can return:

* Product information
* Category
* Features
* Applications
* Specifications
* Keywords
* Confidence score
* Completeness score
* Research sources

## 🔐 Security

API keys are stored locally in:

```text
backend/.env
```

The `.env` file is excluded from Git using `.gitignore`.

A `.env.example` file is provided with placeholder values for setup.

**Never commit or share real API keys.**

## 🔮 Future Scope

Possible future improvements include:

* LLM-based product enrichment
* Product comparison
* PDF and datasheet extraction
* Advanced source verification
* Larger product databases
* Product report export
* Automated product catalog generation

## 🎯 Project Goal

The goal of Product Intelligence AI is to reduce manual product research and transform scattered product information into structured, useful, and presentation-ready product intelligence.

## 👥 Hackathon Project

Built as a hackathon prototype demonstrating automated product research, information extraction, enrichment, and visualization.
