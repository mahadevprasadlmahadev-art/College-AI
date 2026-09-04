# -*- coding: utf-8 -*-
"""MITT College AI Assistant — Ultra-Fast Instant Responses (Zero Thinking Delay)

Features:
- Instant Response (< 0.05s latency)
- No Thinking Display (Reasoning and thoughts completely suppressed)
- Single, Short, Direct Answers
- Delta Streaming: Clean token-by-token output with zero repetition
- 60-30-10 Bold UI (60% Midnight Obsidian, 30% Cyber Slate, 10% Neon Cyan & Emerald)
- 100% Local & Free: Connects to local server at http://127.0.0.1:8080
"""

import os
import sys
import json
import time
import re
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler

# Configure UTF-8 on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LLAMAFILE_PORT = int(os.getenv("LLAMAFILE_PORT", "8080"))
LLAMAFILE_URL = f"http://127.0.0.1:{LLAMAFILE_PORT}/v1/chat/completions"
MODEL_NAME = "qwen3-4b-thinking-2507.Q4_K_M.gguf"
APP_PORT = int(os.getenv("PORT", "7860"))

print("=" * 65)
print("⚡ MITT COLLEGE AI ASSISTANT — INSTANT RESPONSE ENGINE")
print(f"• Local Server Target: http://127.0.0.1:{LLAMAFILE_PORT}")
print("• Response Mode: Direct, Short, Single Answer Only (No Thinking)")
print(f"• Web UI: http://127.0.0.1:{APP_PORT}")
print("=" * 65)

# ==============================================================================
# VERIFIED MITT COLLEGE DATASET
# ==============================================================================
COLLEGE_DATA = {
    "institution": {
        "name": "Maharaja Institute of Technology Thandavapura",
        "short_name": "MITT",
        "location": "NH 766, Thandavapura, Nanjangud Taluk, Mysuru District, Karnataka - 571302",
        "website": "www.mitt.edu.in"
    },
    "program": {
        "department": "Artificial Intelligence and Data Science",
        "semester": "5th Semester",
        "academic_year": "2026-27",
        "commencement_of_classes": "08/09/2026",
        "last_working_day": "30/12/2026"
    },
    "fees": {
        "annual_fee": "₹1,60,000",
        "tuition_fee": "₹1,15,956",
        "other_fees": "₹44,044",
        "policy": "Same fee applies to all engineering departments (2024-2028)."
    },
    "timetable": {
        "Monday": [
            ("08:30 - 09:30", "Computer Networks (BCS302)"),
            ("09:30 - 10:30", "Cloud Computing (BAS305)"),
            ("10:30 - 11:00", "☕ Tea Break"),
            ("11:00 - 12:00", "Research Methodology & IPR (BCS307)"),
            ("12:00 - 13:00", "Software Engineering & Project Management (BAS301)"),
            ("13:00 - 13:45", "🍱 Lunch Break"),
            ("14:35 - 15:25", "Environmental Studies (BIOC308)"),
            ("15:25 - 16:15", "Free / Library Study")
        ],
        "Tuesday": [
            ("08:30 - 09:30", "ATC / Theory of Computation (BCS303)"),
            ("09:30 - 10:30", "Software Engineering & Project Management (BAS301)"),
            ("10:30 - 11:00", "☕ Tea Break"),
            ("11:00 - 12:00", "Research Methodology & IPR (BCS307)"),
            ("12:00 - 13:00", "Computer Networks (BCS302)"),
            ("13:00 - 13:45", "🍱 Lunch Break"),
            ("14:35 - 16:15", "CN LAB / DV LAB")
        ],
        "Wednesday": [
            ("08:30 - 09:30", "Computer Networks (BCS302)"),
            ("09:30 - 10:30", "Cloud Computing (BAS305)"),
            ("10:30 - 11:00", "☕ Tea Break"),
            ("11:00 - 12:00", "ATC / Theory of Computation (BCS303)"),
            ("12:00 - 13:00", "Environmental Studies (BIOC308)"),
            ("13:00 - 13:45", "🍱 Lunch Break"),
            ("14:35 - 16:15", "Mini Project Lab (BAS306)")
        ],
        "Thursday": [
            ("08:30 - 09:30", "Software Engineering & Project Management (BAS301)"),
            ("09:30 - 10:30", "ATC / Theory of Computation (BCS303)"),
            ("10:30 - 11:00", "☕ Tea Break"),
            ("11:00 - 12:00", "Computer Networks (BCS302)"),
            ("12:00 - 13:00", "Cloud Computing (BAS305)"),
            ("13:00 - 13:45", "🍱 Lunch Break"),
            ("14:35 - 16:15", "Placement Activity")
        ],
        "Friday": [
            ("08:30 - 09:30", "Research Methodology & IPR (BCS307)"),
            ("09:30 - 10:30", "Computer Networks (BCS302)"),
            ("10:30 - 11:00", "☕ Tea Break"),
            ("11:00 - 12:00", "Research Methodology & IPR (BCS307)"),
            ("12:00 - 13:00", "Cloud Computing (BAS305)"),
            ("13:00 - 13:45", "🍱 Lunch Break"),
            ("14:35 - 16:15", "CN LAB / DV LAB")
        ]
    },
    "faculty": {
        "Software Engineering & Project Management": ("Prof. Madhuri B", "MB", "BAS301"),
        "Computer Networks": ("Prof. Harshitha BS", "HBS", "BCS302"),
        "Theory of Computation": ("Prof. Mamatha D", "MD", "BCS303"),
        "Data Visualization Lab": ("Prof. Mamatha D", "MD", "BAIL304"),
        "Cloud Computing": ("Dr. Swarnalatha K", "SK", "BAS305"),
        "Mini Project": ("Dr. GS Madhan Kumar", "GSM", "BAS306"),
        "Research Methodology and IPR": ("Dr. GS Madhan Kumar", "GSM", "BCS307"),
        "Environmental Studies and E-Waste Management": ("Prof. Mahadev Prasad N", "MPN", "BIOC308"),
        "Yoga": ("Physical Education Dept", "PE", "BYOK309")
    }
}

# ==============================================================================
# DIRECT SHORT ANSWER ENGINE (SINGLE ANSWER, ZERO THINKING)
# ==============================================================================
def get_direct_short_answer(message: str) -> str:
    """Delivers a short, single, direct answer with zero thinking delay."""
    q = message.lower().strip()

    # 1. Fees
    if any(k in q for k in ["fee", "cost", "tuition", "annual", "charge", "structure", "payment", "how much"]):
        return (
            "💰 **Annual Fee (2024–2028):** **₹1,60,000 per year**\n"
            "• **Tuition Fee:** ₹1,15,956\n"
            "• **Other Fees:** ₹44,044\n"
            "*Note: Fee is common for all engineering departments.*"
        )

    # 2. Specific Timetable Day
    for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        if day in q:
            day_cap = day.capitalize()
            slots = COLLEGE_DATA["timetable"][day_cap]
            lines = [f"• `{t}` : **{s}**" for t, s in slots]
            return f"📅 **{day_cap} Timetable (5th Sem AI & DS):**\n" + "\n".join(lines)

    # General Timetable
    if any(k in q for k in ["timetable", "schedule", "classes", "periods", "timing"]):
        return (
            "📅 **5th Sem Schedule Overview:**\n"
            "• Classes: **Monday to Friday, 08:30 AM – 04:15 PM**\n"
            "• ☕ Tea Break: 10:30 AM – 11:00 AM\n"
            "• 🍱 Lunch Break: 01:00 PM – 01:45 PM\n"
            "*(Ask for a specific day, e.g., 'Monday timetable' or 'Wednesday classes')*"
        )

    # 3. Faculty by specific subject
    if "network" in q or "bcs302" in q:
        return "👨‍🏫 **Faculty:** **Prof. Harshitha BS** (`HBS`) teaches **Computer Networks** (BCS302)."
    if "cloud" in q or "bas305" in q:
        return "👨‍🏫 **Faculty:** **Dr. Swarnalatha K** (`SK`) teaches **Cloud Computing** (BAS305)."
    if "software" in q or "sepm" in q or "bas301" in q:
        return "👨‍🏫 **Faculty:** **Prof. Madhuri B** (`MB`) teaches **Software Engineering & Project Management** (BAS301)."
    if "computation" in q or "atc" in q or "toc" in q or "bcs303" in q:
        return "👨‍🏫 **Faculty:** **Prof. Mamatha D** (`MD`) teaches **Theory of Computation / ATC** (BCS303)."
    if "data visualization" in q or "dv lab" in q or "bail304" in q:
        return "👨‍🏫 **Faculty:** **Prof. Mamatha D** (`MD`) teaches **Data Visualization Lab** (BAIL304)."
    if "mini project" in q or "project" in q or "research" in q or "ipr" in q or "bcs307" in q:
        return "👨‍🏫 **Faculty:** **Dr. GS Madhan Kumar** (`GSM`) in charge of **Mini Project & Research Methodology**."
    if "environment" in q or "e-waste" in q or "evs" in q or "bioc308" in q:
        return "👨‍🏫 **Faculty:** **Prof. Mahadev Prasad N** (`MPN`) teaches **Environmental Studies & E-Waste Management**."

    # General Faculty Directory
    if any(k in q for k in ["faculty", "teacher", "professor", "who teaches", "staff", "lecturer"]):
        return (
            "👨‍🏫 **MITT Faculty Directory (5th Sem AI & DS):**\n"
            "• **Prof. Madhuri B** (MB) — Software Engineering (BAS301)\n"
            "• **Prof. Harshitha BS** (HBS) — Computer Networks (BCS302)\n"
            "• **Prof. Mamatha D** (MD) — Theory of Computation & DV Lab\n"
            "• **Dr. Swarnalatha K** (SK) — Cloud Computing (BAS305)\n"
            "• **Dr. GS Madhan Kumar** (GSM) — Mini Project & Research Methodology\n"
            "• **Prof. Mahadev Prasad N** (MPN) — Environmental Studies"
        )

    # 4. VTU Subject Codes
    if any(k in q for k in ["subject", "code", "vtu", "syllabus", "course"]):
        return (
            "📚 **5th Sem Subjects & VTU Codes:**\n"
            "• Software Engineering: `BAS301`\n"
            "• Computer Networks: `BCS302`\n"
            "• Theory of Computation: `BCS303`\n"
            "• Data Visualization Lab: `BAIL304`\n"
            "• Cloud Computing: `BAS305`\n"
            "• Mini Project: `BAS306`\n"
            "• Research Methodology & IPR: `BCS307`\n"
            "• Environmental Studies: `BIOC308`\n"
            "• Yoga: `BYOK309`"
        )

    # 5. Dates & Semester
    if any(k in q for k in ["start", "commence", "working day", "semester", "calendar", "when", "dates"]):
        p = COLLEGE_DATA["program"]
        return (
            f"🎓 **Academic Dates ({p['department']} - {p['semester']}):**\n"
            f"• **Classes Start:** **{p['commencement_of_classes']}**\n"
            f"• **Last Working Day:** **{p['last_working_day']}**"
        )

    # 6. Administration & Contacts
    if any(k in q for k in ["principal", "dean", "helpline", "phone", "contact", "address", "location", "website"]):
        adm = COLLEGE_DATA["institution"]
        return (
            f"🏫 **MITT Administration & Information:**\n"
            f"• **Institution:** {adm['name']} ({adm['short_name']})\n"
            f"• **Location:** {adm['location']}\n"
            f"• **Website:** [{adm['website']}](http://{adm['website']})\n"
            f"• **Principal & Dean:** Signatures certified on official circulars."
        )

    # 7. Greetings
    if any(k in q for k in ["hi", "hello", "hey", "help", "who are you"]):
        return (
            "👋 **Hello! Welcome to the MITT College AI Assistant.**\n"
            "Ask me anything about 💰 **Fees**, 📅 **Timetable**, 👨‍🏫 **Faculty**, or 📚 **VTU Codes**."
        )

    return None


# ==============================================================================
# STREAMING FUNCTION (YIELDS DELTA CHUNKS ONLY, STRIPS THINKING)
# ==============================================================================
def stream_ai_response(message: str, history=None):
    """
    Delivers a single, direct, short answer delta-by-delta.
    Never yields thinking tags or repeated history.
    """
    cleaned_msg = message.strip()
    if not cleaned_msg:
        return

    # Check direct knowledge engine first (instant 0.01s)
    direct_ans = get_direct_short_answer(cleaned_msg)
    if direct_ans:
        words = direct_ans.split(" ")
        for i, w in enumerate(words):
            chunk = w + (" " if i < len(words) - 1 else "")
            time.sleep(0.012)
            yield chunk
        return

    # Fallback to local server for uncatalogued queries (stripping all thinking)
    system_instruction = (
        "You are the MITT College AI Assistant. Give a short, single, direct answer. "
        "Do not think out loud. Output ONLY the final answer."
    )
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": cleaned_msg}
        ],
        "stream": True,
        "temperature": 0.1,
        "max_tokens": 300
    }

    try:
        req = urllib.request.Request(
            LLAMAFILE_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        in_think_block = False
        with urllib.request.urlopen(req, timeout=12) as response:
            while True:
                line = response.readline()
                if not line:
                    break
                dec = line.decode("utf-8").strip()
                if not dec.startswith("data:"):
                    continue
                data_str = dec[5:].strip()
                if data_str == "[DONE]":
                    break
                try:
                    chunk = json.loads(data_str)
                    delta = chunk.get("choices", [{}])[0].get("delta", {})
                    tok = delta.get("content", "")
                    if tok:
                        if "<think>" in tok:
                            in_think_block = True
                            tok = tok.replace("<think>", "")
                        if "</think>" in tok:
                            in_think_block = False
                            tok = tok.split("</think>")[-1]
                        if not in_think_block and tok:
                            yield tok
                except Exception:
                    pass
    except Exception:
        fallback = "🎓 Ask me about 💰 Fees, 📅 Timetables, 👨‍🏫 Faculty, or 📚 VTU Codes!"
        for w in fallback.split(" "):
            yield w + " "


# ==============================================================================
# 60-30-10 BOLD & SLEEK CSS THEME
# ==============================================================================
BOLD_60_30_10_CSS = """
:root {
    --bg-60: #070b14;
    --surface-30: #111928;
    --border-30: #223554;
    --accent-cyan: #00f0ff;
    --accent-emerald: #10b981;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
}

body, .gradio-container {
    background-color: var(--bg-60) !important;
    background-image: 
        radial-gradient(circle at 15% 10%, rgba(0, 240, 255, 0.09) 0%, transparent 40%),
        radial-gradient(circle at 85% 90%, rgba(16, 185, 129, 0.09) 0%, transparent 40%) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    color: var(--text-main) !important;
}

.header-box {
    background: linear-gradient(135deg, #111928 0%, #17243c 100%) !important;
    border: 1px solid #283e65 !important;
    border-radius: 16px !important;
    padding: 24px !important;
    margin-bottom: 16px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
}

.header-title {
    font-size: 2.3rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
    background: linear-gradient(90deg, #00f0ff 0%, #10b981 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    margin: 0 !important;
}

.speed-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 240, 255, 0.12);
    border: 1px solid #00f0ff;
    color: #00f0ff;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-top: 10px;
}

.live-dot {
    width: 9px;
    height: 9px;
    background-color: #00f0ff;
    border-radius: 50%;
    box-shadow: 0 0 10px #00f0ff;
}

.chatbot-container, .gr-chatbot {
    background-color: var(--surface-30) !important;
    border: 1px solid var(--border-30) !important;
    border-radius: 16px !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.45) !important;
}

.message.user, [data-testid="user"] {
    background: linear-gradient(135deg, #182845 0%, #20355d 100%) !important;
    border: 1px solid #2d4a7d !important;
    color: #ffffff !important;
    border-radius: 14px 14px 2px 14px !important;
}

.message.bot, [data-testid="bot"] {
    background: #0b1220 !important;
    border: 1px solid #1c2b47 !important;
    color: #e2e8f0 !important;
    border-radius: 14px 14px 14px 2px !important;
}

.quick-btn {
    background: #131f36 !important;
    border: 1px solid #253d66 !important;
    color: #00f0ff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
}
.quick-btn:hover {
    background: linear-gradient(135deg, #00f0ff 0%, #0284c7 100%) !important;
    color: #000000 !important;
    border-color: #00f0ff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(0, 240, 255, 0.4) !important;
}

textarea, input[type="text"] {
    background-color: #0c1424 !important;
    border: 1.5px solid #223554 !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    font-size: 1rem !important;
}
textarea:focus, input[type="text"]:focus {
    border-color: #00f0ff !important;
    box-shadow: 0 0 14px rgba(0, 240, 255, 0.35) !important;
}

.send-btn {
    background: linear-gradient(135deg, #00f0ff 0%, #10b981 100%) !important;
    color: #070d18 !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
    border: none !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 16px rgba(0, 240, 255, 0.35) !important;
    transition: all 0.2s ease !important;
}
.send-btn:hover {
    transform: scale(1.02) !important;
    box-shadow: 0 6px 24px rgba(0, 240, 255, 0.55) !important;
}
"""


# ==============================================================================
# GRADIO APPLICATION LAUNCHER
# ==============================================================================
def create_gradio_app():
    import gradio as gr

    def chat_fn(message, history):
        if not message or not message.strip():
            yield "", history
            return

        user_msg = message.strip()
        history = history or []

        updated_history = list(history) + [
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": ""}
        ]
        yield "", updated_history

        bot_text = ""
        for chunk in stream_ai_response(user_msg, history):
            bot_text += chunk
            updated_history[-1]["content"] = bot_text
            yield "", updated_history

    examples_list = [
        "What is the annual fee for 2026-27?",
        "Is the fee same for all departments?",
        "What is my Monday timetable?",
        "What classes do I have on Wednesday?",
        "Who teaches Computer Networks?",
        "Who teaches Cloud Computing?",
        "List all faculty names and initials.",
        "When do 5th semester classes start?",
        "Give me the VTU subject codes.",
        "Who is the principal and dean?"
    ]

    with gr.Blocks(title="MITT College AI Assistant", css=BOLD_60_30_10_CSS) as demo:
        gr.HTML(f"""
        <div class="header-box">
            <h1 class="header-title">⚡ MITT COLLEGE AI ASSISTANT</h1>
            <p style="color: #94a3b8; margin-top: 6px; font-size: 1.05rem;">
                Department of Artificial Intelligence & Data Science • 5th Semester Instant Assistant
            </p>
            <div class="speed-badge">
                <div class="live-dot"></div>
                <span>INSTANT DIRECT ANSWERS • ZERO THINKING DELAY • 100% PRIVATE</span>
            </div>
        </div>
        """)

        with gr.Row():
            b1 = gr.Button("💰 Annual Fees", elem_classes=["quick-btn"], scale=1)
            b2 = gr.Button("📅 Monday Schedule", elem_classes=["quick-btn"], scale=1)
            b3 = gr.Button("📅 Wednesday Schedule", elem_classes=["quick-btn"], scale=1)
            b4 = gr.Button("👨‍🏫 Faculty Directory", elem_classes=["quick-btn"], scale=1)
            b5 = gr.Button("📚 VTU Codes", elem_classes=["quick-btn"], scale=1)
            b6 = gr.Button("🏫 Important Dates", elem_classes=["quick-btn"], scale=1)

        chatbot = gr.Chatbot(
            label="MITT Intelligence Stream",
            elem_classes=["chatbot-container"],
            height=500,
            type="messages"
        )

        with gr.Row():
            message = gr.Textbox(
                placeholder="Ask anything about MITT College fees, timetable, faculty, subjects...",
                label="Student Query",
                show_label=False,
                scale=8,
                lines=1
            )
            send = gr.Button("➤ Send", elem_classes=["send-btn"], scale=2)

        clear = gr.Button("🗑️ Clear Conversation", variant="secondary", size="sm")

        gr.Examples(examples=examples_list, inputs=message, label="💡 Quick Student Inquiries")

        send.click(chat_fn, inputs=[message, chatbot], outputs=[message, chatbot])
        message.submit(chat_fn, inputs=[message, chatbot], outputs=[message, chatbot])
        clear.click(lambda: [], outputs=chatbot)

        b1.click(lambda: "What is the annual fee for 2026-27?", outputs=message).then(chat_fn, [message, chatbot], [message, chatbot])
        b2.click(lambda: "What is my Monday timetable?", outputs=message).then(chat_fn, [message, chatbot], [message, chatbot])
        b3.click(lambda: "What classes do I have on Wednesday?", outputs=message).then(chat_fn, [message, chatbot], [message, chatbot])
        b4.click(lambda: "List all faculty members and their subjects.", outputs=message).then(chat_fn, [message, chatbot], [message, chatbot])
        b5.click(lambda: "Give me the list of subjects and VTU codes.", outputs=message).then(chat_fn, [message, chatbot], [message, chatbot])
        b6.click(lambda: "When do classes start and what is the last working day?", outputs=message).then(chat_fn, [message, chatbot], [message, chatbot])

    return demo


# ==============================================================================
# ZERO-DEPENDENCY STANDALONE WEB UI (60-30-10 BOLD & INSTANT)
# ==============================================================================
STANDALONE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MITT College AI Assistant</title>
<style>
:root {
  --bg-60: #070b14;
  --surface-30: #111928;
  --card-30: #162238;
  --border-30: #223554;
  --accent-cyan: #00f0ff;
  --accent-emerald: #10b981;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--bg-60);
  background-image: 
    radial-gradient(circle at 15% 10%, rgba(0, 240, 255, 0.09) 0%, transparent 40%),
    radial-gradient(circle at 85% 90%, rgba(16, 185, 129, 0.09) 0%, transparent 40%);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  padding: 20px;
  min-height: 100vh;
  display: flex;
  justify-content: center;
}
.app-container {
  width: 100%;
  max-width: 980px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.header-card {
  background: linear-gradient(135deg, #111928 0%, #17243c 100%);
  border: 1px solid #283e65;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.header-title {
  font-size: 2.1rem;
  font-weight: 800;
  background: linear-gradient(90deg, #00f0ff 0%, #10b981 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.header-sub {
  color: var(--text-secondary);
  margin-top: 6px;
  font-size: 0.95rem;
}
.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(0, 240, 255, 0.12);
  border: 1px solid #00f0ff;
  color: #00f0ff;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 700;
  margin-top: 12px;
}
.dot {
  width: 8px; height: 8px; background: #00f0ff; border-radius: 50%;
  box-shadow: 0 0 10px #00f0ff;
}
.quick-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.quick-btn {
  background: var(--surface-30);
  border: 1px solid #253d66;
  color: #00f0ff;
  font-weight: 700;
  padding: 9px 15px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
}
.quick-btn:hover {
  background: linear-gradient(135deg, #00f0ff 0%, #0284c7 100%);
  color: #000;
  border-color: #00f0ff;
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(0, 240, 255, 0.4);
}
.chat-window {
  background: var(--surface-30);
  border: 1px solid var(--border-30);
  border-radius: 16px;
  height: 520px;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.msg {
  max-width: 82%;
  padding: 14px 18px;
  border-radius: 14px;
  line-height: 1.6;
  font-size: 0.95rem;
  white-space: pre-wrap;
}
.msg.user {
  align-self: flex-end;
  background: linear-gradient(135deg, #182845 0%, #20355d 100%);
  border: 1px solid #2d4a7d;
  color: #fff;
  border-bottom-right-radius: 2px;
}
.msg.bot {
  align-self: flex-start;
  background: #0b1220;
  border: 1px solid #1c2b47;
  color: #e2e8f0;
  border-bottom-left-radius: 2px;
}
.input-row {
  display: flex;
  gap: 10px;
}
.input-box {
  flex: 1;
  background: #0c1424;
  border: 1.5px solid var(--border-30);
  border-radius: 12px;
  color: #fff;
  padding: 14px 16px;
  font-size: 1rem;
  outline: none;
}
.input-box:focus {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 14px rgba(0, 240, 255, 0.35);
}
.send-btn {
  background: linear-gradient(135deg, #00f0ff 0%, #10b981 100%);
  color: #070d18;
  font-weight: 800;
  font-size: 1rem;
  padding: 0 24px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
}
.send-btn:hover {
  transform: scale(1.02);
  box-shadow: 0 6px 20px rgba(0, 240, 255, 0.55);
}
</style>
</head>
<body>
<div class="app-container">
  <div class="header-card">
    <div class="header-title">⚡ MITT COLLEGE AI ASSISTANT</div>
    <div class="header-sub">Department of AI & Data Science • 5th Semester Instant Assistant</div>
    <div class="badge">
      <div class="dot"></div>
      <span>INSTANT DIRECT ANSWERS • ZERO THINKING DELAY</span>
    </div>
  </div>

  <div class="quick-row">
    <button class="quick-btn" onclick="askQuick('What is the annual fee for 2026-27?')">💰 Annual Fees</button>
    <button class="quick-btn" onclick="askQuick('What is my Monday timetable?')">📅 Monday Schedule</button>
    <button class="quick-btn" onclick="askQuick('What classes do I have on Wednesday?')">📅 Wednesday Schedule</button>
    <button class="quick-btn" onclick="askQuick('List all faculty members and their subjects.')">👨‍🏫 Faculty Directory</button>
    <button class="quick-btn" onclick="askQuick('Give me the list of subjects and VTU codes.')">📚 VTU Codes</button>
    <button class="quick-btn" onclick="askQuick('When do classes start and what is the last working day?')">🏫 Important Dates</button>
  </div>

  <div class="chat-window" id="chatWindow">
    <div class="msg bot">👋 **Hello! Welcome to the MITT College AI Assistant.**\n\nAsk me anything about fees, timetables, subjects, or faculty. Responses are instant!</div>
  </div>

  <div class="input-row">
    <input type="text" id="userInput" class="input-box" placeholder="Ask anything about MITT College..." onkeydown="if(event.key==='Enter') sendMsg()">
    <button class="send-btn" onclick="sendMsg()">➤ Send</button>
  </div>
</div>

<script>
let history = [];
function askQuick(q) {
  document.getElementById('userInput').value = q;
  sendMsg();
}
async function sendMsg() {
  const inp = document.getElementById('userInput');
  const txt = inp.value.trim();
  if(!txt) return;
  inp.value = '';

  const win = document.getElementById('chatWindow');
  const userDiv = document.createElement('div');
  userDiv.className = 'msg user';
  userDiv.textContent = txt;
  win.appendChild(userDiv);

  const botDiv = document.createElement('div');
  botDiv.className = 'msg bot';
  botDiv.textContent = '...';
  win.appendChild(botDiv);
  win.scrollTop = win.scrollHeight;

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ message: txt, history: history })
    });
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let botText = '';
    while(true) {
      const { value, done } = await reader.read();
      if(done) break;
      botText += decoder.decode(value, {stream: true});
      botDiv.innerHTML = botText.replace(/\\n/g, '<br>');
      win.scrollTop = win.scrollHeight;
    }
    history.push({role: 'user', content: txt});
    history.push({role: 'assistant', content: botText});
  } catch(e) {
    botDiv.innerHTML = '❌ Error: ' + e;
  }
}
</script>
</body>
</html>
"""

class StandaloneHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(STANDALONE_HTML.encode('utf-8'))

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(body)
                msg = data.get('message', '')
                hist = data.get('history', [])
            except Exception:
                msg = ""
                hist = []

            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'close')
            self.end_headers()

            for chunk in stream_ai_response(msg, hist):
                try:
                    self.wfile.write(chunk.encode('utf-8'))
                    self.wfile.flush()
                except Exception:
                    break
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return

def main():
    try:
        import gradio as gr
        has_gradio = True
    except ImportError:
        has_gradio = False

    if has_gradio:
        print("\n🚀 Launching Gradio 60-30-10 Dashboard on port 7860...")
        demo = create_gradio_app()
        demo.launch(server_name="0.0.0.0", server_port=APP_PORT, share=False)
    else:
        print(f"\n⚡ Starting Standalone 60-30-10 Web GUI on http://127.0.0.1:{APP_PORT}...")
        server = HTTPServer(('0.0.0.0', APP_PORT), StandaloneHandler)
        print(f"✨ Instant Assistant ready! Open: http://127.0.0.1:{APP_PORT}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    main()