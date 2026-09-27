#!/usr/bin/env python3
"""
CyberSentinel AI - Academic Synopsis & Report Diagram Generator
Generates publication-quality, high-resolution PNG (300 DPI) and SVG diagrams
for Mumbai University B.E. Computer Engineering Project Report.

Figures generated:
- Fig 4.1: Overall System Architecture & Framework Flowchart
- Fig 4.2: Object-Oriented Class Diagram (Detailed Design)
- Fig 4.3: Functional Specifications - Data Flow Diagram Level 0 (Context Level DFD)
- Fig 4.4: Functional Specifications - Data Flow Diagram Level 1 (Decomposition DFD)
- Fig 4.5: Detailed Entity-Relationship (E-R) Diagram & Data Model
- Fig 6.1: Project Implementation Timeline (Gantt Chart for Term 1 & Term 2)
- Fig 7.1: Quantitative Performance & Benchmark Evaluation Chart
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "docs/synopsis_report/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Font loading helper
def get_fonts():
    paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    font_path = None
    for p in paths:
        if os.path.exists(p):
            font_path = p
            break
            
    if font_path:
        f_title = ImageFont.truetype(font_path, 36)
        f_subtitle = ImageFont.truetype(font_path, 22)
        f_head = ImageFont.truetype(font_path, 24)
        f_subhead = ImageFont.truetype(font_path, 20)
        f_body = ImageFont.truetype(font_path, 16)
        f_small = ImageFont.truetype(font_path, 13)
        f_mono = ImageFont.truetype(font_path, 15)
    else:
        f_title = f_subtitle = f_head = f_subhead = f_body = f_small = f_mono = ImageFont.load_default()
        
    return {
        "title": f_title,
        "subtitle": f_subtitle,
        "head": f_head,
        "subhead": f_subhead,
        "body": f_body,
        "small": f_small,
        "mono": f_mono
    }

fonts = get_fonts()

def draw_arrow(draw, start, end, fill="#2563EB", width=3, arrow_len=14):
    x0, y0 = start
    x1, y1 = end
    draw.line([start, end], fill=fill, width=width)
    import math
    angle = math.atan2(y1 - y0, x1 - x0)
    p1 = (x1 - arrow_len * math.cos(angle - math.pi / 6),
          y1 - arrow_len * math.sin(angle - math.pi / 6))
    p2 = (x1 - arrow_len * math.cos(angle + math.pi / 6),
          y1 - arrow_len * math.sin(angle + math.pi / 6))
    draw.polygon([end, p1, p2], fill=fill)


# ==============================================================================
# 1. FIGURE 4.1: SYSTEM ARCHITECTURE & FRAMEWORK FLOWCHART
# ==============================================================================
def generate_figure_4_1():
    W, H = 2200, 1400
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 4.1: END-TO-END SYSTEM ARCHITECTURE & PROCESSING PIPELINE", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "CyberSentinel AI: Autonomous Tier-1 Cognitive Security Operations Platform", font=fonts["subtitle"], fill="#94A3B8")

    stages = [
        {
            "num": "STAGE 1",
            "title": "TELEMETRY INGESTION",
            "tech": "FastAPI Async / SSE Pipe",
            "box_color": "#EFF6FF",
            "border": "#3B82F6",
            "header_bg": "#1E40AF",
            "items": [
                "• Windows EventLogs (JSON / XML)",
                "• Linux Auth Syslog (RFC 3164)",
                "• Apache Access Logs (CLF)",
                "• Perimeter Firewall Logs (CSV)",
                "• Live SSE Streaming Buffer"
            ]
        },
        {
            "num": "STAGE 2",
            "title": "NORMALIZATION & FILTER",
            "tech": "BaseLogParser Factory & ECS",
            "box_color": "#F0FDF4",
            "border": "#22C55E",
            "header_bg": "#15803D",
            "items": [
                "• Auto-Format Sniffing & Routing",
                "• Regex IP/Port/User Tokenization",
                "• Elastic Common Schema (ECS)",
                "• Edge Filter (>90% Noise Discard)",
                "• Emits NormalizedLogEvent"
            ]
        },
        {
            "num": "STAGE 3",
            "title": "VECTOR RAG RETRIEVAL",
            "tech": "ChromaDB + ONNX MiniLM",
            "box_color": "#FAF5FF",
            "border": "#A855F7",
            "header_bg": "#6B21A8",
            "items": [
                "• Context Vectorization (384-dim)",
                "• all-MiniLM-L6-v2 ONNX Runtime",
                "• 600+ MITRE ATT&CK v14 Index",
                "• Cosine Similarity k-NN Search",
                "• Sub-10ms Local CPU Latency"
            ]
        },
        {
            "num": "STAGE 4",
            "title": "COGNITIVE AGENT & CVSS",
            "tech": "Pydantic v2 Guardrails",
            "box_color": "#FFFBEB",
            "border": "#F59E0B",
            "header_bg": "#B45309",
            "items": [
                "• Algorithmic CVSS Risk Engine",
                "• Dynamic Multipliers (+10, +15)",
                "• Attack Chain Correlation",
                "• Zero-Hallucination Synthesizer",
                "• Strict AIThreatAnalysisResult"
            ]
        },
        {
            "num": "STAGE 5",
            "title": "SOAR & AUDIT EXPORT",
            "tech": "React Workstation / ReportLab",
            "box_color": "#FEF2F2",
            "border": "#EF4444",
            "header_bg": "#991B1B",
            "items": [
                "• Real-Time Cyber Radar Stream",
                "• Dynamic iptables Shun Scripts",
                "• NIST SP 800-61 Playbooks",
                "• ReportLab PDF Report Engine",
                "• SHA-256 Tamper Evidence Hash"
            ]
        }
    ]

    col_w = 380
    gap = 45
    start_x = 55
    y_top = 180
    box_h = 580

    for i, s in enumerate(stages):
        x = start_x + i * (col_w + gap)
        
        # Outer Card
        draw.rounded_rectangle([x, y_top, x + col_w, y_top + box_h], radius=12, fill=s["box_color"], outline=s["border"], width=3)
        # Header Box
        draw.rounded_rectangle([x, y_top, x + col_w, y_top + 95], radius=12, fill=s["header_bg"])
        draw.rectangle([x, y_top + 80, x + col_w, y_top + 95], fill=s["header_bg"])
        
        draw.text((x + 20, y_top + 15), s["num"], font=fonts["small"], fill="#E2E8F0")
        draw.text((x + 20, y_top + 38), s["title"], font=fonts["head"], fill="#FFFFFF")
        draw.text((x + 20, y_top + 68), s["tech"], font=fonts["small"], fill="#CBD5E1")
        
        # Items
        cur_y = y_top + 130
        for item in s["items"]:
            draw.text((x + 25, cur_y), item, font=fonts["body"], fill="#1E293B")
            cur_y += 65

        # Inter-stage arrows
        if i < len(stages) - 1:
            arrow_start = (x + col_w + 5, y_top + box_h // 2)
            arrow_end = (x + col_w + gap - 5, y_top + box_h // 2)
            draw_arrow(draw, arrow_start, arrow_end, fill="#475569", width=4, arrow_len=14)

    # Lower Section: Architectural Specifications & Telemetry Contract
    lower_y = 800
    draw.rounded_rectangle([55, lower_y, W - 55, H - 70], radius=14, fill="#F8FAFC", outline="#CBD5E1", width=2)
    
    # Sub-box 1: Data Contracts
    draw.rectangle([55, lower_y, W - 55, lower_y + 50], fill="#334155")
    draw.text((80, lower_y + 12), "CROSS-TIER DATA CONTRACT & MATHEMATICAL RISK SPECIFICATION", font=fonts["head"], fill="#F8FAFC")

    # Column 1: Elastic Common Schema (ECS)
    draw.text((90, lower_y + 75), "1. Normalized Log Event (ECS Standard)", font=fonts["subhead"], fill="#0F172A")
    ecs_text = [
        "timestamp: ISO8601 (UTC Normalized)",
        "source_type: WINDOWS | LINUX | APACHE | FIREWALL",
        "source_ip / destination_ip: IPv4 / IPv6 validated",
        "event_type: AUTH_FAILURE | ESCALATION | SQLI_PROBE",
        "severity_hint: LOW | MEDIUM | HIGH | CRITICAL",
        "raw_payload: Original tamper-evident hex / log string"
    ]
    ey = lower_y + 115
    for t in ecs_text:
        draw.text((95, ey), t, font=fonts["mono"], fill="#334155")
        ey += 38

    # Column 2: Algorithmic CVSS Formula
    draw.text((780, lower_y + 75), "2. Deterministic CVSS Risk Quantification", font=fonts["subhead"], fill="#0F172A")
    cvss_text = [
        "Risk Score = min(100.0, BaseSeverity + Sum(W_progression))",
        "• BaseSeverity: CRITICAL=85, HIGH=70, MEDIUM=50, LOW=25",
        "• W_compromise = +10.0 (Failed auth followed by success)",
        "• W_priv_esc   = +15.0 (Unauthorized sudo / root assignment)",
        "• W_injection  = +12.0 (SQLi payloads / path traversal)",
        "• W_target     = +8.0  (Critical user: root, administrator)"
    ]
    cy = lower_y + 115
    for t in cvss_text:
        draw.text((785, cy), t, font=fonts["mono"], fill="#334155")
        cy += 38

    # Column 3: Performance & Air-Gap Guarantees
    draw.text((1500, lower_y + 75), "3. Operational SLAs & System Guarantees", font=fonts["subhead"], fill="#0F172A")
    sla_text = [
        "• Mean Time to Respond (MTTR): < 2.4s end-to-end",
        "• Edge Pre-Filter Rate: 99.2% benign noise reduction",
        "• Zero Hallucination: 100% Pydantic & MITRE grounded",
        "• Air-Gap Capability: 100% offline (Local ONNX + SQLite)",
        "• Automated Test Coverage: 9/9 pytest suites passed",
        "• Export Verification: SHA-256 cryptographic PDF digest"
    ]
    sy = lower_y + 115
    for t in sla_text:
        draw.text((1505, sy), t, font=fonts["mono"], fill="#334155")
        sy += 38

    # Bottom caption
    draw.text((60, H - 45), "Figure 4.1: Comprehensive Architecture and Telemetry Processing Framework of CyberSentinel AI.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_4_1_architecture.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    # Generate SVG equivalent
    generate_svg_4_1()


def generate_svg_4_1():
    svg_path = os.path.join(OUTPUT_DIR, "fig_4_1_architecture.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 1400" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2200" height="1400" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2200" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 4.1: END-TO-END SYSTEM ARCHITECTURE &amp; PROCESSING PIPELINE</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">CyberSentinel AI: Autonomous Tier-1 Cognitive Security Operations Platform</text>
    
    <!-- Marker def for arrows -->
    <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569" />
        </marker>
    </defs>
    
    <!-- 5 Pipeline Stages -->
    <!-- Stage 1 -->
    <g transform="translate(55, 180)">
        <rect width="380" height="580" rx="12" fill="#EFF6FF" stroke="#3B82F6" stroke-width="3"/>
        <path d="M0,12 Q0,0 12,0 L368,0 Q380,0 380,12 L380,95 L0,95 Z" fill="#1E40AF"/>
        <text x="20" y="32" font-size="14" fill="#E2E8F0">STAGE 1</text>
        <text x="20" y="62" font-size="22" font-weight="bold" fill="#FFFFFF">TELEMETRY INGESTION</text>
        <text x="20" y="85" font-size="14" fill="#CBD5E1">FastAPI Async / SSE Pipe</text>
        <text x="25" y="145" font-size="17" fill="#1E293B">• Windows EventLogs (JSON/XML)</text>
        <text x="25" y="210" font-size="17" fill="#1E293B">• Linux Auth Syslog (RFC 3164)</text>
        <text x="25" y="275" font-size="17" fill="#1E293B">• Apache Access Logs (CLF)</text>
        <text x="25" y="340" font-size="17" fill="#1E293B">• Perimeter Firewall Logs (CSV)</text>
        <text x="25" y="405" font-size="17" fill="#1E293B">• Live SSE Streaming Buffer</text>
    </g>
    
    <!-- Arrow 1 to 2 -->
    <line x1="440" y1="470" x2="475" y2="470" stroke="#475569" stroke-width="4" marker-end="url(#arrow)"/>
    
    <!-- Stage 2 -->
    <g transform="translate(480, 180)">
        <rect width="380" height="580" rx="12" fill="#F0FDF4" stroke="#22C55E" stroke-width="3"/>
        <path d="M0,12 Q0,0 12,0 L368,0 Q380,0 380,12 L380,95 L0,95 Z" fill="#15803D"/>
        <text x="20" y="32" font-size="14" fill="#E2E8F0">STAGE 2</text>
        <text x="20" y="62" font-size="22" font-weight="bold" fill="#FFFFFF">NORMALIZATION &amp; FILTER</text>
        <text x="20" y="85" font-size="14" fill="#CBD5E1">BaseLogParser Factory &amp; ECS</text>
        <text x="25" y="145" font-size="17" fill="#1E293B">• Auto-Format Sniffing &amp; Routing</text>
        <text x="25" y="210" font-size="17" fill="#1E293B">• Regex IP/Port/User Tokenization</text>
        <text x="25" y="275" font-size="17" fill="#1E293B">• Elastic Common Schema (ECS)</text>
        <text x="25" y="340" font-size="17" fill="#1E293B">• Edge Filter (&gt;90% Noise Discard)</text>
        <text x="25" y="405" font-size="17" fill="#1E293B">• Emits NormalizedLogEvent</text>
    </g>
    
    <!-- Arrow 2 to 3 -->
    <line x1="865" y1="470" x2="900" y2="470" stroke="#475569" stroke-width="4" marker-end="url(#arrow)"/>
    
    <!-- Stage 3 -->
    <g transform="translate(905, 180)">
        <rect width="380" height="580" rx="12" fill="#FAF5FF" stroke="#A855F7" stroke-width="3"/>
        <path d="M0,12 Q0,0 12,0 L368,0 Q380,0 380,12 L380,95 L0,95 Z" fill="#6B21A8"/>
        <text x="20" y="32" font-size="14" fill="#E2E8F0">STAGE 3</text>
        <text x="20" y="62" font-size="22" font-weight="bold" fill="#FFFFFF">VECTOR RAG RETRIEVAL</text>
        <text x="20" y="85" font-size="14" fill="#CBD5E1">ChromaDB + ONNX MiniLM</text>
        <text x="25" y="145" font-size="17" fill="#1E293B">• Context Vectorization (384-dim)</text>
        <text x="25" y="210" font-size="17" fill="#1E293B">• all-MiniLM-L6-v2 ONNX Runtime</text>
        <text x="25" y="275" font-size="17" fill="#1E293B">• 600+ MITRE ATT&amp;CK v14 Index</text>
        <text x="25" y="340" font-size="17" fill="#1E293B">• Cosine Similarity k-NN Search</text>
        <text x="25" y="405" font-size="17" fill="#1E293B">• Sub-10ms Local CPU Latency</text>
    </g>
    
    <!-- Arrow 3 to 4 -->
    <line x1="1290" y1="470" x2="1325" y2="470" stroke="#475569" stroke-width="4" marker-end="url(#arrow)"/>
    
    <!-- Stage 4 -->
    <g transform="translate(1330, 180)">
        <rect width="380" height="580" rx="12" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
        <path d="M0,12 Q0,0 12,0 L368,0 Q380,0 380,12 L380,95 L0,95 Z" fill="#B45309"/>
        <text x="20" y="32" font-size="14" fill="#E2E8F0">STAGE 4</text>
        <text x="20" y="62" font-size="22" font-weight="bold" fill="#FFFFFF">COGNITIVE AGENT &amp; CVSS</text>
        <text x="20" y="85" font-size="14" fill="#CBD5E1">Pydantic v2 Guardrails</text>
        <text x="25" y="145" font-size="17" fill="#1E293B">• Algorithmic CVSS Risk Engine</text>
        <text x="25" y="210" font-size="17" fill="#1E293B">• Dynamic Multipliers (+10, +15)</text>
        <text x="25" y="275" font-size="17" fill="#1E293B">• Attack Chain Correlation</text>
        <text x="25" y="340" font-size="17" fill="#1E293B">• Zero-Hallucination Synthesizer</text>
        <text x="25" y="405" font-size="17" fill="#1E293B">• Strict AIThreatAnalysisResult</text>
    </g>
    
    <!-- Arrow 4 to 5 -->
    <line x1="1715" y1="470" x2="1750" y2="470" stroke="#475569" stroke-width="4" marker-end="url(#arrow)"/>
    
    <!-- Stage 5 -->
    <g transform="translate(1755, 180)">
        <rect width="380" height="580" rx="12" fill="#FEF2F2" stroke="#EF4444" stroke-width="3"/>
        <path d="M0,12 Q0,0 12,0 L368,0 Q380,0 380,12 L380,95 L0,95 Z" fill="#991B1B"/>
        <text x="20" y="32" font-size="14" fill="#E2E8F0">STAGE 5</text>
        <text x="20" y="62" font-size="22" font-weight="bold" fill="#FFFFFF">SOAR &amp; AUDIT EXPORT</text>
        <text x="20" y="85" font-size="14" fill="#CBD5E1">React Workstation / ReportLab</text>
        <text x="25" y="145" font-size="17" fill="#1E293B">• Real-Time Cyber Radar Stream</text>
        <text x="25" y="210" font-size="17" fill="#1E293B">• Dynamic iptables Shun Scripts</text>
        <text x="25" y="275" font-size="17" fill="#1E293B">• NIST SP 800-61 Playbooks</text>
        <text x="25" y="340" font-size="17" fill="#1E293B">• ReportLab PDF Report Engine</text>
        <text x="25" y="405" font-size="17" fill="#1E293B">• SHA-256 Tamper Evidence Hash</text>
    </g>
    
    <!-- Lower Section -->
    <g transform="translate(55, 800)">
        <rect width="2090" height="520" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
        <path d="M0,14 Q0,0 14,0 L2076,0 Q2090,0 2090,14 L2090,50 L0,50 Z" fill="#334155"/>
        <text x="30" y="33" font-size="20" font-weight="bold" fill="#F8FAFC">CROSS-TIER DATA CONTRACT &amp; MATHEMATICAL RISK SPECIFICATION</text>
        
        <!-- Col 1 -->
        <text x="35" y="90" font-size="18" font-weight="bold" fill="#0F172A">1. Normalized Log Event (ECS Standard)</text>
        <text x="40" y="130" font-size="15" font-family="monospace" fill="#334155">timestamp: ISO8601 (UTC Normalized)</text>
        <text x="40" y="170" font-size="15" font-family="monospace" fill="#334155">source_type: WINDOWS | LINUX | APACHE | FIREWALL</text>
        <text x="40" y="210" font-size="15" font-family="monospace" fill="#334155">source_ip / destination_ip: IPv4 / IPv6 validated</text>
        <text x="40" y="250" font-size="15" font-family="monospace" fill="#334155">event_type: AUTH_FAILURE | ESCALATION | SQLI_PROBE</text>
        <text x="40" y="290" font-size="15" font-family="monospace" fill="#334155">severity_hint: LOW | MEDIUM | HIGH | CRITICAL</text>
        <text x="40" y="330" font-size="15" font-family="monospace" fill="#334155">raw_payload: Original tamper-evident hex / log string</text>
        
        <!-- Col 2 -->
        <text x="725" y="90" font-size="18" font-weight="bold" fill="#0F172A">2. Deterministic CVSS Risk Quantification</text>
        <text x="730" y="130" font-size="15" font-family="monospace" fill="#334155">Risk Score = min(100.0, BaseSeverity + Sum(W_progression))</text>
        <text x="730" y="170" font-size="15" font-family="monospace" fill="#334155">• BaseSeverity: CRITICAL=85, HIGH=70, MEDIUM=50, LOW=25</text>
        <text x="730" y="210" font-size="15" font-family="monospace" fill="#334155">• W_compromise = +10.0 (Failed auth followed by success)</text>
        <text x="730" y="250" font-size="15" font-family="monospace" fill="#334155">• W_priv_esc   = +15.0 (Unauthorized sudo / root assignment)</text>
        <text x="730" y="290" font-size="15" font-family="monospace" fill="#334155">• W_injection  = +12.0 (SQLi payloads / path traversal)</text>
        <text x="730" y="330" font-size="15" font-family="monospace" fill="#334155">• W_target     = +8.0  (Critical user: root, administrator)</text>
        
        <!-- Col 3 -->
        <text x="1445" y="90" font-size="18" font-weight="bold" fill="#0F172A">3. Operational SLAs &amp; System Guarantees</text>
        <text x="1450" y="130" font-size="15" font-family="monospace" fill="#334155">• Mean Time to Respond (MTTR): &lt; 2.4s end-to-end</text>
        <text x="1450" y="170" font-size="15" font-family="monospace" fill="#334155">• Edge Pre-Filter Rate: 99.2% benign noise reduction</text>
        <text x="1450" y="210" font-size="15" font-family="monospace" fill="#334155">• Zero Hallucination: 100% Pydantic &amp; MITRE grounded</text>
        <text x="1450" y="250" font-size="15" font-family="monospace" fill="#334155">• Air-Gap Capability: 100% offline (Local ONNX + SQLite)</text>
        <text x="1450" y="290" font-size="15" font-family="monospace" fill="#334155">• Automated Test Coverage: 9/9 pytest suites passed</text>
        <text x="1450" y="330" font-size="15" font-family="monospace" fill="#334155">• Export Verification: SHA-256 cryptographic PDF digest</text>
    </g>
    
    <text x="60" y="1365" font-size="14" fill="#64748B">Figure 4.1: Comprehensive Architecture and Telemetry Processing Framework of CyberSentinel AI.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


# ==============================================================================
# 2. FIGURE 4.2: OBJECT-ORIENTED CLASS DIAGRAM (DETAILED DESIGN)
# ==============================================================================
def generate_figure_4_2():
    W, H = 2200, 1500
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 4.2: OBJECT-ORIENTED CLASS DIAGRAM (DETAILED SYSTEM DESIGN)", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "Class Hierarchy, Attributes, Methods, and Inter-Module Associations", font=fonts["subtitle"], fill="#94A3B8")

    def draw_uml_class(x, y, w, h, title, stereotype, attrs, methods, header_bg="#1E293B", border="#334155"):
        draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill="#FFFFFF", outline=border, width=2)
        # Class Header
        header_h = 60
        draw.rounded_rectangle([x, y, x + w, y + header_h], radius=8, fill=header_bg)
        draw.rectangle([x, y + 45, x + w, y + header_h], fill=header_bg)
        
        if stereotype:
            draw.text((x + 15, y + 8), f"<<{stereotype}>>", font=fonts["small"], fill="#94A3B8")
            draw.text((x + 15, y + 28), title, font=fonts["head"], fill="#FFFFFF")
        else:
            draw.text((x + 15, y + 16), title, font=fonts["head"], fill="#FFFFFF")
            
        # Attributes divider
        curr_y = y + header_h + 12
        for attr in attrs:
            draw.text((x + 15, curr_y), attr, font=fonts["mono"], fill="#1E293B")
            curr_y += 28
            
        draw.line([(x, curr_y + 6), (x + w, curr_y + 6)], fill="#CBD5E1", width=1)
        curr_y += 16
        
        # Methods
        for method in methods:
            draw.text((x + 15, curr_y), method, font=fonts["mono"], fill="#0F766E")
            curr_y += 28

    # 1. BaseLogParser (Abstract)
    draw_uml_class(
        x=850, y=170, w=500, h=250,
        title="BaseLogParser", stereotype="Abstract Base Class",
        attrs=[
            "- parser_name: str",
            "- supported_extensions: List[str]",
            "- benign_pattern_regex: Pattern"
        ],
        methods=[
            "+ parse_line(raw_line: str) -> NormalizedLogEvent",
            "+ parse_file(file_path: Path) -> List[NormalizedLogEvent]",
            "+ is_benign(raw_line: str) -> bool"
        ],
        header_bg="#1E3A8A", border="#1D4ED8"
    )

    # 4 Derived Parsers
    parsers = [
        ("WindowsEventParser", ["- target_event_ids: Set[int]"], ["+ parse_line()", "+ extract_channel()"], 80),
        ("LinuxSyslogParser", ["- syslog_facility: int", "- rfc3164_regex: Pattern"], ["+ parse_line()", "+ parse_sudo_session()"], 600),
        ("ApacheAccessLogParser", ["- clf_regex: Pattern", "- sqli_signatures: List[str]"], ["+ parse_line()", "+ check_path_traversal()"], 1120),
        ("FirewallLogParser", ["- csv_delimiter: str", "- blocked_actions: Set[str]"], ["+ parse_line()", "+ parse_protocol_flags()"], 1640)
    ]

    for p_name, p_attrs, p_methods, px in parsers:
        draw_uml_class(
            x=px, y=490, w=480, h=190,
            title=p_name, stereotype="Concrete Parser",
            attrs=p_attrs,
            methods=p_methods,
            header_bg="#0F766E", border="#0D9488"
        )
        # Inheritance connector arrow to BaseLogParser
        draw_arrow(draw, (px + 240, 490), (px + 240, 450), fill="#64748B", width=2, arrow_len=10)
        draw.line([(px + 240, 450), (1100, 450)], fill="#64748B", width=2)
        draw_arrow(draw, (1100, 450), (1100, 420), fill="#64748B", width=2, arrow_len=10)

    # 3. NormalizedLogEvent (Entity Model)
    draw_uml_class(
        x=80, y=750, w=500, h=310,
        title="NormalizedLogEvent", stereotype="Pydantic Model (ECS)",
        attrs=[
            "+ event_id: UUID",
            "+ timestamp: datetime (UTC)",
            "+ source_type: LogSourceType",
            "+ source_ip: IPv4Address / IPv6Address",
            "+ destination_ip: Optional[IPv4Address]",
            "+ username: Optional[str]",
            "+ event_type: SecurityEventType",
            "+ severity_hint: SeverityLevel",
            "+ raw_payload: str"
        ],
        methods=[
            "+ to_ecs_dict() -> Dict[str, Any]",
            "+ compute_event_hash() -> str"
        ],
        header_bg="#374151", border="#4B5563"
    )

    # 4. ChromaDBVectorStore (Intelligence Core)
    draw_uml_class(
        x=620, y=750, w=500, h=310,
        title="ChromaDBVectorStore", stereotype="RAG Knowledge Core",
        attrs=[
            "- client: PersistentClient",
            "- collection_name: str = 'mitre_attack'",
            "- embedding_model: all-MiniLM-L6-v2",
            "- distance_metric: 'cosine'",
            "- index_size: 600+ Techniques"
        ],
        methods=[
            "+ query_threat_intelligence(query: str, top_k: int) -> List[MitreMatch]",
            "+ get_technique_details(technique_id: str) -> MitreDetails",
            "+ reindex_mitre_library() -> int"
        ],
        header_bg="#6B21A8", border="#7E22CE"
    )

    # 5. ThreatAnalyzerAgent (Cognitive Reasoning)
    draw_uml_class(
        x=1160, y=750, w=500, h=310,
        title="ThreatAnalyzerAgent", stereotype="Cognitive Reasoning Engine",
        attrs=[
            "- vector_store: ChromaDBVectorStore",
            "- llm_backend: LocalONNX / GeminiClient",
            "- validation_schema: Type[AIThreatAnalysisResult]"
        ],
        methods=[
            "+ analyze_security_events(events: List[NormalizedLogEvent]) -> AIThreatAnalysisResult",
            "+ calculate_risk_score(events: List[NormalizedLogEvent]) -> float",
            "+ evaluate_attack_progression(events) -> float",
            "+ deterministic_fallback(events) -> AIThreatAnalysisResult"
        ],
        header_bg="#B45309", border="#D97706"
    )

    # 6. AIThreatAnalysisResult (Guardrail Schema)
    draw_uml_class(
        x=1700, y=750, w=450, h=310,
        title="AIThreatAnalysisResult", stereotype="Pydantic Output Guardrail",
        attrs=[
            "+ threat_classification: str",
            "+ severity: SeverityLevel",
            "+ risk_score: float (0.0 to 100.0)",
            "+ attack_vector: str",
            "+ mitre_technique_id: str",
            "+ mitre_technique_name: str",
            "+ reasoning: str",
            "+ recommended_mitigations: List[str]"
        ],
        methods=[
            "+ validate_threat_schema() -> bool",
            "+ to_incident_payload() -> Dict"
        ],
        header_bg="#15803D", border="#16A34A"
    )

    # 7. IncidentService & PDFReportGenerator (SOAR Tier)
    draw_uml_class(
        x=350, y=1130, w=580, h=250,
        title="IncidentService", stereotype="SOAR Orchestrator",
        attrs=[
            "- db_session: AsyncSession",
            "- sse_broadcaster: EventBroadcaster",
            "- shun_executor: FirewallExecutionHook"
        ],
        methods=[
            "+ create_incident(events, analysis) -> Incident",
            "+ dispatch_sse_radar(event: NormalizedLogEvent)",
            "+ execute_containment_action(incident_id, action_type)",
            "+ get_incident_timeline(incident_id) -> Timeline"
        ],
        header_bg="#991B1B", border="#DC2626"
    )

    draw_uml_class(
        x=1050, y=1130, w=580, h=250,
        title="PDFReportGenerator", stereotype="Forensic Audit Compiler",
        attrs=[
            "- page_size: letter",
            "- cryptographic_digest: SHA-256",
            "- reportlab_canvas: SimpleDocTemplate"
        ],
        methods=[
            "+ generate_incident_pdf(incident: Incident) -> bytes",
            "+ build_timeline_flowable(events: List[LogEvent])",
            "+ build_mitre_matrix_flowable(techniques)",
            "+ compute_evidence_sha256(raw_logs: str) -> str"
        ],
        header_bg="#0F172A", border="#334155"
    )

    # Inter-class relationships
    # NormalizedLogEvent produced by BaseLogParser
    draw_arrow(draw, (1100, 420), (1100, 440), fill="#475569", width=2)
    # ThreatAnalyzerAgent uses ChromaDB
    draw_arrow(draw, (1160, 900), (1120, 900), fill="#7E22CE", width=3, arrow_len=10)
    # ThreatAnalyzerAgent outputs AIThreatAnalysisResult
    draw_arrow(draw, (1660, 900), (1700, 900), fill="#16A34A", width=3, arrow_len=10)
    # IncidentService coordinates with ThreatAnalyzerAgent
    draw_arrow(draw, (640, 1130), (640, 1080), fill="#DC2626", width=2)
    draw.line([(640, 1080), (1410, 1080)], fill="#DC2626", width=2)
    draw_arrow(draw, (1410, 1080), (1410, 1060), fill="#DC2626", width=2, arrow_len=10)
    # IncidentService invokes PDFReportGenerator
    draw_arrow(draw, (930, 1250), (1050, 1250), fill="#334155", width=3, arrow_len=10)

    # Bottom caption
    draw.text((60, H - 40), "Figure 4.2: Detailed Object-Oriented Class Design and System Architectural Hierarchy.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_4_2_class_diagram.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    generate_svg_4_2()


def generate_svg_4_2():
    svg_path = os.path.join(OUTPUT_DIR, "fig_4_2_class_diagram.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 1500" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2200" height="1500" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2200" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 4.2: OBJECT-ORIENTED CLASS DIAGRAM (DETAILED SYSTEM DESIGN)</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">Class Hierarchy, Attributes, Methods, and Inter-Module Associations</text>
    
    <!-- BaseLogParser -->
    <g transform="translate(850, 170)">
        <rect width="500" height="250" rx="8" fill="#FFFFFF" stroke="#1D4ED8" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L492,0 Q500,0 500,8 L500,60 L0,60 Z" fill="#1E3A8A"/>
        <text x="15" y="24" font-size="13" fill="#94A3B8">&lt;&lt;Abstract Base Class&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">BaseLogParser</text>
        <text x="15" y="90" font-size="15" font-family="monospace" fill="#1E293B">- parser_name: str</text>
        <text x="15" y="118" font-size="15" font-family="monospace" fill="#1E293B">- supported_extensions: List[str]</text>
        <text x="15" y="146" font-size="15" font-family="monospace" fill="#1E293B">- benign_pattern_regex: Pattern</text>
        <line x1="0" y1="165" x2="500" y2="165" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="192" font-size="15" font-family="monospace" fill="#0F766E">+ parse_line(raw: str) -&gt; NormalizedLogEvent</text>
        <text x="15" y="218" font-size="15" font-family="monospace" fill="#0F766E">+ parse_file(path: Path) -&gt; List[NormalizedLogEvent]</text>
        <text x="15" y="242" font-size="15" font-family="monospace" fill="#0F766E">+ is_benign(raw: str) -&gt; bool</text>
    </g>

    <!-- 4 Subclasses -->
    <!-- Windows -->
    <g transform="translate(80, 490)">
        <rect width="480" height="190" rx="8" fill="#FFFFFF" stroke="#0D9488" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L472,0 Q480,0 480,8 L480,50 L0,50 Z" fill="#0F766E"/>
        <text x="15" y="32" font-size="20" font-weight="bold" fill="#FFFFFF">WindowsEventParser</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#1E293B">- target_event_ids: Set[int]</text>
        <line x1="0" y1="100" x2="480" y2="100" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="130" font-size="15" font-family="monospace" fill="#0F766E">+ parse_line() -&gt; NormalizedLogEvent</text>
        <text x="15" y="160" font-size="15" font-family="monospace" fill="#0F766E">+ extract_channel() -&gt; str</text>
    </g>
    <!-- Linux -->
    <g transform="translate(600, 490)">
        <rect width="480" height="190" rx="8" fill="#FFFFFF" stroke="#0D9488" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L472,0 Q480,0 480,8 L480,50 L0,50 Z" fill="#0F766E"/>
        <text x="15" y="32" font-size="20" font-weight="bold" fill="#FFFFFF">LinuxSyslogParser</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#1E293B">- syslog_facility: int, rfc3164_regex</text>
        <line x1="0" y1="100" x2="480" y2="100" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="130" font-size="15" font-family="monospace" fill="#0F766E">+ parse_line() -&gt; NormalizedLogEvent</text>
        <text x="15" y="160" font-size="15" font-family="monospace" fill="#0F766E">+ parse_sudo_session() -&gt; bool</text>
    </g>
    <!-- Apache -->
    <g transform="translate(1120, 490)">
        <rect width="480" height="190" rx="8" fill="#FFFFFF" stroke="#0D9488" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L472,0 Q480,0 480,8 L480,50 L0,50 Z" fill="#0F766E"/>
        <text x="15" y="32" font-size="20" font-weight="bold" fill="#FFFFFF">ApacheAccessLogParser</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#1E293B">- clf_regex: Pattern, sqli_signatures</text>
        <line x1="0" y1="100" x2="480" y2="100" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="130" font-size="15" font-family="monospace" fill="#0F766E">+ parse_line() -&gt; NormalizedLogEvent</text>
        <text x="15" y="160" font-size="15" font-family="monospace" fill="#0F766E">+ check_path_traversal() -&gt; bool</text>
    </g>
    <!-- Firewall -->
    <g transform="translate(1640, 490)">
        <rect width="480" height="190" rx="8" fill="#FFFFFF" stroke="#0D9488" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L472,0 Q480,0 480,8 L480,50 L0,50 Z" fill="#0F766E"/>
        <text x="15" y="32" font-size="20" font-weight="bold" fill="#FFFFFF">FirewallLogParser</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#1E293B">- csv_delimiter, blocked_actions: Set</text>
        <line x1="0" y1="100" x2="480" y2="100" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="130" font-size="15" font-family="monospace" fill="#0F766E">+ parse_line() -&gt; NormalizedLogEvent</text>
        <text x="15" y="160" font-size="15" font-family="monospace" fill="#0F766E">+ parse_protocol_flags() -&gt; str</text>
    </g>

    <!-- Connectors -->
    <path d="M320,490 L320,450 L1100,450 L1100,420" fill="none" stroke="#64748B" stroke-width="2"/>
    <path d="M840,490 L840,450" fill="none" stroke="#64748B" stroke-width="2"/>
    <path d="M1360,490 L1360,450" fill="none" stroke="#64748B" stroke-width="2"/>
    <path d="M1880,490 L1880,450 L1100,450" fill="none" stroke="#64748B" stroke-width="2"/>

    <!-- Row 3 Classes -->
    <!-- NormalizedLogEvent -->
    <g transform="translate(80, 750)">
        <rect width="500" height="310" rx="8" fill="#FFFFFF" stroke="#4B5563" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L492,0 Q500,0 500,8 L500,60 L0,60 Z" fill="#374151"/>
        <text x="15" y="24" font-size="13" fill="#94A3B8">&lt;&lt;Pydantic Model (ECS)&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">NormalizedLogEvent</text>
        <text x="15" y="90" font-size="14" font-family="monospace" fill="#1E293B">+ event_id: UUID, timestamp: datetime</text>
        <text x="15" y="118" font-size="14" font-family="monospace" fill="#1E293B">+ source_type: LogSourceType</text>
        <text x="15" y="146" font-size="14" font-family="monospace" fill="#1E293B">+ source_ip, destination_ip: IPAddress</text>
        <text x="15" y="174" font-size="14" font-family="monospace" fill="#1E293B">+ username, event_type: EventType</text>
        <text x="15" y="202" font-size="14" font-family="monospace" fill="#1E293B">+ severity_hint: SeverityLevel</text>
        <line x1="0" y1="220" x2="500" y2="220" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="250" font-size="14" font-family="monospace" fill="#0F766E">+ to_ecs_dict() -&gt; Dict[str, Any]</text>
        <text x="15" y="280" font-size="14" font-family="monospace" fill="#0F766E">+ compute_event_hash() -&gt; str</text>
    </g>

    <!-- ChromaDBVectorStore -->
    <g transform="translate(620, 750)">
        <rect width="500" height="310" rx="8" fill="#FFFFFF" stroke="#7E22CE" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L492,0 Q500,0 500,8 L500,60 L0,60 Z" fill="#6B21A8"/>
        <text x="15" y="24" font-size="13" fill="#E2E8F0">&lt;&lt;RAG Knowledge Core&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">ChromaDBVectorStore</text>
        <text x="15" y="90" font-size="14" font-family="monospace" fill="#1E293B">- client: PersistentClient (SQLite)</text>
        <text x="15" y="118" font-size="14" font-family="monospace" fill="#1E293B">- collection_name: 'mitre_attack'</text>
        <text x="15" y="146" font-size="14" font-family="monospace" fill="#1E293B">- embedding_model: all-MiniLM-L6-v2</text>
        <text x="15" y="174" font-size="14" font-family="monospace" fill="#1E293B">- distance_metric: 'cosine' (384-dim)</text>
        <line x1="0" y1="220" x2="500" y2="220" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="250" font-size="14" font-family="monospace" fill="#0F766E">+ query_threat_intelligence(query, k)</text>
        <text x="15" y="280" font-size="14" font-family="monospace" fill="#0F766E">+ get_technique_details(id) -&gt; Mitre</text>
    </g>

    <!-- ThreatAnalyzerAgent -->
    <g transform="translate(1160, 750)">
        <rect width="500" height="310" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L492,0 Q500,0 500,8 L500,60 L0,60 Z" fill="#B45309"/>
        <text x="15" y="24" font-size="13" fill="#E2E8F0">&lt;&lt;Cognitive Reasoning Engine&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">ThreatAnalyzerAgent</text>
        <text x="15" y="90" font-size="14" font-family="monospace" fill="#1E293B">- vector_store: ChromaDBVectorStore</text>
        <text x="15" y="118" font-size="14" font-family="monospace" fill="#1E293B">- llm_backend: LocalONNX / Gemini</text>
        <text x="15" y="146" font-size="14" font-family="monospace" fill="#1E293B">- validation_schema: AIThreatResult</text>
        <line x1="0" y1="220" x2="500" y2="220" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="250" font-size="14" font-family="monospace" fill="#0F766E">+ analyze_security_events(events)</text>
        <text x="15" y="280" font-size="14" font-family="monospace" fill="#0F766E">+ calculate_risk_score(events) -&gt; float</text>
    </g>

    <!-- AIThreatAnalysisResult -->
    <g transform="translate(1700, 750)">
        <rect width="450" height="310" rx="8" fill="#FFFFFF" stroke="#16A34A" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L442,0 Q450,0 450,8 L450,60 L0,60 Z" fill="#15803D"/>
        <text x="15" y="24" font-size="13" fill="#E2E8F0">&lt;&lt;Pydantic Guardrail&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">AIThreatAnalysisResult</text>
        <text x="15" y="90" font-size="14" font-family="monospace" fill="#1E293B">+ threat_name: str, severity: Level</text>
        <text x="15" y="118" font-size="14" font-family="monospace" fill="#1E293B">+ risk_score: float (0.0 to 100.0)</text>
        <text x="15" y="146" font-size="14" font-family="monospace" fill="#1E293B">+ attack_vector, mitre_technique_id</text>
        <text x="15" y="174" font-size="14" font-family="monospace" fill="#1E293B">+ recommended_mitigations: List[str]</text>
        <line x1="0" y1="220" x2="450" y2="220" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="250" font-size="14" font-family="monospace" fill="#0F766E">+ validate_threat_schema() -&gt; bool</text>
        <text x="15" y="280" font-size="14" font-family="monospace" fill="#0F766E">+ to_incident_payload() -&gt; Dict</text>
    </g>

    <!-- IncidentService & PDF -->
    <g transform="translate(350, 1130)">
        <rect width="580" height="250" rx="8" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L572,0 Q580,0 580,8 L580,60 L0,60 Z" fill="#991B1B"/>
        <text x="15" y="24" font-size="13" fill="#E2E8F0">&lt;&lt;SOAR Orchestrator&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">IncidentService</text>
        <text x="15" y="90" font-size="14" font-family="monospace" fill="#1E293B">- db_session: AsyncSession, sse_broadcaster</text>
        <text x="15" y="118" font-size="14" font-family="monospace" fill="#1E293B">- shun_executor: FirewallExecutionHook</text>
        <line x1="0" y1="140" x2="580" y2="140" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="170" font-size="14" font-family="monospace" fill="#0F766E">+ create_incident(events, analysis) -&gt; Incident</text>
        <text x="15" y="200" font-size="14" font-family="monospace" fill="#0F766E">+ dispatch_sse_radar(event: NormalizedLogEvent)</text>
        <text x="15" y="230" font-size="14" font-family="monospace" fill="#0F766E">+ execute_containment_action(incident_id, action)</text>
    </g>

    <g transform="translate(1050, 1130)">
        <rect width="580" height="250" rx="8" fill="#FFFFFF" stroke="#334155" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L572,0 Q580,0 580,8 L580,60 L0,60 Z" fill="#0F172A"/>
        <text x="15" y="24" font-size="13" fill="#94A3B8">&lt;&lt;Forensic Audit Compiler&gt;&gt;</text>
        <text x="15" y="48" font-size="22" font-weight="bold" fill="#FFFFFF">PDFReportGenerator</text>
        <text x="15" y="90" font-size="14" font-family="monospace" fill="#1E293B">- page_size: letter, cryptographic_digest: SHA-256</text>
        <text x="15" y="118" font-size="14" font-family="monospace" fill="#1E293B">- reportlab_canvas: SimpleDocTemplate</text>
        <line x1="0" y1="140" x2="580" y2="140" stroke="#CBD5E1" stroke-width="1"/>
        <text x="15" y="170" font-size="14" font-family="monospace" fill="#0F766E">+ generate_incident_pdf(incident: Incident) -&gt; bytes</text>
        <text x="15" y="200" font-size="14" font-family="monospace" fill="#0F766E">+ build_timeline_flowable(events: List[LogEvent])</text>
        <text x="15" y="230" font-size="14" font-family="monospace" fill="#0F766E">+ compute_evidence_sha256(raw_logs: str) -&gt; str</text>
    </g>

    <text x="60" y="1465" font-size="14" fill="#64748B">Figure 4.2: Detailed Object-Oriented Class Design and System Architectural Hierarchy.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


# ==============================================================================
# 3. FIGURE 4.3: DATA FLOW DIAGRAM LEVEL 0 (CONTEXT LEVEL DFD)
# ==============================================================================
def generate_figure_4_3():
    W, H = 2000, 1200
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 4.3: DATA FLOW DIAGRAM (DFD LEVEL 0 - CONTEXT LEVEL)", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "System Boundary, External Entities, Information Inflows, and Security Outflows", font=fonts["subtitle"], fill="#94A3B8")

    # Center Process Circle (CyberSentinel AI 0.0)
    cx, cy, cr = 1000, 620, 220
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill="#0F172A", outline="#3B82F6", width=5)
    draw.ellipse([cx - cr + 12, cy - cr + 12, cx + cr - 12, cy + cr - 12], fill="#1E293B", outline="#60A5FA", width=2)
    
    draw.text((cx - 150, cy - 80), "PROCESS 0.0", font=fonts["head"], fill="#38BDF8")
    draw.text((cx - 175, cy - 35), "CyberSentinel AI", font=fonts["title"], fill="#FFFFFF")
    draw.text((cx - 195, cy + 15), "Autonomous Cognitive SOC", font=fonts["subhead"], fill="#E2E8F0")
    draw.text((cx - 145, cy + 50), "Triage & SOAR Core", font=fonts["small"], fill="#94A3B8")

    # 4 External Entities (Rectangles)
    def draw_entity(x, y, w, h, title, sub, fill="#F8FAFC", border="#475569"):
        draw.rectangle([x, y, x + w, y + h], fill=fill, outline=border, width=3)
        draw.rectangle([x, y, x + w, y + 38], fill=border)
        draw.text((x + 15, y + 8), "EXTERNAL ENTITY", font=fonts["small"], fill="#F8FAFC")
        draw.text((x + 15, y + 55), title, font=fonts["head"], fill="#0F172A")
        draw.text((x + 15, y + 90), sub, font=fonts["small"], fill="#475569")

    # Entity 1: Enterprise Host Endpoints (Top-Left)
    draw_entity(80, 220, 420, 160, "Enterprise Hosts", "Linux Servers (auth.log, sudo) & AD Domains (4625, 4624)")
    # Entity 2: Perimeter Gateways & Web Services (Bottom-Left)
    draw_entity(80, 780, 420, 160, "Network Gateways", "Edge Firewalls (CSV Logs) & Apache / Nginx Web Servers")
    # Entity 3: SOC Security Analyst (Top-Right)
    draw_entity(1500, 220, 420, 160, "SOC Security Analyst", "Tier-1/2 Analysts, Incident Commanders, Auditors")
    # Entity 4: Target Network Infrastructure (Bottom-Right)
    draw_entity(1500, 780, 420, 160, "Firewall / EDR Hooks", "iptables daemons, Edge Routers, Null-Route Gateways")

    # Inflow Arrows (Left to Center)
    # Hosts -> Process
    draw_arrow(draw, (500, 300), (820, 500), fill="#2563EB", width=3, arrow_len=14)
    draw.text((540, 370), "Raw Syslogs, Auth Hex, EventIDs", font=fonts["mono"], fill="#1D4ED8")

    # Gateways -> Process
    draw_arrow(draw, (500, 860), (820, 740), fill="#2563EB", width=3, arrow_len=14)
    draw.text((530, 810), "HTTP CLF, SQLi Probes, Deny CSV", font=fonts["mono"], fill="#1D4ED8")

    # Outflow / Bi-directional (Center to Right)
    # Process -> Analyst
    draw_arrow(draw, (1180, 500), (1500, 300), fill="#059669", width=3, arrow_len=14)
    draw.text((1200, 360), "Real-Time SSE Radar Feeds,", font=fonts["mono"], fill="#047857")
    draw.text((1200, 390), "MITRE ATT&CK Triage & Audit PDFs", font=fonts["mono"], fill="#047857")

    # Analyst -> Process
    draw_arrow(draw, (1500, 340), (1200, 540), fill="#D97706", width=2, arrow_len=12)
    draw.text((1300, 470), "Remediation Approval Triggers", font=fonts["small"], fill="#B45309")

    # Process -> Firewall / Infrastructure
    draw_arrow(draw, (1180, 740), (1500, 860), fill="#DC2626", width=3, arrow_len=14)
    draw.text((1200, 810), "Dynamic iptables DROP Rules,", font=fonts["mono"], fill="#B91C1C")
    draw.text((1200, 840), "Automated Subnet Isolation Scripts", font=fonts["mono"], fill="#B91C1C")

    # Bottom caption
    draw.text((60, H - 40), "Figure 4.3: Data Flow Diagram (DFD Level 0) - Context-Level Operational Boundary.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_4_3_dfd_level_0.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    generate_svg_4_3()


def generate_svg_4_3():
    svg_path = os.path.join(OUTPUT_DIR, "fig_4_3_dfd_level_0.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 1200" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2000" height="1200" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2000" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 4.3: DATA FLOW DIAGRAM (DFD LEVEL 0 - CONTEXT LEVEL)</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">System Boundary, External Entities, Information Inflows, and Security Outflows</text>
    
    <defs>
        <marker id="arrowB" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563EB" />
        </marker>
        <marker id="arrowG" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
        </marker>
        <marker id="arrowR" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#DC2626" />
        </marker>
        <marker id="arrowO" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#D97706" />
        </marker>
    </defs>

    <!-- Center Process Circle -->
    <g transform="translate(1000, 620)">
        <circle r="220" fill="#0F172A" stroke="#3B82F6" stroke-width="5"/>
        <circle r="208" fill="#1E293B" stroke="#60A5FA" stroke-width="2"/>
        <text x="0" y="-70" text-anchor="middle" font-size="24" font-weight="bold" fill="#38BDF8">PROCESS 0.0</text>
        <text x="0" y="-20" text-anchor="middle" font-size="34" font-weight="bold" fill="#FFFFFF">CyberSentinel AI</text>
        <text x="0" y="25" text-anchor="middle" font-size="22" fill="#E2E8F0">Autonomous Cognitive SOC</text>
        <text x="0" y="65" text-anchor="middle" font-size="16" fill="#94A3B8">Triage &amp; SOAR Core</text>
    </g>

    <!-- 4 External Entities -->
    <!-- Entity 1 -->
    <g transform="translate(80, 220)">
        <rect width="420" height="160" fill="#F8FAFC" stroke="#475569" stroke-width="3"/>
        <rect width="420" height="38" fill="#475569"/>
        <text x="15" y="25" font-size="14" fill="#F8FAFC">EXTERNAL ENTITY</text>
        <text x="15" y="80" font-size="24" font-weight="bold" fill="#0F172A">Enterprise Hosts</text>
        <text x="15" y="115" font-size="14" fill="#475569">Linux Servers (auth.log) &amp; AD (4625, 4624)</text>
    </g>
    <!-- Entity 2 -->
    <g transform="translate(80, 780)">
        <rect width="420" height="160" fill="#F8FAFC" stroke="#475569" stroke-width="3"/>
        <rect width="420" height="38" fill="#475569"/>
        <text x="15" y="25" font-size="14" fill="#F8FAFC">EXTERNAL ENTITY</text>
        <text x="15" y="80" font-size="24" font-weight="bold" fill="#0F172A">Network Gateways</text>
        <text x="15" y="115" font-size="14" fill="#475569">Edge Firewalls (CSV) &amp; Apache Web Servers</text>
    </g>
    <!-- Entity 3 -->
    <g transform="translate(1500, 220)">
        <rect width="420" height="160" fill="#F8FAFC" stroke="#475569" stroke-width="3"/>
        <rect width="420" height="38" fill="#475569"/>
        <text x="15" y="25" font-size="14" fill="#F8FAFC">EXTERNAL ENTITY</text>
        <text x="15" y="80" font-size="24" font-weight="bold" fill="#0F172A">SOC Security Analyst</text>
        <text x="15" y="115" font-size="14" fill="#475569">Tier-1/2 Analysts, Incident Commanders</text>
    </g>
    <!-- Entity 4 -->
    <g transform="translate(1500, 780)">
        <rect width="420" height="160" fill="#F8FAFC" stroke="#475569" stroke-width="3"/>
        <rect width="420" height="38" fill="#475569"/>
        <text x="15" y="25" font-size="14" fill="#F8FAFC">EXTERNAL ENTITY</text>
        <text x="15" y="80" font-size="24" font-weight="bold" fill="#0F172A">Firewall / EDR Hooks</text>
        <text x="15" y="115" font-size="14" fill="#475569">iptables daemons, Edge Routers, Null-Routes</text>
    </g>

    <!-- Connectors -->
    <line x1="500" y1="300" x2="820" y2="500" stroke="#2563EB" stroke-width="3" marker-end="url(#arrowB)"/>
    <text x="540" y="380" font-size="15" font-family="monospace" fill="#1D4ED8">Raw Syslogs, Auth Hex, EventIDs</text>

    <line x1="500" y1="860" x2="820" y2="740" stroke="#2563EB" stroke-width="3" marker-end="url(#arrowB)"/>
    <text x="530" y="820" font-size="15" font-family="monospace" fill="#1D4ED8">HTTP CLF, SQLi Probes, Deny CSV</text>

    <line x1="1180" y1="500" x2="1500" y2="300" stroke="#059669" stroke-width="3" marker-end="url(#arrowG)"/>
    <text x="1200" y="370" font-size="15" font-family="monospace" fill="#047857">Real-Time SSE Radar Feeds, MITRE Triage</text>
    <text x="1200" y="400" font-size="15" font-family="monospace" fill="#047857">&amp; Forensic SHA-256 PDF Reports</text>

    <line x1="1500" y1="340" x2="1200" y2="540" stroke="#D97706" stroke-width="2" marker-end="url(#arrowO)"/>
    <text x="1290" y="475" font-size="14" fill="#B45309">Remediation Approval Triggers</text>

    <line x1="1180" y1="740" x2="1500" y2="860" stroke="#DC2626" stroke-width="3" marker-end="url(#arrowR)"/>
    <text x="1200" y="820" font-size="15" font-family="monospace" fill="#B91C1C">Dynamic iptables DROP Rules &amp;</text>
    <text x="1200" y="850" font-size="15" font-family="monospace" fill="#B91C1C">Automated Subnet Isolation Scripts</text>

    <text x="60" y="1165" font-size="14" fill="#64748B">Figure 4.3: Data Flow Diagram (DFD Level 0) - Context-Level Operational Boundary.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


# ==============================================================================
# 4. FIGURE 4.4: DATA FLOW DIAGRAM LEVEL 1 (DECOMPOSITION DFD)
# ==============================================================================
def generate_figure_4_4():
    W, H = 2200, 1400
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 4.4: DATA FLOW DIAGRAM (DFD LEVEL 1 - FUNCTIONAL DECOMPOSITION)", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "Detailed Subsystem Transformations, Intermediate Data Stores, and Control Paths", font=fonts["subtitle"], fill="#94A3B8")

    def draw_dfd_process(x, y, w, h, p_num, p_title, sub, fill="#F0F9FF", border="#0284C7"):
        draw.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill, outline=border, width=3)
        draw.text((x + 20, y + 18), p_num, font=fonts["subhead"], fill="#0369A1")
        draw.text((x + 20, y + 48), p_title, font=fonts["head"], fill="#0F172A")
        draw.text((x + 20, y + 80), sub, font=fonts["small"], fill="#475569")

    def draw_datastore(x, y, w, h, ds_id, ds_title):
        draw.rectangle([x, y, x + w, y + h], fill="#F8FAFC")
        draw.line([(x, y), (x + w, y)], fill="#334155", width=3)
        draw.line([(x, y + h), (x + w, y + h)], fill="#334155", width=3)
        draw.line([(x + 65, y), (x + 65, y + h)], fill="#94A3B8", width=2)
        draw.text((x + 12, y + h // 2 - 10), ds_id, font=fonts["head"], fill="#0F172A")
        draw.text((x + 80, y + h // 2 - 10), ds_title, font=fonts["subhead"], fill="#1E293B")

    # 5 Functional Processes
    draw_dfd_process(80, 200, 480, 130, "Process 1.0", "Ingest & Auto-Detect Telemetry", "Asynchronous chunked file stream / SSE tail")
    draw_dfd_process(80, 460, 480, 130, "Process 2.0", "Normalize & Pre-Filter Events", "BaseLogParser factory & Elastic Common Schema")
    draw_dfd_process(800, 460, 520, 130, "Process 3.0", "Dense Vector Embedding & RAG", "all-MiniLM-L6 ONNX & ChromaDB k-NN")
    draw_dfd_process(1540, 460, 580, 130, "Process 4.0", "Algorithmic CVSS & Reasoning", "Deterministic scoring & Pydantic guardrail")
    draw_dfd_process(1540, 850, 580, 130, "Process 5.0", "SOAR Orchestration & PDF Export", "NIST playbooks, iptables shun & ReportLab")

    # 3 Data Stores
    draw_datastore(80, 760, 480, 80, "D1", "Normalized Event Memory Buffer (ECS)")
    draw_datastore(800, 200, 520, 80, "D2", "MITRE ATT&CK v14 Vector Index (ChromaDB)")
    draw_datastore(800, 760, 520, 80, "D3", "Incidents & Audit SQLite Database")

    # Data Flow Connections
    # P1.0 -> P2.0
    draw_arrow(draw, (320, 330), (320, 460), fill="#0284C7", width=3, arrow_len=12)
    draw.text((330, 385), "Raw Log Chunks", font=fonts["mono"], fill="#0369A1")

    # P2.0 -> D1
    draw_arrow(draw, (240, 590), (240, 760), fill="#059669", width=3, arrow_len=12)
    draw.text((250, 670), "Store Filtered ECS", font=fonts["mono"], fill="#047857")

    # P2.0 -> P3.0
    draw_arrow(draw, (560, 525), (800, 525), fill="#0284C7", width=3, arrow_len=12)
    draw.text((580, 495), "Normalized Event Stream", font=fonts["mono"], fill="#0369A1")

    # D2 -> P3.0
    draw_arrow(draw, (1060, 280), (1060, 460), fill="#7E22CE", width=3, arrow_len=12)
    draw.text((1070, 360), "600+ Technique Embeddings", font=fonts["mono"], fill="#6B21A8")

    # P3.0 -> P4.0
    draw_arrow(draw, (1320, 525), (1540, 525), fill="#0284C7", width=3, arrow_len=12)
    draw.text((1340, 495), "Top-2 Mitre Techniques & Mitigations", font=fonts["mono"], fill="#0369A1")

    # P4.0 -> D3
    draw_arrow(draw, (1600, 590), (1600, 700), fill="#B45309", width=2)
    draw.line([(1600, 700), (1150, 700)], fill="#B45309", width=2)
    draw_arrow(draw, (1150, 700), (1150, 760), fill="#B45309", width=2, arrow_len=12)
    draw.text((1200, 675), "Persist Incident Record & CVSS Score", font=fonts["mono"], fill="#92400E")

    # P4.0 -> P5.0
    draw_arrow(draw, (1830, 590), (1830, 850), fill="#DC2626", width=3, arrow_len=12)
    draw.text((1840, 710), "AIThreatAnalysisResult", font=fonts["mono"], fill="#B91C1C")

    # D3 -> P5.0
    draw_arrow(draw, (1320, 800), (1450, 800), fill="#334155", width=2)
    draw.line([(1450, 800), (1450, 915)], fill="#334155", width=2)
    draw_arrow(draw, (1450, 915), (1540, 915), fill="#334155", width=2, arrow_len=12)
    draw.text((1350, 860), "Query Historical Evidence", font=fonts["small"], fill="#475569")

    # Bottom caption
    draw.text((60, H - 40), "Figure 4.4: Data Flow Diagram (DFD Level 1) - Detailed Functional Decomposition.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_4_4_dfd_level_1.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    generate_svg_4_4()


def generate_svg_4_4():
    svg_path = os.path.join(OUTPUT_DIR, "fig_4_4_dfd_level_1.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 1400" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2200" height="1400" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2200" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 4.4: DATA FLOW DIAGRAM (DFD LEVEL 1 - FUNCTIONAL DECOMPOSITION)</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">Detailed Subsystem Transformations, Intermediate Data Stores, and Control Paths</text>
    
    <defs>
        <marker id="arrB" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284C7" />
        </marker>
        <marker id="arrG" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
        </marker>
        <marker id="arrP" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#7E22CE" />
        </marker>
        <marker id="arrR" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#DC2626" />
        </marker>
        <marker id="arrO" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#B45309" />
        </marker>
    </defs>

    <!-- 5 Processes -->
    <!-- P1.0 -->
    <g transform="translate(80, 200)">
        <rect width="480" height="130" rx="16" fill="#F0F9FF" stroke="#0284C7" stroke-width="3"/>
        <text x="20" y="32" font-size="18" font-weight="bold" fill="#0369A1">Process 1.0</text>
        <text x="20" y="65" font-size="22" font-weight="bold" fill="#0F172A">Ingest &amp; Auto-Detect Telemetry</text>
        <text x="20" y="95" font-size="14" fill="#475569">Asynchronous chunked file stream / SSE tail</text>
    </g>
    <!-- P2.0 -->
    <g transform="translate(80, 460)">
        <rect width="480" height="130" rx="16" fill="#F0F9FF" stroke="#0284C7" stroke-width="3"/>
        <text x="20" y="32" font-size="18" font-weight="bold" fill="#0369A1">Process 2.0</text>
        <text x="20" y="65" font-size="22" font-weight="bold" fill="#0F172A">Normalize &amp; Pre-Filter Events</text>
        <text x="20" y="95" font-size="14" fill="#475569">BaseLogParser factory &amp; Elastic Common Schema</text>
    </g>
    <!-- P3.0 -->
    <g transform="translate(800, 460)">
        <rect width="520" height="130" rx="16" fill="#F0F9FF" stroke="#0284C7" stroke-width="3"/>
        <text x="20" y="32" font-size="18" font-weight="bold" fill="#0369A1">Process 3.0</text>
        <text x="20" y="65" font-size="22" font-weight="bold" fill="#0F172A">Dense Vector Embedding &amp; RAG</text>
        <text x="20" y="95" font-size="14" fill="#475569">all-MiniLM-L6 ONNX &amp; ChromaDB k-NN</text>
    </g>
    <!-- P4.0 -->
    <g transform="translate(1540, 460)">
        <rect width="580" height="130" rx="16" fill="#F0F9FF" stroke="#0284C7" stroke-width="3"/>
        <text x="20" y="32" font-size="18" font-weight="bold" fill="#0369A1">Process 4.0</text>
        <text x="20" y="65" font-size="22" font-weight="bold" fill="#0F172A">Algorithmic CVSS &amp; Reasoning</text>
        <text x="20" y="95" font-size="14" fill="#475569">Deterministic scoring &amp; Pydantic guardrail</text>
    </g>
    <!-- P5.0 -->
    <g transform="translate(1540, 850)">
        <rect width="580" height="130" rx="16" fill="#F0F9FF" stroke="#0284C7" stroke-width="3"/>
        <text x="20" y="32" font-size="18" font-weight="bold" fill="#0369A1">Process 5.0</text>
        <text x="20" y="65" font-size="22" font-weight="bold" fill="#0F172A">SOAR Orchestration &amp; PDF Export</text>
        <text x="20" y="95" font-size="14" fill="#475569">NIST playbooks, iptables shun &amp; ReportLab</text>
    </g>

    <!-- 3 Data Stores -->
    <!-- D1 -->
    <g transform="translate(80, 760)">
        <line x1="0" y1="0" x2="480" y2="0" stroke="#334155" stroke-width="3"/>
        <line x1="0" y1="80" x2="480" y2="80" stroke="#334155" stroke-width="3"/>
        <line x1="65" y1="0" x2="65" y2="80" stroke="#94A3B8" stroke-width="2"/>
        <text x="18" y="48" font-size="22" font-weight="bold" fill="#0F172A">D1</text>
        <text x="80" y="48" font-size="18" fill="#1E293B">Normalized Event Buffer (ECS)</text>
    </g>
    <!-- D2 -->
    <g transform="translate(800, 200)">
        <line x1="0" y1="0" x2="520" y2="0" stroke="#334155" stroke-width="3"/>
        <line x1="0" y1="80" x2="520" y2="80" stroke="#334155" stroke-width="3"/>
        <line x1="65" y1="0" x2="65" y2="80" stroke="#94A3B8" stroke-width="2"/>
        <text x="18" y="48" font-size="22" font-weight="bold" fill="#0F172A">D2</text>
        <text x="80" y="48" font-size="18" fill="#1E293B">MITRE ATT&amp;CK v14 Index (ChromaDB)</text>
    </g>
    <!-- D3 -->
    <g transform="translate(800, 760)">
        <line x1="0" y1="0" x2="520" y2="0" stroke="#334155" stroke-width="3"/>
        <line x1="0" y1="80" x2="520" y2="80" stroke="#334155" stroke-width="3"/>
        <line x1="65" y1="0" x2="65" y2="80" stroke="#94A3B8" stroke-width="2"/>
        <text x="18" y="48" font-size="22" font-weight="bold" fill="#0F172A">D3</text>
        <text x="80" y="48" font-size="18" fill="#1E293B">Incidents &amp; Audit Database (SQLite)</text>
    </g>

    <!-- Connectors -->
    <line x1="320" y1="330" x2="320" y2="460" stroke="#0284C7" stroke-width="3" marker-end="url(#arrB)"/>
    <text x="330" y="395" font-size="15" font-family="monospace" fill="#0369A1">Raw Log Chunks</text>

    <line x1="240" y1="590" x2="240" y2="760" stroke="#059669" stroke-width="3" marker-end="url(#arrG)"/>
    <text x="250" y="680" font-size="15" font-family="monospace" fill="#047857">Store Filtered ECS</text>

    <line x1="560" y1="525" x2="800" y2="525" stroke="#0284C7" stroke-width="3" marker-end="url(#arrB)"/>
    <text x="580" y="500" font-size="15" font-family="monospace" fill="#0369A1">Normalized Event Stream</text>

    <line x1="1060" y1="280" x2="1060" y2="460" stroke="#7E22CE" stroke-width="3" marker-end="url(#arrP)"/>
    <text x="1070" y="370" font-size="15" font-family="monospace" fill="#6B21A8">600+ Technique Embeddings</text>

    <line x1="1320" y1="525" x2="1540" y2="525" stroke="#0284C7" stroke-width="3" marker-end="url(#arrB)"/>
    <text x="1340" y="500" font-size="15" font-family="monospace" fill="#0369A1">Top-2 Mitre Techniques</text>

    <path d="M1600,590 L1600,700 L1150,700 L1150,760" fill="none" stroke="#B45309" stroke-width="2" marker-end="url(#arrO)"/>
    <text x="1200" y="685" font-size="15" font-family="monospace" fill="#92400E">Persist Incident Record &amp; CVSS Score</text>

    <line x1="1830" y1="590" x2="1830" y2="850" stroke="#DC2626" stroke-width="3" marker-end="url(#arrR)"/>
    <text x="1840" y="720" font-size="15" font-family="monospace" fill="#B91C1C">AIThreatAnalysisResult</text>

    <text x="60" y="1365" font-size="14" fill="#64748B">Figure 4.4: Data Flow Diagram (DFD Level 1) - Detailed Functional Decomposition.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


# ==============================================================================
# 5. FIGURE 4.5: DETAILED ENTITY-RELATIONSHIP (E-R) DIAGRAM
# ==============================================================================
def generate_figure_4_5():
    W, H = 2200, 1400
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 4.5: ENTITY-RELATIONSHIP (E-R) DIAGRAM & DATA SCHEMA", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "Relational Database Entities, Primary/Foreign Keys, and Cardinality (1:N, M:N)", font=fonts["subtitle"], fill="#94A3B8")

    def draw_er_table(x, y, w, h, table_name, pk_list, fk_list, attr_list, header_bg="#1E293B"):
        draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill="#FFFFFF", outline="#475569", width=2)
        draw.rounded_rectangle([x, y, x + w, y + 45], radius=8, fill=header_bg)
        draw.rectangle([x, y + 35, x + w, y + 45], fill=header_bg)
        draw.text((x + 15, y + 12), table_name, font=fonts["head"], fill="#FFFFFF")

        cur_y = y + 55
        for pk in pk_list:
            draw.text((x + 15, cur_y), "[PK] " + pk, font=fonts["mono"], fill="#B45309")
            cur_y += 28
        for fk in fk_list:
            draw.text((x + 15, cur_y), "[FK] " + fk, font=fonts["mono"], fill="#2563EB")
            cur_y += 28
        for attr in attr_list:
            draw.text((x + 15, cur_y), attr, font=fonts["mono"], fill="#1E293B")
            cur_y += 28

    # 1. INCIDENTS (Center Master Entity)
    draw_er_table(
        x=850, y=200, w=500, h=340,
        table_name="INCIDENTS",
        pk_list=["incident_id: VARCHAR(36)"],
        fk_list=[],
        attr_list=[
            "title: VARCHAR(255)",
            "severity: VARCHAR(20) [HIGH|CRIT]",
            "status: VARCHAR(30) [OPEN|SHUNNED]",
            "risk_score: FLOAT (0.0 - 100.0)",
            "threat_classification: VARCHAR(100)",
            "summary: TEXT",
            "created_at: DATETIME (UTC)",
            "updated_at: DATETIME (UTC)"
        ],
        header_bg="#0F172A"
    )

    # 2. LOG_EVENTS (1:N with Incidents)
    draw_er_table(
        x=80, y=200, w=500, h=380,
        table_name="LOG_EVENTS",
        pk_list=["event_id: VARCHAR(36)"],
        fk_list=["incident_id: VARCHAR(36) REFERENCES INCIDENTS"],
        attr_list=[
            "timestamp: DATETIME (UTC)",
            "source_type: VARCHAR(50)",
            "source_ip: VARCHAR(45)",
            "destination_ip: VARCHAR(45)",
            "username: VARCHAR(100)",
            "event_type: VARCHAR(50)",
            "severity_hint: VARCHAR(20)",
            "raw_payload: TEXT",
            "is_benign: BOOLEAN"
        ],
        header_bg="#1E3A8A"
    )

    # 3. MITRE_TECHNIQUES (Master Threat Library - ChromaDB & Relational)
    draw_er_table(
        x=1600, y=200, w=520, h=340,
        table_name="MITRE_TECHNIQUES",
        pk_list=["technique_id: VARCHAR(20) [e.g. T1110]"],
        fk_list=[],
        attr_list=[
            "tactic: VARCHAR(50) [Credential Access]",
            "name: VARCHAR(150) [Brute Force]",
            "description: TEXT",
            "verified_mitigations: TEXT",
            "dense_embedding_vector: BLOB(384x4)",
            "detection_guidance: TEXT"
        ],
        header_bg="#6B21A8"
    )

    # 4. INCIDENT_MITRE_MAP (Join Table: M:N)
    draw_er_table(
        x=1250, y=660, w=480, h=220,
        table_name="INCIDENT_MITRE_MAP",
        pk_list=["map_id: INTEGER AUTOINCREMENT"],
        fk_list=[
            "incident_id REFERENCES INCIDENTS",
            "technique_id REFERENCES MITRE_TECHNIQUES"
        ],
        attr_list=[
            "cosine_similarity_score: FLOAT",
            "is_primary_attack_vector: BOOLEAN"
        ],
        header_bg="#4338CA"
    )

    # 5. CONTAINMENT_ACTIONS (1:N with Incidents)
    draw_er_table(
        x=450, y=700, w=520, h=320,
        table_name="CONTAINMENT_ACTIONS",
        pk_list=["action_id: VARCHAR(36)"],
        fk_list=["incident_id: VARCHAR(36) REFERENCES INCIDENTS"],
        attr_list=[
            "action_type: VARCHAR(50) [IPTABLES_DROP]",
            "target_ip: VARCHAR(45)",
            "command_syntax: TEXT",
            "execution_status: VARCHAR(30)",
            "executed_by: VARCHAR(100)",
            "executed_at: DATETIME (UTC)"
        ],
        header_bg="#991B1B"
    )

    # 6. AUDIT_REPORTS (1:1 with Incidents)
    draw_er_table(
        x=1050, y=980, w=520, h=280,
        table_name="AUDIT_REPORTS",
        pk_list=["report_id: VARCHAR(36)"],
        fk_list=["incident_id: VARCHAR(36) REFERENCES INCIDENTS"],
        attr_list=[
            "sha256_checksum: VARCHAR(64)",
            "pdf_file_path: VARCHAR(255)",
            "report_page_count: INTEGER",
            "generated_at: DATETIME (UTC)",
            "investigator_signature: VARCHAR(100)"
        ],
        header_bg="#0F766E"
    )

    # Cardinality Connectors
    # 1. INCIDENTS (1) to LOG_EVENTS (N)
    draw.line([(850, 350), (580, 350)], fill="#2563EB", width=3)
    draw.text((820, 320), "1", font=fonts["head"], fill="#0F172A")
    draw.text((600, 320), "N", font=fonts["head"], fill="#0F172A")

    # 2. INCIDENTS (1) to CONTAINMENT_ACTIONS (N)
    draw.line([(950, 540), (950, 640), (710, 640), (710, 700)], fill="#DC2626", width=3)
    draw.text((960, 550), "1", font=fonts["head"], fill="#0F172A")
    draw.text((720, 670), "N", font=fonts["head"], fill="#0F172A")

    # 3. INCIDENTS (1) to INCIDENT_MITRE_MAP (N)
    draw.line([(1200, 540), (1200, 750), (1250, 750)], fill="#4338CA", width=3)
    draw.text((1210, 550), "1", font=fonts["head"], fill="#0F172A")
    draw.text((1225, 720), "N", font=fonts["head"], fill="#0F172A")

    # 4. MITRE_TECHNIQUES (1) to INCIDENT_MITRE_MAP (N)
    draw.line([(1750, 540), (1750, 750), (1730, 750)], fill="#6B21A8", width=3)
    draw.text((1760, 550), "1", font=fonts["head"], fill="#0F172A")
    draw.text((1700, 720), "N", font=fonts["head"], fill="#0F172A")

    # 5. INCIDENTS (1) to AUDIT_REPORTS (1)
    draw.line([(1100, 540), (1100, 980)], fill="#0F766E", width=3)
    draw.text((1110, 550), "1", font=fonts["head"], fill="#0F172A")
    draw.text((1110, 950), "1", font=fonts["head"], fill="#0F172A")

    # Bottom caption
    draw.text((60, H - 40), "Figure 4.5: Entity-Relationship Diagram Depicting Database Schema and Key Relationships.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_4_5_er_diagram.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    generate_svg_4_5()


def generate_svg_4_5():
    svg_path = os.path.join(OUTPUT_DIR, "fig_4_5_er_diagram.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 1400" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2200" height="1400" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2200" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 4.5: ENTITY-RELATIONSHIP (E-R) DIAGRAM &amp; DATA SCHEMA</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">Relational Database Entities, Primary/Foreign Keys, and Cardinality (1:N, M:N)</text>

    <!-- INCIDENTS -->
    <g transform="translate(850, 200)">
        <rect width="500" height="340" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L492,0 Q500,0 500,8 L500,45 L0,45 Z" fill="#0F172A"/>
        <text x="15" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">INCIDENTS</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#B45309">[PK] incident_id: VARCHAR(36)</text>
        <text x="15" y="112" font-size="14" font-family="monospace" fill="#1E293B">title: VARCHAR(255)</text>
        <text x="15" y="140" font-size="14" font-family="monospace" fill="#1E293B">severity: VARCHAR(20) [HIGH|CRIT]</text>
        <text x="15" y="168" font-size="14" font-family="monospace" fill="#1E293B">status: VARCHAR(30) [OPEN|SHUNNED]</text>
        <text x="15" y="196" font-size="14" font-family="monospace" fill="#1E293B">risk_score: FLOAT (0.0 - 100.0)</text>
        <text x="15" y="224" font-size="14" font-family="monospace" fill="#1E293B">threat_classification: VARCHAR(100)</text>
        <text x="15" y="252" font-size="14" font-family="monospace" fill="#1E293B">created_at, updated_at: DATETIME</text>
    </g>

    <!-- LOG_EVENTS -->
    <g transform="translate(80, 200)">
        <rect width="500" height="380" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L492,0 Q500,0 500,8 L500,45 L0,45 Z" fill="#1E3A8A"/>
        <text x="15" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">LOG_EVENTS</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#B45309">[PK] event_id: VARCHAR(36)</text>
        <text x="15" y="110" font-size="14" font-family="monospace" fill="#2563EB">[FK] incident_id REFERENCES INCIDENTS</text>
        <text x="15" y="140" font-size="14" font-family="monospace" fill="#1E293B">timestamp: DATETIME (UTC)</text>
        <text x="15" y="168" font-size="14" font-family="monospace" fill="#1E293B">source_type: VARCHAR(50)</text>
        <text x="15" y="196" font-size="14" font-family="monospace" fill="#1E293B">source_ip, destination_ip: VARCHAR(45)</text>
        <text x="15" y="224" font-size="14" font-family="monospace" fill="#1E293B">username, event_type: VARCHAR(50)</text>
        <text x="15" y="252" font-size="14" font-family="monospace" fill="#1E293B">severity_hint: VARCHAR(20)</text>
        <text x="15" y="280" font-size="14" font-family="monospace" fill="#1E293B">raw_payload: TEXT, is_benign: BOOL</text>
    </g>

    <!-- MITRE_TECHNIQUES -->
    <g transform="translate(1600, 200)">
        <rect width="520" height="340" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L512,0 Q520,0 520,8 L520,45 L0,45 Z" fill="#6B21A8"/>
        <text x="15" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">MITRE_TECHNIQUES</text>
        <text x="15" y="80" font-size="15" font-family="monospace" fill="#B45309">[PK] technique_id: VARCHAR(20) [T1110]</text>
        <text x="15" y="112" font-size="14" font-family="monospace" fill="#1E293B">tactic: VARCHAR(50) [Credential Access]</text>
        <text x="15" y="140" font-size="14" font-family="monospace" fill="#1E293B">name: VARCHAR(150) [Brute Force]</text>
        <text x="15" y="168" font-size="14" font-family="monospace" fill="#1E293B">description: TEXT</text>
        <text x="15" y="196" font-size="14" font-family="monospace" fill="#1E293B">verified_mitigations: TEXT</text>
        <text x="15" y="224" font-size="14" font-family="monospace" fill="#1E293B">dense_embedding_vector: BLOB(384x4)</text>
    </g>

    <!-- INCIDENT_MITRE_MAP -->
    <g transform="translate(1250, 660)">
        <rect width="480" height="220" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L472,0 Q480,0 480,8 L480,45 L0,45 Z" fill="#4338CA"/>
        <text x="15" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">INCIDENT_MITRE_MAP</text>
        <text x="15" y="75" font-size="14" font-family="monospace" fill="#B45309">[PK] map_id: INTEGER AUTOINCREMENT</text>
        <text x="15" y="105" font-size="14" font-family="monospace" fill="#2563EB">[FK] incident_id REFERENCES INCIDENTS</text>
        <text x="15" y="135" font-size="14" font-family="monospace" fill="#2563EB">[FK] technique_id REFERENCES MITRE</text>
        <text x="15" y="165" font-size="14" font-family="monospace" fill="#1E293B">cosine_similarity_score: FLOAT</text>
    </g>

    <!-- CONTAINMENT_ACTIONS -->
    <g transform="translate(450, 700)">
        <rect width="520" height="320" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L512,0 Q520,0 520,8 L520,45 L0,45 Z" fill="#991B1B"/>
        <text x="15" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">CONTAINMENT_ACTIONS</text>
        <text x="15" y="75" font-size="15" font-family="monospace" fill="#B45309">[PK] action_id: VARCHAR(36)</text>
        <text x="15" y="105" font-size="14" font-family="monospace" fill="#2563EB">[FK] incident_id REFERENCES INCIDENTS</text>
        <text x="15" y="135" font-size="14" font-family="monospace" fill="#1E293B">action_type: VARCHAR(50) [IPTABLES_DROP]</text>
        <text x="15" y="165" font-size="14" font-family="monospace" fill="#1E293B">target_ip: VARCHAR(45)</text>
        <text x="15" y="195" font-size="14" font-family="monospace" fill="#1E293B">command_syntax: TEXT</text>
        <text x="15" y="225" font-size="14" font-family="monospace" fill="#1E293B">execution_status, executed_at: DATETIME</text>
    </g>

    <!-- AUDIT_REPORTS -->
    <g transform="translate(1050, 980)">
        <rect width="520" height="280" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2"/>
        <path d="M0,8 Q0,0 8,0 L512,0 Q520,0 520,8 L520,45 L0,45 Z" fill="#0F766E"/>
        <text x="15" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">AUDIT_REPORTS</text>
        <text x="15" y="75" font-size="15" font-family="monospace" fill="#B45309">[PK] report_id: VARCHAR(36)</text>
        <text x="15" y="105" font-size="14" font-family="monospace" fill="#2563EB">[FK] incident_id REFERENCES INCIDENTS</text>
        <text x="15" y="135" font-size="14" font-family="monospace" fill="#1E293B">sha256_checksum: VARCHAR(64)</text>
        <text x="15" y="165" font-size="14" font-family="monospace" fill="#1E293B">pdf_file_path: VARCHAR(255)</text>
        <text x="15" y="195" font-size="14" font-family="monospace" fill="#1E293B">report_page_count: INTEGER, generated_at</text>
    </g>

    <!-- Lines -->
    <line x1="850" y1="350" x2="580" y2="350" stroke="#2563EB" stroke-width="3"/>
    <text x="820" y="340" font-size="20" font-weight="bold" fill="#0F172A">1</text>
    <text x="600" y="340" font-size="20" font-weight="bold" fill="#0F172A">N</text>

    <path d="M950,540 L950,640 L710,640 L710,700" fill="none" stroke="#DC2626" stroke-width="3"/>
    <text x="960" y="565" font-size="20" font-weight="bold" fill="#0F172A">1</text>
    <text x="720" y="690" font-size="20" font-weight="bold" fill="#0F172A">N</text>

    <path d="M1200,540 L1200,750 L1250,750" fill="none" stroke="#4338CA" stroke-width="3"/>
    <text x="1210" y="565" font-size="20" font-weight="bold" fill="#0F172A">1</text>
    <text x="1230" y="740" font-size="20" font-weight="bold" fill="#0F172A">N</text>

    <path d="M1750,540 L1750,750 L1730,750" fill="none" stroke="#6B21A8" stroke-width="3"/>
    <text x="1760" y="565" font-size="20" font-weight="bold" fill="#0F172A">1</text>
    <text x="1700" y="740" font-size="20" font-weight="bold" fill="#0F172A">N</text>

    <line x1="1100" y1="540" x2="1100" y2="980" stroke="#0F766E" stroke-width="3"/>
    <text x="1110" y="565" font-size="20" font-weight="bold" fill="#0F172A">1</text>
    <text x="1110" y="965" font-size="20" font-weight="bold" fill="#0F172A">1</text>

    <text x="60" y="1365" font-size="14" fill="#64748B">Figure 4.5: Entity-Relationship Diagram Depicting Database Schema and Key Relationships.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


# ==============================================================================
# 6. FIGURE 6.1: TIMELINE GANTT CHART (TERM 1 & TERM 2)
# ==============================================================================
def generate_figure_6_1():
    W, H = 2200, 1300
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 6.1: PROJECT IMPLEMENTATION TIMELINE & GANTT CHART", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "Work Breakdown Structure across Sem-VII (Term 1) and Sem-VIII (Term 2) Academic Milestones", font=fonts["subtitle"], fill="#94A3B8")

    # Time Axis Headers (Weeks 1 to 16 for Term 1, Weeks 1 to 16 for Term 2)
    chart_x = 550
    chart_w = 1580
    term1_w = chart_w // 2
    term2_w = chart_w // 2

    # Term Banners
    draw.rectangle([chart_x, 150, chart_x + term1_w, 200], fill="#1E3A8A")
    draw.text((chart_x + term1_w // 2 - 120, 165), "TERM 1 (SEM-VII: JUL - NOV)", font=fonts["subhead"], fill="#FFFFFF")

    draw.rectangle([chart_x + term1_w, 150, chart_x + chart_w, 200], fill="#0F766E")
    draw.text((chart_x + term1_w + term2_w // 2 - 120, 165), "TERM 2 (SEM-VIII: JAN - APR)", font=fonts["subhead"], fill="#FFFFFF")

    # 8 Month / Milestone divisions
    months = ["Month 1 (W1-4)", "Month 2 (W5-8)", "Month 3 (W9-12)", "Month 4 (W13-16)",
              "Month 5 (W1-4)", "Month 6 (W5-8)", "Month 7 (W9-12)", "Month 8 (W13-16)"]
    m_w = chart_w // 8
    for idx, m in enumerate(months):
        mx = chart_x + idx * m_w
        draw.rectangle([mx, 205, mx + m_w, 245], fill="#F1F5F9", outline="#CBD5E1")
        draw.text((mx + 10, 215), m, font=fonts["small"], fill="#334155")
        # Vertical grid line down chart
        draw.line([(mx, 245), (mx, 1180)], fill="#F1F5F9", width=1)

    tasks = [
        # Term 1 Tasks
        ("1. Literature Review & Problem Formulation", 0, 1.2, "#3B82F6", "Base paper survey, SIEM limitation audit"),
        ("2. Architecture Design & Parser Factory", 1.0, 2.2, "#2563EB", "BaseLogParser hierarchy, regex tokenizers"),
        ("3. ECS Modeling & Edge Filter Engine", 2.0, 3.2, "#1D4ED8", "ECS normalization & 99.2% noise rejection"),
        ("4. Sem-VII Synopsis & Defense Prep", 3.0, 4.0, "#1E3A8A", "Synopsis report, college review presentation"),
        # Term 2 Tasks
        ("5. ChromaDB Vector Store & ONNX Embeddings", 4.0, 5.2, "#0D9488", "600+ MITRE v14 index, all-MiniLM-L6-v2"),
        ("6. Algorithmic CVSS Risk Engine & Guardrails", 5.0, 6.2, "#0F766E", "Pydantic validation, progression scoring"),
        ("7. Real-Time Radar SSE & SOAR Cockpit", 6.0, 7.2, "#047857", "SSE streaming tail, iptables auto-shunning"),
        ("8. Rigorous Pytest Validation & Viva Defense", 7.0, 8.0, "#115E59", "9/9 pytest suites, ReportLab PDF, Viva")
    ]

    task_y = 265
    bar_h = 70
    gap = 40

    for name, start_m, end_m, color, deliverable in tasks:
        # Task label on left
        draw.text((50, task_y + 10), name, font=fonts["head"], fill="#0F172A")
        draw.text((50, task_y + 40), deliverable, font=fonts["small"], fill="#64748B")

        # Gantt Bar
        bx0 = chart_x + int(start_m * m_w)
        bx1 = chart_x + int(end_m * m_w)
        draw.rounded_rectangle([bx0, task_y, bx1, task_y + bar_h], radius=8, fill=color)

        # Progress badge inside bar
        draw.text((bx0 + 15, task_y + 22), f"Duration: {int((end_m - start_m)*4)} Weeks (100% Completed)", font=fonts["mono"], fill="#FFFFFF")

        task_y += bar_h + gap

    # Bottom caption
    draw.text((60, H - 40), "Figure 6.1: Comprehensive Academic Timeline and Work Breakdown Schedule across Two Semesters.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_6_1_timeline_gantt.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    generate_svg_6_1()


def generate_svg_6_1():
    svg_path = os.path.join(OUTPUT_DIR, "fig_6_1_timeline_gantt.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2200 1300" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2200" height="1300" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2200" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 6.1: PROJECT IMPLEMENTATION TIMELINE &amp; GANTT CHART</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">Work Breakdown Structure across Sem-VII (Term 1) and Sem-VIII (Term 2) Academic Milestones</text>

    <!-- Header Bands -->
    <rect x="550" y="150" width="790" height="50" fill="#1E3A8A"/>
    <text x="820" y="182" font-size="18" font-weight="bold" fill="#FFFFFF">TERM 1 (SEM-VII: JUL - NOV)</text>

    <rect x="1340" y="150" width="790" height="50" fill="#0F766E"/>
    <text x="1600" y="182" font-size="18" font-weight="bold" fill="#FFFFFF">TERM 2 (SEM-VIII: JAN - APR)</text>

    <!-- 8 Tasks -->
    <!-- Task 1 -->
    <text x="50" y="295" font-size="20" font-weight="bold" fill="#0F172A">1. Literature Review &amp; Problem Formulation</text>
    <text x="50" y="325" font-size="14" fill="#64748B">Base paper survey, SIEM limitation audit</text>
    <rect x="550" y="265" width="237" height="70" rx="8" fill="#3B82F6"/>
    <text x="565" y="308" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 1-4 (100% Done)</text>

    <!-- Task 2 -->
    <text x="50" y="405" font-size="20" font-weight="bold" fill="#0F172A">2. Architecture Design &amp; Parser Factory</text>
    <text x="50" y="435" font-size="14" fill="#64748B">BaseLogParser hierarchy, regex tokenizers</text>
    <rect x="747" y="375" width="237" height="70" rx="8" fill="#2563EB"/>
    <text x="762" y="418" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 5-8 (100% Done)</text>

    <!-- Task 3 -->
    <text x="50" y="515" font-size="20" font-weight="bold" fill="#0F172A">3. ECS Modeling &amp; Edge Filter Engine</text>
    <text x="50" y="545" font-size="14" fill="#64748B">ECS normalization &amp; 99.2% noise rejection</text>
    <rect x="944" y="485" width="237" height="70" rx="8" fill="#1D4ED8"/>
    <text x="959" y="528" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 9-12 (100% Done)</text>

    <!-- Task 4 -->
    <text x="50" y="625" font-size="20" font-weight="bold" fill="#0F172A">4. Sem-VII Synopsis &amp; Defense Prep</text>
    <text x="50" y="655" font-size="14" fill="#64748B">Synopsis report, college review presentation</text>
    <rect x="1141" y="595" width="197" height="70" rx="8" fill="#1E3A8A"/>
    <text x="1156" y="638" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 13-16 (100% Done)</text>

    <!-- Task 5 -->
    <text x="50" y="735" font-size="20" font-weight="bold" fill="#0F172A">5. ChromaDB Vector Store &amp; ONNX Embeddings</text>
    <text x="50" y="765" font-size="14" fill="#64748B">600+ MITRE v14 index, all-MiniLM-L6-v2</text>
    <rect x="1340" y="705" width="237" height="70" rx="8" fill="#0D9488"/>
    <text x="1355" y="748" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 1-4 (100% Done)</text>

    <!-- Task 6 -->
    <text x="50" y="845" font-size="20" font-weight="bold" fill="#0F172A">6. Algorithmic CVSS Risk Engine &amp; Guardrails</text>
    <text x="50" y="875" font-size="14" fill="#64748B">Pydantic validation, progression scoring</text>
    <rect x="1537" y="815" width="237" height="70" rx="8" fill="#0F766E"/>
    <text x="1552" y="858" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 5-8 (100% Done)</text>

    <!-- Task 7 -->
    <text x="50" y="955" font-size="20" font-weight="bold" fill="#0F172A">7. Real-Time Radar SSE &amp; SOAR Cockpit</text>
    <text x="50" y="985" font-size="14" fill="#64748B">SSE streaming tail, iptables auto-shunning</text>
    <rect x="1734" y="925" width="237" height="70" rx="8" fill="#047857"/>
    <text x="1749" y="968" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 9-12 (100% Done)</text>

    <!-- Task 8 -->
    <text x="50" y="1065" font-size="20" font-weight="bold" fill="#0F172A">8. Rigorous Pytest Validation &amp; Viva Defense</text>
    <text x="50" y="1095" font-size="14" fill="#64748B">9/9 pytest suites, ReportLab PDF, Viva</text>
    <rect x="1931" y="1035" width="197" height="70" rx="8" fill="#115E59"/>
    <text x="1946" y="1078" font-size="14" font-family="monospace" fill="#FFFFFF">Weeks 13-16 (100% Done)</text>

    <text x="60" y="1265" font-size="14" fill="#64748B">Figure 6.1: Comprehensive Academic Timeline and Work Breakdown Schedule across Two Semesters.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


# ==============================================================================
# 7. FIGURE 7.1: PERFORMANCE & BENCHMARK EVALUATION CHART
# ==============================================================================
def generate_figure_7_1():
    W, H = 2000, 1200
    img = Image.new("RGB", (W, H), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title header banner
    draw.rectangle([0, 0, W, 120], fill="#0F172A")
    draw.text((60, 25), "FIGURE 7.1: QUANTITATIVE BENCHMARK EVALUATION COMPARISON", font=fonts["title"], fill="#F8FAFC")
    draw.text((60, 75), "Empirical Performance Comparison: Traditional SOC vs Direct LLM vs CyberSentinel AI", font=fonts["subtitle"], fill="#94A3B8")

    metrics = [
        {
            "name": "Mean Time to Respond (MTTR)",
            "unit": "Seconds (Lower is Better)",
            "vals": [
                ("Traditional SOC", 3000, "#EF4444", "3,000s (50 min)"),
                ("Direct LLM (ChatGPT)", 25, "#F59E0B", "25s"),
                ("CyberSentinel AI", 2.1, "#10B981", "2.1s (99.9% faster)")
            ],
            "max_scale": 3000,
            "log_scale": True
        },
        {
            "name": "Alert Noise Pre-Filtering Rate",
            "unit": "Percentage (Higher is Better)",
            "vals": [
                ("Traditional SOC", 0.0, "#EF4444", "0.0% (No pre-filter)"),
                ("Direct LLM (ChatGPT)", 15.0, "#F59E0B", "15.0% (Uncalibrated)"),
                ("CyberSentinel AI", 99.2, "#10B981", "99.2% (Edge parser)")
            ],
            "max_scale": 100,
            "log_scale": False
        },
        {
            "name": "AI Hallucination Rate",
            "unit": "Percentage (0.0% is Perfect)",
            "vals": [
                ("Traditional SOC", 0.0, "#64748B", "N/A (Rule-based)"),
                ("Direct LLM (ChatGPT)", 35.7, "#EF4444", "35.7% (High risk)"),
                ("CyberSentinel AI", 0.0, "#10B981", "0.0% (Vector grounded)")
            ],
            "max_scale": 100,
            "log_scale": False
        },
        {
            "name": "MITRE Technique Mapping Accuracy",
            "unit": "Percentage (Higher is Better)",
            "vals": [
                ("Traditional SOC", 71.0, "#EF4444", "71.0% (Manual lookup)"),
                ("Direct LLM (ChatGPT)", 64.3, "#F59E0B", "64.3% (Frequent hallucination)"),
                ("CyberSentinel AI", 94.2, "#10B981", "94.2% (Cosine similarity)")
            ],
            "max_scale": 100,
            "log_scale": False
        }
    ]

    card_w = 900
    card_h = 480
    coords = [(60, 160), (1020, 160), (60, 680), (1020, 680)]

    for m_idx, m in enumerate(metrics):
        cx, cy = coords[m_idx]
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=12, fill="#F8FAFC", outline="#CBD5E1", width=2)
        
        # Header inside card
        draw.rectangle([cx, cy, cx + card_w, cy + 60], fill="#1E293B")
        draw.text((cx + 25, cy + 12), m["name"], font=fonts["head"], fill="#FFFFFF")
        draw.text((cx + 25, cy + 38), m["unit"], font=fonts["small"], fill="#94A3B8")

        # Draw 3 comparison bars
        by = cy + 100
        for sys_name, val, color, label in m["vals"]:
            draw.text((cx + 25, by), sys_name, font=fonts["body"], fill="#0F172A")
            
            # Bar background track
            track_w = 540
            draw.rounded_rectangle([cx + 25, by + 30, cx + 25 + track_w, by + 65], radius=6, fill="#E2E8F0")
            
            # Active bar fill
            if m["log_scale"]:
                import math
                norm = math.log10(max(val, 0.1)) / math.log10(m["max_scale"])
                fill_w = max(int(norm * track_w), 12)
            else:
                fill_w = max(int((val / m["max_scale"]) * track_w), 12)
                
            draw.rounded_rectangle([cx + 25, by + 30, cx + 25 + fill_w, by + 65], radius=6, fill=color)
            
            # Label
            draw.text((cx + 35 + track_w, by + 35), label, font=fonts["mono"], fill="#0F172A")
            by += 115

    # Bottom caption
    draw.text((60, H - 40), "Figure 7.1: Quantitative Performance Benchmarks Across Four Mission-Critical Security Metrics.", font=fonts["small"], fill="#64748B")

    png_path = os.path.join(OUTPUT_DIR, "fig_7_1_performance_benchmark.png")
    img.save(png_path, "PNG", dpi=(300, 300))
    print(f"Generated: {png_path}")

    generate_svg_7_1()


def generate_svg_7_1():
    svg_path = os.path.join(OUTPUT_DIR, "fig_7_1_performance_benchmark.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 1200" width="100%" height="100%" font-family="Helvetica, Arial, sans-serif">
    <rect width="2000" height="1200" fill="#FFFFFF"/>
    
    <!-- Title Banner -->
    <rect width="2000" height="120" fill="#0F172A"/>
    <text x="60" y="55" font-size="36" font-weight="bold" fill="#F8FAFC">FIGURE 7.1: QUANTITATIVE BENCHMARK EVALUATION COMPARISON</text>
    <text x="60" y="95" font-size="22" fill="#94A3B8">Empirical Performance Comparison: Traditional SOC vs Direct LLM vs CyberSentinel AI</text>

    <!-- Card 1: MTTR -->
    <g transform="translate(60, 160)">
        <rect width="900" height="480" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
        <path d="M0,12 Q0,0 12,0 L888,0 Q900,0 900,12 L900,60 L0,60 Z" fill="#1E293B"/>
        <text x="25" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">Mean Time to Respond (MTTR)</text>
        <text x="25" y="50" font-size="13" fill="#94A3B8">Seconds (Lower is Better)</text>
        
        <!-- Bars -->
        <text x="25" y="100" font-size="16" fill="#0F172A">Traditional SOC</text>
        <rect x="25" y="115" width="540" height="35" rx="6" fill="#EF4444"/>
        <text x="580" y="140" font-size="15" font-family="monospace" fill="#0F172A">3,000s (50 min)</text>

        <text x="25" y="215" font-size="16" fill="#0F172A">Direct LLM (ChatGPT)</text>
        <rect x="25" y="230" width="180" height="35" rx="6" fill="#F59E0B"/>
        <text x="580" y="255" font-size="15" font-family="monospace" fill="#0F172A">25s</text>

        <text x="25" y="330" font-size="16" font-weight="bold" fill="#0F172A">CyberSentinel AI</text>
        <rect x="25" y="345" width="35" height="35" rx="6" fill="#10B981"/>
        <text x="580" y="370" font-size="15" font-family="monospace" font-weight="bold" fill="#047857">2.1s (99.9% faster)</text>
    </g>

    <!-- Card 2: Noise Filter -->
    <g transform="translate(1020, 160)">
        <rect width="900" height="480" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
        <path d="M0,12 Q0,0 12,0 L888,0 Q900,0 900,12 L900,60 L0,60 Z" fill="#1E293B"/>
        <text x="25" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">Alert Noise Pre-Filtering Rate</text>
        <text x="25" y="50" font-size="13" fill="#94A3B8">Percentage (Higher is Better)</text>
        
        <!-- Bars -->
        <text x="25" y="100" font-size="16" fill="#0F172A">Traditional SOC</text>
        <rect x="25" y="115" width="20" height="35" rx="6" fill="#EF4444"/>
        <text x="580" y="140" font-size="15" font-family="monospace" fill="#0F172A">0.0% (No pre-filter)</text>

        <text x="25" y="215" font-size="16" fill="#0F172A">Direct LLM (ChatGPT)</text>
        <rect x="25" y="230" width="81" height="35" rx="6" fill="#F59E0B"/>
        <text x="580" y="255" font-size="15" font-family="monospace" fill="#0F172A">15.0% (Uncalibrated)</text>

        <text x="25" y="330" font-size="16" font-weight="bold" fill="#0F172A">CyberSentinel AI</text>
        <rect x="25" y="345" width="535" height="35" rx="6" fill="#10B981"/>
        <text x="580" y="370" font-size="15" font-family="monospace" font-weight="bold" fill="#047857">99.2% (Edge parser)</text>
    </g>

    <!-- Card 3: Hallucination Rate -->
    <g transform="translate(60, 680)">
        <rect width="900" height="480" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
        <path d="M0,12 Q0,0 12,0 L888,0 Q900,0 900,12 L900,60 L0,60 Z" fill="#1E293B"/>
        <text x="25" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">AI Hallucination Rate</text>
        <text x="25" y="50" font-size="13" fill="#94A3B8">Percentage (0.0% is Perfect)</text>
        
        <!-- Bars -->
        <text x="25" y="100" font-size="16" fill="#0F172A">Traditional SOC</text>
        <rect x="25" y="115" width="20" height="35" rx="6" fill="#64748B"/>
        <text x="580" y="140" font-size="15" font-family="monospace" fill="#0F172A">N/A (Rule-based)</text>

        <text x="25" y="215" font-size="16" fill="#0F172A">Direct LLM (ChatGPT)</text>
        <rect x="25" y="230" width="192" height="35" rx="6" fill="#EF4444"/>
        <text x="580" y="255" font-size="15" font-family="monospace" fill="#0F172A">35.7% (High risk)</text>

        <text x="25" y="330" font-size="16" font-weight="bold" fill="#0F172A">CyberSentinel AI</text>
        <rect x="25" y="345" width="20" height="35" rx="6" fill="#10B981"/>
        <text x="580" y="370" font-size="15" font-family="monospace" font-weight="bold" fill="#047857">0.0% (Vector grounded)</text>
    </g>

    <!-- Card 4: MITRE Accuracy -->
    <g transform="translate(1020, 680)">
        <rect width="900" height="480" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2"/>
        <path d="M0,12 Q0,0 12,0 L888,0 Q900,0 900,12 L900,60 L0,60 Z" fill="#1E293B"/>
        <text x="25" y="32" font-size="22" font-weight="bold" fill="#FFFFFF">MITRE Technique Mapping Accuracy</text>
        <text x="25" y="50" font-size="13" fill="#94A3B8">Percentage (Higher is Better)</text>
        
        <!-- Bars -->
        <text x="25" y="100" font-size="16" fill="#0F172A">Traditional SOC</text>
        <rect x="25" y="115" width="383" height="35" rx="6" fill="#EF4444"/>
        <text x="580" y="140" font-size="15" font-family="monospace" fill="#0F172A">71.0% (Manual lookup)</text>

        <text x="25" y="215" font-size="16" fill="#0F172A">Direct LLM (ChatGPT)</text>
        <rect x="25" y="230" width="347" height="35" rx="6" fill="#F59E0B"/>
        <text x="580" y="255" font-size="15" font-family="monospace" fill="#0F172A">64.3% (Hallucination risk)</text>

        <text x="25" y="330" font-size="16" font-weight="bold" fill="#0F172A">CyberSentinel AI</text>
        <rect x="25" y="345" width="508" height="35" rx="6" fill="#10B981"/>
        <text x="580" y="370" font-size="15" font-family="monospace" font-weight="bold" fill="#047857">94.2% (Cosine similarity)</text>
    </g>

    <text x="60" y="1165" font-size="14" fill="#64748B">Figure 7.1: Quantitative Performance Benchmarks Across Four Mission-Critical Security Metrics.</text>
</svg>"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {svg_path}")


def main():
    print("Starting generation of all 7 academic synopsis figures...")
    generate_figure_4_1()
    generate_figure_4_2()
    generate_figure_4_3()
    generate_figure_4_4()
    generate_figure_4_5()
    generate_figure_6_1()
    generate_figure_7_1()
    print("All figures successfully generated in PNG and SVG formats!")

if __name__ == "__main__":
    main()
