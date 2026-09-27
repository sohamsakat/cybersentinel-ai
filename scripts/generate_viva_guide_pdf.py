import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


class NumberedCanvas(canvas.Canvas):
    """
    Canvas that performs a two-pass calculation to display total page count: 'Page X of Y'
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 755, "CYBERSENTINEL AI  |  Viva Voce Master Guide (Beginner to Pro)")
            self.drawRightString(572, 755, "Final Year B.Tech Engineering Project")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(40, 748, 572, 748)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(40, 45, 572, 45)
        self.drawString(40, 32, "Confidential - Final Year Engineering Project Defense Guide")
        self.drawRightString(572, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_viva_guide_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=55,
        bottomMargin=55,
    )

    styles = getSampleStyleSheet()

    # Color Palette
    c_primary = colors.HexColor("#0f172a")    # Slate 900
    c_accent = colors.HexColor("#0284c7")     # Sky 600
    c_purple = colors.HexColor("#7c3aed")     # Violet 600
    c_dark = colors.HexColor("#1e293b")       # Slate 800
    c_muted = colors.HexColor("#64748b")      # Slate 500
    c_box_bg = colors.HexColor("#f8fafc")     # Slate 50
    c_box_border = colors.HexColor("#e2e8f0") # Slate 200
    c_alert_bg = colors.HexColor("#fef2f2")   # Red 50
    c_alert_border = colors.HexColor("#fecaca")# Red 200

    # Custom Typography Styles
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=c_primary,
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=c_accent,
        spaceAfter=14,
    )
    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=c_primary,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True,
    )
    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=c_accent,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True,
    )
    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=c_dark,
        spaceAfter=6,
    )
    body_bold = ParagraphStyle(
        "Body_Bold",
        parent=body_style,
        fontName="Helvetica-Bold",
    )
    code_style = ParagraphStyle(
        "Code_Custom",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#090d16"),
    )
    qa_q_style = ParagraphStyle(
        "QA_Question",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=c_primary,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True,
    )
    qa_simple_style = ParagraphStyle(
        "QA_Simple",
        parent=body_style,
        textColor=colors.HexColor("#0369a1"),
        fontSize=9,
        leading=12.5,
    )
    qa_tech_style = ParagraphStyle(
        "QA_Tech",
        parent=body_style,
        textColor=c_dark,
        fontSize=9,
        leading=12.5,
    )

    story = []

    def make_box(content_flowables, bg_color=c_box_bg, border_color=c_box_border):
        t = Table([[content_flowables]], colWidths=[532])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg_color),
            ("BOX", (0, 0), (-1, -1), 1, border_color),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        return t

    # =========================================================================
    # COVER / HEADER
    # =========================================================================
    story.append(Paragraph("CYBERSENTINEL AI", title_style))
    story.append(Paragraph("The Ultimate Viva Voce Master Guide: Explained Like You're 10 Years Old", subtitle_style))
    story.append(Paragraph(
        "<b>Project Title:</b> CyberSentinel AI: An Intelligent Security Operations Center (SOC) Assistant using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG)<br/>"
        "<b>Domain:</b> Artificial Intelligence & Cybersecurity (SecOps, RAG, SIEM, Full-Stack Software Engineering)<br/>"
        "<b>Target Audience:</b> University Viva Examiners, Campus Placement Recruiters, and Final-Year Students",
        body_style
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceBefore=6, spaceAfter=14))

    # =========================================================================
    # CHAPTER 1: THE BIG PICTURE
    # =========================================================================
    story.append(Paragraph("Chapter 1: The Big Picture (What is CyberSentinel AI?)", h1_style))

    c1_content = [
        Paragraph("<b>1. The 10-Year-Old Story: The Grand Bank and the CCTV Room</b>", body_bold),
        Paragraph(
            "Imagine a huge bank with 1,000 doors, 5,000 windows, and hundreds of lockers. Inside every room, there is a small diary. "
            "Every time someone touches a door, enters a room, or opens a computer, the computer writes a single line in its diary: "
            "<i>'Door 4 opened by Alice at 10:02 AM'</i> or <i>'Wrong password typed for Bob at 10:05 AM'</i>. These diary lines are called <b>LOGS</b>.",
            body_style
        ),
        Spacer(1, 4),
        Paragraph("<b>2. What is a SOC (Security Operations Center)?</b>", body_bold),
        Paragraph(
            "A <b>SOC</b> is the central security control room with hundreds of TV screens. The security guards (called <i>SOC Analysts</i>) "
            "sit there watching the computers to make sure no thief (hacker) is breaking in.",
            body_style
        ),
        Spacer(1, 4),
        Paragraph("<b>3. The Pain: Alert Fatigue (Why Humans Can't Do It Alone)</b>", body_bold),
        Paragraph(
            "Every single day, a company creates <b>100,000+ log lines</b>! Over 99% of them are harmless everyday things (people checking email, printer printing). "
            "A human guard's eyes get tired. If a real hacker tries 500 secret passwords at 3:00 AM, the guard misses it because it is buried under a mountain of boring logs! "
            "This is called <b>Alert Fatigue</b>.",
            body_style
        ),
        Spacer(1, 4),
        Paragraph("<b>4. The Hero: What CyberSentinel AI Does</b>", body_bold),
        Paragraph(
            "<b>CyberSentinel AI</b> is like an untiring, genius robot detective that sits in the control room. "
            "It reads all 100,000 diary pages in a few seconds, ignores the boring normal stuff, instantly spots the thief, "
            "figures out what trick the thief is using, calculates how dangerous it is (0 to 100 score), gives the human guard a step-by-step checklist to stop them, "
            "and prints out an official police report in PDF format with 1 click!",
            body_style
        ),
    ]
    story.append(make_box(c1_content))
    story.append(Spacer(1, 12))

    # =========================================================================
    # CHAPTER 2: THE AI MAGIC
    # =========================================================================
    story.append(Paragraph("Chapter 2: The AI Magic (LLMs, RAG, and ChromaDB)", h1_style))

    c2_content = [
        Paragraph("<b>1. What is an LLM (Large Language Model)?</b>", body_bold),
        Paragraph(
            "An <b>LLM</b> (like Google Gemini or ChatGPT) is like a super-smart student who has read millions of books and can talk like a human expert. "
            "You give it messy text, and it explains it in simple, beautiful English.",
            body_style
        ),
        Spacer(1, 3),
        Paragraph("<b>2. What is 'Hallucination' (And why is it deadly in Cybersecurity)?</b>", body_bold),
        Paragraph(
            "Sometimes, when a student doesn't know the exact answer to an exam question, they <b>guess</b> and invent a fake fact with total confidence! "
            "In AI, this is called a <b>Hallucination</b>. In cybersecurity, hallucinations are deadly: if an AI makes up a fake hacker technique or invents a wrong firewall command, the company gets hacked!",
            body_style
        ),
        Spacer(1, 3),
        Paragraph("<b>3. What is RAG (Retrieval-Augmented Generation)?</b>", body_bold),
        Paragraph(
            "<b>RAG</b> turns a closed-book memory exam into an <b>open-book exam</b>! "
            "Instead of asking the LLM to guess from its memory, CyberSentinel AI does this:<br/>"
            "• <i>Step 1 (Retrieve):</i> The system takes the suspicious log and searches a trusted cybersecurity library.<br/>"
            "• <i>Step 2 (Augment):</i> It hands the exact textbook page to the LLM.<br/>"
            "• <i>Step 3 (Generate):</i> The LLM reads only that verified page to write the explanation.<br/>"
            "<b>Result:</b> Exactly <b>ZERO Hallucinations</b>. Everything is 100% grounded in verified truth.",
            body_style
        ),
        Spacer(1, 3),
        Paragraph("<b>4. What is ChromaDB?</b>", body_bold),
        Paragraph(
            "<b>ChromaDB</b> is our <b>Vector Database</b>. Normal databases (like SQL) look for exact words. "
            "ChromaDB looks for <b>meaning</b>! It converts sentences into numbers (embeddings). "
            "If a log says <i>'bad password entered 10 times'</i>, ChromaDB instantly knows it means <i>'Brute Force Attack'</i> even though the words are completely different!",
            body_style
        ),
        Spacer(1, 3),
        Paragraph("<b>5. What is MITRE ATT&CK?</b>", body_bold),
        Paragraph(
            "<b>MITRE ATT&CK</b> is the world's official encyclopedia of every trick hackers use. "
            "Just like doctors have official names for diseases (like <i>Influenza</i>), cybersecurity teams have official codes for hacker tricks: "
            "<b>T1110</b> = Brute Force (guessing passwords), <b>T1548</b> = Privilege Escalation (becoming admin/root), <b>T1190</b> = Web App Exploit (SQL Injection).",
            body_style
        ),
    ]
    story.append(make_box(c2_content))
    story.append(Spacer(1, 14))

    # =========================================================================
    # CHAPTER 3: WEBSITE MODULES WALKTHROUGH
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 3: Tour of Every Website Module (What You See On Screen)", h1_style))
    story.append(Paragraph(
        "During your viva or interview demo, you will show the examiner each screen. Here is how to explain every single module with 100% clarity:",
        body_style
    ))

    modules = [
        ("1. Login & Roles (RBAC)", "Security Guard vs Police Chief Badge",
         "What it is: A dark, sleek login screen with two roles: Tier-1 Analyst (day-to-day triage) and Admin (full control).<br/>"
         "Why we have it: In real companies, junior analysts should not have permission to delete audit logs or change security configurations. We use JWT (JSON Web Tokens) with 1-click demo buttons for instant viva login."),

        ("2. Live Cyber Radar", "The YouTube Live Chat of Computer Logs",
         "What it is: The premier screen! Computer logs stream in from the bottom line-by-line just like YouTube live chat comments. Normal logs stream in quietly. The second an attacker strikes, the stream flashes RED with a '⚡ THREAT DETECTED' badge, and an animated AI Threat Card slides into the side panel.<br/>"
         "The Viva Secret: Has a red 'Simulate Attack Wave' button! Click it in front of the examiner to trigger an instant live cyber attack and watch the AI intercept it in real time!"),

        ("3. SOC Dashboard", "The Car Speedometer & Security Health Check",
         "What it is: Displays total correlated incidents, critical threat counts, a visual CVSS severity spectrum bar (Critical, High, Medium, Low), and top MITRE ATT&CK techniques.<br/>"
         "Why we have it: Gives executives and security managers a 5-second bird's-eye view of whether their enterprise is under attack right now."),

        ("4. Incidents & Triage", "The Police Detective's Case Files",
         "What it is: A searchable registry of all detected security crimes. You can filter by severity (Critical/High/Medium/Low) or status (Open, Investigating, Resolved).<br/>"
         "Why we have it: Allows analysts to organize, track, and assign active intrusions so nothing gets forgotten."),

        ("5. Incident Detail & NIST Playbook", "Crime Scene Investigation & Doctor's Prescription",
         "What it is: Deep-dive view of a single attack. Shows the calculated CVSS Risk Score (e.g. 95/100), attacker IP, target server, exact chronological log evidence, and an interactive checklist of the NIST SP 800-61 remediation playbook.<br/>"
         "Interactive Feature: You can click the checkboxes (e.g., '1. Block IP on firewall', '2. Reset user password') as you fix the issue!"),

        ("6. Log Ingestion & Normalizer", "The Universal Translator for Logs",
         "What it is: A file upload modal with drag-and-drop. Supports 4 formats: Windows Event (JSON), Linux Syslog (.log), Apache Web (.log), and Firewall (.csv).<br/>"
         "Why we have it: Translates logs written in completely different formats into one uniform standard called the Elastic Common Schema (ECS)."),

        ("7. SecOps AI Copilot", "The 24/7 Smart Cybersecurity Tutor",
         "What it is: An interactive AI chat window strictly grounded in MITRE ATT&CK and active incident logs.<br/>"
         "Why we have it: Analysts can ask: 'How do I block IP 198.51.100.45?' or 'Explain MITRE technique T1110', and the AI answers with verified mitigation steps and citations badges."),

        ("8. NIST PDF Report Generator", "The 1-Click Official Police Report",
         "What it is: A blue button on every incident that downloads a pixel-perfect, publication-grade incident report PDF.<br/>"
         "Why we have it: After stopping an attack, executives and compliance auditors need proof of what happened, who did it, root cause, and how it was fixed.")
    ]

    for m_title, m_analogy, m_desc in modules:
        m_content = [
            Paragraph(f"<b>{m_title}</b>  <font color='{c_accent.hexval()}'>({m_analogy})</font>", h2_style),
            Paragraph(m_desc, body_style),
        ]
        story.append(make_box(m_content))
        story.append(Spacer(1, 6))

    # =========================================================================
    # CHAPTER 4: TECH STACK UNDER THE HOOD
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 4: Under The Hood (The Code & Tech Stack)", h1_style))
    story.append(Paragraph(
        "Examiners will ask: <i>'Why did you use FastAPI instead of Django?'</i> or <i>'Why ChromaDB instead of SQLite for search?'</i> "
        "Here is the simple explanation of every piece of technology used:",
        body_style
    ))

    tech_table_data = [
        [Paragraph("<b>Technology</b>", body_bold), Paragraph("<b>What it does (Simple)</b>", body_bold), Paragraph("<b>Why we chose it (Technical Viva Answer)</b>", body_bold)],
        [
            Paragraph("<b>Python 3.11+</b>", body_style),
            Paragraph("The core brain of the application.", body_style),
            Paragraph("Standard language for AI, data processing, and cybersecurity parsing libraries.", body_style)
        ],
        [
            Paragraph("<b>FastAPI</b>", body_style),
            Paragraph("The speedy waiter taking orders from the screen.", body_style),
            Paragraph("High performance ASGI framework with native asynchronous async/await, automatic OpenAPI documentation, and strict Pydantic data validation.", body_style)
        ],
        [
            Paragraph("<b>React + Vite</b>", body_style),
            Paragraph("The glowing dark-theme screen you look at.", body_style),
            Paragraph("Blazing fast virtual DOM, component modularity, instant hot module reloading (HMR), and lightning 1-second production builds.", body_style)
        ],
        [
            Paragraph("<b>Tailwind CSS</b>", body_style),
            Paragraph("The paint and styling box.", body_style),
            Paragraph("Utility-first styling allowing cyber-themed neon glowing accents, responsive grid layouts, and custom scrollbars without CSS bloat.", body_style)
        ],
        [
            Paragraph("<b>ChromaDB</b>", body_style),
            Paragraph("The AI memory library.", body_style),
            Paragraph("Open-source, in-process vector database that performs cosine similarity search on MITRE ATT&CK embeddings with zero cloud API costs.", body_style)
        ],
        [
            Paragraph("<b>SQLite / PostgreSQL</b>", body_style),
            Paragraph("The sturdy file cabinet.", body_style),
            Paragraph("ACID-compliant relational database storing user credentials, incident records, and audit logs via SQLAlchemy ORM.", body_style)
        ],
        [
            Paragraph("<b>ReportLab</b>", body_style),
            Paragraph("The digital printing press.", body_style),
            Paragraph("Programmatic PDF generation engine creating multi-page, tamper-evident NIST SP 800-61 forensic triage documents.", body_style)
        ],
        [
            Paragraph("<b>Docker</b>", body_style),
            Paragraph("The self-contained lunchbox.", body_style),
            Paragraph("Packs the entire operating system, Python runtime, Node assets, and dependencies into one container so it runs identically anywhere.", body_style)
        ],
    ]

    t_tech = Table(tech_table_data, colWidths=[110, 150, 272])
    t_tech.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_tech)
    story.append(Spacer(1, 14))

    # =========================================================================
    # CHAPTER 5: TOP 15 VIVA QUESTIONS & WINNING ANSWERS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Chapter 5: Top 15 Viva Questions & Winning Answers", h1_style))
    story.append(Paragraph(
        "Here are the exact questions external examiners love to ask, with both a simple intuitive answer and the technical keywords that guarantee top marks:",
        body_style
    ))

    viva_qa = [
        ("Q1: What is the main novelty of your project compared to tools like Splunk?",
         "Simple: Splunk tells you 'Door 4 opened 500 times' and leaves you to figure out why. CyberSentinel AI uses AI to say: 'A thief is guessing passwords using trick T1110. Here is how dangerous it is, and here is your 4-step checklist to stop them.'",
         "Technical: Traditional SIEMs rely on static threshold alert rules. CyberSentinel AI introduces a cognitive RAG layer that correlates multi-source logs, retrieves MITRE ATT&CK tactics from a vector database, and generates automated NIST-compliant remediation playbooks."),

        ("Q2: What is your Base Research Paper?",
         "Simple: A recent IEEE/ACM paper on using RAG for cybersecurity log analysis.",
         "Technical: Our base paper is 'Retrieval-Augmented Generation for Automated Incident Response and Threat Intelligence Mapping in Modern SOCs' (ACM/IEEE 2024/2025). Its limitation was that it only tested offline alert benchmarks. We improved it by building an end-to-end full-stack system with raw log ingestion, live streaming radar, and exportable PDF reporting."),

        ("Q3: How do you guarantee the AI will never hallucinate in security?",
         "Simple: We never let the AI answer from its open memory. We give it an open-book test where it can only read verified MITRE ATT&CK documents from ChromaDB.",
         "Technical: We enforce strict RAG grounding. Incoming telemetry signatures query ChromaDB for top-k nearest semantic neighbors. The retrieved context and a strict Pydantic JSON schema are injected into the prompt, rejecting any ungrounded assertions."),

        ("Q4: How does your log normalization pipeline work?",
         "Simple: Different computers speak different languages (Windows speaks JSON, Linux speaks syslog). Our parser translates all of them into one single standard language.",
         "Technical: We implemented the Factory Pattern via BaseLogParser. Specialized parsers (Windows, Linux, Apache, Firewall) extract timestamp, source IP, user, and action into a standardized Pydantic NormalizedLogEvent model matching the Elastic Common Schema (ECS)."),

        ("Q5: How is the Risk Score calculated? Is it random?",
         "Simple: It's like a danger score from 0 to 100 based on clues. If someone knocks, it's 20. If they guess 50 passwords, it becomes 70. If they unlock the root admin account, it jumps to 95.",
         "Technical: It is an algorithmic CVSS-inspired mathematical model. It assigns a baseline from severity (Critical: 85, High: 70, Med: 50, Low: 25) and applies additive multipliers for attack progression (+10 for failed followed by success, +15 for privilege escalation, +8 for root/administrator targeting)."),

        ("Q6: Why ChromaDB instead of Pinecone or FAISS?",
         "Simple: Pinecone is cloud-only and costs money. FAISS is too low-level. ChromaDB runs right inside our server, is 100% free, and needs no internet during viva!",
         "Technical: Pinecone introduces external API latency, recurring costs, and confidentiality issues with sensitive security logs. FAISS lacks native document metadata filtering. ChromaDB provides in-process persistence, metadata filtering, and offline ONNX embedding execution."),

        ("Q7: What happens if your server has no internet during the viva demo?",
         "Simple: The system still works 100% perfectly! The AI memory is saved right on your laptop.",
         "Technical: Embeddings are generated locally via the cached all-MiniLM-L6-v2 ONNX runtime, and our deterministic RAG expert synthesizer formats grounded responses even with zero internet connectivity."),

        ("Q8: How does user authentication work in your application?",
         "Simple: When you type your password, the server scrambles it with bcrypt. If correct, it hands you a digital VIP pass (JWT token) stamped with your role.",
         "Technical: We implement stateless OAuth2 with JWT (JSON Web Tokens) signed via HS256. Passwords are salted and hashed using bcrypt (12 rounds). Route endpoints enforce Role-Based Access Control (RBAC) via FastAPI dependencies."),

        ("Q9: What is the difference between MITRE T1110 and T1078?",
         "Simple: T1110 is guessing the key to the door (Brute Force). T1078 is stealing a real guard's key and walking in quietly (Valid Accounts).",
         "Technical: T1110 (Brute Force) involves iterative password guessing or credential stuffing against authentication interfaces. T1078 (Valid Accounts) involves abusing legitimate, already-compromised credentials to evade defense detection."),

        ("Q10: What is the purpose of the Live Cyber Radar?",
         "Simple: To let humans watch the computers talk in real time, and watch the AI catch the bad guys live on screen.",
         "Technical: It simulates real-time SIEM syslog tailing. It ingests an event stream, highlights anomalous telemetry, and triggers asynchronous AI interceptor cards with MITRE technique mapping."),

        ("Q11: Why did you use FastAPI over Django?",
         "Simple: Django is a giant heavy truck. FastAPI is a lightning-fast sports car made specifically for APIs and AI.",
         "Technical: FastAPI is built on ASGI (Starlette + Uvicorn) with non-blocking async I/O, native Pydantic data validation, and 3x higher throughput compared to synchronous WSGI Django/Flask."),

        ("Q12: How do you protect against SQL Injection in your own app?",
         "Simple: We never let user text touch the database directly; we use an ORM translator.",
         "Technical: We use SQLAlchemy Object Relational Mapper (ORM), which compiles parameterized queries (prepared statements), completely neutralizing SQL injection vulnerabilities."),

        ("Q13: How does the PDF report generator work?",
         "Simple: When you click the button, Python uses ReportLab to draw lines, tables, colors, and text into a real PDF file and sends it to your downloads folder.",
         "Technical: backend/app/services/pdf_generator.py programmatically constructs a ReportLab Flowable document with custom TableStyles and streams it via FastAPI's StreamingResponse with application/pdf MIME type."),

        ("Q14: How does your Docker deployment work?",
         "Simple: Stage 1 builds the pretty React website. Stage 2 installs Python, copies the website into FastAPI, and runs everything on a single port.",
         "Technical: We use a multi-stage Dockerfile. Stage 1 (node:20-alpine) runs npm run build. Stage 2 (python:3.11-slim) installs backend dependencies, copies frontend/dist, and runs Uvicorn on ${PORT:-8000} with unified static serving."),

        ("Q15: What is the future scope of CyberSentinel AI?",
         "Simple: In the future, the robot won't just tell you how to block the hacker—it will click the button to block them automatically (SOAR automation), and handle millions of cloud logs from AWS and Azure.",
         "Technical: Future enhancements include bidirectional SOAR (Security Orchestration, Automation, and Response) automated firewall shunning, native AWS CloudTrail/Kubernetes audit log collectors, and multi-agent debate reasoning via LangGraph.")
    ]

    for q_text, s_ans, t_ans in viva_qa:
        qa_box = [
            Paragraph(q_text, qa_q_style),
            Paragraph(f"<b>• 10-Year-Old Explanation:</b> {s_ans}", qa_simple_style),
            Spacer(1, 2),
            Paragraph(f"<b>• Technical Viva Answer:</b> {t_ans}", qa_tech_style),
        ]
        story.append(make_box(qa_box, bg_color=colors.HexColor("#f8fafc"), border_color=colors.HexColor("#cbd5e1")))
        story.append(Spacer(1, 6))

    # Build Document using NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {output_path}")


if __name__ == "__main__":
    output_pdf = sys.argv[1] if len(sys.argv) > 1 else "CyberSentinel_Viva_Master_Guide.pdf"
    build_viva_guide_pdf(output_pdf)
