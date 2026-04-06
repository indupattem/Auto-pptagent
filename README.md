# Auto-pptagent

# 🎯 Auto-PPT Agent (AI + MCP Based Presentation Generator)

## 📌 Overview

The **Auto-PPT Agent** is an AI-powered system that automatically generates a complete PowerPoint presentation from a single user prompt.

It follows an **Agentic Architecture using MCP (Model Context Protocol)** where:

* The agent plans slide structure
* Dynamically generates content
* Uses tools to build and save a `.pptx` file

---

## 🚀 Features

* 🧠 **Agentic Planning**

  * Automatically creates slide structure before execution

* 📄 **Dynamic Content Generation**

  * Generates 6–7 bullet points per slide
  * Uses AI (Gemini API) + Wikipedia fallback
  * No hardcoded content

* 🖼️ **Automatic Image Integration**

  * Fetches relevant images dynamically for each slide

* 🎨 **Professional PPT Design**

  * Styled slides (dark theme, layout, spacing)
  * Title formatting + aligned content

* 🔧 **MCP Tool Integration**

  * Uses custom MCP tools:

    * `create_presentation`
    * `add_slide`
    * `write_content`
    * `save_presentation`

* 🌐 **Frontend Interface**

  * Simple Flask-based UI
  * Enter topic → Download PPT instantly

---

## 🏗️ Project Structure

```
Auto-ppt/
│
├── agent/
│   └── agent_ppt.py          # Main agent logic
│
├── mcp_servers/
│   ├── ppt_mcp_server.py     # PPT generation tools (MCP)
│   └── search_mcp_server.py  # Dynamic content retrieval
│
├── templates/
│   └── index.html            # Frontend UI
│
├── presentations/            # Generated PPT files
│
├── app.py                    # Flask backend
├── run.py                    # CLI runner
├── .env                      # API keys
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone https://github.com/your-username/auto-ppt-agent.git
cd auto-ppt-agent
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

### 🖥️ Option 1: Web UI (Recommended)

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

👉 Enter topic → PPT downloads automatically

---

### 💻 Option 2: CLI

```
python run.py
```

---

## 🧠 How It Works

1. User enters a topic
2. Agent plans slide structure
3. For each slide:

   * Generates content using AI / Wikipedia
   * Calls MCP tools to create slides
4. Adds images dynamically
5. Saves `.pptx` file

---

## 🛠️ Technologies Used

* Python
* Flask (Frontend + Backend)
* MCP (Model Context Protocol)
* python-pptx
* Gemini API (google-genai)
* Wikipedia API
* Requests

---

## 📊 Example Input

```
Create a presentation on Artificial Intelligence
```

## 📈 Output

✔ 5–6 slides
✔ Each slide contains:

* Title
* 6 bullet points
* Relevant image
  ✔ Professionally styled PPT

---

## ⚠️ Challenges Faced

* API quota issues (OpenAI → switched to Gemini)
* Image fetching failures → fixed with stable sources
* Static content → replaced with dynamic generation
* MCP server path & environment issues

---

## 💡 Improvements

* Added fallback system (AI → Wikipedia → dynamic)
* Improved slide styling and layout
* Built frontend UI for usability

---

## 🎤 Conclusion

This project demonstrates how **AI agents + MCP architecture** can automate real-world tasks like presentation creation with minimal human input.

---

## 👩‍💻 Author

**Indu Harshitha Pattem**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
