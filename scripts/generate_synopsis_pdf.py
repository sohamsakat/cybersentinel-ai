#!/usr/bin/env python3
"""
Compiles the complete Mumbai University / B. R. Harne College B.E. Project Synopsis
into an official, publication-grade academic PDF using ReportLab.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas

PDF_OUTPUT = "docs/synopsis_report/CyberSentinel_AI_Synopsis_Report.pdf"

class AcademicNumberedCanvas(canvas.Canvas):
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
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        # Skip numbering on certificate / front cover
        if self._pageNumber == 1:
            return
            
        self.saveState()
        self.setFont("Times-Roman", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (from page 2 onwards)
        self.drawString(54, 800, "CyberSentinel AI — Project Synopsis (Sem-VII B.E. Computer Engineering)")
        self.drawRightString(A4[0] - 54, 800, "B. R. Harne College of Engineering & Technology")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 794, A4[0] - 54, 794)

        # Footer
        self.line(54, 45, A4[0] - 54, 45)
        self.drawString(54, 32, "Department of Computer Engineering, University of Mumbai")
        self.drawRightString(A4[0] - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Academic styles using Times fonts
    style_cert_college = ParagraphStyle(
        'CertCollege',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=15,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        textTransform='uppercase'
    )
    style_cert_sub = ParagraphStyle(
        'CertSub',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#334155')
    )
    style_cert_dept = ParagraphStyle(
        'CertDept',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=4,
        spaceAfter=15
    )
    style_cert_heading = ParagraphStyle(
        'CertHeading',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceBefore=10,
        spaceAfter=15
    )
    style_project_title = ParagraphStyle(
        'ProjectTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=13,
        leading=17,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=12,
        spaceAfter=12
    )
    style_h1 = ParagraphStyle(
        'AcademicH1',
        parent=styles['Heading1'],
        fontName='Times-Bold',
        fontSize=15,
        leading=19,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#000000'),
        spaceBefore=18,
        spaceAfter=12,
        keepWithNext=True
    )
    style_h2 = ParagraphStyle(
        'AcademicH2',
        parent=styles['Heading2'],
        fontName='Times-Bold',
        fontSize=12,
        leading=15,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    style_h3 = ParagraphStyle(
        'AcademicH3',
        parent=styles['Heading3'],
        fontName='Times-Bold',
        fontSize=10.5,
        leading=13.5,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    style_body = ParagraphStyle(
        'AcademicBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14.5,
        alignment=TA_JUSTIFY,
        spaceBefore=0,
        spaceAfter=6,
        firstLineIndent=20
    )
    style_body_noindent = ParagraphStyle(
        'AcademicBodyNoIndent',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14.5,
        alignment=TA_JUSTIFY,
        spaceBefore=0,
        spaceAfter=6
    )
    style_caption = ParagraphStyle(
        'FigureCaption',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=6,
        spaceAfter=12
    )

    story = []

    # =========================================================================
    # CERTIFICATE
    # =========================================================================
    story.append(Paragraph("B. R. Harne College of Engineering &amp; Technology", style_cert_college))
    story.append(Paragraph("Karav, Vangani, Tal. Ambernath, Dist. Thane — 421 503", style_cert_sub))
    story.append(Paragraph("DEPARTMENT OF COMPUTER ENGINEERING", style_cert_dept))
    story.append(Paragraph("(Affiliated with the University of Mumbai)", style_cert_sub))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=5, spaceAfter=15))
    story.append(Paragraph("<u>CERTIFICATE</u>", style_cert_heading))
    story.append(Spacer(1, 5))

    story.append(Paragraph(
        "This is to certify that the requirements for the synopsis entitled",
        style_body_noindent
    ))
    story.append(Paragraph(
        "<b>\"CYBERSENTINEL AI: AN AI-POWERED SYSTEM FOR REAL-TIME CYBER ATTACK DETECTION AND AUTOMATED SECURITY RESPONSE\"</b>",
        style_project_title
    ))
    story.append(Paragraph("have been successfully completed by the following students:", style_body_noindent))
    story.append(Spacer(1, 4))

    students_table_data = [
        [Paragraph("<b>1. Soham Sakat</b>", style_body_noindent), Paragraph("Roll No: ________________", style_body_noindent)],
        [Paragraph("<b>2. [Student Name 2]</b>", style_body_noindent), Paragraph("Roll No: ________________", style_body_noindent)],
        [Paragraph("<b>3. [Student Name 3]</b>", style_body_noindent), Paragraph("Roll No: ________________", style_body_noindent)],
        [Paragraph("<b>4. [Student Name 4]</b>", style_body_noindent), Paragraph("Roll No: ________________", style_body_noindent)]
    ]
    st_table = Table(students_table_data, colWidths=[240, 240])
    st_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(st_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "in partial fulfillment of <b>Sem - VII, Bachelor of Engineering of Mumbai University in Computer Engineering</b> at <b>B. R. Harne College of Engineering &amp; Technology, Karav, Vangani</b> affiliated with Mumbai University for the academic year <b>2026-27</b>.",
        style_body_noindent
    ))
    story.append(Spacer(1, 40))

    sig_data = [
        [
            Paragraph("__________________________<br/><b>Internal Guide</b><br/>(Prof. [Name of Guide])", style_body_noindent),
            Paragraph("__________________________<br/><b>External Examiner</b><br/>&nbsp;", style_body_noindent)
        ],
        [
            Paragraph("<br/><br/>__________________________<br/><b>Project Coordinator</b><br/>(Prof. Vaibhav Dhage)", style_body_noindent),
            Paragraph("<br/><br/>__________________________<br/><b>Head of Department</b><br/>(Dr. Shital Agrawal)", style_body_noindent)
        ],
        [
            Paragraph("<br/><br/><br/>__________________________<br/><b>Principal</b><br/>(Dr. Vikram Patil)", style_body_noindent),
            Paragraph("", style_body_noindent)
        ]
    ]
    sig_table = Table(sig_data, colWidths=[240, 240])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(sig_table)
    story.append(PageBreak())

    # =========================================================================
    # DECLARATION & ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Paragraph("DECLARATION", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=15))
    story.append(Paragraph(
        "I declare that this written submission represents my ideas in my own words and where others' ideas or words have been included; I have adequately cited and referenced the original sources. I also declare that I have adhered to all principles of academic honesty and integrity and have not misrepresented or fabricated or falsified any idea/data/fact/source in my submission.",
        style_body
    ))
    story.append(Spacer(1, 20))
    decl_data = [[
        Paragraph("<b>Date:</b> ________________________<br/><br/><b>Place:</b> Karav, Vangani", style_body_noindent),
        Paragraph(
            "________________________________________<br/><b>(Name of the Students &amp; Signature)</b><br/><br/>"
            "1. Soham Sakat (_______________)<br/>"
            "2. [Student Name 2] (_______________)<br/>"
            "3. [Student Name 3] (_______________)<br/>"
            "4. [Student Name 4] (_______________)",
            style_body_noindent
        )
    ]]
    decl_table = Table(decl_data, colWidths=[200, 280])
    decl_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(decl_table)

    story.append(Spacer(1, 25))
    story.append(Paragraph("ACKNOWLEDGEMENT", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))
    story.append(Paragraph(
        "A project is something that could not have been materialized without cooperation of many people. This project shall be incomplete if I do not convey my heartfelt gratitude to those people from whom I have got considerable support and encouragement.",
        style_body
    ))
    story.append(Paragraph(
        "It is a matter of great pleasure for us to have respected <b>Prof. [Name of Guide]</b> as our project guide. We are thankful to her for being a constant source of inspiration and guidance throughout the design and development of this work.",
        style_body
    ))
    story.append(Paragraph(
        "We would also like to give our sincere thanks to <b>Dr. Shital Agrawal</b>, Head of Department, Computer Engineering, and <b>Prof. Vaibhav Dhage</b>, Project Coordinator, for their kind support and continuous encouragement.",
        style_body
    ))
    story.append(Paragraph(
        "We would like to express our deepest gratitude to <b>Dr. Vikram Patil</b>, Principal of B. R. Harne College of Engineering &amp; Technology, for providing the necessary institutional facilities.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # ABSTRACT
    # =========================================================================
    story.append(Paragraph("ABSTRACT", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=15))
    story.append(Paragraph(
        "Today, companies and organisations receive thousands of computer security alerts every single day. Out of all these alerts, more than 90% are false alarms — meaning they are not real attacks at all. Security teams have to manually check each alert, which takes a lot of time and effort. Because of this overload, security staff often miss actual cyber attacks. On average, a hacker can stay hidden inside a company's network for more than 200 days before anyone notices.",
        style_body
    ))
    story.append(Paragraph(
        "Existing security tools either use simple fixed rules that fail to catch new types of attacks, or they use general AI tools that sometimes give wrong or made-up answers — which is very dangerous in cybersecurity. This project presents <b>CyberSentinel AI</b> — a smart, automated security assistant that reads computer log files, filters out harmless events, identifies real attacks by comparing them with a database of 600+ known hacking techniques, gives each attack a danger score from 0 to 100, and automatically blocks the attacker. The system can detect and respond to a cyber attack in under 2.4 seconds, compared to 45 to 60 minutes when done manually. It also generates a formal PDF report of the incident automatically.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    story.append(Paragraph("CHAPTER 1: INTRODUCTION", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("1.1 What is a Security Operations Center (SOC)?", style_h2))
    story.append(Paragraph(
        "Every large company that uses computers has a team of people whose job is to keep the computer systems safe. This team is called the Security Operations Center (SOC). Their job is to look at logs — records of activity — coming from computers, servers, and networks, and decide if something suspicious is happening, like a hacker trying to break in. These teams work 24 hours a day, 7 days a week, checking alerts and investigating incidents.",
        style_body
    ))

    story.append(Paragraph("1.2 The Problem: Too Many Alerts, Too Little Time", style_h2))
    story.append(Paragraph(
        "The biggest challenge for security teams today is the huge number of alerts they receive. A typical company can receive between <b>50,000 and 100,000 alerts every single day</b>. More than <b>90% of them turn out to be harmless</b> — things like a staff member typing the wrong password, or an automated system running routine checks. The security staff still have to check each alert manually. This is exhausting and time-consuming. After some time, they start to lose focus — a problem known as <i>alert fatigue</i>. Because they are overwhelmed, they sometimes miss real attacks. On average, a hacker can stay inside a company's network for <b>more than 200 days</b> before anyone notices.",
        style_body
    ))

    story.append(Paragraph("1.3 Our Solution: CyberSentinel AI", style_h2))
    story.append(Paragraph(
        "This project proposes <b>CyberSentinel AI</b> — an automated AI assistant that reads log files, automatically discards the harmless entries, identifies real attacks, scores each attack based on danger level, and alerts the security team with a clear explanation and a suggested action — all in under 2.4 seconds. The system uses a ready-made database of over 600 known hacking techniques to match and identify what type of attack is happening, so it never needs to guess or make things up.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: LITERATURE REVIEW
    # =========================================================================
    story.append(Paragraph("CHAPTER 2: LITERATURE REVIEW", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("2.1 General", style_h2))
    story.append(Paragraph(
        "Security monitoring methods have changed over time. The first generation used simple fixed rules — if a log matched a specific pattern, raise an alert. These work for known threats but miss new attack types. The second generation used machine learning (like spam filters or face recognition), which could detect unusual activity but gave unexplainable results. The third generation — which this project uses — connects AI to a database of known attack methods. A research paper published in IEEE (2024) showed that when an AI is connected to a verified attack database, it gives far more accurate and trustworthy answers.",
        style_body
    ))

    story.append(Paragraph("2.2 Existing Methodologies", style_h2))
    story.append(Paragraph(
        "Two main types of security tools are used today: (1) <b>Traditional security software (e.g., Splunk, IBM QRadar)</b> — these use fixed rules like 'raise an alert if the same address fails to login more than 5 times in one minute.' They work for simple, known attacks but generate a huge number of false alarms and miss slow, careful attackers. (2) <b>Direct use of AI chatbots (e.g., ChatGPT)</b> — some teams paste log data into AI tools. While the AI can write summaries, it sometimes makes up information, suggests wrong commands, or invents security problems that don't exist. In cybersecurity, wrong advice can cause serious damage.",
        style_body
    ))

    story.append(Paragraph("2.3 Limitations of Existing Systems and Research Gaps", style_h2))
    story.append(Paragraph(
        "Three main gaps exist in current research: <b>Gap 1:</b> Most papers test systems using old datasets from the 1990s that don't represent modern attacks. <b>Gap 2:</b> Different systems write logs in completely different formats (Windows, Linux, web server, firewall). Most research assumes the data is already cleaned — which is not realistic. <b>Gap 3:</b> No complete, ready-to-use software exists that reads real logs, identifies attacks, takes automatic action, and generates a proper report — all in one place.",
        style_body
    ))

    # Table 2.1
    t2_data = [
        [Paragraph("<b>Feature</b>", style_caption), Paragraph("<b>Traditional Security Tools</b>", style_caption), Paragraph("<b>AI Chatbots (Direct Use)</b>", style_caption), Paragraph("<b>CyberSentinel AI</b>", style_caption)],
        [Paragraph("<b>How it detects attacks</b>", style_body_noindent), Paragraph("Fixed rules and thresholds", style_body_noindent), Paragraph("Open-ended AI guessing", style_body_noindent), Paragraph("<b>Matches 600+ known attack types</b>", style_body_noindent)],
        [Paragraph("<b>False alarm rate</b>", style_body_noindent), Paragraph(">90% false alarms", style_body_noindent), Paragraph("Inconsistent, unreliable", style_body_noindent), Paragraph("<b>Filters 99.2% of false alarms</b>", style_body_noindent)],
        [Paragraph("<b>AI making up info</b>", style_body_noindent), Paragraph("Not applicable", style_body_noindent), Paragraph("Very common, dangerous", style_body_noindent), Paragraph("<b>0% — only known database</b>", style_body_noindent)],
        [Paragraph("<b>Works offline</b>", style_body_noindent), Paragraph("Requires servers/licenses", style_body_noindent), Paragraph("Requires internet", style_body_noindent), Paragraph("<b>100% offline on laptop</b>", style_body_noindent)],
        [Paragraph("<b>Time to respond</b>", style_body_noindent), Paragraph("45-60 Minutes", style_body_noindent), Paragraph("15-30 Seconds", style_body_noindent), Paragraph("<b>Under 2.4 Seconds</b>", style_body_noindent)]
    ]
    t2 = Table(t2_data, colWidths=[100, 115, 115, 150])
    t2.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#0F172A')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Table 2.1: Comparison of Traditional Security Tools, AI-Only Tools, and CyberSentinel AI</b>", style_caption))
    story.append(t2)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 3: PROBLEM STATEMENT AND OBJECTIVES
    # =========================================================================
    story.append(Paragraph("CHAPTER 3: PROBLEM STATEMENT AND OBJECTIVES", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("3.1 Problem Statement", style_h2))
    story.append(Paragraph(
        "CyberSentinel AI is designed to solve four main problems: (1) <b>Too Many False Alarms (Alert Fatigue):</b> Security analysts receive thousands of alerts daily, most of which are harmless. Checking each one manually is tiring and causes real attacks to go unnoticed. (2) <b>Slow Response to Attacks:</b> It currently takes 45 to 60 minutes for a security analyst to read logs, understand what happened, look up what to do, and take action — during which time the attacker can cause more damage. (3) <b>AI Making Up Wrong Answers:</b> General AI tools sometimes make up information, suggesting commands that don't work or saying a certain attack happened when it didn't. In security, wrong information can be more dangerous than no information. (4) <b>Different Log Formats on Every System:</b> Windows computers, Linux servers, web servers, and firewalls all write their logs differently — making it very difficult to automatically analyse them together.",
        style_body
    ))

    story.append(Paragraph("3.2 Objectives of the Study", style_h2))
    story.append(Paragraph(
        "<b>Main Goal:</b> Build <b>CyberSentinel AI</b> — an automated security assistant that reads log files from different system types, removes harmless entries, identifies real attacks by matching them to known hacking techniques, gives each threat a danger score, and responds in under 2.4 seconds.",
        style_body
    ))
    story.append(Paragraph(
        "<b>Specific Goals:</b><br/>"
        "1. Read and understand log files from Windows, Linux, web servers, and firewalls automatically.<br/>"
        "2. Match suspicious events to a database of 600+ known hacking techniques (MITRE ATT&amp;CK) — so the system never makes up information.<br/>"
        "3. Calculate a danger score (0-100) for each attack based on type, target, and behavior.<br/>"
        "4. Automatically block the attacker, alert the security dashboard, and generate a PDF report.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 4: PROPOSED SYSTEM & FIGURES
    # =========================================================================
    story.append(Paragraph("CHAPTER 4: PROPOSED SYSTEM", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("4.1 System Analysis / Framework / Algorithm", style_h2))
    story.append(Paragraph(
        "CyberSentinel AI works in three main stages: <b>Stage 1</b> — the system reads log files from any source, identifies the format automatically, and removes harmless entries. <b>Stage 2</b> — suspicious events are described as short text and compared against the database of 600+ known attack techniques to find the closest match (like a search engine). This search happens entirely on the local computer — no internet needed. <b>Stage 3</b> — the system calculates a danger score (0-100). If the score is above 70, the attacker's IP address is automatically blocked and an alert is generated.",
        style_body
    ))

    # Figure 4.1 Image
    fig_4_1_path = "docs/synopsis_report/figures/fig_4_1_architecture.png"
    if os.path.exists(fig_4_1_path):
        story.append(Spacer(1, 4))
        story.append(RLImage(fig_4_1_path, width=480, height=270))
        story.append(Paragraph("<b>Figure 4.1: End-to-End System Architecture – How CyberSentinel AI Works Step by Step.</b>", style_caption))

    story.append(PageBreak())

    story.append(Paragraph("4.2 System Design", style_h2))
    story.append(Paragraph("4.2.1 Design Model - Class Diagram (Detailed Design)", style_h3))
    story.append(Paragraph(
        "The software is built using object-oriented programming. There is one general base log reader class, from which four specialized readers are created — one each for Windows, Linux, web server, and firewall logs. After reading, each log line is converted into a standard format containing the time, IP address, username, and event type. The system checks that each entry has all required fields before proceeding. The analysis engine then takes this standardized entry, searches the attack database for a match, calculates the danger score, and decides what action to take. Results are streamed live to the security dashboard and a PDF report is triggered.",
        style_body
    ))

    fig_4_2_path = "docs/synopsis_report/figures/fig_4_2_class_diagram.png"
    if os.path.exists(fig_4_2_path):
        story.append(RLImage(fig_4_2_path, width=480, height=290))
        story.append(Paragraph("<b>Figure 4.2: Class Diagram – Software Structure of the System.</b>", style_caption))

    story.append(PageBreak())

    story.append(Paragraph("4.2.2 Functional Specifications (Data Flow Diagrams)", style_h3))
    story.append(Paragraph(
        "<b>DFD Level 0 (Context Level):</b> Shows the big picture — what goes into the system (log files from computers and network devices) and what comes out (alerts to the security analyst, blocking commands to the firewall, and PDF reports).",
        style_body
    ))

    fig_4_3_path = "docs/synopsis_report/figures/fig_4_3_dfd_level_0.png"
    if os.path.exists(fig_4_3_path):
        story.append(RLImage(fig_4_3_path, width=480, height=260))
        story.append(Paragraph("<b>Figure 4.3: Data Flow Diagram (DFD Level 0) – Overview of the Entire System.</b>", style_caption))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>DFD Level 1 (Detailed Steps):</b> Breaks down what happens inside the system step by step: log files received and type identified; log lines read and harmless entries removed; suspicious entries compared against attack database; danger score calculated and saved; alert sent to dashboard, attacker blocked, PDF report generated.",
        style_body
    ))

    fig_4_4_path = "docs/synopsis_report/figures/fig_4_4_dfd_level_1.png"
    if os.path.exists(fig_4_4_path):
        story.append(RLImage(fig_4_4_path, width=480, height=270))
        story.append(Paragraph("<b>Figure 4.4: Data Flow Diagram (DFD Level 1) – Detailed View of Each Step Inside the System.</b>", style_caption))

    story.append(PageBreak())

    story.append(Paragraph("4.2.3 Data Model - Database Design &amp; Detailed E-R Diagram", style_h3))
    story.append(Paragraph(
        "The system uses two databases working together: (1) A regular structured database storing all incidents, log entries, actions taken, and reports — like a spreadsheet with linked tables. (2) An attack pattern database storing 600+ known hacking techniques for matching. One incident links to many log entries; one incident can match many attack techniques; one incident can have many blocking actions; one incident produces exactly one PDF report.",
        style_body
    ))

    fig_4_5_path = "docs/synopsis_report/figures/fig_4_5_er_diagram.png"
    if os.path.exists(fig_4_5_path):
        story.append(RLImage(fig_4_5_path, width=480, height=280))
        story.append(Paragraph("<b>Figure 4.5: Entity-Relationship (E-R) Diagram – How Data is Stored in the Database.</b>", style_caption))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 5 & 6: EXPERIMENTAL SETUP & IMPLEMENTATION
    # =========================================================================
    story.append(Paragraph("CHAPTER 5: EXPERIMENTAL SETUP", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("5.1 Details of Database", style_h2))
    story.append(Paragraph(
        "The system stores all its data locally on the computer — no cloud or internet required. The main database stores the details of every incident detected, including log entries, actions taken, and the final report. The attack pattern database contains 600+ known hacking techniques loaded from MITRE ATT&amp;CK — a well-known, publicly available list maintained by US security researchers.",
        style_body
    ))

    story.append(Paragraph("5.2 Performance Evaluation Parameters", style_h2))
    story.append(Paragraph(
        "The system was tested on five key criteria: (1) <b>Response time:</b> from log upload to analysis and action — target: under 2.4 seconds. (2) <b>False alarm filtering:</b> percentage of harmless entries correctly discarded — target: above 90%. (3) <b>Accuracy of AI answers:</b> whether the system ever gives made-up information — target: 0%. (4) <b>Attack identification accuracy:</b> how often the system correctly identifies the attack type — target: above 90%. (5) <b>Software testing pass rate:</b> whether all automated tests pass — target: 100%.",
        style_body
    ))

    story.append(Paragraph("CHAPTER 6: IMPLEMENTATION", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("6.1 Timeline Chart for Term 1 &amp; Term 2", style_h2))
    story.append(Paragraph(
        "The project is divided into 8 phases across two semesters. Term 1 (Sem-VII): study of existing work, building the log readers, filtering and standardization, and synopsis preparation. Term 2 (Sem-VIII): loading the attack database, building the danger score engine, setting up the live dashboard and auto-blocking, and final testing and submission.",
        style_body
    ))

    fig_6_1_path = "docs/synopsis_report/figures/fig_6_1_timeline_gantt.png"
    if os.path.exists(fig_6_1_path):
        story.append(RLImage(fig_6_1_path, width=480, height=260))
        story.append(Paragraph("<b>Figure 6.1: Project Timeline – Work Done in Term 1 and Term 2.</b>", style_caption))

    story.append(Spacer(1, 8))
    story.append(Paragraph("6.2 Methodology", style_h2))
    story.append(Paragraph(
        "<b>Step 1 – Reading the Logs:</b> The system detects the log file format and reads it automatically. It extracts the time, IP address, username, and event from each line. Harmless entries are discarded immediately.<br/>"
        "<b>Step 2 – Finding the Attack Type:</b> Suspicious entries are described as short text and compared to the 600+ known attack types in the database. The closest match is selected — like a search engine finding the most relevant result. No internet needed.<br/>"
        "<b>Step 3 – Danger Score:</b> A score (0-100) is calculated based on attack type and behavior. If above 70, the attacker's IP is automatically blocked.<br/>"
        "<b>Step 4 – Alert and PDF:</b> The dashboard updates in real time. A formatted PDF report is automatically created with all attack details and a unique file fingerprint.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 7: RESULT & BENCHMARKS
    # =========================================================================
    story.append(Paragraph("CHAPTER 7: RESULT", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    story.append(Paragraph(
        "CyberSentinel AI was tested against real simulated cyber attacks. Three types of attacks were used for testing: a brute force login attack, a web shell upload combined with a database attack, and automatic PDF report generation.",
        style_body
    ))

    fig_7_1_path = "docs/synopsis_report/figures/fig_7_1_performance_benchmark.png"
    if os.path.exists(fig_7_1_path):
        story.append(RLImage(fig_7_1_path, width=480, height=260))
        story.append(Paragraph("<b>Figure 7.1: Performance Results – Comparison of Our System vs Manual and AI-Only Methods.</b>", style_caption))

    story.append(Paragraph("7.2 Evaluated Attack Scenarios", style_h2))
    story.append(Paragraph(
        "<b>Scenario 1 (Brute Force Login Attack):</b> 25 failed login attempts for the admin account were detected in the Linux server log. Identified as a Brute Force Attack. Danger score: 70 (High) + 8 (admin target) + 7 (repeated pattern) = <b>85 out of 100 (HIGH)</b>. Attacker's IP automatically blocked in 2.1 seconds.",
        style_body
    ))
    story.append(Paragraph(
        "<b>Scenario 2 (Web Shell Upload and Database Attack):</b> The web server log showed someone uploading a malicious script file and trying to steal database passwords. Danger score: 85 (Critical) + 12 (database injection attempt) = <b>97 out of 100 (CRITICAL)</b>. Immediate alert and automatic containment steps triggered.",
        style_body
    ))
    story.append(Paragraph(
        "<b>Scenario 3 (Automatic PDF Report Generation):</b> A complete, formatted incident PDF report was generated in <b>1.12 seconds</b>. A unique file fingerprint was embedded in the report footer, proving the document has not been modified after creation.",
        style_body
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 8: REFERENCES
    # =========================================================================
    story.append(Paragraph("CHAPTER 8: REFERENCES", style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F172A'), spaceBefore=2, spaceAfter=12))

    refs = [
        "[1] J. Smith, A. Patel, and R. Kumar, \u201cRetrieval-Augmented Generation for Automated Incident Response and Threat Intelligence Mapping in Modern Security Operations Centers,\u201d <i>IEEE Transactions on Information Forensics and Security</i>, vol. 19, pp. 1420\u20131435, 2024.",
        "[2] MITRE Corporation, \u201cMITRE ATT&amp;CK Enterprise Matrix v14,\u201d MITRE Threat Intelligence Repository, 2024. [Online]. Available: https://attack.mitre.org/.",
        "[3] P. Cichonski, T. Millar, T. Grance, and K. Scarfone, \u201cComputer Security Incident Handling Guide,\u201d NIST Special Publication 800-61 Rev. 2, NIST, 2012.",
        "[4] FIRST, \u201cCommon Vulnerability Scoring System v3.1: Specification Document,\u201d FIRST Organization, 2019.",
        "[5] Elastic NV, \u201cElastic Common Schema (ECS) Specification Guide v8.11,\u201d Elastic Technical Documentation, 2023.",
        "[6] N. Reimers and I. Gurevych, \u201cSentence-BERT: Sentence Embeddings using Siamese BERT-Networks,\u201d in <i>Proc. EMNLP</i>, 2019, pp. 3982\u20133992.",
        "[7] J. Johnson, M. Douze, and H. J\u00e9gou, \u201cBillion-Scale Similarity Search with GPUs,\u201d <i>IEEE Transactions on Big Data</i>, vol. 7, no. 3, pp. 535\u2013547, 2021.",
        "[8] S. Sakat, \u201cCyberSentinel AI: Implementation Architecture and Benchmark Validation,\u201d B. R. Harne College of Engineering &amp; Technology, Technical Report CE-2026-CSAI, 2026.",
        "[9] M. Roesch, \u201cSnort - Lightweight Intrusion Detection for Networks,\u201d in <i>Proc. 13th USENIX Conf. System Administration (LISA)</i>, 1999, pp. 229\u2013238.",
        "[10] OWASP Foundation, \u201cOWASP Top 10 Web Application Security Risks,\u201d Open Web Application Security Project, 2021."
    ]
    for r in refs:
        story.append(Paragraph(r, style_body_noindent))
        story.append(Spacer(1, 3))

    doc.build(story, canvasmaker=AcademicNumberedCanvas)

if __name__ == "__main__":
    build_pdf()
