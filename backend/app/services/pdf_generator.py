import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from app.models.incident import Incident


def generate_incident_pdf(incident: Incident) -> io.BytesIO:
    """
    Generates a professional NIST SP 800-61 compliant Incident Triage Report in PDF format.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )
    styles = getSampleStyleSheet()

    # Custom CyberSentinel Dark-Themed Accents
    primary_color = colors.HexColor("#0f172a")  # Dark slate
    accent_blue = colors.HexColor("#2563eb")
    text_dark = colors.HexColor("#1e293b")
    text_muted = colors.HexColor("#64748b")

    # Severity Colors
    sev_colors = {
        "CRITICAL": colors.HexColor("#dc2626"),
        "HIGH": colors.HexColor("#ea580c"),
        "MEDIUM": colors.HexColor("#d97706"),
        "LOW": colors.HexColor("#16a34a"),
    }
    sev_color = sev_colors.get(incident.severity, colors.HexColor("#2563eb"))

    # Custom Typography Styles
    header_title_style = ParagraphStyle(
        "HeaderTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=primary_color,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=text_muted,
    )
    section_heading = ParagraphStyle(
        "SectionHeading",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=accent_blue,
        spaceBefore=10,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=text_dark,
    )

    story = []

    # 1. Header Banner
    story.append(Paragraph("CYBERSENTINEL AI // SOC INCIDENT REPORT", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"Incident #{incident.id}: {incident.title}", header_title_style))
    story.append(Paragraph(f"Standard: NIST SP 800-61 Computer Security Incident Handling | Classification: CONFIDENTIAL", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceBefore=2, spaceAfter=12))

    # 2. Key Forensic Metadata Table
    metadata_data = [
        [
            Paragraph("<b>Severity:</b>", body_style),
            Paragraph(f"<font color='{sev_color.hexval()}'><b>{incident.severity}</b> (Risk: {incident.risk_score}/100)</font>", body_style),
            Paragraph("<b>Incident Status:</b>", body_style),
            Paragraph(f"<b>{incident.status}</b>", body_style),
        ],
        [
            Paragraph("<b>Source Actor IP:</b>", body_style),
            Paragraph(f"<code>{incident.source_ip or 'Unspecified'}</code>", body_style),
            Paragraph("<b>Impacted Asset:</b>", body_style),
            Paragraph(f"<code>{incident.target_host or 'Internal Endpoint'}</code>", body_style),
        ],
        [
            Paragraph("<b>MITRE ATT&CK:</b>", body_style),
            Paragraph(f"<b>{incident.mitre_technique_id or 'T1110'}</b> - {incident.mitre_technique_name or 'Brute Force'}", body_style),
            Paragraph("<b>Tactic Category:</b>", body_style),
            Paragraph(f"{incident.attack_category}", body_style),
        ],
        [
            Paragraph("<b>AI Confidence:</b>", body_style),
            Paragraph(f"{int(incident.confidence_score * 100)}%", body_style),
            Paragraph("<b>Report Generated:</b>", body_style),
            Paragraph(f"{incident.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}", body_style),
        ],
    ]

    meta_table = Table(metadata_data, colWidths=[1.4 * inch, 2.3 * inch, 1.4 * inch, 2.3 * inch])
    meta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # 3. Executive Summary
    story.append(Paragraph("1. EXECUTIVE SUMMARY", section_heading))
    story.append(Paragraph(incident.summary, body_style))
    story.append(Spacer(1, 12))

    # 4. Forensic Narrative & Technical Correlation
    story.append(Paragraph("2. TECHNICAL DETAILS & LOG EVIDENCE CORRELATION", section_heading))
    tech_details_clean = incident.technical_details or "No raw telemetry logs logged."
    for paragraph_line in tech_details_clean.split("\n"):
        if paragraph_line.strip():
            story.append(Paragraph(paragraph_line, body_style))
            story.append(Spacer(1, 2))
    story.append(Spacer(1, 12))

    # 5. NIST Remediation Playbook
    story.append(Paragraph("3. RECOMMENDED REMEDIATION PLAYBOOK", section_heading))
    mitigation_clean = incident.recommended_mitigation or "Contain affected endpoint and enforce network segmentation."
    for playbook_step in mitigation_clean.split("\n"):
        if playbook_step.strip():
            story.append(Paragraph(playbook_step, body_style))
            story.append(Spacer(1, 2))
    story.append(Spacer(1, 16))

    # 6. Audit & Sign-off Block
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#94a3b8"), spaceBefore=4, spaceAfter=8))
    signoff_data = [
        [
            Paragraph("<b>Automated Triage:</b> CyberSentinel AI Engine v1.0", subtitle_style),
            Paragraph("<b>SOC Lead Reviewer:</b> ___________________________", subtitle_style),
        ]
    ]
    signoff_table = Table(signoff_data, colWidths=[3.7 * inch, 3.7 * inch])
    story.append(signoff_table)

    doc.build(story)
    buffer.seek(0)
    return buffer
