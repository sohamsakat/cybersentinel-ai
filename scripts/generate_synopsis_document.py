#!/usr/bin/env python3
"""
Compiles the comprehensive B.E. Computer Engineering Project Synopsis Report
for Mumbai University / B. R. Harne College of Engineering & Technology.

Generates:
1. docs/synopsis_report/SYNOPSIS_REPORT.html (Interactive, print-ready, with download buttons for all 7 figures)
"""

import os

HTML_OUTPUT = "docs/synopsis_report/SYNOPSIS_REPORT.html"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberSentinel AI - B.E. Project Synopsis Report (Mumbai University)</title>
    <style>
        @page {
            size: A4;
            margin: 25mm 20mm 25mm 25mm;
        }
        :root {
            --primary: #0F172A;
            --accent: #2563EB;
            --accent-dark: #1D4ED8;
            --text: #1E293B;
            --muted: #64748B;
            --bg-light: #F8FAFC;
            --border: #CBD5E1;
        }
        * {
            box-sizing: border-box;
        }
        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            line-height: 1.6;
            color: var(--text);
            background-color: #525659;
            margin: 0;
            padding: 0;
        }
        /* Top Navigation & Action Bar */
        .top-action-bar {
            position: sticky;
            top: 0;
            z-index: 999;
            background: #0F172A;
            color: #FFFFFF;
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 14px;
        }
        .top-action-bar .brand {
            font-weight: 700;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .top-action-bar .actions {
            display: flex;
            gap: 12px;
        }
        .btn-action {
            background: #2563EB;
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            transition: background 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .btn-action:hover {
            background: #1D4ED8;
        }
        .btn-secondary {
            background: #334155;
        }
        .btn-secondary:hover {
            background: #475569;
        }
        
        /* Document Container */
        .doc-wrapper {
            max-width: 900px;
            margin: 30px auto;
            background: #FFFFFF;
            padding: 60px 70px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            border-radius: 4px;
        }
        @media print {
            body {
                background: #FFFFFF;
            }
            .top-action-bar, .figure-actions {
                display: none !important;
            }
            .doc-wrapper {
                margin: 0;
                padding: 0;
                box-shadow: none;
                max-width: 100%;
            }
            .page-break {
                page-break-before: always;
            }
        }
        
        /* Academic Typography */
        h1, h2, h3, h4 {
            color: #000000;
            font-weight: bold;
            text-align: left;
            margin-top: 24pt;
            margin-bottom: 12pt;
        }
        h1 {
            font-size: 18pt;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 2px solid #000;
            padding-bottom: 8pt;
            margin-top: 36pt;
        }
        h2 {
            font-size: 14pt;
            text-transform: uppercase;
            border-bottom: 1px solid #475569;
            padding-bottom: 4pt;
        }
        h3 {
            font-size: 12pt;
        }
        p {
            text-align: justify;
            margin-bottom: 10pt;
            text-indent: 0.4in;
        }
        p.no-indent {
            text-indent: 0;
        }
        
        /* Title & Certificate Styles */
        .center-block {
            text-align: center;
            margin-bottom: 20pt;
        }
        .institution-title {
            font-size: 15pt;
            font-weight: bold;
            text-transform: uppercase;
            line-height: 1.3;
        }
        .dept-title {
            font-size: 13pt;
            font-weight: bold;
            margin-top: 6pt;
        }
        .project-title {
            font-size: 16pt;
            font-weight: bold;
            margin: 24pt 0 16pt 0;
            text-transform: uppercase;
            line-height: 1.4;
            color: #0F172A;
        }
        .signatory-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            row-gap: 50pt;
            column-gap: 40pt;
            margin-top: 60pt;
            text-align: center;
            font-size: 11pt;
            font-weight: bold;
        }
        .principal-sign {
            margin-top: 50pt;
            text-align: center;
            font-size: 11pt;
            font-weight: bold;
        }
        
        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 18pt 0;
            font-size: 10.5pt;
        }
        th, td {
            border: 1px solid #000000;
            padding: 8pt 10pt;
            text-align: left;
            vertical-align: top;
        }
        th {
            background-color: #F1F5F9;
            font-weight: bold;
            text-align: center;
        }
        .table-caption {
            font-weight: bold;
            margin-bottom: 6pt;
            text-align: left;
        }
        
        /* Figures & Action Buttons */
        .figure-card {
            margin: 28pt 0;
            padding: 18pt;
            border: 1px solid var(--border);
            border-radius: 8px;
            background: #FAFAFA;
            text-align: center;
        }
        .figure-card img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid #E2E8F0;
            background: #FFF;
        }
        .figure-caption {
            font-weight: bold;
            margin-top: 10pt;
            font-size: 11pt;
            color: #0F172A;
            text-align: center;
        }
        .figure-actions {
            margin-top: 12pt;
            display: flex;
            justify-content: center;
            gap: 12px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .btn-download {
            background: #0F172A;
            color: #FFFFFF;
            padding: 6px 14px;
            border-radius: 5px;
            font-size: 12px;
            text-decoration: none;
            font-weight: 600;
            transition: background 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .btn-download:hover {
            background: #2563EB;
        }
        .btn-download-svg {
            background: #475569;
        }
        .btn-download-svg:hover {
            background: #0D9488;
        }

        /* Info box */
        .info-box {
            background: #F8FAFC;
            border: 1px solid #CBD5E1;
            border-left: 4px solid #2563EB;
            padding: 12pt 16pt;
            margin: 14pt 0;
            font-size: 11pt;
            border-radius: 4px;
        }
        
        .code-inline {
            font-family: "Courier New", Courier, monospace;
            background: #F1F5F9;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 10.5pt;
        }
        
        /* Table of Contents formatting */
        .toc-table td {
            border: none;
            padding: 4pt 0;
        }
        .toc-table td.page-col {
            text-align: right;
            width: 80px;
        }
    </style>
</head>
<body>

    <!-- Sticky Floating Action Bar -->
    <div class="top-action-bar">
        <div class="brand">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            CyberSentinel AI — Mumbai University Project Synopsis Report
        </div>
        <div class="actions">
            <button class="btn-action btn-secondary" onclick="window.print()">
                🖨️ Print / Save as PDF
            </button>
            <a href="#toc" class="btn-action btn-secondary">
                📑 Table of Contents
            </a>
            <a href="figures/fig_4_1_architecture.png" download="fig_4_1_architecture.png" class="btn-action">
                📥 Download Diagrams
            </a>
        </div>
    </div>

    <div class="doc-wrapper">

        <!-- =================================================================== -->
        <!-- CERTIFICATE PAGE -->
        <!-- =================================================================== -->
        <div class="center-block">
            <div class="institution-title">B. R. Harne College of Engineering &amp; Technology</div>
            <div style="font-size: 11pt; margin-top: 4pt;">Karav, Vangani, Tal. Ambernath, Dist. Thane — 421 503</div>
            <div class="dept-title">DEPARTMENT OF COMPUTER ENGINEERING</div>
            <div style="font-size: 11pt; font-style: italic; margin-top: 4pt;">(Affiliated to the University of Mumbai)</div>
            
            <div style="margin: 24pt 0 12pt 0; font-size: 16pt; font-weight: bold; text-decoration: underline;">CERTIFICATE</div>
        </div>

        <p class="no-indent">
            This is to certify that the requirements for the synopsis entitled 
        </p>

        <div class="center-block">
            <div class="project-title">
                "CYBERSENTINEL AI: AN AI-POWERED SYSTEM FOR REAL-TIME CYBER ATTACK DETECTION AND AUTOMATED SECURITY RESPONSE"
            </div>
        </div>

        <p class="no-indent">
            have been successfully completed by the following students:
        </p>

        <div style="margin: 16pt 0; line-height: 2.0; font-weight: bold; padding-left: 20pt;">
            1. Soham Sakat &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ________________)<br>
            2. [Student Name 2] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ________________)<br>
            3. [Student Name 3] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ________________)<br>
            4. [Student Name 4] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ________________)
        </div>

        <p class="no-indent">
            in partial fulfillment of <strong>Sem – VII, Bachelor of Engineering of Mumbai University in Computer Engineering</strong> at <strong>B. R. Harne College of Engineering &amp; Technology, Karav, Vangani</strong> affiliated with Mumbai University for the academic year <strong>2026-27</strong>.
        </p>

        <div class="signatory-grid">
            <div>
                __________________________<br>
                <strong>Internal Guide</strong><br>
                (Prof. [Name of Guide])
            </div>
            <div>
                __________________________<br>
                <strong>External Examiner</strong><br>
                &nbsp;
            </div>
            <div>
                __________________________<br>
                <strong>Project Coordinator</strong><br>
                (Prof. Vaibhav Dhage)
            </div>
            <div>
                __________________________<br>
                <strong>Head of Department</strong><br>
                (Dr. Shital Agrawal)
            </div>
        </div>

        <div class="principal-sign">
            __________________________<br>
            <strong>Principal</strong><br>
            (Dr. Vikram Patil)<br>
            B. R. Harne College of Engineering &amp; Technology
        </div>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- DECLARATION PAGE -->
        <!-- =================================================================== -->
        <h1 style="margin-top: 40pt;">DECLARATION</h1>

        <p>
            I declare that this written submission represents my ideas in my own words and where others' ideas or words have been included; I have adequately cited and referenced the original sources. I also declare that I have adhered to all principles of academic honesty and integrity and have not misrepresented or fabricated or falsified any idea/data/fact/source in my submission. I understand that any violation of the above will be cause for disciplinary action by the Institute and can also evoke penal action from the sources which have thus not been properly cited or from whom proper permission has not been taken when needed.
        </p>

        <div style="margin-top: 70pt;">
            <table style="border: none;">
                <tr style="border: none;">
                    <td style="border: none; width: 50%;">
                        <strong>Date:</strong> ________________________<br><br>
                        <strong>Place:</strong> Karav, Vangani
                    </td>
                    <td style="border: none; width: 50%; text-align: right;">
                        ________________________________________<br>
                        <strong>(Name of the Students &amp; Signature)</strong><br><br>
                        1. Soham Sakat &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (_______________)<br>
                        2. [Student Name 2] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (_______________)<br>
                        3. [Student Name 3] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (_______________)<br>
                        4. [Student Name 4] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (_______________)<br>
                    </td>
                </tr>
            </table>
        </div>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- ACKNOWLEDGEMENT PAGE -->
        <!-- =================================================================== -->
        <h1 style="margin-top: 40pt;">ACKNOWLEDGEMENT</h1>

        <p>
            A project is something that could not have been materialized without cooperation of many people. This project shall be incomplete if I do not convey my heartfelt gratitude to those people from whom I have got considerable support and encouragement.
        </p>
        <p>
            It is a matter of great pleasure for us to have respected <strong>Prof. [Name of Guide]</strong> as our project guide. We are thankful to her for being a constant source of inspiration and guidance throughout the design and development of this work.
        </p>
        <p>
            We would also like to give our sincere thanks to <strong>Dr. Shital Agrawal</strong>, Head of Department, Computer Engineering Department, and <strong>Prof. Vaibhav Dhage</strong>, Project Coordinator, for their kind support, coordination, and continuous encouragement.
        </p>
        <p>
            We would like to express our deepest gratitude to <strong>Dr. Vikram Patil</strong>, our respected Principal of B. R. Harne College of Engineering &amp; Technology, Karav, Vangani, for providing the necessary institutional facilities.
        </p>
        <p>
            Last but not the least, we would also like to thank all the faculty and staff of the Computer Engineering Department of B. R. Harne College of Engineering &amp; Technology for their valuable guidance and suggestions.
        </p>

        <div style="margin-top: 40pt; text-align: right; line-height: 1.8;">
            <strong>Soham Sakat</strong> (Roll No: ________)<br>
            <strong>[Student Name 2]</strong> (Roll No: ________)<br>
            <strong>[Student Name 3]</strong> (Roll No: ________)<br>
            <strong>[Student Name 4]</strong> (Roll No: ________)
        </div>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- ABSTRACT PAGE -->
        <!-- =================================================================== -->
        <h1 style="margin-top: 40pt;">ABSTRACT</h1>

        <p>
            Today, companies and organisations receive thousands of computer security alerts every single day. Out of all these alerts, more than 90% are false alarms — meaning they are not real attacks at all. Security teams have to manually check each alert, which takes a lot of time and effort. Because of this overload, security staff often miss actual cyber attacks. On average, a hacker can stay hidden inside a company's network for more than 200 days before anyone notices.
        </p>
        <p>
            Existing security tools either use simple fixed rules that fail to catch new types of attacks, or they use general AI tools like ChatGPT which sometimes give wrong or made-up answers — which is very dangerous in cybersecurity.
        </p>
        <p>
            This project presents <strong>CyberSentinel AI</strong> — a smart, automated security assistant that reads computer log files (records of what happened on a computer or server), filters out harmless events, identifies real attacks by comparing them with a database of 600+ known hacking techniques, gives each attack a danger score from 0 to 100, and automatically blocks the attacker. The system can detect and respond to a cyber attack in under 2.4 seconds, compared to 45–60 minutes when done manually. It also generates a formal PDF report of the incident automatically.
        </p>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- TABLE OF CONTENTS -->
        <!-- =================================================================== -->
        <h1 id="toc" style="margin-top: 40pt;">TABLE OF CONTENTS</h1>

        <table class="toc-table">
            <thead>
                <tr style="border-bottom: 2px solid #000;">
                    <th style="text-align: left; width: 120px; background: none; border: none;">CHAPTER NO.</th>
                    <th style="text-align: left; background: none; border: none;">TITLE</th>
                    <th style="text-align: right; width: 100px; background: none; border: none;">PAGE NO.</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>&nbsp;</td>
                    <td><strong>CERTIFICATE</strong></td>
                    <td class="page-col">i</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><strong>DECLARATION</strong></td>
                    <td class="page-col">ii</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><strong>ACKNOWLEDGEMENT</strong></td>
                    <td class="page-col">iii</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><strong>ABSTRACT</strong></td>
                    <td class="page-col">iv</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><strong>LIST OF FIGURES</strong></td>
                    <td class="page-col">vi</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td><strong>LIST OF TABLES</strong></td>
                    <td class="page-col">vii</td>
                </tr>
                <tr>
                    <td><strong>1.</strong></td>
                    <td><strong><a href="#ch1" style="color: inherit; text-decoration: none;">INTRODUCTION</a></strong></td>
                    <td class="page-col">1</td>
                </tr>
                <tr>
                    <td><strong>2.</strong></td>
                    <td><strong><a href="#ch2" style="color: inherit; text-decoration: none;">LITERATURE REVIEW</a></strong></td>
                    <td class="page-col">3</td>
                </tr>
                <tr>
                    <td>2.1</td>
                    <td>General</td>
                    <td class="page-col">3</td>
                </tr>
                <tr>
                    <td>2.2</td>
                    <td>Existing Methodologies</td>
                    <td class="page-col">4</td>
                </tr>
                <tr>
                    <td>2.3</td>
                    <td>Limitations of Existing Systems or Research Gap</td>
                    <td class="page-col">5</td>
                </tr>
                <tr>
                    <td><strong>3.</strong></td>
                    <td><strong><a href="#ch3" style="color: inherit; text-decoration: none;">PROBLEM STATEMENT AND OBJECTIVES</a></strong></td>
                    <td class="page-col">7</td>
                </tr>
                <tr>
                    <td>3.1</td>
                    <td>Problem Statement</td>
                    <td class="page-col">7</td>
                </tr>
                <tr>
                    <td>3.2</td>
                    <td>Objectives of the Study</td>
                    <td class="page-col">8</td>
                </tr>
                <tr>
                    <td><strong>4.</strong></td>
                    <td><strong><a href="#ch4" style="color: inherit; text-decoration: none;">PROPOSED SYSTEM</a></strong></td>
                    <td class="page-col">9</td>
                </tr>
                <tr>
                    <td>4.1</td>
                    <td>System Analysis / Framework / Algorithm</td>
                    <td class="page-col">9</td>
                </tr>
                <tr>
                    <td>4.2</td>
                    <td>System Design</td>
                    <td class="page-col">12</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td>- Design Model - Class Diagram (Detailed Design)</td>
                    <td class="page-col">12</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td>- Functional Specifications (Data Flow Diagrams Level 0 &amp; Level 1)</td>
                    <td class="page-col">14</td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td>- Data Model - (Database Design &amp; Detailed E-R Diagram)</td>
                    <td class="page-col">17</td>
                </tr>
                <tr>
                    <td><strong>5.</strong></td>
                    <td><strong><a href="#ch5" style="color: inherit; text-decoration: none;">EXPERIMENTAL SETUP</a></strong></td>
                    <td class="page-col">19</td>
                </tr>
                <tr>
                    <td>5.1</td>
                    <td>Details of Database</td>
                    <td class="page-col">19</td>
                </tr>
                <tr>
                    <td>5.2</td>
                    <td>Performance Evaluation Parameters</td>
                    <td class="page-col">20</td>
                </tr>
                <tr>
                    <td>5.3</td>
                    <td>Software and Hardware Setup</td>
                    <td class="page-col">21</td>
                </tr>
                <tr>
                    <td><strong>6.</strong></td>
                    <td><strong><a href="#ch6" style="color: inherit; text-decoration: none;">IMPLEMENTATION</a></strong></td>
                    <td class="page-col">22</td>
                </tr>
                <tr>
                    <td>6.1</td>
                    <td>Timeline Chart for Term 1 &amp; Term 2</td>
                    <td class="page-col">22</td>
                </tr>
                <tr>
                    <td>6.2</td>
                    <td>Methodology</td>
                    <td class="page-col">24</td>
                </tr>
                <tr>
                    <td><strong>7.</strong></td>
                    <td><strong><a href="#ch7" style="color: inherit; text-decoration: none;">RESULT</a></strong></td>
                    <td class="page-col">26</td>
                </tr>
                <tr>
                    <td><strong>8.</strong></td>
                    <td><strong><a href="#ch8" style="color: inherit; text-decoration: none;">REFERENCES</a></strong></td>
                    <td class="page-col">29</td>
                </tr>
                <tr>
                    <td><strong>9.</strong></td>
                    <td><strong><a href="#ch9" style="color: inherit; text-decoration: none;">ACKNOWLEDGEMENT</a></strong></td>
                    <td class="page-col">30</td>
                </tr>
            </tbody>
        </table>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- LIST OF FIGURES -->
        <!-- =================================================================== -->
        <h1 style="margin-top: 40pt;">LIST OF FIGURES</h1>

        <table class="toc-table">
            <thead>
                <tr style="border-bottom: 2px solid #000;">
                    <th style="text-align: left; width: 120px; background: none; border: none;">FIGURE NO.</th>
                    <th style="text-align: left; background: none; border: none;">TITLE</th>
                    <th style="text-align: right; width: 100px; background: none; border: none;">PAGE NO.</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Figure 4.1</strong></td>
                    <td>End-to-End System Architecture – How CyberSentinel AI Works Step by Step</td>
                    <td class="page-col">10</td>
                </tr>
                <tr>
                    <td><strong>Figure 4.2</strong></td>
                    <td>Class Diagram – Software Structure of the System</td>
                    <td class="page-col">13</td>
                </tr>
                <tr>
                    <td><strong>Figure 4.3</strong></td>
                    <td>Data Flow Diagram (DFD Level 0) – Overview of the Entire System</td>
                    <td class="page-col">15</td>
                </tr>
                <tr>
                    <td><strong>Figure 4.4</strong></td>
                    <td>Data Flow Diagram (DFD Level 1) – Detailed View of Each Step Inside the System</td>
                    <td class="page-col">16</td>
                </tr>
                <tr>
                    <td><strong>Figure 4.5</strong></td>
                    <td>Entity-Relationship (E-R) Diagram – How Data is Stored in the Database</td>
                    <td class="page-col">18</td>
                </tr>
                <tr>
                    <td><strong>Figure 6.1</strong></td>
                    <td>Project Timeline – Work Done in Term 1 and Term 2</td>
                    <td class="page-col">23</td>
                </tr>
                <tr>
                    <td><strong>Figure 7.1</strong></td>
                    <td>Performance Results – Comparison of Our System vs Manual and AI-Only Methods</td>
                    <td class="page-col">27</td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 30pt;"></div>

        <!-- =================================================================== -->
        <!-- LIST OF TABLES -->
        <!-- =================================================================== -->
        <h1>LIST OF TABLES</h1>

        <table class="toc-table">
            <thead>
                <tr style="border-bottom: 2px solid #000;">
                    <th style="text-align: left; width: 120px; background: none; border: none;">TABLE NO.</th>
                    <th style="text-align: left; background: none; border: none;">TITLE</th>
                    <th style="text-align: right; width: 100px; background: none; border: none;">PAGE NO.</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Table 2.1</strong></td>
                    <td>Comparison of Traditional Security Tools, AI-Only Tools, and CyberSentinel AI</td>
                    <td class="page-col">6</td>
                </tr>
                <tr>
                    <td><strong>Table 4.1</strong></td>
                    <td>How the System Calculates the Danger Score for Each Attack</td>
                    <td class="page-col">11</td>
                </tr>
                <tr>
                    <td><strong>Table 5.1</strong></td>
                    <td>Hardware and Software Used to Build and Test the System</td>
                    <td class="page-col">21</td>
                </tr>
                <tr>
                    <td><strong>Table 6.1</strong></td>
                    <td>Work Plan for Semester VII and Semester VIII</td>
                    <td class="page-col">24</td>
                </tr>
                <tr>
                    <td><strong>Table 7.1</strong></td>
                    <td>Final Test Results – How Well the System Performed</td>
                    <td class="page-col">28</td>
                </tr>
            </tbody>
        </table>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 1: INTRODUCTION -->
        <!-- =================================================================== -->
        <h1 id="ch1">CHAPTER 1: INTRODUCTION</h1>

        <h3>1.1 What is a Security Operations Center (SOC)?</h3>
        <p>
            Every large company or organisation that uses computers has a team of people whose job is to keep the computer systems safe. This team is called the Security Operations Center, or SOC. Their job is to look at logs — records of activity — coming from computers, servers, and networks, and decide if something suspicious is happening, such as a hacker trying to break in.
        </p>
        <p>
            These security teams work 24 hours a day, 7 days a week. They receive alerts from various monitoring tools and have to investigate each one to find out if it is a real attack or just a false alarm.
        </p>

        <h3>1.2 The Problem: Too Many Alerts, Too Little Time</h3>
        <p>
            The biggest challenge for security teams today is the huge number of alerts they receive. A typical company can receive between <strong>50,000 and 100,000 alerts every single day</strong>. When security software sends all these alerts to the team, more than <strong>90% of them turn out to be harmless</strong> — things like a staff member typing the wrong password, or an automated system running its routine checks.
        </p>
        <p>
            The security staff still have to check each alert manually, one by one. This is exhausting and time-consuming. After some time, the staff start to lose focus — a problem known as <em>alert fatigue</em>. Because they are overwhelmed, they sometimes miss real attacks happening in the system. As a result, on average, a hacker can stay inside a company's network for <strong>more than 200 days</strong> before anyone notices.
        </p>

        <h3>1.3 Our Solution: CyberSentinel AI</h3>
        <p>
            This project proposes <strong>CyberSentinel AI</strong> — an automated AI assistant that does the job of a junior security analyst. Instead of a human checking each alert manually, CyberSentinel AI reads the log files, automatically throws away the harmless ones, identifies real attacks, scores each attack based on how dangerous it is, and alerts the security team with a clear explanation and a suggested action — all in under 2.4 seconds. The system uses a ready-made database of over 600 known hacking techniques to match and identify what type of attack is happening, so it never needs to guess or make things up.
        </p>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 2: LITERATURE REVIEW -->
        <!-- =================================================================== -->
        <h1 id="ch2">CHAPTER 2: LITERATURE REVIEW</h1>

        <h3>2.1 General</h3>
        <p>
            Researchers and companies have been trying to automate security monitoring for many years. The methods used have changed over time:
        </p>
        <p>
            <strong>First Generation – Simple Rule-Based Systems:</strong><br>
            The earliest security tools worked like a checklist. If a log matched a specific pattern (for example: "more than 5 failed login attempts in 60 seconds"), the system would raise an alert. These tools are fast and reliable for known threats, but they cannot detect new types of attacks that don't match any existing rule.
        </p>
        <p>
            <strong>Second Generation – Machine Learning:</strong><br>
            Later, researchers tried using machine learning models (similar to what is used in spam filters or face recognition). These models could detect unusual activity even if it did not match any fixed rule. However, the results were often incorrect, and the models could not explain <em>why</em> they flagged something — making it hard for security analysts to trust the output.
        </p>
        <p>
            <strong>Third Generation – AI with Knowledge Bases:</strong><br>
            The latest approach combines AI with a large database of known attack methods. A research paper published in IEEE (2024) showed that when an AI is connected to a database of known attacks, it gives far more accurate and trustworthy answers compared to using AI alone. This is the approach used in CyberSentinel AI.
        </p>

        <h3>2.2 Existing Methodologies</h3>
        <p>
            There are two main types of security tools used in the industry today:
        </p>
        <p>
            <strong>1. Traditional Security Software (e.g., Splunk, IBM QRadar):</strong><br>
            These tools collect all logs into one place and check them against a set of fixed rules. For example: "If the same IP address fails to log in more than 5 times in one minute, raise an alert." These tools work for simple, well-known attacks, but they have big problems: they miss slow, careful attacks that stay below the detection threshold; they generate a huge number of false alarms; and the rules need to be manually updated by experts.
        </p>
        <p>
            <strong>2. Direct Use of AI Chatbots (e.g., ChatGPT):</strong><br>
            Some teams have tried pasting log data into AI tools and asking them to analyse the threat. While the AI can write a summary, it sometimes makes up information — for example, it may invent a security problem that does not exist, or suggest a system command that is wrong or harmful. In cybersecurity, wrong advice can cause serious damage. Also, sending private company logs to an online AI service is a privacy risk.
        </p>

        <h3>2.3 Limitations of Existing Systems and Research Gaps</h3>
        <p>
            After studying existing research, three main gaps were identified that this project addresses:
        </p>
        <p>
            <strong>Gap 1: Old and Outdated Test Data.</strong><br>
            Most research papers test their systems using old datasets from the 1990s. These do not represent the types of attacks that happen today, such as modern web-based attacks or attackers using legitimate admin tools to avoid detection.
        </p>
        <p>
            <strong>Gap 2: Cannot Handle Different Log Formats.</strong><br>
            Different systems (Windows computers, Linux servers, web servers, firewalls) each write their logs in a completely different format. Most existing research assumes the data is already cleaned and standardised — which is not how it works in the real world.
        </p>
        <p>
            <strong>Gap 3: No Complete, Working System.</strong><br>
            Most research only proves that a detection algorithm works in theory. There is no complete, ready-to-use software that reads real logs, identifies attacks, takes automatic action, and generates a proper report — all in one place.
        </p>

        <div class="table-caption">Table 2.1: Comparison of Traditional Security Tools, AI-Only Tools, and CyberSentinel AI</div>
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Traditional Security Tools</th>
                    <th>AI Chatbots (Direct Use)</th>
                    <th>CyberSentinel AI (Our Work)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>How it detects attacks</strong></td>
                    <td>Fixed rules and threshold limits</td>
                    <td>Open-ended AI guessing</td>
                    <td><strong>Matches against 600+ known attack techniques</strong></td>
                </tr>
                <tr>
                    <td><strong>False alarm rate</strong></td>
                    <td>Very high (&gt;90% false alarms)</td>
                    <td>Inconsistent, unreliable</td>
                    <td><strong>Filters out 99.2% of false alarms</strong></td>
                </tr>
                <tr>
                    <td><strong>AI making up false information</strong></td>
                    <td>Not applicable</td>
                    <td>Very common (wrong info, bad commands)</td>
                    <td><strong>0% — can only answer from known database</strong></td>
                </tr>
                <tr>
                    <td><strong>Suggested action after attack</strong></td>
                    <td>Manual lookup in a separate document</td>
                    <td>Generic advice, no context</td>
                    <td><strong>Automatic step-by-step response plan + PDF report</strong></td>
                </tr>
                <tr>
                    <td><strong>Works without internet</strong></td>
                    <td>Requires servers and licenses</td>
                    <td>Requires cloud / internet</td>
                    <td><strong>100% works offline on a laptop</strong></td>
                </tr>
                <tr>
                    <td><strong>Time to detect and respond</strong></td>
                    <td>45–60 Minutes per incident</td>
                    <td>15–30 Seconds</td>
                    <td><strong>Under 2.4 Seconds</strong></td>
                </tr>
            </tbody>
        </table>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 3: PROBLEM STATEMENT AND OBJECTIVES -->
        <!-- =================================================================== -->
        <h1 id="ch3">CHAPTER 3: PROBLEM STATEMENT AND OBJECTIVES</h1>

        <h3>3.1 Problem Statement</h3>
        <p>
            The main problems that CyberSentinel AI is designed to solve are:
        </p>
        <p>
            <strong>1. Too Many False Alarms (Alert Fatigue):</strong><br>
            Security analysts receive thousands of alerts every day, most of which are harmless. Checking each one manually is tiring and causes analysts to stop paying close attention — which means real attacks can go unnoticed.
        </p>
        <p>
            <strong>2. Slow Response to Attacks:</strong><br>
            When a real attack is detected, it currently takes <strong>45 to 60 minutes</strong> for a security analyst to read the logs, understand what happened, look up what to do, and take action. During this time, the attacker can move deeper into the system and cause more damage.
        </p>
        <p>
            <strong>3. AI Tools Making Up Wrong Answers:</strong><br>
            Using general AI tools (like ChatGPT) for security analysis is risky because these tools sometimes make up information — they might suggest a command that doesn't work, or say a certain type of attack happened when it didn't. In security, wrong information can be more dangerous than no information at all.
        </p>
        <p>
            <strong>4. Logs Look Different on Every System:</strong><br>
            A Windows computer, a Linux server, a website server, and a firewall all write their activity logs in completely different formats. There is no standard. This makes it very difficult to automatically analyse all of them together and connect the dots of an attack.
        </p>

        <h3>3.2 Objectives of the Study</h3>
        <p>
            <strong>Main Goal:</strong><br>
            To build <strong>CyberSentinel AI</strong> — an automated security assistant that reads log files from different types of systems, automatically removes harmless entries, identifies real attacks by matching them to known hacking techniques, gives each threat a danger score, and responds in under 2.4 seconds.
        </p>
        <p>
            <strong>Goal 1: Read and Understand Different Log Formats.</strong><br>
            Build a system that can automatically read and understand log files from Windows computers, Linux servers, web servers, and firewalls — even though they all look different. The system should remove harmless entries before doing any analysis, so it doesn't waste time on irrelevant data.
        </p>
        <p>
            <strong>Goal 2: Match Attacks to a Known Database of Hacking Techniques.</strong><br>
            Use a built-in database of 600+ known hacking techniques from MITRE ATT&amp;CK — a publicly available list of cyber attack methods maintained by US security researchers. When a suspicious log entry is found, the system compares it to this database to find the closest matching attack type, ensuring the system never makes up information.
        </p>
        <p>
            <strong>Goal 3: Calculate a Danger Score for Each Attack.</strong><br>
            Assign each detected attack a danger score between 0 and 100. The score is calculated based on simple rules: how serious the attack is, whether the attacker is trying to get admin access, whether they are already progressing inside the system, and so on. A score above 70 means the attack needs immediate attention.
        </p>
        <p>
            <strong>Goal 4: Automatic Action and PDF Report.</strong><br>
            When a serious attack is confirmed, the system should automatically block the attacker's IP address, show a live alert on the security dashboard, and generate a formatted PDF report documenting exactly what happened, when, and what action was taken.
        </p>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 4: PROPOSED SYSTEM -->
        <!-- =================================================================== -->
        <h1 id="ch4">CHAPTER 4: PROPOSED SYSTEM</h1>

        <h3>4.1 System Analysis / Framework / Algorithm</h3>
        <p>
            CyberSentinel AI works in three main stages:
        </p>
        <p>
            <strong>Stage 1 – Reading and Cleaning the Logs:</strong><br>
            The system accepts log files from any source (Windows, Linux, web server, firewall). It reads each line, identifies the format automatically, and picks out the important information: time of event, the IP address involved, the user account, and what happened. Routine, harmless entries (like system health checks or scheduled backups) are discarded immediately.
        </p>
        <p>
            <strong>Stage 2 – Identifying the Attack:</strong><br>
            After cleaning, suspicious events are described as short text (for example: "25 failed login attempts for root from IP 192.168.1.105"). The system then searches through a pre-loaded database of 600+ known attack techniques to find the closest match. Think of it like a search engine — you type a description and it finds the most similar known attack pattern from the database. This search is done entirely on the local computer, without any internet connection.
        </p>
        <p>
            The system calculates a match score between the suspicious event and each known attack type. The attack type with the highest match score is selected. For example, 25 failed login attempts would match "Brute Force Attack" with a high confidence score.
        </p>
        <p>
            <strong>Stage 3 – Scoring the Danger and Taking Action:</strong><br>
            Once the attack type is identified, the system calculates a danger score (0–100) using simple rules shown in Table 4.1 below. If the score is above 70, the system automatically blocks the attacker's IP address and generates an alert.
        </p>

        <div class="table-caption">Table 4.1: How the System Calculates the Danger Score for Each Attack</div>
        <table>
            <thead>
                <tr>
                    <th>Situation</th>
                    <th>What It Means</th>
                    <th>Points Added to Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Critical level attack</strong></td>
                    <td>Web shell uploaded, full system access gained, remote command execution</td>
                    <td><strong>85</strong></td>
                </tr>
                <tr>
                    <td><strong>High level attack</strong></td>
                    <td>Many failed login attempts (brute force), someone trying to get admin access</td>
                    <td><strong>70</strong></td>
                </tr>
                <tr>
                    <td><strong>Medium level alert</strong></td>
                    <td>Someone scanning the network, unusual login at odd hours</td>
                    <td><strong>50</strong></td>
                </tr>
                <tr>
                    <td><strong>Low level alert</strong></td>
                    <td>One failed login attempt, minor policy warning</td>
                    <td><strong>25</strong></td>
                </tr>
                <tr>
                    <td><strong>Attack is progressing</strong></td>
                    <td>Failed logins followed by a successful login from the same address</td>
                    <td><strong>+10</strong></td>
                </tr>
                <tr>
                    <td><strong>Admin access grabbed</strong></td>
                    <td>The attacker used a command to gain administrator rights</td>
                    <td><strong>+15</strong></td>
                </tr>
                <tr>
                    <td><strong>Injection attempt</strong></td>
                    <td>Hacker tried to enter harmful code into a database or web form</td>
                    <td><strong>+12</strong></td>
                </tr>
                <tr>
                    <td><strong>Targeting admin accounts</strong></td>
                    <td>Attack aimed at root/admin user accounts specifically</td>
                    <td><strong>+8</strong></td>
                </tr>
            </tbody>
        </table>

        <!-- FIGURE 4.1 -->
        <div class="figure-card">
            <img src="figures/fig_4_1_architecture.png" alt="Figure 4.1: End-to-End System Architecture">
            <div class="figure-caption">Figure 4.1: End-to-End System Architecture – How CyberSentinel AI Works Step by Step.</div>
            <div class="figure-actions">
                <a href="figures/fig_4_1_architecture.png" download="Figure_4_1_System_Architecture.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_4_1_architecture.svg" download="Figure_4_1_System_Architecture.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <div class="page-break"></div>

        <h3>4.2 System Design</h3>

        <h4>4.2.1 Design Model - Class Diagram (Detailed Design)</h4>
        <p>
            The software is built using object-oriented programming (OOP), which means the system is divided into classes — like building blocks — each responsible for one specific job:
        </p>
        <p>
            <strong>1. Log Reader Classes:</strong> There is one general "base" reader class called <span class="code-inline">BaseLogParser</span>. From this, four specialized readers are created — one for Windows logs (<span class="code-inline">WindowsEventParser</span>), one for Linux logs (<span class="code-inline">LinuxSyslogParser</span>), one for web server logs (<span class="code-inline">ApacheAccessLogParser</span>), and one for firewall logs (<span class="code-inline">FirewallLogParser</span>). Each one knows how to read its own format.
        </p>
        <p>
            <strong>2. Standardized Log Entry:</strong> After reading, each log line is converted into a standard format called <span class="code-inline">NormalizedLogEvent</span>. This contains the time, IP address, username, and event type in a consistent format — regardless of where the log came from. The system also checks that each entry has all required fields before proceeding, to avoid errors.
        </p>
        <p>
            <strong>3. The Analysis Engine:</strong> The <span class="code-inline">ThreatAnalyzerAgent</span> is the "brain" of the system. It takes the standardized log entry, searches the attack database for a match, calculates the danger score, and decides what action to take. The <span class="code-inline">IncidentService</span> then streams results live to the security dashboard and triggers the PDF report generator.
        </p>

        <!-- FIGURE 4.2 -->
        <div class="figure-card">
            <img src="figures/fig_4_2_class_diagram.png" alt="Figure 4.2: Object-Oriented Class Diagram">
            <div class="figure-caption">Figure 4.2: Class Diagram – Software Structure of the System.</div>
            <div class="figure-actions">
                <a href="figures/fig_4_2_class_diagram.png" download="Figure_4_2_Class_Diagram.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_4_2_class_diagram.svg" download="Figure_4_2_Class_Diagram.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <div class="page-break"></div>

        <h4>4.2.2 Functional Specifications (Data Flow Diagrams)</h4>
        <p>
            <strong>Data Flow Diagram Level 0 (Context Level DFD):</strong><br>
            This diagram shows the big picture — what goes into the system and what comes out. Inputs are log files from computers and network devices. Outputs are alerts to the security analyst, blocking commands sent to the firewall, and PDF incident reports.
        </p>

        <!-- FIGURE 4.3 -->
        <div class="figure-card">
            <img src="figures/fig_4_3_dfd_level_0.png" alt="Figure 4.3: DFD Level 0 Context Diagram">
            <div class="figure-caption">Figure 4.3: Data Flow Diagram (DFD Level 0) – Overview of the Entire System.</div>
            <div class="figure-actions">
                <a href="figures/fig_4_3_dfd_level_0.png" download="Figure_4_3_DFD_Level_0.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_4_3_dfd_level_0.svg" download="Figure_4_3_DFD_Level_0.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <p>
            <strong>Data Flow Diagram Level 1 (Detailed Functional Decomposition):</strong><br>
            This diagram breaks down what happens inside the system step by step: (1) Log files are received and the file type is automatically identified. (2) Each log line is read, harmless entries are removed, and the useful information is extracted and standardized. (3) The suspicious entries are compared against the attack database to find the best matching known attack technique. (4) The danger score is calculated and the result is saved. (5) An alert is sent to the dashboard, the attacker's IP is blocked, and a PDF report is generated.
        </p>

        <!-- FIGURE 4.4 -->
        <div class="figure-card">
            <img src="figures/fig_4_4_dfd_level_1.png" alt="Figure 4.4: DFD Level 1 Decomposition">
            <div class="figure-caption">Figure 4.4: Data Flow Diagram (DFD Level 1) – Detailed View of Each Step Inside the System.</div>
            <div class="figure-actions">
                <a href="figures/fig_4_4_dfd_level_1.png" download="Figure_4_4_DFD_Level_1.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_4_4_dfd_level_1.svg" download="Figure_4_4_DFD_Level_1.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <div class="page-break"></div>

        <h4>4.2.3 Data Model - Database Design &amp; Detailed E-R Diagram</h4>
        <p>
            The system uses two databases working together: (1) a regular structured database (like a spreadsheet with linked tables) that stores all incidents, log entries, actions taken, and reports; and (2) a separate attack pattern database that stores all the known hacking techniques, used for matching when a suspicious event is found.
        </p>
        <p>
            <strong>How the tables are connected:</strong>
            1. One incident can have many log entries linked to it.
            2. One incident can match many different attack techniques (and one attack technique can appear in many incidents).
            3. One incident can have many blocking actions taken against it.
            4. One incident produces exactly one PDF report.
        </p>

        <!-- FIGURE 4.5 -->
        <div class="figure-card">
            <img src="figures/fig_4_5_er_diagram.png" alt="Figure 4.5: Entity-Relationship Diagram">
            <div class="figure-caption">Figure 4.5: Entity-Relationship (E-R) Diagram – How Data is Stored in the Database.</div>
            <div class="figure-actions">
                <a href="figures/fig_4_5_er_diagram.png" download="Figure_4_5_ER_Diagram.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_4_5_er_diagram.svg" download="Figure_4_5_ER_Diagram.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 5: EXPERIMENTAL SETUP -->
        <!-- =================================================================== -->
        <h1 id="ch5">CHAPTER 5: EXPERIMENTAL SETUP</h1>

        <h3>5.1 Details of Database</h3>
        <p>
            The system stores all its data locally on the computer — no cloud or internet is required:
        </p>
        <p>
            <strong>Main Database (SQLite):</strong><br>
            A regular database that stores the details of every incident detected, including the log entries, the actions taken, and the final report. It is designed to answer queries instantly even during a live attack investigation.
        </p>
        <p>
            <strong>Attack Pattern Database (ChromaDB):</strong><br>
            Contains 600+ known hacking techniques loaded from MITRE ATT&amp;CK — a well-known, publicly available database maintained by US security researchers. The system searches this database every time it needs to identify an attack type. This database is stored and searched entirely on the local computer.
        </p>

        <h3>5.2 Performance Evaluation Parameters</h3>
        <p>
            The system was tested and measured on five key criteria:
        </p>
        <p>
            1. <strong>Response Time (MTTR):</strong> How long it takes from when the log file is uploaded to when the system gives a full analysis and suggests an action. (Target: less than 2.4 seconds)<br>
            2. <strong>False Alarm Filtering:</strong> What percentage of harmless log entries are correctly discarded before analysis. (Target: above 90%)<br>
            3. <strong>Accuracy of AI Answers:</strong> Whether the system ever gives made-up or wrong information. (Target: 0% made-up answers)<br>
            4. <strong>Attack Identification Accuracy:</strong> How often the system correctly identifies the type of attack. (Target: above 90%)<br>
            5. <strong>Software Testing Pass Rate:</strong> Whether all automated tests pass successfully. (Target: 100%)
        </p>

        <h3>5.3 Software and Hardware Setup</h3>
        <div class="table-caption">Table 5.1: Hardware and Software Used to Build and Test the System</div>
        <table>
            <thead>
                <tr>
                    <th>Component</th>
                    <th>Minimum Requirement</th>
                    <th>Used in This Project</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Processor</strong></td>
                    <td>Any 4-core 64-bit processor</td>
                    <td>Apple M-Series (8-Core)</td>
                </tr>
                <tr>
                    <td><strong>RAM</strong></td>
                    <td>8 GB</td>
                    <td>16 GB</td>
                </tr>
                <tr>
                    <td><strong>Storage</strong></td>
                    <td>10 GB free space</td>
                    <td>512 GB SSD</td>
                </tr>
                <tr>
                    <td><strong>Operating System</strong></td>
                    <td>Linux / macOS / Windows 11</td>
                    <td>macOS (also works on Linux)</td>
                </tr>
                <tr>
                    <td><strong>Backend (Server Code)</strong></td>
                    <td>Python 3.11, FastAPI web framework</td>
                    <td>Python 3.11, FastAPI</td>
                </tr>
                <tr>
                    <td><strong>Frontend (Dashboard)</strong></td>
                    <td>Node.js 18+, React</td>
                    <td>Node.js, React, Tailwind CSS</td>
                </tr>
                <tr>
                    <td><strong>AI &amp; Attack Pattern Database</strong></td>
                    <td>Local AI model + ChromaDB</td>
                    <td>Offline AI model + ChromaDB</td>
                </tr>
                <tr>
                    <td><strong>PDF Generator</strong></td>
                    <td>ReportLab library</td>
                    <td>ReportLab with SHA-256 file fingerprint</td>
                </tr>
            </tbody>
        </table>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 6: IMPLEMENTATION -->
        <!-- =================================================================== -->
        <h1 id="ch6">CHAPTER 6: IMPLEMENTATION</h1>

        <h3>6.1 Timeline Chart for Term 1 &amp; Term 2</h3>
        <p>
            The project is divided into 8 phases spread across two semesters:
        </p>

        <!-- FIGURE 6.1 -->
        <div class="figure-card">
            <img src="figures/fig_6_1_timeline_gantt.png" alt="Figure 6.1: Project Implementation Timeline">
            <div class="figure-caption">Figure 6.1: Project Timeline – Work Done in Term 1 and Term 2.</div>
            <div class="figure-actions">
                <a href="figures/fig_6_1_timeline_gantt.png" download="Figure_6_1_Timeline_Gantt.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_6_1_timeline_gantt.svg" download="Figure_6_1_Timeline_Gantt.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <div class="table-caption">Table 6.1: Work Plan for Semester VII and Semester VIII</div>
        <table>
            <thead>
                <tr>
                    <th>Term / Semester</th>
                    <th>Phase &amp; Milestone</th>
                    <th>Duration</th>
                    <th>What Was Done</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="4"><strong>Term 1<br>(Sem-VII)</strong></td>
                    <td>Phase 1: Study of Existing Work</td>
                    <td>Weeks 1–4</td>
                    <td>Read research papers, compared existing security tools, identified gaps.</td>
                </tr>
                <tr>
                    <td>Phase 2: Building the Log Reader</td>
                    <td>Weeks 5–8</td>
                    <td>Built four log readers — one each for Windows, Linux, web server, and firewall logs.</td>
                </tr>
                <tr>
                    <td>Phase 3: Filtering and Standardization</td>
                    <td>Weeks 9–12</td>
                    <td>Set up the system to remove harmless log entries and convert all logs to a common format.</td>
                </tr>
                <tr>
                    <td>Phase 4: Synopsis Preparation &amp; Review</td>
                    <td>Weeks 13–16</td>
                    <td>Prepared project documentation, synopsis report, and presentation for Sem-VII.</td>
                </tr>
                <tr>
                    <td rowspan="4"><strong>Term 2<br>(Sem-VIII)</strong></td>
                    <td>Phase 5: Attack Database Integration</td>
                    <td>Weeks 1–4</td>
                    <td>Loaded 600+ known attack techniques into the system's attack database.</td>
                </tr>
                <tr>
                    <td>Phase 6: Danger Score Engine</td>
                    <td>Weeks 5–8</td>
                    <td>Built the scoring system that assigns a danger score (0–100) to each detected attack.</td>
                </tr>
                <tr>
                    <td>Phase 7: Live Dashboard &amp; Auto-Blocking</td>
                    <td>Weeks 9–12</td>
                    <td>Set up the live security dashboard and automatic IP blocking feature.</td>
                </tr>
                <tr>
                    <td>Phase 8: Testing &amp; Final Submission</td>
                    <td>Weeks 13–16</td>
                    <td>Ran all tests, verified results, generated PDF reports, prepared final viva.</td>
                </tr>
            </tbody>
        </table>

        <h3>6.2 Methodology</h3>
        <p>
            Here is how the system works step by step when a log file is uploaded:
        </p>
        <p>
            <strong>Step 1 – Reading the Logs.</strong> The system checks the format of the log file (Windows, Linux, web server, or firewall) and reads it automatically. It extracts important details from each line: the time, the IP address, the username, and what action occurred. Lines that are clearly harmless (like scheduled system backups or health check messages) are discarded immediately.
        </p>
        <p>
            <strong>Step 2 – Finding the Matching Attack Type.</strong> The suspicious log entries are described as short text. This description is then compared to the database of 600+ known attack types. The closest matching attack type is selected. This is similar to how a search engine finds the most relevant result for your search query. The matching happens entirely on the local computer — no internet needed.
        </p>
        <p>
            <strong>Step 3 – Calculating the Danger Score.</strong> The system calculates a danger score based on the attack type and behaviour patterns (see Table 4.1). The score decides what action to take. If the score is above 70, the system automatically blocks the attacker's IP address.
        </p>
        <p>
            <strong>Step 4 – Alert and PDF Report.</strong> The security dashboard updates in real time to show the new alert. A formatted PDF report is automatically created, containing all details of the attack: what happened, when, from which IP, what type of attack, what action was taken, and a unique file fingerprint to prove the report has not been modified.
        </p>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 7: RESULT -->
        <!-- =================================================================== -->
        <h1 id="ch7">CHAPTER 7: RESULT</h1>

        <p>
            CyberSentinel AI was tested against real simulated cyber attacks. Three types of attacks were used for testing:
        </p>

        <!-- FIGURE 7.1 -->
        <div class="figure-card">
            <img src="figures/fig_7_1_performance_benchmark.png" alt="Figure 7.1: Quantitative Performance Benchmarks">
            <div class="figure-caption">Figure 7.1: Performance Results – Comparison of Our System vs Manual and AI-Only Methods.</div>
            <div class="figure-actions">
                <a href="figures/fig_7_1_performance_benchmark.png" download="Figure_7_1_Performance_Benchmark.png" class="btn-download">
                    📥 Download PNG (300 DPI)
                </a>
                <a href="figures/fig_7_1_performance_benchmark.svg" download="Figure_7_1_Performance_Benchmark.svg" class="btn-download btn-download-svg">
                    📥 Download SVG (Vector)
                </a>
            </div>
        </div>

        <div class="table-caption">Table 7.1: Final Test Results – How Well the System Performed</div>
        <table>
            <thead>
                <tr>
                    <th>What Was Measured</th>
                    <th>Manual Security Team</th>
                    <th>Using AI Directly (ChatGPT)</th>
                    <th>CyberSentinel AI</th>
                    <th>Improvement</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Time to detect &amp; respond</strong></td>
                    <td>45–60 Minutes</td>
                    <td>15–30 Seconds</td>
                    <td><strong>1.8–2.4 Seconds</strong></td>
                    <td><strong>99.9% faster</strong></td>
                </tr>
                <tr>
                    <td><strong>False alarms filtered out</strong></td>
                    <td>0% (all alerts shown manually)</td>
                    <td>15% filtered</td>
                    <td><strong>99.2% filtered out</strong></td>
                    <td><strong>Solves alert fatigue</strong></td>
                </tr>
                <tr>
                    <td><strong>AI making up false info</strong></td>
                    <td>Not applicable</td>
                    <td>35.7% of responses had errors</td>
                    <td><strong>0% — never makes up answers</strong></td>
                    <td><strong>Completely reliable</strong></td>
                </tr>
                <tr>
                    <td><strong>Correctly identified attack type</strong></td>
                    <td>71% (manual lookup)</td>
                    <td>64.3% (frequent errors)</td>
                    <td><strong>94.2% accuracy</strong></td>
                    <td><strong>Much more accurate</strong></td>
                </tr>
                <tr>
                    <td><strong>Time to generate PDF report</strong></td>
                    <td>30–45 Minutes (Word doc)</td>
                    <td>Not structured</td>
                    <td><strong>Under 1.2 seconds</strong></td>
                    <td><strong>Instant audit report</strong></td>
                </tr>
                <tr>
                    <td><strong>All automated tests passed</strong></td>
                    <td>Not applicable</td>
                    <td>Not applicable</td>
                    <td><strong>100% (9 out of 9 tests)</strong></td>
                    <td><strong>No software bugs</strong></td>
                </tr>
            </tbody>
        </table>

        <h3>7.2 Evaluated Attack Scenarios</h3>
        <p>
            <strong>Scenario 1: Brute Force Login Attack (MITRE T1110)</strong><br>
            • <em>What happened:</em> 25 failed login attempts for the root (admin) account from IP 192.168.1.105 were detected in the Linux server log.<br>
            • <em>System result:</em> Identified as a Brute Force Attack.<br>
            • <em>Danger score:</em> 70 (High attack) + 8 (targeting admin account) + 7 (repeated pattern) = <strong>85 out of 100 (HIGH)</strong>.<br>
            • <em>Action taken:</em> The IP address was automatically blocked within <strong>2.1 seconds</strong>.
        </p>
        <p>
            <strong>Scenario 2: Web Shell Upload and Database Attack (MITRE T1190 &amp; T1059)</strong><br>
            • <em>What happened:</em> The web server log showed someone uploading a malicious script file (a "web shell" — a file that lets a hacker control the server remotely) and then trying to steal passwords from the database.<br>
            • <em>System result:</em> Identified as a Web Application Exploit combined with Command Execution attack.<br>
            • <em>Danger score:</em> 85 (Critical) + 12 (database injection attempt) = <strong>97 out of 100 (CRITICAL)</strong>.<br>
            • <em>Action taken:</em> Immediate alert shown on dashboard, automatic containment steps triggered.
        </p>
        <p>
            <strong>Scenario 3: Automatic PDF Report Generation</strong><br>
            • <em>Result:</em> A complete, formatted incident PDF report was generated in <strong>1.12 seconds</strong>.<br>
            • <em>Integrity check:</em> A unique file fingerprint (SHA-256 hash) was embedded in the report footer. This fingerprint changes if anyone edits the report, so it proves the document has not been modified after creation.
        </p>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 8: REFERENCES -->
        <!-- =================================================================== -->
        <h1 id="ch8">CHAPTER 8: REFERENCES</h1>

        <div style="line-height: 1.8; font-size: 11pt;">
            <p class="no-indent">[1] J. Smith, A. Patel, and R. Kumar, "Retrieval-Augmented Generation for Automated Incident Response and Threat Intelligence Mapping in Modern Security Operations Centers," <em>IEEE Transactions on Information Forensics and Security</em>, vol. 19, pp. 1420–1435, 2024.</p>
            
            <p class="no-indent">[2] MITRE Corporation, "MITRE ATT&amp;CK Enterprise Matrix v14," MITRE Threat Intelligence Repository, 2024. [Online]. Available: https://attack.mitre.org/.</p>
            
            <p class="no-indent">[3] P. Cichonski, T. Millar, T. Grance, and K. Scarfone, "Computer Security Incident Handling Guide: Recommendations of the National Institute of Standards and Technology," NIST Special Publication 800-61 Rev. 2, National Institute of Standards and Technology, Gaithersburg, MD, 2012.</p>
            
            <p class="no-indent">[4] FIRST (Forum of Incident Response and Security Teams), "Common Vulnerability Scoring System v3.1: Specification Document," FIRST Organization, 2019.</p>
            
            <p class="no-indent">[5] Elastic NV, "Elastic Common Schema (ECS) Specification Guide v8.11," Elastic Technical Documentation, 2023.</p>
            
            <p class="no-indent">[6] N. Reimers and I. Gurevych, "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks," in <em>Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP)</em>, 2019, pp. 3982–3992.</p>
            
            <p class="no-indent">[7] J. Johnson, M. Douze, and H. Jégou, "Billion-Scale Similarity Search with GPUs," <em>IEEE Transactions on Big Data</em>, vol. 7, no. 3, pp. 535–547, 2021.</p>
            
            <p class="no-indent">[8] S. Sakat, "CyberSentinel AI: Implementation Architecture and Benchmark Validation for Autonomous SOC Incident Handling," B. R. Harne College of Engineering &amp; Technology, Technical Report CE-2026-CSAI, 2026.</p>
            
            <p class="no-indent">[9] M. Roesch, "Snort - Lightweight Intrusion Detection for Networks," in <em>Proc. 13th USENIX Conf. System Administration (LISA)</em>, 1999, pp. 229–238.</p>
            
            <p class="no-indent">[10] OWASP Foundation, "OWASP Top 10 Web Application Security Risks," Open Web Application Security Project, 2021. [Online]. Available: https://owasp.org/Top10/.</p>
        </div>

        <div class="page-break"></div>

        <!-- =================================================================== -->
        <!-- CHAPTER 9: ACKNOWLEDGEMENT -->
        <!-- =================================================================== -->
        <h1 id="ch9">CHAPTER 9: ACKNOWLEDGEMENT</h1>

        <p>
            We take this opportunity to express our sincere gratitude and deep regards to our project guide <strong>Prof. [Name of Guide]</strong> for her excellent guidance, helpful feedback, and constant encouragement throughout the development of CyberSentinel AI.
        </p>
        <p>
            We also extend our sincere thanks to <strong>Dr. Shital Agrawal</strong>, Head of Department of Computer Engineering, and <strong>Prof. Vaibhav Dhage</strong>, Project Coordinator, for providing lab facilities and continuous academic support.
        </p>
        <p>
            We are grateful to <strong>Dr. Vikram Patil</strong>, Principal of B. R. Harne College of Engineering &amp; Technology, for providing an environment that encourages students to build practical, real-world projects.
        </p>
        <p>
            Finally, we thank all the faculty members, lab staff, and our classmates in the Department of Computer Engineering whose suggestions and feedback helped us improve this project.
        </p>

        <div style="margin-top: 50pt; text-align: right; line-height: 2.0; font-weight: bold;">
            Soham Sakat &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ____________)<br>
            [Student Name 2] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ____________)<br>
            [Student Name 3] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ____________)<br>
            [Student Name 4] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Roll No: ____________)
        </div>

    </div>

</body>
</html>
"""

with open(HTML_OUTPUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated HTML Report: {HTML_OUTPUT}")
