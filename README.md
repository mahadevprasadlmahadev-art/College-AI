# 🎓 MITT College AI Assistant

> An intelligent, fast and privacy-focused AI assistant for students of **Maharaja Institute of Technology Thandavapura (MITT)**.

The **MITT College AI Assistant** provides students with quick answers about college fees, timetables, faculty, VTU subject codes, important academic information and other college-related queries.

The application uses a **local Qwen3-4B model through Llamafile** for uncatalogued questions, while frequently requested college information is answered directly from the built-in MITT knowledge base.

---

## ✨ Features

* 🤖 AI-powered college assistant
* ⚡ Fast direct responses
* 🔒 Local and privacy-focused AI inference
* 🌐 Web-based interface using Gradio
* 📅 Complete 5th Semester timetable
* 💰 Fee information
* 👨‍🏫 Faculty and subject information
* 📚 VTU subject codes
* 🏫 College and department information
* 📡 Streaming AI responses
* 🧠 Qwen3-4B local language model
* 🎨 Modern 60-30-10 dark UI design
* 🔌 Works with a local Llamafile server

---

## 🏫 College Information

**Maharaja Institute of Technology Thandavapura (MITT)**

📍 **Location:**
NH 766, Thandavapura, Nanjangud Taluk, Mysuru District, Karnataka – 571302

🌐 **Website:**
https://www.mitt.edu.in/

### Department

**Artificial Intelligence and Data Science**

* Semester: **5th Semester**
* Academic Year: **2026–27**
* Classes Start: **08/09/2026**
* Last Working Day: **30/12/2026**

---

## 💰 Fee Information

According to the project's built-in college dataset:

| Fee Type    |    Amount |
| ----------- | --------: |
| Annual Fee  | ₹1,60,000 |
| Tuition Fee | ₹1,15,956 |
| Other Fees  |   ₹44,044 |

**Fee policy:** The project specifies the same fee structure for engineering departments for the 2024–2028 period.

---

## 📅 5th Semester Timetable

The assistant contains the weekly timetable for the **AI & DS 5th Semester**.

### Monday

* 08:30–09:30 — Computer Networks
* 09:30–10:30 — Cloud Computing
* 10:30–11:00 — Tea Break
* 11:00–12:00 — Research Methodology & IPR
* 12:00–13:00 — Software Engineering & Project Management
* 13:00–13:45 — Lunch Break
* 14:35–15:25 — Environmental Studies
* 15:25–16:15 — Free / Library Study

The application also contains schedules for **Tuesday, Wednesday, Thursday and Friday**.

---

## 👨‍🏫 Faculty Directory

| Subject                                    | Faculty                       | Code |
| ------------------------------------------ | ----------------------------- | ---- |
| Computer Networks                          | Prof. Harshitha BS            | HBS  |
| Cloud Computing                            | Dr. Swarnalatha K             | SK   |
| Software Engineering & Project Management  | Prof. Madhuri B               | MB   |
| Theory of Computation                      | Prof. Mamatha D               | MD   |
| Data Visualization Lab                     | Prof. Mamatha D               | MD   |
| Mini Project                               | Dr. GS Madhan Kumar           | GSM  |
| Research Methodology & IPR                 | Dr. GS Madhan Kumar           | GSM  |
| Environmental Studies & E-Waste Management | Prof. Mahadev Prasad N        | MPN  |
| Yoga                                       | Physical Education Department | PE   |

---

## 🧠 AI Architecture

The application follows a two-level response system:

```text
                 ┌─────────────────────┐
                 │       Student       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Gradio Web UI     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Direct Answer Engine│
                 │   MITT Knowledge    │
                 │       Base          │
                 └──────────┬──────────┘
                            │
                    Unknown Question
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Local Llamafile     │
                 │ Server :8080        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Qwen3-4B GGUF Model │
                 └─────────────────────┘
```

### Response Flow

1. Student enters a question.
2. The application checks the built-in MITT knowledge base.
3. Known questions receive a direct answer.
4. Unknown questions are sent to the local Llamafile server.
5. Qwen3-4B generates the response.
6. The response is streamed back to the interface.
7. Internal `<think>` content is filtered before displaying the answer.

---

## 🛠️ Technology Stack

* **Python**
* **Gradio**
* **Llamafile**
* **llama.cpp**
* **Qwen3-4B**
* **GGUF**
* **HTTP / REST API**
* **Server-Sent Events (SSE)**
* **HTML/CSS**

---

## 🎨 User Interface

The project uses a **60-30-10 design system**:

* **60%** — Midnight Obsidian background
* **30%** — Cyber Slate panels
* **10%** — Neon Cyan and Emerald accents

The interface includes quick-action buttons for:

* 💰 Annual Fees
* 📅 Monday Schedule
* 📅 Wednesday Schedule
* 👨‍🏫 Faculty Directory
* 📚 VTU Codes
* 🏫 Important Dates

---

## 📁 Project Structure

```text
clg-ai-main/
│
├── college_ai_.py
├── College_AI_.ipynb
├── requirements.txt
├── README.md
│
└── __pycache__/
```

### Files

| File                | Description                   |
| ------------------- | ----------------------------- |
| `college_ai_.py`    | Main AI assistant application |
| `College_AI_.ipynb` | Jupyter/Google Colab notebook |
| `requirements.txt`  | Python dependencies           |
| `README.md`         | Project documentation         |

> The `.venv` folder should generally **not be uploaded to GitHub**. Add it to `.gitignore`.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd clg-ai-main
```

Replace `YOUR-USERNAME/YOUR-REPOSITORY` with your GitHub repository.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The project's `requirements.txt` currently requires:

```text
gradio>=5.0.0
```

---

# 🤖 Configure Llamafile

The application expects a local Llamafile server at:

```text
http://127.0.0.1:8080
```

Start the Llamafile server with the Qwen3-4B GGUF model:

```powershell
.\llamafile-0.10.5.exe -m qwen3-4b-thinking-2507.Q4_K_M.gguf --port 8080 --host 127.0.0.1
```

The application communicates with:

```text
http://127.0.0.1:8080/v1/chat/completions
```

---

# ▶️ Run the Application

After starting the local AI server:

```bash
python college_ai_.py
```

The application uses port:

```text
7860
```

Open your browser and visit:

```text
http://127.0.0.1:7860
```

---

# 💬 Example Questions

You can ask questions such as:

### 💰 Fees

```text
What is the annual fee for 2026-27?
```

```text
Is the fee same for all departments?
```

```text
What is the tuition fee?
```

### 📅 Timetable

```text
What is my Monday timetable?
```

```text
What classes do I have on Wednesday?
```

```text
When is the lunch break?
```

### 👨‍🏫 Faculty

```text
Who teaches Computer Networks?
```

```text
Who teaches Cloud Computing?
```

```text
List all faculty names and initials.
```

### 📚 Academic Information

```text
Give me the VTU subject codes.
```

```text
When do 5th semester classes start?
```

```text
Who is the principal and dean?
```

---

# 🔐 Privacy

One of the main goals of the project is **local AI inference**.

The application connects to a local server:

```text
127.0.0.1:8080
```

This allows uncatalogued questions to be processed using the locally running model instead of requiring a cloud AI API.

---

# ⚡ Key Advantages

| Feature                            | MITT College AI Assistant |
| ---------------------------------- | ------------------------- |
| College-specific information       | ✅                         |
| Local AI model                     | ✅                         |
| Gradio interface                   | ✅                         |
| Timetable support                  | ✅                         |
| Faculty information                | ✅                         |
| Fee information                    | ✅                         |
| Streaming responses                | ✅                         |
| Cloud API required for local model | ❌                         |
| Modern dark UI                     | ✅                         |

---

# 🎯 Project Objectives

* Build a useful AI assistant for college students.
* Provide quick access to academic information.
* Reduce the time required to search college information manually.
* Demonstrate local Large Language Model integration.
* Learn practical AI application development.
* Build an interactive Python-based AI interface.

---

# 🔮 Future Improvements

Possible improvements include:

* 🔎 RAG-based document search
* 📄 PDF/college handbook integration
* 🗃️ Vector database integration
* 🌐 Automatic college website crawling
* 📱 Mobile-friendly interface
* 🧑‍🎓 Student-specific authentication
* 📢 College notices and announcements
* 🗓️ Automatic timetable updates
* 💬 Conversation history
* 🎤 Voice input and output
* 🌍 Kannada and multilingual support

---

# 👨‍💻 Author

**Mahadev Prasad L**

🎓 B.E. Artificial Intelligence & Data Science
🏫 Maharaja Institute of Technology Thandavapura
📚 VTU — 3rd Year / 5th Semester

---

# 📜 License

This project is developed for **educational and academic purposes**.

You are free to modify and improve the project for learning and development.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ **Star** on GitHub.

**Made with Python, AI and ❤️ for students.**
