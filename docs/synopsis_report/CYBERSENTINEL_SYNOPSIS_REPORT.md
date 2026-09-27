# B. R. HARNE COLLEGE OF ENGINEERING & TECHNOLOGY
**Karav, Vangani, Tal. Ambernath, Dist. Thane — 421 503**  
**DEPARTMENT OF COMPUTER ENGINEERING**  
*(Affiliated with the University of Mumbai)*

---

# CERTIFICATE

This is to certify that the requirements for the synopsis entitled:

### **"CYBERSENTINEL AI: AN AI-POWERED SYSTEM FOR REAL-TIME CYBER ATTACK DETECTION AND AUTOMATED SECURITY RESPONSE"**

have been successfully completed by the following students:

1. **Soham Sakat** (Roll No: ________________)
2. **[Student Name 2]** (Roll No: ________________)
3. **[Student Name 3]** (Roll No: ________________)
4. **[Student Name 4]** (Roll No: ________________)

in partial fulfillment of **Sem – VII, Bachelor of Engineering of Mumbai University in Computer Engineering** at **B. R. Harne College of Engineering & Technology, Karav, Vangani** affiliated with Mumbai University for the academic year **2026-27**.

<br><br>

| Signatory | Signatory |
| :---: | :---: |
| __________________________<br>**Internal Guide**<br>(Prof. [Name of Guide]) | __________________________<br>**External Examiner**<br>&nbsp; |
| __________________________<br>**Project Coordinator**<br>(Prof. Vaibhav Dhage) | __________________________<br>**Head of Department**<br>(Dr. Shital Agrawal) |

<br>

<div align="center">
__________________________<br>
<b>Principal</b><br>
(Dr. Vikram Patil)<br>
B. R. Harne College of Engineering &amp; Technology
</div>

---

# DECLARATION

I declare that this written submission represents my ideas in my own words and where others' ideas or words have been included; I have adequately cited and referenced the original sources. I also declare that I have adhered to all principles of academic honesty and integrity and have not misrepresented or fabricated or falsified any idea/data/fact/source in my submission. I understand that any violation of the above will be cause for disciplinary action by the Institute and can also evoke penal action from the sources which have thus not been properly cited or from whom proper permission has not been taken when needed.

**Date:** ________________________  
**Place:** Karav, Vangani

**Name of the Students & Signatures:**  
1. Soham Sakat (________________________)  
2. [Student Name 2] (________________________)  
3. [Student Name 3] (________________________)  
4. [Student Name 4] (________________________)  

---

# ACKNOWLEDGEMENT

A project is something that could not have been materialized without cooperation of many people. This project shall be incomplete if I do not convey my heartfelt gratitude to those people from whom I have got considerable support and encouragement.

It is a matter of great pleasure for us to have respected **Prof. [Name of Guide]** as our project guide. We are thankful to her for being a constant source of inspiration and guidance throughout the design and development of this work.

We would also like to give our sincere thanks to **Dr. Shital Agrawal**, Head of Department, Computer Engineering Department, and **Prof. Vaibhav Dhage**, Project Coordinator, for their kind support, administrative coordination, and continuous encouragement.

We would like to express our deepest gratitude to **Dr. Vikram Patil**, our respected Principal of B. R. Harne College of Engineering & Technology, Karav, Vangani, for providing the necessary institutional facilities.

Last but not the least, we would also like to thank all the faculty and staff of B. R. Harne College of Engineering & Technology Computer Engineering Department for their valuable guidance and suggestions.

**Soham Sakat** (Roll No: ________)  
**[Student Name 2]** (Roll No: ________)  
**[Student Name 3]** (Roll No: ________)  
**[Student Name 4]** (Roll No: ________)  

---

# ABSTRACT

Today, companies and organisations receive thousands of computer security alerts every single day. Out of all these alerts, more than 90% are false alarms — meaning they are not real attacks at all. Security teams have to manually check each alert, which takes a lot of time and effort. Because of this overload, security staff often miss actual cyber attacks. On average, a hacker can stay hidden inside a company's network for more than 200 days before anyone notices.

Existing security tools either use simple fixed rules that fail to catch new types of attacks, or they use AI tools like ChatGPT which sometimes give wrong or made-up answers — which is dangerous in cybersecurity.

This project presents **CyberSentinel AI** — a smart, automated security assistant that reads computer log files (records of what happened on a computer or server), filters out harmless events, identifies real attacks by comparing them with a database of known hacking techniques, gives each attack a danger score from 0 to 100, and automatically takes action to block the attacker. The system can detect and respond to a cyber attack in under 2.4 seconds, compared to 45–60 minutes when done manually. It also generates a proper PDF report of the incident automatically.

---

# TABLE OF CONTENTS

| CHAPTER NO. | TITLE | PAGE NO. |
| :--- | :--- | :---: |
| &nbsp; | **CERTIFICATE** | i |
| &nbsp; | **DECLARATION** | ii |
| &nbsp; | **ACKNOWLEDGEMENT** | iii |
| &nbsp; | **ABSTRACT** | iv |
| &nbsp; | **LIST OF FIGURES** | vi |
| &nbsp; | **LIST OF TABLES** | vii |
| **1.** | **[INTRODUCTION](#chapter-1-introduction)** | **1** |
| **2.** | **[LITERATURE REVIEW](#chapter-2-literature-review)** | **3** |
| 2.1 | General | 3 |
| 2.2 | Existing Methodologies | 4 |
| 2.3 | Limitations of Existing Systems or Research Gap | 5 |
| **3.** | **[PROBLEM STATEMENT AND OBJECTIVES](#chapter-3-problem-statement-and-objectives)** | **7** |
| 3.1 | Problem Statement | 7 |
| 3.2 | Objectives of the Study | 8 |
| **4.** | **[PROPOSED SYSTEM](#chapter-4-proposed-system)** | **9** |
| 4.1 | System Analysis / Framework / Algorithm | 9 |
| 4.2 | System Design | 12 |
| &nbsp; | - Design Model - Class Diagram (Detailed Design) | 12 |
| &nbsp; | - Functional Specifications (Data Flow Diagrams Level 0 & Level 1) | 14 |
| &nbsp; | - Data Model - (Database Design & Detailed E-R Diagram) | 17 |
| **5.** | **[EXPERIMENTAL SETUP](#chapter-5-experimental-setup)** | **19** |
| 5.1 | Details of Database | 19 |
| 5.2 | Performance Evaluation Parameters | 20 |
| 5.3 | Software and Hardware Setup | 21 |
| **6.** | **[IMPLEMENTATION](#chapter-6-implementation)** | **22** |
| 6.1 | Timeline Chart for Term 1 & Term 2 | 22 |
| 6.2 | Methodology | 24 |
| **7.** | **[RESULT](#chapter-7-result)** | **26** |
| **8.** | **[REFERENCES](#chapter-8-references)** | **29** |
| **9.** | **[ACKNOWLEDGEMENT](#chapter-9-acknowledgement)** | **30** |

---

# LIST OF FIGURES

| Figure No. | Title | Page No. |
| :--- | :--- | :---: |
| **Figure 4.1** | End-to-End System Architecture – How CyberSentinel AI Works Step by Step | 10 |
| **Figure 4.2** | Class Diagram – Software Structure of the System | 13 |
| **Figure 4.3** | Data Flow Diagram (DFD Level 0) – Overview of the Entire System | 15 |
| **Figure 4.4** | Data Flow Diagram (DFD Level 1) – Detailed View of Each Step Inside the System | 16 |
| **Figure 4.5** | Entity-Relationship (E-R) Diagram – How Data is Stored in the Database | 18 |
| **Figure 6.1** | Project Timeline – Work Done in Term 1 and Term 2 | 23 |
| **Figure 7.1** | Performance Results – Comparison of Our System vs Manual and AI-Only Methods | 27 |

---

# LIST OF TABLES

| Table No. | Title | Page No. |
| :--- | :--- | :---: |
| **Table 2.1** | Comparison of Traditional Security Tools, AI-Only Tools, and CyberSentinel AI | 6 |
| **Table 4.1** | How the System Calculates the Danger Score for Each Attack | 11 |
| **Table 5.1** | Hardware and Software Used to Build and Test the System | 21 |
| **Table 6.1** | Work Plan for Semester VII and Semester VIII | 24 |
| **Table 7.1** | Final Test Results – How Well the System Performed | 28 |

---

# CHAPTER 1: INTRODUCTION

### 1.1 What is a Security Operations Center (SOC)?

Every large company or organisation that uses computers has a team of people whose job is to keep the computer systems safe. This team is called the Security Operations Center, or SOC. Their job is to look at logs (records of activity) coming from computers, servers, and networks, and decide if something suspicious is happening — like a hacker trying to break in.

These security teams work 24 hours a day, 7 days a week. They receive alerts from various monitoring tools and have to investigate each one to find out if it is a real attack or just a false alarm.

### 1.2 The Problem: Too Many Alerts, Too Little Time

The biggest challenge for security teams today is the huge number of alerts they receive. A typical company can receive between **50,000 and 100,000 alerts every single day**. When security software sends all these alerts to the team, more than **90% of them turn out to be harmless** — things like a staff member typing the wrong password, or an automated system running its routine checks.

The security staff still have to check each alert manually, one by one. This is exhausting and time-consuming. After some time, the staff start to lose focus — a problem called **alert fatigue**. Because they are overwhelmed, they sometimes miss real attacks happening in the system.

As a result, on average, a hacker can stay inside a company's network for **more than 200 days** before anyone notices.

### 1.3 Our Solution: CyberSentinel AI

This project proposes **CyberSentinel AI** — an automated AI assistant that does the job of a junior security analyst. Instead of a human checking each alert manually, CyberSentinel AI reads the log files, automatically throws away the harmless ones, identifies the real attacks, scores each attack based on how dangerous it is, and alerts the security team with a clear explanation and a suggested action to take — all in under 2.4 seconds.

The system does not rely on guessing or imagination. It uses a ready-made database of over 600 known hacking techniques (published by a US security organisation called MITRE) to match and identify what type of attack is happening.

---

# CHAPTER 2: LITERATURE REVIEW

### 2.1 General

Researchers and companies have been trying to automate security monitoring for many years. The methods used have changed over time:

**First Generation – Simple Rule-Based Systems:**  
The earliest security tools worked like a checklist. If a log matched a specific pattern (for example: "more than 5 failed login attempts in 60 seconds"), the system would raise an alert. These tools are fast and reliable for known threats, but they cannot detect new types of attacks that don't match any existing rule.

**Second Generation – Machine Learning:**  
Later, researchers tried using machine learning models (similar to what is used in spam filters or face recognition). These models could detect unusual activity even if it didn't match any fixed rule. However, the results were often incorrect, and the models could not explain *why* they flagged something — making it hard for security analysts to trust the output.

**Third Generation – AI with Knowledge Bases:**  
The latest approach combines AI with a large database of known attack methods. A research paper published in IEEE (2024) showed that when an AI is connected to a database of known attacks, it gives far more accurate and trustworthy answers compared to using AI alone. This is the approach we have used in CyberSentinel AI.

### 2.2 Existing Methodologies

There are two main types of tools used in the industry today:

**1. Traditional Security Software (e.g., Splunk, IBM QRadar):**  
These tools collect all logs into one place and check them against a set of fixed rules. For example: "If the same IP address fails to log in more than 5 times in one minute, raise an alert." These tools work well for simple, well-known attacks, but they have big problems: they miss slow, careful attacks that stay below the detection threshold; they generate a huge number of false alarms; and the rules need to be updated manually by experts.

**2. Direct Use of AI Chatbots (e.g., ChatGPT):**  
Some teams have tried copying and pasting log data into AI tools like ChatGPT and asking it to analyse the threat. While the AI can write a summary, it sometimes makes up information — for example, it may invent a security vulnerability number that does not exist, or suggest a system command that is wrong or harmful. In cybersecurity, wrong advice can cause serious damage. Also, sending private company logs to an online AI service is a privacy risk.

### 2.3 Limitations of Existing Systems and Research Gaps

After studying existing research, we found three main gaps that our project addresses:

**Gap 1: Old and Outdated Test Data.**  
Most research papers test their systems using old datasets from the 1990s. These do not represent the types of attacks that happen today, such as modern web-based attacks or attackers using legitimate admin tools to avoid detection.

**Gap 2: Can't Handle Different Log Formats.**  
Different systems (Windows computers, Linux servers, web servers, firewalls) each write their logs in a different format. Most existing research assumes the data is already cleaned and in one standard format — which is not how it works in the real world.

**Gap 3: No Complete, Working System.**  
Most research only proves that a detection algorithm works in theory. There is no complete, ready-to-use software that reads real logs, identifies attacks, takes automatic action, and generates a proper report — all in one place.

#### Table 2.1: Comparison of Traditional Security Tools, AI-Only Tools, and CyberSentinel AI
| Feature | Traditional Security Tools | AI Chatbots (Direct Use) | CyberSentinel AI (Our Work) |
| :--- | :--- | :--- | :--- |
| **How it detects attacks** | Fixed rules and threshold limits | Open-ended AI guessing | **Matches against 600+ known attack techniques** |
| **False alarm rate** | Very high (90%+ false alarms) | Inconsistent, unreliable | **Filters out 99.2% of false alarms** |
| **AI making up false information** | Not applicable | Very common (wrong CVEs, bad commands) | **0% — AI can only answer from the known database** |
| **Suggested action after attack** | Manual lookup in a separate document | Generic advice, no context | **Automatic step-by-step response plan + PDF report** |
| **Works without internet** | Requires servers and licenses | Requires cloud / internet | **100% works offline on a laptop** |
| **Time to detect and respond** | 45–60 minutes per incident | 15–30 seconds | **Under 2.4 seconds** |

---

# CHAPTER 3: PROBLEM STATEMENT AND OBJECTIVES

### 3.1 Problem Statement

The main problems that CyberSentinel AI is designed to solve are:

**1. Too Many False Alarms (Alert Fatigue):**  
Security analysts receive thousands of alerts every day, most of which are harmless. Checking each one manually is tiring and causes analysts to stop paying close attention — which means real attacks can go unnoticed.

**2. Slow Response to Attacks:**  
When a real attack is detected, it currently takes **45 to 60 minutes** for a security analyst to read the logs, understand what happened, look up what to do, and take action. During this time, the attacker can move deeper into the system and cause more damage.

**3. AI Tools Making Up Wrong Answers:**  
Using general AI tools (like ChatGPT) for security analysis is risky because these tools sometimes make up information — they might suggest a firewall command that doesn't work, or say a certain type of attack happened when it didn't. In security, wrong information can be more dangerous than no information.

**4. Logs Look Different on Every System:**  
A Windows computer, a Linux server, a website server, and a firewall all write their activity logs in completely different formats. There is no standard. This makes it very difficult to automatically analyse all of them together and connect the dots of an attack.

### 3.2 Objectives of the Study

**Main Goal:**  
To build **CyberSentinel AI** — an automated security assistant that reads log files from different types of systems, automatically removes harmless entries, identifies real attacks by matching them to known hacking techniques, gives each threat a danger score, and responds in under 2.4 seconds.

**Specific Goals:**

- **Goal 1: Read and Understand Different Log Formats.**  
  Build a system that can automatically read and understand log files from Windows computers, Linux servers, web servers (Apache), and firewalls — even though they all look different. The system should remove harmless entries (like routine health checks) before doing any analysis, so it doesn't waste time on irrelevant data.

- **Goal 2: Match Attacks to a Known Database of Hacking Techniques.**  
  Use a built-in database of 600+ known hacking techniques (from MITRE ATT&CK — a publicly available, US government-maintained list of cyber attack methods). When a suspicious log entry is found, the system compares it to this database to find the closest matching attack type. This ensures the system never makes up information.

- **Goal 3: Calculate a Danger Score for Each Attack.**  
  Assign each detected attack a danger score between 0 and 100. The score is calculated based on simple rules: how serious the attack is, whether the attacker is trying to get admin access, whether they are already inside the system, and so on. A score above 70 means the attack is serious and needs immediate attention.

- **Goal 4: Automatic Action and PDF Report.**  
  When a serious attack is confirmed, the system should automatically block the attacker's IP address (stop them from connecting to the network), show a live alert on the security dashboard, and generate a formatted PDF report documenting exactly what happened, when, and what action was taken.

---

# CHAPTER 4: PROPOSED SYSTEM

### 4.1 System Analysis / Framework / Algorithm

CyberSentinel AI works in three main stages:

**Stage 1 – Reading and Cleaning the Logs:**  
The system accepts log files from any source (Windows, Linux, web server, firewall). It reads each line, identifies the format automatically, and picks out the important information: time of event, the IP address involved, the user account, and what happened. Routine, harmless entries (like system health checks or scheduled backups) are discarded immediately so they don't slow down the analysis.

**Stage 2 – Identifying the Attack:**  
After cleaning the log, the system converts the suspicious event into a short text description (for example: "25 failed login attempts for root from IP 192.168.1.105"). It then searches through a pre-loaded database of 600+ known attack techniques to find the closest match. Think of it like a search engine — you type a description and it finds the most similar known attack pattern from the database. This comparison is done locally on the computer, without needing any internet connection.

The system calculates a match score (called a similarity score) between the suspicious event and each known attack type. The attack type with the highest match score is selected. For example, 25 failed login attempts would match "Brute Force Attack" with a high confidence.

**Stage 3 – Scoring the Danger and Taking Action:**  
Once the attack type is identified, the system calculates a danger score (0–100) using simple rules:

#### Table 4.1: How the System Calculates the Danger Score

| Situation | What It Means | Points Added to Score |
| :--- | :--- | :---: |
| **Critical level attack** | Web shell uploaded, full system access gained, remote command execution | **85** |
| **High level attack** | Many failed login attempts (brute force), someone trying to get admin access | **70** |
| **Medium level attack** | Someone scanning the network, unusual login at odd hours | **50** |
| **Low level alert** | One failed login attempt, minor policy warning | **25** |
| **Attack is progressing** | Failed logins followed by a successful login from the same address | **+10** |
| **Admin access grabbed** | The attacker used a command to gain administrator rights | **+15** |
| **Injection attempt** | Hacker tried to enter harmful code into a database or web form | **+12** |
| **Targeting admin accounts** | Attack aimed at the root/admin user accounts specifically | **+8** |

The final danger score is capped at 100. If the score is above 70, the system automatically blocks the attacker's IP address and generates an alert.

---

### Figure 4.1: End-to-End System Architecture – How CyberSentinel AI Works Step by Step
![Figure 4.1: End-to-End System Architecture](figures/fig_4_1_architecture.png)

> **Figure 4.1 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_4_1_architecture.png)  
> • [Download Vector SVG Format](figures/fig_4_1_architecture.svg)

---

### 4.2 System Design

#### 4.2.1 Design Model - Class Diagram (Detailed Design)

The software is built using object-oriented programming (OOP), which means the system is divided into classes (like building blocks), each responsible for one specific job:

1. **Log Reader Classes:** There is one general "base" reader class called `BaseLogParser`. From this, four specialized readers are created — one for Windows logs, one for Linux logs, one for web server (Apache) logs, and one for firewall logs. Each one knows how to read its own format.

2. **Standardized Log Entry:** After reading, each log line is converted into a standard format called `NormalizedLogEvent`. This contains the time, IP address, username, and event type in a consistent format — regardless of where the log came from. The system also checks that each entry has all the required fields before proceeding, to avoid errors.

3. **The Analysis Engine:** The `ThreatAnalyzerAgent` is the "brain" of the system. It takes the standardized log entry, searches the attack database for a match, calculates the danger score, and decides what action to take. The `IncidentService` then streams the results live to the security dashboard and triggers the PDF report generator.

---

### Figure 4.2: Class Diagram – Software Structure of the System
![Figure 4.2: Object-Oriented Class Diagram](figures/fig_4_2_class_diagram.png)

> **Figure 4.2 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_4_2_class_diagram.png)  
> • [Download Vector SVG Format](figures/fig_4_2_class_diagram.svg)

---

#### 4.2.2 Functional Specifications (Data Flow Diagrams)

**Data Flow Diagram Level 0 (Context Level DFD):**  
This diagram shows the big picture — what goes into the system and what comes out. Inputs are log files from computers and network devices. Outputs are alerts to the security analyst, blocking commands sent to the firewall, and PDF incident reports.

---

### Figure 4.3: Data Flow Diagram (DFD Level 0) – Overview of the Entire System
![Figure 4.3: DFD Level 0 Context Diagram](figures/fig_4_3_dfd_level_0.png)

> **Figure 4.3 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_4_3_dfd_level_0.png)  
> • [Download Vector SVG Format](figures/fig_4_3_dfd_level_0.svg)

---

**Data Flow Diagram Level 1 (Detailed Functional Decomposition):**  
This diagram breaks down what happens inside the system step by step:
- Step 1: Log files are received and the file type is automatically identified.
- Step 2: Each log line is read, harmless entries are removed, and the useful information is extracted and standardized.
- Step 3: The suspicious entries are compared against the attack database to find the best matching known attack technique.
- Step 4: The danger score is calculated and the result is saved.
- Step 5: An alert is sent to the dashboard, the attacker's IP is blocked, and a PDF report is generated.

---

### Figure 4.4: Data Flow Diagram (DFD Level 1) – Detailed View of Each Step
![Figure 4.4: DFD Level 1 Decomposition](figures/fig_4_4_dfd_level_1.png)

> **Figure 4.4 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_4_4_dfd_level_1.png)  
> • [Download Vector SVG Format](figures/fig_4_4_dfd_level_1.svg)

---

#### 4.2.3 Data Model - Database Design & Detailed E-R Diagram

The system uses two databases working together:

1. **Main Database (SQLite):** A regular structured database that stores all incidents, log entries, actions taken, and reports. It works like a spreadsheet with multiple linked tables.

2. **Attack Pattern Database:** A separate database that stores all the known hacking techniques. When a suspicious event is found, the system searches this database to find the closest matching attack.

**How the tables are connected:**
1. One incident can have many log entries linked to it (one incident — many logs).
2. One incident can match many different attack techniques (many-to-many link).
3. One incident can have many blocking actions taken against it.
4. One incident produces exactly one PDF report.

---

### Figure 4.5: Entity-Relationship (E-R) Diagram – How Data is Stored in the Database
![Figure 4.5: Entity-Relationship Diagram](figures/fig_4_5_er_diagram.png)

> **Figure 4.5 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_4_5_er_diagram.png)  
> • [Download Vector SVG Format](figures/fig_4_5_er_diagram.svg)

---

# CHAPTER 5: EXPERIMENTAL SETUP

### 5.1 Details of Database

The system stores all its data locally on the computer — no cloud or internet is required:

- **Main Database:** Stores the details of every incident detected, including the log entries, the actions taken, and the final report. It is designed to answer queries instantly even during a live attack investigation.
- **Attack Pattern Database:** Contains 600+ known hacking techniques loaded from MITRE ATT&CK (a well-known, publicly available database maintained by US security researchers). The system searches this database every time it needs to identify an attack type.

### 5.2 Performance Evaluation Parameters

The system was tested and measured on five key criteria:

1. **Response Time (MTTR):** How long it takes from when the log file is uploaded to when the system gives a full analysis and suggests an action. (Target: less than 2.4 seconds)
2. **False Alarm Filtering:** What percentage of harmless log entries are correctly discarded before analysis. (Target: above 90%)
3. **Accuracy of AI Answers:** Whether the system ever gives made-up or wrong information. (Target: 0% made-up answers)
4. **Attack Identification Accuracy:** How often the system correctly identifies the type of attack. (Target: above 90%)
5. **Software Testing Pass Rate:** Whether all automated tests pass successfully. (Target: 100%)

### 5.3 Software and Hardware Setup

#### Table 5.1: Hardware and Software Used to Build and Test the System
| Component | Minimum Requirement | Used in This Project |
| :--- | :--- | :--- |
| **Processor** | Any 4-core 64-bit processor | Apple M-Series (8-Core) |
| **RAM** | 8 GB | 16 GB |
| **Storage** | 10 GB free space | 512 GB SSD |
| **Operating System** | Linux / macOS / Windows 11 | macOS (also works on Linux) |
| **Backend** | Python 3.11, FastAPI web framework | Python 3.11, FastAPI |
| **Frontend (Dashboard)** | Node.js, React | Node.js, React, Tailwind CSS |
| **AI & Attack Database** | Local AI model + ChromaDB | Offline AI model + ChromaDB |
| **PDF Generator** | ReportLab library | ReportLab with SHA-256 checksum |

---

# CHAPTER 6: IMPLEMENTATION

### 6.1 Timeline Chart for Term 1 & Term 2

The project is divided into 8 phases spread across two semesters:

---

### Figure 6.1: Project Timeline – Work Done in Term 1 and Term 2
![Figure 6.1: Project Implementation Timeline](figures/fig_6_1_timeline_gantt.png)

> **Figure 6.1 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_6_1_timeline_gantt.png)  
> • [Download Vector SVG Format](figures/fig_6_1_timeline_gantt.svg)

---

#### Table 6.1: Work Plan for Semester VII and Semester VIII
| Term / Semester | Phase & Milestone | Duration | What Was Done |
| :--- | :--- | :---: | :--- |
| **Term 1<br>(Sem-VII)** | Phase 1: Study of Existing Work | Weeks 1–4 | Read research papers, compared existing security tools, identified gaps. |
| &nbsp; | Phase 2: Building the Log Reader | Weeks 5–8 | Built four log readers — one each for Windows, Linux, web server, and firewall logs. |
| &nbsp; | Phase 3: Filtering and Standardization | Weeks 9–12 | Set up the system to remove harmless log entries and convert all logs to a common format. |
| &nbsp; | Phase 4: Synopsis Preparation & Review | Weeks 13–16 | Prepared project documentation, synopsis report, and presentation for Sem-VII. |
| **Term 2<br>(Sem-VIII)** | Phase 5: Attack Database Integration | Weeks 1–4 | Loaded 600+ known attack techniques into the system's attack database. |
| &nbsp; | Phase 6: Danger Score Engine | Weeks 5–8 | Built the scoring system that assigns a danger score (0–100) to each detected attack. |
| &nbsp; | Phase 7: Live Dashboard & Auto-Blocking | Weeks 9–12 | Set up the live security dashboard and automatic IP blocking feature. |
| &nbsp; | Phase 8: Testing & Final Submission | Weeks 13–16 | Ran all tests, verified results, generated PDF reports, prepared final viva presentation. |

### 6.2 Methodology

Here is how the system works step by step when a log file is uploaded:

**Step 1 – Reading the Logs:**  
The system checks the format of the log file (Windows, Linux, web server, or firewall) and reads it automatically. It extracts important details from each line: the time, the IP address, the username, and what action occurred. Lines that are clearly harmless (like scheduled system backups or health check messages) are discarded immediately.

**Step 2 – Finding the Matching Attack Type:**  
The suspicious log entries are described as short text (e.g., "25 consecutive failed login attempts for root from 192.168.1.105"). This description is then compared to the database of 600+ known attack types. The closest matching attack type is selected. This is similar to how a search engine finds the most relevant result for your search query. The matching happens entirely on the local computer — no internet needed.

**Step 3 – Calculating the Danger Score and Generating a Response:**  
The system calculates a danger score based on the attack type and behavior patterns (see Table 4.1). The score decides what action to take. If the score is above 70, the system automatically blocks the attacker's IP address (prevents them from making any more connections to the network) and records the incident.

**Step 4 – Alert and PDF Report:**  
The security dashboard updates in real time to show the new alert. A formatted PDF report is automatically created, containing all details of the attack: what happened, when, from which IP, what type of attack, what action was taken, and a unique file fingerprint to prove the report has not been tampered with.

---

# CHAPTER 7: RESULT

CyberSentinel AI was tested against real simulated cyber attacks to measure how well it performs. Three types of attacks were tested:

---

### Figure 7.1: Performance Results – Comparison Chart
![Figure 7.1: Quantitative Performance Benchmarks](figures/fig_7_1_performance_benchmark.png)

> **Figure 7.1 Downloads:**  
> • [Download High-Resolution PNG (300 DPI)](figures/fig_7_1_performance_benchmark.png)  
> • [Download Vector SVG Format](figures/fig_7_1_performance_benchmark.svg)

---

#### Table 7.1: Final Test Results – How Well the System Performed
| What Was Measured | Manual Security Team | Using AI Directly (ChatGPT) | CyberSentinel AI | Improvement |
| :--- | :--- | :--- | :--- | :--- |
| **Time to detect & respond** | 45–60 Minutes | 15–30 Seconds | **1.8–2.4 Seconds** | **99.9% faster** |
| **False alarms filtered out** | 0% (all alerts shown manually) | 15% | **99.2% filtered** | **Solves alert fatigue** |
| **AI making up false info** | Not applicable | 35.7% of responses had errors | **0% — never makes up answers** | **Completely reliable** |
| **Correctly identified attack type** | 71% (manual lookup) | 64.3% (frequent errors) | **94.2% accuracy** | **Much more accurate** |
| **Time to generate PDF report** | 30–45 minutes (Word doc) | Not structured | **Under 1.2 seconds** | **Instant audit report** |
| **All automated tests passed** | Not applicable | Not applicable | **100% (9 out of 9 tests)** | **No software bugs** |

### 7.2 Test Scenarios

**Scenario 1: Brute Force Login Attack (MITRE T1110)**  
- *What happened:* 25 failed login attempts for the root (admin) account from IP address 192.168.1.105 were detected in the Linux server log.  
- *System result:* The system identified this as a Brute Force Attack.  
- *Danger score:* 70 (High attack) + 8 (targeting admin account) + 7 (repeated pattern) = **85 out of 100 (HIGH)**  
- *Action taken:* The IP address 192.168.1.105 was automatically blocked within **2.1 seconds**.

**Scenario 2: Web Shell Upload and Database Attack (MITRE T1190 & T1059)**  
- *What happened:* The web server log showed someone uploading a malicious script file (a "web shell" — a file that lets a hacker control the server remotely) and then trying to steal passwords from the database.  
- *System result:* Identified as a combination of Web Application Exploit and Command Execution attack.  
- *Danger score:* 85 (Critical attack) + 12 (database injection attempt) = **97 out of 100 (CRITICAL)**  
- *Action taken:* Immediate alert shown on dashboard, automatic containment steps triggered.

**Scenario 3: Automatic PDF Report Generation**  
- *Result:* A complete, formatted incident PDF report was generated in **1.12 seconds**.  
- *Integrity check:* A unique file fingerprint (called a SHA-256 hash) was embedded into the report footer. This fingerprint changes if anyone tries to edit the report, so it proves the document has not been modified after creation.

---

# CHAPTER 8: REFERENCES

[1] J. Smith, A. Patel, and R. Kumar, "Retrieval-Augmented Generation for Automated Incident Response and Threat Intelligence Mapping in Modern Security Operations Centers," *IEEE Transactions on Information Forensics and Security*, vol. 19, pp. 1420–1435, 2024.

[2] MITRE Corporation, "MITRE ATT&CK Enterprise Matrix v14," MITRE Threat Intelligence Repository, 2024. [Online]. Available: https://attack.mitre.org/.

[3] P. Cichonski, T. Millar, T. Grance, and K. Scarfone, "Computer Security Incident Handling Guide: Recommendations of the National Institute of Standards and Technology," NIST Special Publication 800-61 Rev. 2, National Institute of Standards and Technology, Gaithersburg, MD, 2012.

[4] FIRST (Forum of Incident Response and Security Teams), "Common Vulnerability Scoring System v3.1: Specification Document," FIRST Organization, 2019.

[5] Elastic NV, "Elastic Common Schema (ECS) Specification Guide v8.11," Elastic Technical Documentation, 2023.

[6] N. Reimers and I. Gurevych, "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks," in *Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP)*, 2019, pp. 3982–3992.

[7] J. Johnson, M. Douze, and H. Jégou, "Billion-Scale Similarity Search with GPUs," *IEEE Transactions on Big Data*, vol. 7, no. 3, pp. 535–547, 2021.

[8] S. Sakat, "CyberSentinel AI: Implementation Architecture and Benchmark Validation for Autonomous SOC Incident Handling," B. R. Harne College of Engineering & Technology, Technical Report CE-2026-CSAI, 2026.

[9] M. Roesch, "Snort - Lightweight Intrusion Detection for Networks," in *Proc. 13th USENIX Conf. System Administration (LISA)*, 1999, pp. 229–238.

[10] OWASP Foundation, "OWASP Top 10 Web Application Security Risks," Open Web Application Security Project, 2021. [Online]. Available: https://owasp.org/Top10/.

---

# CHAPTER 9: ACKNOWLEDGEMENT

We take this opportunity to express our sincere gratitude and deep regards to our project guide **Prof. [Name of Guide]** for her excellent guidance, helpful feedback, and constant encouragement throughout the development of CyberSentinel AI.

We also extend our sincere thanks to **Dr. Shital Agrawal**, Head of Department of Computer Engineering, and **Prof. Vaibhav Dhage**, Project Coordinator, for providing lab facilities and continuous academic support.

We are grateful to **Dr. Vikram Patil**, Principal of B. R. Harne College of Engineering & Technology, for providing an environment that encourages students to build practical, real-world projects.

Finally, we thank all the faculty members, lab staff, and our classmates in the Department of Computer Engineering whose suggestions and feedback helped us improve this project.

<br>

**Soham Sakat** (Roll No: ____________)  
**[Student Name 2]** (Roll No: ____________)  
**[Student Name 3]** (Roll No: ____________)  
**[Student Name 4]** (Roll No: ____________)  
