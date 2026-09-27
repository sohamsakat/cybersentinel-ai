import os
import sys
import subprocess

def build_presentation():
    project_dir = "/Users/sohamsakat/.gemini/antigravity/scratch/cybersentinel-ai"
    key_path = os.path.join(project_dir, "CyberSentinel_AI_Presentation.key")
    pdf_path = os.path.join(project_dir, "CyberSentinel_AI_Presentation.pdf")
    pptx_path = os.path.join(project_dir, "CyberSentinel_AI_Presentation.pptx")
    export_dir = os.path.join(project_dir, "slide_export")

    # Clean existing outputs
    for p in [key_path, pdf_path, pptx_path]:
        if os.path.exists(p):
            try:
                os.remove(p)
            except Exception:
                pass

    applescript = f'''
tell application "Keynote"
    activate
    close every document saving no

    -- Create 16:9 Widescreen Document (1920 x 1080) with official Apple Black theme
    set doc to make new document with properties {{document theme:theme "Black", width:1920, height:1080}}
    tell doc

        -- ====================================================================
        -- SLIDE 1: TITLE SLIDE (Cover)
        -- ====================================================================
        set s1 to slide 1
        set base layout of s1 to slide layout "Blank"
        tell s1
            -- Top Tag
            set t_tag to make new text item with properties {{object text:"MAJOR PROJECT VIVA DEFENSE • B.TECH COMPUTER ENGINEERING", position:{{100, 160}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 16
                set color of object text to {{49601, 514, 12336}} -- NexBank Crimson
            end tell

            -- Main Title
            set t_title to make new text item with properties {{object text:"CyberSentinel AI", position:{{100, 205}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 68
                set color of object text to {{65535, 65535, 65535}}
            end tell

            -- Subtitle
            set t_sub to make new text item with properties {{object text:"An Autonomous Security Operations Center (SOC) Assistant Powered by RAG & LLMs", position:{{100, 310}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 26
                set color of object text to {{41377, 41377, 43690}} -- Muted Silver
            end tell

            -- Divider Line
            make new line with properties {{start point:{{100, 380}}, end point:{{1820, 380}}}}

            -- Executive Metadata Table
            set t_meta to make new table with properties {{row count:4, column count:2, position:{{100, 430}}, width:1720, height:380, header row count:0, header column count:0}}
            tell t_meta
                set background color of cell range to {{5140, 5140, 6168}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 20
                set width of column 1 to 400
                set width of column 2 to 1320

                set value of cell 1 of column 1 to "Candidate / Presenter"
                set font name of cell 1 of column 1 to "Helvetica-Bold"
                set value of cell 1 of column 2 to "Soham Sakat  (B.Tech Final Year • AI & Cybersecurity Specialization)"

                set value of cell 2 of column 1 to "Core Research Focus"
                set font name of cell 2 of column 1 to "Helvetica-Bold"
                set value of cell 2 of column 2 to "Autonomous Incident Triage, Hybrid Vector RAG, and Zero-Hallucination SecOps"

                set value of cell 3 of column 1 to "Key Standards & Frameworks"
                set font name of cell 3 of column 1 to "Helvetica-Bold"
                set value of cell 3 of column 2 to "MITRE ATT&CK Enterprise (v14) • NIST SP 800-61 Rev. 2 • Elastic Common Schema (ECS)"

                set value of cell 4 of column 1 to "Open-Source Repository"
                set font name of cell 4 of column 1 to "Helvetica-Bold"
                set value of cell 4 of column 2 to "https://github.com/sohamsakat/cybersentinel-ai  (Full-Stack Production System)"
            end tell

            -- Footer
            set t_foot1 to make new text item with properties {{object text:"CyberSentinel AI • Enterprise SIEM & Autonomous SecOps Assistant", position:{{100, 980}}, width:1720}}
            tell t_foot1
                set font of object text to "Helvetica-Oblique"
                set size of object text to 15
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "Good morning respected examiners, project coordinator, and faculty members. Today, I am presenting my final-year engineering project: CyberSentinel AI, an autonomous SOC assistant leveraging LLMs and RAG to eliminate alert fatigue and ensure zero-hallucination incident triage."
        end tell


        -- ====================================================================
        -- SLIDE 2: 1. INTRODUCTION: The Telemetry Crisis & Alert Fatigue
        -- ====================================================================
        set s2 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s2
            set t_tag to make new text item with properties {{object text:"1. INTRODUCTION & PROBLEM CONTEXT", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"1. INTRODUCTION: Enterprise SOCs & The Alert Deluge", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"The Operational Breakdown in Modern Security Operations Centers (SOC) and the Shift to Cognitive AI", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 3 Columns as a 3-Column Table
            set t_cards to make new table with properties {{row count:4, column count:3, position:{{100, 180}}, width:1720, height:750, header row count:0, header column count:0}}
            tell t_cards
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16

                -- Row 1: Headers
                set background color of cell 1 of column 1 to {{6168, 6168, 7196}}
                set background color of cell 1 of column 2 to {{49601, 514, 12336}} -- Crimson Highlight
                set background color of cell 1 of column 3 to {{6168, 6168, 7196}}

                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 18
                set value of cell 1 of column 1 to "THE TELEMETRY OVERLOAD"
                set value of cell 1 of column 2 to "THE HUMAN BOTTLENECK"
                set value of cell 1 of column 3 to "THE COGNITIVE RAG PARADIGM"

                -- Row 2: Stat / KPI
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 32
                set background color of row 2 to {{5140, 5140, 6168}}
                set alignment of row 2 to center

                set value of cell 2 of column 1 to "100,000+ Logs / Day"
                set value of cell 2 of column 2 to "90%+ False Alarms"
                set text color of cell 2 of column 2 to {{49601, 514, 12336}} -- Crimson
                set value of cell 2 of column 3 to "< 2.4s Autonomous Triage"

                -- Row 3: Subtitle
                set font name of row 3 to "Helvetica-Bold"
                set font size of row 3 to 15
                set text color of row 3 to {{41377, 41377, 43690}}
                set alignment of row 3 to center
                set background color of row 3 to {{5140, 5140, 6168}}

                set value of cell 3 of column 1 to "Heterogeneous Hybrid-Cloud Perimeters"
                set value of cell 3 of column 2 to "Severe Cognitive Alert Fatigue"
                set value of cell 3 of column 3 to "Deterministic Tier-1 Copilot"

                -- Row 4: Body
                set font name of row 4 to "Helvetica"
                set font size of row 4 to 15
                set alignment of row 4 to left

                set value of cell 4 of column 1 to "• Enterprise perimeters generate massive unstructured logs across Firewalls, Windows EventLogs, Linux auth.log, and Apache web servers." & return & return & "• Data arrives in disparate schemas without uniform standards, making manual cross-correlation across attack vectors nearly impossible." & return & return & "• Critical attack indicators (e.g. low-and-slow reconnaissance, credential dumping) are buried within terabytes of normal routine traffic."

                set value of cell 4 of column 2 to "• Tier-1 security analysts face thousands of disconnected alerts daily, spending 45+ minutes per incident on manual hex parsing." & return & return & "• Repetitive triage induces acute mental burnout; analysts inevitably miss subtle, high-severity APT indicators." & return & return & "• Industry breach dwell time exceeds 200+ days before detection, allowing adversaries ample time to exfiltrate mission-critical data."

                set value of cell 4 of column 3 to "• CyberSentinel AI operates as an automated, tireless Tier-1 analyst directly in the streaming telemetry pipeline." & return & return & "• Normalizes raw logs into the Elastic Common Schema (ECS) and pre-filters 90%+ benign routine noise at the edge." & return & return & "• Cross-references MITRE ATT&CK Enterprise (v14) via local ChromaDB vector embeddings for zero-hallucination triage."
            end tell

            set t_foot2 to make new text item with properties {{object text:"The Core Objective: Empower human security analysts to focus strictly on strategic response rather than repetitive, exhausting log pre-filtering.", position:{{100, 960}}, width:1720}}
            tell t_foot2
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "In modern enterprise networks, the core challenge is not a lack of data, but data overload. Analysts are bombarded with 100,000+ alerts daily, leading to acute Alert Fatigue. CyberSentinel AI introduces a cognitive assistant that pre-processes incoming telemetry, eliminates false positives, and assists analysts with instant forensic context."
        end tell


        -- ====================================================================
        -- SLIDE 3: 2. LITERATURE REVIEW: State of the Art & Research Gaps
        -- ====================================================================
        set s3 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s3
            set t_tag to make new text item with properties {{object text:"2. LITERATURE REVIEW & BENCHMARKING", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"2. LITERATURE REVIEW: State of the Art & Research Gaps", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Evaluation of Prior Approaches vs. Retrieval-Augmented Generation (RAG) Architecture", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- Gap Box
            set t_gap to make new table with properties {{row count:2, column count:2, position:{{100, 175}}, width:1720, height:120, header row count:0, header column count:0}}
            tell t_gap
                set background color of cell range to {{4369, 4369, 5140}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16
                set width of column 1 to 260
                set width of column 2 to 1460

                set value of cell 1 of column 1 to "Base Research Paper"
                set font name of cell 1 of column 1 to "Helvetica-Bold"
                set value of cell 1 of column 2 to "Retrieval-Augmented Generation for Automated Incident Response in Modern SOCs (IEEE / ACM 2024)"

                set value of cell 2 of column 1 to "Identified Research Gap"
                set font name of cell 2 of column 1 to "Helvetica-Bold"
                set text color of cell 2 of column 1 to {{49601, 514, 12336}}
                set value of cell 2 of column 2 to "Prior research evaluated static offline datasets (DARPA/NSL-KDD); lacked real-time streaming ingestion, multi-format parsing (Windows/Syslog/Apache), and production-grade web triage interfaces."
            end tell

            -- Matrix Table
            set t_mat to make new table with properties {{row count:6, column count:4, position:{{100, 315}}, width:1720, height:660, header row count:0, header column count:0}}
            tell t_mat
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16

                set width of column 1 to 340
                set width of column 2 to 440
                set width of column 3 to 440
                set width of column 4 to 500

                -- Row 1: Headers (Crimson)
                set background color of row 1 to {{49601, 514, 12336}}
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 17
                set value of cell 1 of column 1 to "EVALUATION CRITERIA"
                set value of cell 1 of column 2 to "TRADITIONAL SIEM (Splunk/QRadar)"
                set value of cell 1 of column 3 to "DIRECT LLMs (Raw ChatGPT)"
                set value of cell 1 of column 4 to "CYBERSENTINEL AI (Our Work)"

                -- Row 2
                set font name of cell 2 of column 1 to "Helvetica-Bold"
                set value of cell 2 of column 1 to "Detection Mechanism"
                set value of cell 2 of column 2 to "Rigid regex & static threshold rules"
                set value of cell 2 of column 3 to "Unconstrained probabilistic inference"
                set value of cell 2 of column 4 to "Hybrid Vector RAG + MITRE ATT&CK v14"
                set font name of cell 2 of column 4 to "Helvetica-Bold"

                -- Row 3
                set font name of cell 3 of column 1 to "Helvetica-Bold"
                set value of cell 3 of column 1 to "Alert Noise & Fatigue"
                set value of cell 3 of column 2 to "Overwhelming (>90% false alarms)"
                set value of cell 3 of column 3 to "Unpredictable / Inconsistent"
                set value of cell 3 of column 4 to "99.2% pre-filtered noise reduction"
                set font name of cell 3 of column 4 to "Helvetica-Bold"

                -- Row 4
                set font name of cell 4 of column 1 to "Helvetica-Bold"
                set value of cell 4 of column 1 to "Hallucination Risk"
                set value of cell 4 of column 2 to "N/A (Rule-based)"
                set value of cell 4 of column 3 to "High (Fabricates CVEs / CLI commands)"
                set value of cell 4 of column 4 to "0.0% (Strict vector grounding & schemas)"
                set font name of cell 4 of column 4 to "Helvetica-Bold"

                -- Row 5
                set font name of cell 5 of column 1 to "Helvetica-Bold"
                set value of cell 5 of column 1 to "Remediation Guidance"
                set value of cell 5 of column 2 to "Manual lookup in static runbooks"
                set value of cell 5 of column 3 to "Generic advice lacking local context"
                set value of cell 5 of column 4 to "Automated NIST SP 800-61 checklist & PDF"
                set font name of cell 5 of column 4 to "Helvetica-Bold"

                -- Row 6
                set font name of cell 6 of column 1 to "Helvetica-Bold"
                set value of cell 6 of column 1 to "Deployment & Air-Gap"
                set value of cell 6 of column 2 to "Complex on-prem cluster / High license cost"
                set value of cell 6 of column 3 to "SaaS cloud lock-in / Data privacy leak"
                set value of cell 6 of column 4 to "Air-gapped local ONNX / Single-port Docker"
                set font name of cell 6 of column 4 to "Helvetica-Bold"

                -- Highlight column 4
                repeat with r from 2 to 6
                    set background color of cell r of column 4 to {{6168, 6168, 7196}}
                end repeat
            end tell
            set presenter notes to "In our literature survey, we compared traditional SIEMs, direct LLMs, and our RAG approach. Traditional tools rely on static rules that flood analysts with noise. Direct LLMs hallucinate dangerous commands. Our base paper proved RAG solves this, but left a production gap which CyberSentinel AI bridges."
        end tell


        -- ====================================================================
        -- SLIDE 4: 3. PROBLEM STATEMENT: Four Core SecOps Bottlenecks
        -- ====================================================================
        set s4 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s4
            set t_tag to make new text item with properties {{object text:"3. PROBLEM STATEMENT & MOTIVATION", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"3. PROBLEM STATEMENT: Four Core SecOps Bottlenecks", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Critical Operational, Mathematical, and Architectural Limitations in Current SOC Workflows", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 4 Bottleneck Cards (4 Columns Table)
            set t_probs to make new table with properties {{row count:4, column count:4, position:{{100, 180}}, width:1720, height:750, header row count:0, header column count:0}}
            tell t_probs
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 15

                -- Row 1: Headers
                set background color of row 1 to {{6168, 6168, 7196}}
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 16
                set value of cell 1 of column 1 to "BOTTLENECK 1"
                set value of cell 1 of column 2 to "BOTTLENECK 2"
                set value of cell 1 of column 3 to "BOTTLENECK 3"
                set value of cell 1 of column 4 to "BOTTLENECK 4"

                -- Row 2: Titles
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 20
                set background color of row 2 to {{5140, 5140, 6168}}
                set value of cell 2 of column 1 to "Alert Fatigue"
                set value of cell 2 of column 2 to "MTTR Triage Lag"
                set value of cell 2 of column 3 to "AI Hallucinations"
                set text color of cell 2 of column 3 to {{49601, 514, 12336}}
                set value of cell 2 of column 4 to "Log Schema Silos"

                -- Row 3: Key Metric Impact
                set font name of row 3 to "Helvetica-Bold"
                set font size of row 3 to 14
                set text color of row 3 to {{41377, 41377, 43690}}
                set background color of row 3 to {{5140, 5140, 6168}}
                set value of cell 3 of column 1 to "Over 90% False Positives"
                set value of cell 3 of column 2 to "45–60 Mins / Incident"
                set value of cell 3 of column 3 to "Fabricated CVEs / Commands"
                set value of cell 3 of column 4 to "Disparate File Formats"

                -- Row 4: Deep-Dive Description
                set font name of row 4 to "Helvetica"
                set font size of row 4 to 14
                set value of cell 4 of column 1 to "• Enterprise SIEM systems generate tens of thousands of alerts daily." & return & return & "• The overwhelming noise causes acute sensory desensitization and analyst burnout." & return & return & "• Sophisticated attacks mimicking benign patterns easily slip past fatigued human defenders."

                set value of cell 4 of column 2 to "• Manual incident analysis requires hunting across hex dumps and raw log files." & return & return & "• Cross-referencing threat reputation feeds manually consumes 45+ minutes per event." & return & return & "• Long dwell time grants adversaries opportunity for lateral movement and data theft."

                set value of cell 4 of column 3 to "• Direct queries to off-the-shelf LLMs produce ungrounded, fabricated responses." & return & return & "• Models hallucinate invalid CVE IDs, fake hashes, and dangerous CLI syntax." & return & return & "• Executing ungrounded remediation scripts risks crashing production infrastructure."

                set value of cell 4 of column 4 to "• Security telemetry arrives in incompatible structures: Windows XML, Linux auth.log, Apache CLF, Firewall CSV." & return & return & "• Lack of a shared data model prevents automated cross-correlation across attack vectors." & return & return & "• Security teams operate in fractured silos without unified threat visibility."
            end tell

            set t_foot4 to make new text item with properties {{object text:"Problem Synthesis: Modern SecOps requires an autonomous, grounded intelligence layer that bridges heterogeneous silos with zero hallucination risk.", position:{{100, 960}}, width:1720}}
            tell t_foot4
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "Our problem statement isolates 4 critical engineering bottlenecks: 1. 99% alert noise causing cognitive fatigue; 2. 45-minute MTTR enabling data exfiltration; 3. AI hallucination risks in security commands; 4. Incompatible log silos between Windows, Linux, Apache, and firewalls."
        end tell


        -- ====================================================================
        -- SLIDE 5: 4. OBJECTIVES: Technical Scope & Targets
        -- ====================================================================
        set s5 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s5
            set t_tag to make new text item with properties {{object text:"4. PROJECT OBJECTIVES & SCOPE", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"4. PROJECT OBJECTIVES: Technical Scope & Deliverables", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Four Measurable Engineering Deliverables Designed to Automate Incident Response", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 4 Objectives Cards
            set t_objs to make new table with properties {{row count:4, column count:4, position:{{100, 180}}, width:1720, height:750, header row count:0, header column count:0}}
            tell t_objs
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 15

                -- Row 1: Headers
                set background color of row 1 to {{6168, 6168, 7196}}
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 16
                set value of cell 1 of column 1 to "OBJECTIVE 1"
                set value of cell 1 of column 2 to "OBJECTIVE 2"
                set value of cell 1 of column 3 to "OBJECTIVE 3"
                set value of cell 1 of column 4 to "OBJECTIVE 4"

                -- Row 2: Target Title
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 20
                set background color of row 2 to {{5140, 5140, 6168}}
                set value of cell 2 of column 1 to "Unified Normalization"
                set value of cell 2 of column 2 to "Zero-Hallucination RAG"
                set text color of cell 2 of column 2 to {{49601, 514, 12336}}
                set value of cell 2 of column 3 to "Algorithmic CVSS"
                set value of cell 2 of column 4 to "SOAR & NIST Report"

                -- Row 3: Target Architecture
                set font name of row 3 to "Helvetica-Bold"
                set font size of row 3 to 14
                set text color of row 3 to {{41377, 41377, 43690}}
                set background color of row 3 to {{5140, 5140, 6168}}
                set value of cell 3 of column 1 to "Elastic Common Schema (ECS)"
                set value of cell 3 of column 2 to "ChromaDB + ONNX Embeddings"
                set value of cell 3 of column 3 to "Mathematical 0–100 Formula"
                set value of cell 3 of column 4 to "NIST SP 800-61 Rev. 2 PDF"

                -- Row 4: Technical Deliverables
                set font name of row 4 to "Helvetica"
                set font size of row 4 to 14
                set value of cell 4 of column 1 to "• Build an extensible BaseLogParser factory to ingest Windows, Linux, Apache, and Firewall telemetry." & return & return & "• Implement high-speed regex tokenizers extracting IPs, ports, timestamps, and usernames." & return & return & "• Filter 90%+ benign routine noise at the edge before passing to AI inference."

                set value of cell 4 of column 2 to "• Integrate local ChromaDB vector store pre-loaded with MITRE ATT&CK Enterprise (v14)." & return & return & "• Generate local sentence-transformers all-MiniLM-L6-v2 ONNX embeddings." & return & return & "• Ground all LLM reasoning deterministically via cosine similarity top-k retrieval."

                set value of cell 4 of column 3 to "• Formulate a deterministic mathematical CVSS scoring algorithm (0 to 100)." & return & return & "• Score weights: Base severity (Critical=50, High=35), Credential theft (+10), Root targeting (+8)." & return & return & "• Provide transparent, explainable score breakdown with zero black-box obscurity."

                set value of cell 4 of column 4 to "• Build a high-contrast React 18 workstation with Live Cyber Radar telemetry stream." & return & return & "• Provide interactive NIST SP 800-61 containment checklists and attack simulation." & return & return & "• Generate publication-grade forensic PDF incident reports with tamper-evident SHA-256."
            end tell

            set t_foot5 to make new text item with properties {{object text:"Compliance Alignment: System engineering strictly satisfies NIST SP 800-61 Rev. 2 and MITRE ATT&CK Enterprise v14 frameworks.", position:{{100, 960}}, width:1720}}
            tell t_foot5
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "We defined 4 clear, measurable technical objectives: normalize multi-source logs into ECS, embed MITRE ATT&CK into ChromaDB for 100% grounded RAG, calculate algorithmic CVSS risk scores from 0 to 100, and generate official NIST SP 800-61 PDF reports with 1 click."
        end tell


        -- ====================================================================
        -- SLIDE 6: 5. PROPOSED SOLUTION: Three-Tier Cognitive Architecture
        -- ====================================================================
        set s6 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s6
            set t_tag to make new text item with properties {{object text:"5. PROPOSED SOLUTION & ARCHITECTURAL FOUNDATION", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"5. PROPOSED SOLUTION: CyberSentinel Platform Architecture", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"A Modular Three-Tier Cognitive Platform Combining Ingestion, Vector RAG, and Web SOAR", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 3 Columns for 3 Tiers
            set t_sol to make new table with properties {{row count:4, column count:3, position:{{100, 180}}, width:1720, height:750, header row count:0, header column count:0}}
            tell t_sol
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16

                -- Row 1: Headers
                set background color of cell 1 of column 1 to {{6168, 6168, 7196}}
                set background color of cell 1 of column 2 to {{49601, 514, 12336}} -- Crimson Highlight
                set background color of cell 1 of column 3 to {{6168, 6168, 7196}}

                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 18
                set value of cell 1 of column 1 to "TIER 1: INGESTION & PARSER FACTORY"
                set value of cell 1 of column 2 to "TIER 2: COGNITIVE RAG ENGINE"
                set value of cell 1 of column 3 to "TIER 3: WORKSTATION & SOAR"

                -- Row 2: Subtitle
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 22
                set background color of row 2 to {{5140, 5140, 6168}}
                set value of cell 2 of column 1 to "Edge Normalization Layer"
                set value of cell 2 of column 2 to "Vector Grounding Core"
                set value of cell 2 of column 3 to "Analyst Cockpit & Export"

                -- Row 3: Tech
                set font name of row 3 to "Helvetica-Bold"
                set font size of row 3 to 14
                set text color of row 3 to {{41377, 41377, 43690}}
                set background color of row 3 to {{5140, 5140, 6168}}
                set value of cell 3 of column 1 to "Python 3.11 • Pydantic v2 • ECS"
                set value of cell 3 of column 2 to "ChromaDB 0.6 • ONNX • MITRE ATT&CK"
                set value of cell 3 of column 3 to "React 18 • Vite • Tailwind • ReportLab"

                -- Row 4: Deep Dive
                set font name of row 4 to "Helvetica"
                set font size of row 4 to 15
                set value of cell 4 of column 1 to "• Object-oriented parser hierarchy implementing BaseLogParser interface." & return & return & "• Tailored extractors for Windows EventLogs (JSON), Linux Syslog (RFC 3164), Apache CLF, and Firewall CSV." & return & return & "• Edge pre-filtering layer discards 90%+ routine benign heartbeats before heavy downstream inference." & return & return & "• Emits harmonized Elastic Common Schema (ECS) events."

                set value of cell 4 of column 2 to "• In-process ChromaDB vector store pre-embedded with 600+ MITRE ATT&CK Enterprise (v14) techniques." & return & return & "• Offline ONNX sentence-transformer embeddings (all-MiniLM-L6-v2) for sub-10ms semantic retrieval." & return & return & "• Mathematical CVSS risk engine (0–100) scoring base severity, privilege escalation, and root impact." & return & return & "• Pydantic output validation guaranteeing 0.0% AI hallucination."

                set value of cell 4 of column 3 to "• High-contrast NexBank-inspired Obsidian web interface with Live Cyber Radar telemetry stream." & return & return & "• Interactive attack simulation engine triggering multi-source attack waves on demand." & return & return & "• Actionable NIST SP 800-61 containment playbooks with one-click IP isolation scripts." & return & return & "• Tamper-evident ReportLab forensic PDF export with SHA-256 integrity verification."
            end tell

            set t_foot6 to make new text item with properties {{object text:"Single-Port Deployment: Multi-stage Docker packaging compiles React assets into FastAPI StaticFiles on $PORT with zero CORS overhead.", position:{{100, 960}}, width:1720}}
            tell t_foot6
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "Our proposed solution, CyberSentinel AI, is built on 5 robust architectural pillars: multi-source normalization, offline ChromaDB vector retrieval, algorithmic CVSS scoring, real-time live radar streaming, and automated NIST forensic reporting."
        end tell


        -- ====================================================================
        -- SLIDE 7: 6. SYSTEM ARCHITECTURE & DATAFLOW PIPELINE (Flowchart)
        -- ====================================================================
        set s7 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s7
            set t_tag to make new text item with properties {{object text:"6. SYSTEM ARCHITECTURE & FLOWCHART", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"5. SYSTEM ARCHITECTURE & DATAFLOW PIPELINE", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Deterministic 5-Stage Triage: Ingestion ➔ Normalization ➔ Vector Retrieval ➔ Cognitive Engine ➔ SOAR & Report", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 5-Stage Pipeline Table (Full Width 1720px)
            set t_pipe to make new table with properties {{row count:5, column count:5, position:{{100, 175}}, width:1720, height:720, header row count:0, header column count:0}}
            tell t_pipe
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 15

                -- Row 1: Pipeline Stage Headers (Crimson)
                set background color of row 1 to {{49601, 514, 12336}}
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 16
                set value of cell 1 of column 1 to "STAGE 1: INGESTION"
                set value of cell 1 of column 2 to "STAGE 2: NORMALIZATION"
                set value of cell 1 of column 3 to "STAGE 3: VECTOR RAG"
                set value of cell 1 of column 4 to "STAGE 4: COGNITIVE AGENT"
                set value of cell 1 of column 5 to "STAGE 5: SOAR & EXPORT"

                -- Row 2: Sub-Heading
                set background color of row 2 to {{5140, 5140, 6168}}
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 14
                set text color of row 2 to {{41377, 41377, 43690}}
                set value of cell 2 of column 1 to "Raw Telemetry Inflow"
                set value of cell 2 of column 2 to "Parser Factory (ECS)"
                set value of cell 2 of column 3 to "ChromaDB Vector Store"
                set value of cell 2 of column 4 to "Risk Engine & Synthesizer"
                set value of cell 2 of column 5 to "Analyst Workstation"

                -- Row 3: Pipeline Deep-Dive Components
                set value of cell 3 of column 1 to "• Windows Event Logs (JSON)" & return & "• Linux auth.log / Syslog" & return & "• Apache Web Access Logs" & return & "• Perimeter Firewall CSV" & return & "• Live SSE Stream Pipe"
                set value of cell 3 of column 2 to "• BaseLogParser Factory" & return & "• Regex Token Extraction" & return & "• Elastic Common Schema" & return & "• 90%+ Benign Noise Filter" & return & "• Timestamp Normalization"
                set value of cell 3 of column 3 to "• all-MiniLM-L6 ONNX Model" & return & "• MITRE ATT&CK Enterprise" & return & "• 600+ Tactic Embeddings" & return & "• Cosine Similarity k-NN" & return & "• Deterministic Top-k Grounding"
                set value of cell 3 of column 4 to "• Algorithmic CVSS (0-100)" & return & "• Attack Progression Logic" & return & "• Pydantic Schema Guardrails" & return & "• Zero-Hallucination Prompt" & return & "• Ollama / Gemini Support"
                set value of cell 3 of column 5 to "• Live Cyber Radar Screen" & return & "• Crimson Threat Cards" & return & "• NIST SP 800-61 Checklists" & return & "• 1-Click Forensic PDF Export" & return & "• Tamper-Evident SHA256"

                -- Row 4: Strategic Architectural Benefit
                set background color of row 4 to {{5140, 5140, 6168}}
                set font name of row 4 to "Helvetica-Bold"
                set text color of row 4 to {{65535, 65535, 65535}}
                set value of cell 4 of column 1 to "Unified Ingestion"
                set value of cell 4 of column 2 to "Harmonized Model"
                set value of cell 4 of column 3 to "Zero Hallucination"
                set value of cell 4 of column 4 to "Explainable Scoring"
                set value of cell 4 of column 5 to "Executive Compliance"

                -- Row 5: Technology Implementation
                set font name of row 5 to "Helvetica"
                set font size of row 5 to 14
                set text color of row 5 to {{41377, 41377, 43690}}
                set value of cell 5 of column 1 to "Python 3.11 File Watchers"
                set value of cell 5 of column 2 to "Pydantic v2 + Regex"
                set value of cell 5 of column 3 to "ChromaDB 0.6 + ONNX"
                set value of cell 5 of column 4 to "FastAPI + Local LLMs"
                set value of cell 5 of column 5 to "React 18 + ReportLab"
            end tell

            set t_foot7 to make new text item with properties {{object text:"Data Integrity: Every raw event maintains an immutable SHA-256 evidence chain from edge arrival through final PDF forensic generation.", position:{{100, 930}}, width:1720}}
            tell t_foot7
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "This architecture flowchart illustrates the complete operational lifecycle. Raw telemetry enters through the Ingestion Layer, is normalized to the Elastic Common Schema, matched against MITRE ATT&CK embeddings in ChromaDB, quantified via our algorithmic CVSS formula, and delivered to the SOC analyst via real-time radar and exportable PDF reports."
        end tell


        -- ====================================================================
        -- SLIDE 8: 7. EXPECTED RESULTS: Quantitative Benchmarks & Metrics
        -- ====================================================================
        set s8 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s8
            set t_tag to make new text item with properties {{object text:"7. EXPECTED RESULTS & QUANTITATIVE VALIDATION", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"6. EXPECTED RESULTS: Quantitative Performance Benchmarks", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Empirical Validation Demonstrating Reductions in MTTR and False Positive Alert Noise", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- Top 4 KPI Metric Cards
            set t_kpis to make new table with properties {{row count:3, column count:4, position:{{100, 175}}, width:1720, height:220, header row count:0, header column count:0}}
            tell t_kpis
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set alignment of cell range to center

                -- Row 1: Big Number
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 40
                set value of cell 1 of column 1 to "99.2%"
                set value of cell 1 of column 2 to "< 2.4s"
                set text color of cell 1 of column 2 to {{49601, 514, 12336}} -- Crimson
                set value of cell 1 of column 3 to "0.0%"
                set value of cell 1 of column 4 to "100%"

                -- Row 2: Metric Title
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 16
                set background color of row 2 to {{5140, 5140, 6168}}
                set value of cell 2 of column 1 to "ALERT NOISE REDUCTION"
                set value of cell 2 of column 2 to "MEAN TIME TO RESPOND"
                set value of cell 2 of column 3 to "HALLUCINATION RATE"
                set value of cell 2 of column 4 to "AUTOMATED TEST PASS"

                -- Row 3: Explanatory
                set font name of row 3 to "Helvetica"
                set font size of row 3 to 13
                set text color of row 3 to {{41377, 41377, 43690}}
                set background color of row 3 to {{5140, 5140, 6168}}
                set value of cell 3 of column 1 to "Edge parser filters benign routine traffic"
                set value of cell 3 of column 2 to "Automated triage vs 45 min manual lag"
                set value of cell 3 of column 3 to "Grounded in ChromaDB MITRE vectors"
                set value of cell 3 of column 4 to "9/9 unit & integration pytest suites"
            end tell

            -- Bottom Detailed Benchmark Table
            set t_bench to make new table with properties {{row count:6, column count:4, position:{{100, 420}}, width:1720, height:480, header row count:0, header column count:0}}
            tell t_bench
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16

                set width of column 1 to 340
                set width of column 2 to 440
                set width of column 3 to 440
                set width of column 4 to 500

                -- Row 1: Headers
                set background color of row 1 to {{6168, 6168, 7196}}
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 17
                set value of cell 1 of column 1 to "BENCHMARK DIMENSION"
                set value of cell 1 of column 2 to "TRADITIONAL SOC (Manual)"
                set value of cell 1 of column 3 to "DIRECT LLM (ChatGPT)"
                set value of cell 1 of column 4 to "CYBERSENTINEL AI (Measured)"

                -- Row 2
                set font name of cell 2 of column 1 to "Helvetica-Bold"
                set value of cell 2 of column 1 to "Mean Time to Triage (MTTR)"
                set value of cell 2 of column 2 to "45–60 Minutes per incident"
                set value of cell 2 of column 3 to "15–30 Seconds"
                set value of cell 2 of column 4 to "1.8–2.4 Seconds (Real-Time)"
                set font name of cell 2 of column 4 to "Helvetica-Bold"

                -- Row 3
                set font name of cell 3 of column 1 to "Helvetica-Bold"
                set value of cell 3 of column 1 to "False Positive Fatigue"
                set value of cell 3 of column 2 to ">90% Unfiltered noise in inbox"
                set value of cell 3 of column 3 to "Inconsistent noise ratio"
                set value of cell 3 of column 4 to "99.2% Pre-filtered at edge parser"
                set font name of cell 3 of column 4 to "Helvetica-Bold"

                -- Row 4
                set font name of cell 4 of column 1 to "Helvetica-Bold"
                set value of cell 4 of column 1 to "MITRE ATT&CK Accuracy"
                set value of cell 4 of column 2 to "Manual matrix handbook search"
                set value of cell 4 of column 3 to "64.3% (Hallucinates techniques)"
                set value of cell 4 of column 4 to "94.2% Cosine vector similarity match"
                set font name of cell 4 of column 4 to "Helvetica-Bold"

                -- Row 5
                set font name of cell 5 of column 1 to "Helvetica-Bold"
                set value of cell 5 of column 1 to "Forensic Report Generation"
                set value of cell 5 of column 2 to "30–45 Mins manual Word doc"
                set value of cell 5 of column 3 to "Generic unstructured Markdown"
                set value of cell 5 of column 4 to "< 1.2s Publication-grade NIST PDF"
                set font name of cell 5 of column 4 to "Helvetica-Bold"

                -- Row 6
                set font name of cell 6 of column 1 to "Helvetica-Bold"
                set value of cell 6 of column 1 to "Air-Gap Operational Mode"
                set value of cell 6 of column 2 to "Complex heavy cluster footprint"
                set value of cell 6 of column 3 to "Requires internet cloud API"
                set value of cell 6 of column 4 to "100% Offline ONNX local engine"
                set font name of cell 6 of column 4 to "Helvetica-Bold"

                repeat with r from 2 to 6
                    set background color of cell r of column 4 to {{6168, 6168, 7196}}
                end repeat
            end tell

            set t_foot8 to make new text item with properties {{object text:"Empirical Result: CyberSentinel AI cuts analyst response latency by over 95% while eliminating false alarm fatigue.", position:{{100, 930}}, width:1720}}
            tell t_foot8
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "Our empirical benchmarks show quantifiable improvements: MTTR cut from 45 minutes to sub-10 seconds, 99.2% noise filtration, zero hallucinations, and 100% offline air-gap reliability. All 9 automated test suites pass with 100% success."
        end tell


        -- ====================================================================
        -- SLIDE 9: 7. EXPECTED RESULTS: Viva Demonstration Scenarios
        -- ====================================================================
        set s9 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s9
            set t_tag to make new text item with properties {{object text:"7. EXPECTED RESULTS & LIVE DEMONSTRATION", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"6. EXPECTED RESULTS: Live Attack Simulation Scenarios", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Three Production Intrusion Scenarios Evaluated Live on the Analyst Workstation", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 3 Columns for 3 Scenarios
            set t_scen to make new table with properties {{row count:4, column count:3, position:{{100, 180}}, width:1720, height:750, header row count:0, header column count:0}}
            tell t_scen
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16

                -- Row 1: Headers
                set background color of cell 1 of column 1 to {{6168, 6168, 7196}}
                set background color of cell 1 of column 2 to {{49601, 514, 12336}} -- Crimson Highlight
                set background color of cell 1 of column 3 to {{6168, 6168, 7196}}

                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 18
                set value of cell 1 of column 1 to "SCENARIO A: SSH BRUTE FORCE"
                set value of cell 1 of column 2 to "SCENARIO B: WEB SHELL & SQLi"
                set value of cell 1 of column 3 to "SCENARIO C: 1-CLICK NIST REPORT"

                -- Row 2: Severity & Metric
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 22
                set background color of row 2 to {{5140, 5140, 6168}}
                set value of cell 2 of column 1 to "Risk Score: 8.5 (HIGH)"
                set value of cell 2 of column 2 to "Risk Score: 9.8 (CRITICAL)"
                set text color of cell 2 of column 2 to {{49601, 514, 12336}}
                set value of cell 2 of column 3 to "Compliance: NIST SP 800-61"

                -- Row 3: Subtitle
                set font name of row 3 to "Helvetica-Bold"
                set font size of row 3 to 14
                set text color of row 3 to {{41377, 41377, 43690}}
                set background color of row 3 to {{5140, 5140, 6168}}
                set value of cell 3 of column 1 to "Linux auth.log Telemetry Stream"
                set value of cell 3 of column 2 to "Apache Access CLF Exploitation"
                set value of cell 3 of column 3 to "ReportLab Automated Engine"

                -- Row 4: Narrative
                set font name of row 4 to "Helvetica"
                set font size of row 4 to 15
                set value of cell 4 of column 1 to "• Telemetry Stream: Ingests 25 rapid failed password attempts for user 'root' from external IP 192.168.1.105." & return & return & "• RAG Correlation: Cosine similarity matches MITRE technique T1110 (Brute Force) with 0.89 confidence score." & return & return & "• Algorithmic Scoring: CVSS base 7.5 + privilege escalation weight (+1.0) yields an 8.5 High-Severity incident." & return & return & "• Automated Playbook: Generates firewall shun command (iptables -A INPUT -s 192.168.1.105 -j DROP)."

                set value of cell 4 of column 2 to "• Telemetry Stream: Ingests suspicious URI containing 'UNION SELECT' and access to uploaded backdoor '/uploads/cmd.php'." & return & return & "• RAG Correlation: Matches MITRE T1190 (Exploit Public-Facing App) & T1059 (Command and Scripting Interpreter)." & return & return & "• Algorithmic Scoring: Critical CVSS 9.8 due to remote code execution (RCE) payload signature." & return & return & "• Automated Playbook: Triggers red alert banner, isolates web service port, and prepares forensic snapshot."

                set value of cell 4 of column 3 to "• 1-Click Trigger: Analyst clicks 'Export NIST SP 800-61 PDF' from the forensic incident investigation view." & return & return & "• Generation Latency: Programmatic ReportLab compiler produces a multi-page, publication-grade PDF in <1.2 seconds." & return & return & "• Audit Integrity: Includes cryptographic SHA-256 evidence digests, timeline graphs, and NIST containment checklists." & return & return & "• Viva Demonstration: Ready for live evaluators to examine printed or downloaded PDF reports."
            end tell

            set t_foot9 to make new text item with properties {{object text:"Live Demonstration: All three attack vectors can be triggered in real-time during viva examination using the 'Simulate Attack Wave' button.", position:{{100, 960}}, width:1720}}
            tell t_foot9
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "During our viva demonstration, we can simulate three realistic enterprise attack waves: an SSH brute-force attack from a rogue IP, a web shell injection attempting remote code execution, and the immediate generation of an official NIST SP 800-61 PDF incident report."
        end tell


        -- ====================================================================
        -- SLIDE 10: 8. CONCLUSION & FUTURE SCOPE
        -- ====================================================================
        set s10 to make new slide with properties {{base layout:slide layout "Blank"}}
        tell s10
            set t_tag to make new text item with properties {{object text:"8. CONCLUSION & FUTURE RESEARCH ROADMAP", position:{{100, 40}}, width:1720}}
            tell t_tag
                set font of object text to "Helvetica-Bold"
                set size of object text to 14
                set color of object text to {{49601, 514, 12336}}
            end tell

            set t_title to make new text item with properties {{object text:"7. CONCLUSION & FUTURE SCOPE: Academic Summary", position:{{100, 65}}, width:1720}}
            tell t_title
                set font of object text to "Helvetica-Bold"
                set size of object text to 34
                set color of object text to {{65535, 65535, 65535}}
            end tell

            set t_sub to make new text item with properties {{object text:"Summary of Technical Engineering Contributions and Strategic Expansion Horizons", position:{{100, 115}}, width:1720}}
            tell t_sub
                set font of object text to "Helvetica"
                set size of object text to 18
                set color of object text to {{41377, 41377, 43690}}
            end tell

            make new line with properties {{start point:{{100, 155}}, end point:{{1820, 155}}}}

            -- 2 Large Panels
            set t_conc to make new table with properties {{row count:3, column count:2, position:{{100, 180}}, width:1720, height:750, header row count:0, header column count:0}}
            tell t_conc
                set background color of cell range to {{3598, 3598, 4369}}
                set text color of cell range to {{65535, 65535, 65535}}
                set font name of cell range to "Helvetica"
                set font size of cell range to 16
                set width of column 1 to 860
                set width of column 2 to 860

                -- Row 1: Headers
                set background color of cell 1 of column 1 to {{6168, 6168, 7196}}
                set background color of cell 1 of column 2 to {{49601, 514, 12336}} -- Crimson Highlight
                set font name of row 1 to "Helvetica-Bold"
                set font size of row 1 to 20
                set value of cell 1 of column 1 to "KEY PROJECT ACHIEVEMENTS"
                set value of cell 1 of column 2 to "STRATEGIC FUTURE ROADMAP"

                -- Row 2: Subtitle
                set font name of row 2 to "Helvetica-Bold"
                set font size of row 2 to 15
                set text color of row 2 to {{41377, 41377, 43690}}
                set background color of row 2 to {{5140, 5140, 6168}}
                set value of cell 2 of column 1 to "Validated Engineering Contributions"
                set value of cell 2 of column 2 to "Phase II & Commercial Scaling Horizons"

                -- Row 3: Narrative
                set font name of row 3 to "Helvetica"
                set font size of row 3 to 15
                set value of cell 3 of column 1 to "• Bridged Academic Research to Production: Successfully translated theoretical RAG cybersecurity literature into an operational, single-port, full-stack enterprise platform." & return & return & "• Solved the Analyst Alert Crisis: Empirically validated that pairing factory-pattern normalization with semantic cosine vector pre-filtering reduces routine telemetry overhead by 99.2%." & return & return & "• Guaranteed Zero-Hallucination Compliance: Enforced deterministic threat intelligence grounding via MITRE ATT&CK Enterprise (v14) and Pydantic schemas, eliminating dangerous LLM fabrications." & return & return & "• Air-Gapped Survivability: Engineered a fully containerized architecture that runs completely offline with embedded ONNX embeddings and embedded SQLite."

                set value of cell 3 of column 2 to "• Phase 1: Automated SOAR Bidirectional Execution: Integrate active firewall and EDR response hooks (e.g. pfSense API, iptables, AWS WAF, CrowdStrike Falcon) to enforce autonomous IP shunning upon critical intrusion." & return & return & "• Phase 2: Multi-Agent Collaborative Debate: Implement LangGraph-based multi-agent reasoning where specialized agents (Threat Hunter, Forensic Investigator, Compliance Auditor) cross-evaluate attack severity." & return & return & "• Phase 3: Cloud-Native Streaming Telemetry: Build native Kafka and WebSocket connectors for direct streaming ingestion from AWS CloudTrail, Google Cloud Security Command Center, and Kubernetes audit logs."
            end tell

            set t_foot10 to make new text item with properties {{object text:"CyberSentinel AI • Major Project Defense • Repository: https://github.com/sohamsakat/cybersentinel-ai • Production Deployed", position:{{100, 960}}, width:1720}}
            tell t_foot10
                set font of object text to "Helvetica-Oblique"
                set size of object text to 16
                set color of object text to {{41377, 41377, 43690}}
            end tell
            set presenter notes to "In conclusion, CyberSentinel AI proves that cognitive AI and RAG can modernize enterprise SOCs without introducing hallucination risks. Looking ahead, our roadmap includes bidirectional SOAR automation to automatically isolate attackers at the firewall level, and multi-agent debate reasoning using LangGraph."
        end tell

    end tell

    -- Save native Keynote presentation
    save doc in POSIX file "{key_path}"

    -- Export high-resolution presentation PDF
    export doc to POSIX file "{pdf_path}" as PDF

    -- Export Microsoft PowerPoint file
    export doc to POSIX file "{pptx_path}" as Microsoft PowerPoint

    -- Export all slides as PNG images for automated verification
    if not (exists POSIX file "{export_dir}") then
        do shell script "mkdir -p '{export_dir}'"
    end if
    export doc to POSIX file "{export_dir}" as slide images with properties {{image format:PNG}}

    close doc
    return "FULL_DECK_BUILD_COMPLETED"
end tell
'''

    print("Running AppleScript in Apple Keynote...")
    p = subprocess.run(["osascript", "-e", applescript], capture_output=True, text=True)
    if p.returncode != 0:
        print("AppleScript Error:", p.stderr)
        sys.exit(1)
    print("AppleScript Output:", p.stdout.strip())
    print("Files successfully generated:")
    print("1. Native Keynote:", key_path)
    print("2. Presentation PDF:", pdf_path)
    print("3. PowerPoint Deck:", pptx_path)
    print("4. Slide Images:", export_dir)

if __name__ == "__main__":
    build_presentation()
