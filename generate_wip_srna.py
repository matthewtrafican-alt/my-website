"""
Generates WIP-SRNA-001 v1.0
Workforce Intelligence Platform — System Requirements & Notional Architecture
Expands H2R-SRNA-001 v1.0 with strategic workforce planning, competency intelligence,
and multi-horizon planning capabilities.
"""

from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# ── Helper functions ──────────────────────────────────────────────────────────

def set_cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_color)
    tcPr.append(shd)

def heading(text, level):
    p = doc.add_heading(text, level=level)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after  = Pt(4)
    return p

def body(text, bold=False, space_after=6):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(space_after)
    if bold:
        for run in p.runs:
            run.bold = True
    return p

def bullet(text):
    p = doc.add_paragraph(text, style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    return p

def action_box(ref, text):
    """Amber action-required box"""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = 'Table Grid'
    cell = tbl.rows[0].cells[0]
    set_cell_bg(cell, 'FFF3CD')
    p = cell.paragraphs[0]
    p.clear()
    run = p.add_run(f'ACTION REQUIRED — {ref}')
    run.bold = True
    run.font.color.rgb = RGBColor(0x85, 0x64, 0x04)
    run.font.size = Pt(9)
    cell.add_paragraph(text).paragraph_format.space_after = Pt(3)
    owner_p = cell.add_paragraph()
    owner_p.add_run('Owner: ________________________    Date: ________________________    Status: ☐ Open  ☐ In Progress  ☐ Resolved').font.size = Pt(8)
    doc.add_paragraph()

def req_table(rows_data, has_source=True):
    """Requirements table: ID | Requirement | MoSCoW | Source"""
    cols = 4 if has_source else 3
    headers = ['ID', 'Requirement', 'MoSCoW', 'Source / Rationale'] if has_source else ['ID', 'Requirement', 'MoSCoW']
    tbl = doc.add_table(rows=1, cols=cols)
    tbl.style = 'Table Grid'
    hdr = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        set_cell_bg(hdr[i], '1F3864')
        for para in hdr[i].paragraphs:
            for run in para.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                run.font.size = Pt(9)
    moscow_colors = {'Must': 'C6EFCE', 'Should': 'FFEB9C', 'Could': 'DDEBF7', "Won't": 'FCE4D6'}
    for row_data in rows_data:
        row = tbl.add_row().cells
        for i, val in enumerate(row_data):
            row[i].text = val
            for para in row[i].paragraphs:
                for run in para.runs:
                    run.font.size = Pt(9)
        if cols >= 3:
            moscow = row_data[2]
            color  = moscow_colors.get(moscow, 'FFFFFF')
            set_cell_bg(row[2], color)
    doc.add_paragraph()

def simple_table(headers, rows, header_color='1F3864'):
    tbl = doc.add_table(rows=1, cols=len(headers))
    tbl.style = 'Table Grid'
    hdr = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        set_cell_bg(hdr[i], header_color)
        for para in hdr[i].paragraphs:
            for run in para.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                run.font.size = Pt(9)
    for row_data in rows:
        row = tbl.add_row().cells
        for i, val in enumerate(row_data):
            row[i].text = val
            for para in row[i].paragraphs:
                for run in para.runs:
                    run.font.size = Pt(9)
    doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('S Y S T E M   R E Q U I R E M E N T S   &   N O T I O N A L\nA R C H I T E C T U R E')
run.font.size = Pt(11)
run.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)
run.bold = True

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = p2.add_run('Workforce Intelligence Platform')
run2.font.size = Pt(26)
run2.bold = True
run2.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
run3 = p3.add_run('AI-Powered Strategic Workforce Planning, Competency Intelligence\n& H2R Process Analytics')
run3.font.size = Pt(13)
run3.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)

doc.add_paragraph()

meta = doc.add_table(rows=4, cols=4)
meta.style = 'Table Grid'
meta_data = [
    ['Organisation', 'AeroDefend Group (Illustrative)', 'Version', '1.0 — DRAFT'],
    ['Classification', 'Internal — Confidential', 'Status', 'Pending IT Review'],
    ['Prepared by', 'HR Transformation Initiative', 'Prepared for', 'IT VP & HR VP'],
    ['Document ref', 'WIP-SRNA-001', 'Date', '29 May 2026'],
]
for r, row_data in enumerate(meta_data):
    cells = meta.rows[r].cells
    for c, val in enumerate(row_data):
        cells[c].text = val
        if c % 2 == 0:
            set_cell_bg(cells[c], 'D6E4F0')
            for para in cells[c].paragraphs:
                for run in para.runs:
                    run.bold = True
                    run.font.size = Pt(9)
        else:
            for para in cells[c].paragraphs:
                for run in para.runs:
                    run.font.size = Pt(9)

doc.add_paragraph()

info_tbl = doc.add_table(rows=1, cols=1)
info_tbl.style = 'Table Grid'
info_cell = info_tbl.rows[0].cells[0]
set_cell_bg(info_cell, 'D6E4F0')
info_p = info_cell.paragraphs[0]
info_p.clear()
run_info = info_p.add_run('Relationship to H2R-SRNA-001')
run_info.bold = True
run_info.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)
info_cell.add_paragraph(
    'This document (WIP-SRNA-001) directly extends H2R-SRNA-001 v1.0. All functional and '
    'non-functional requirements from the H2R Process Intelligence Platform are carried forward '
    'and supplemented with multi-horizon workforce planning capabilities, a competency '
    'intelligence layer grounded in external occupational frameworks, and a cascade engine that '
    'connects strategic workforce decisions to daily H2R execution. Requirement IDs prefixed '
    'FR-H2R are inherited from H2R-SRNA-001. New requirements are prefixed FR-WIP.'
)
doc.add_paragraph()

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 1. DOCUMENT CONTROL
# ══════════════════════════════════════════════════════════════════════════════
heading('1. Document Control & Revision History', 1)
simple_table(
    ['Version', 'Date', 'Author', 'Changes'],
    [
        ['1.0', '29/05/2026', 'HR Transformation Team', 'Initial draft — expands H2R-SRNA-001 with multi-horizon workforce planning and competency intelligence layers'],
    ]
)
heading('1.1 Document Approvals Required', 2)
simple_table(
    ['Role', 'Name', 'Date', 'Signature / Approval'],
    [
        ['IT Vice President', '', '', ''],
        ['HR Vice President', '', '', ''],
        ['Chief People Officer', '', '', ''],
        ['IT Architecture Lead', '', '', ''],
        ['Data Engineering Lead', '', '', ''],
        ['CISO / Information Security', '', '', ''],
        ['Legal / Compliance', '', '', ''],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 2. EXECUTIVE SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
heading('2. Executive Summary', 1)
body(
    'The AeroDefend Group Workforce Intelligence Platform extends the H2R Process Intelligence '
    'Platform (H2R-SRNA-001) into a full-spectrum workforce planning capability. Where the H2R '
    'platform addresses operational HR execution — process conformance, SLA management, and '
    'compliance monitoring — this platform adds the strategic intelligence layer that most '
    'organisations lack: the ability to see three years ahead, identify capability gaps before '
    'they become hiring emergencies, and generate legally defensible competency models grounded '
    'in industry-standard occupational frameworks.'
)
body(
    'Research confirms that approximately 90% of organisations want skills-based workforce '
    'planning, yet only 26% actively implement it. The primary barrier is not ambition but '
    'architecture: organisations operate in reverse, managing what they have today without a '
    'clear view of what they need tomorrow. This platform resolves that by connecting four '
    'planning horizons — Strategic (3–5 years), Operational (12–36 months), Tactical (0–12 '
    'months), and Execution (daily/weekly) — through a single Databricks Lakehouse and a '
    'shared competency ontology.'
)

heading('2.1 Platform Capabilities at a Glance', 2)
simple_table(
    ['Capability', 'Description', 'Planning Horizon'],
    [
        ['Strategic Workforce Planning', '3-year capability gap analysis, scenario modelling, build/buy/borrow/bot decisions', 'Strategic (3–5 yr)'],
        ['Headcount & Capacity Planning', 'Annual headcount planning linked to budget cycles and business strategy', 'Operational (1–3 yr)'],
        ['Competency Intelligence', 'AI-generated competency models grounded in O*NET, NICE, INCOSE SECF, R&M BoK', 'Operational / Tactical'],
        ['Tactical Workforce Planning', 'Active requisition management, deployment, retention risk, internal mobility', 'Tactical (0–12 mo)'],
        ['H2R Process Intelligence', 'Process mining, SLA management, compliance monitoring (inherited from H2R-SRNA-001)', 'Execution (daily)'],
        ['Cascade Engine', 'Bidirectional flow: strategy → execution and operational data → strategic forecast', 'All horizons'],
        ['UGESP Compliance Engine', 'Auto-generated legal documentation for selection procedures and competency validation', 'All horizons'],
        ['Talent Marketplace', 'Internal mobility matching based on competency profiles and career pathway models', 'Tactical / Execution'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 3. SCOPE & BUSINESS CONTEXT
# ══════════════════════════════════════════════════════════════════════════════
heading('3. Scope & Business Context', 1)
heading('3.1 Initiative Purpose', 2)
body(
    'The Workforce Intelligence Platform transforms AeroDefend Group\'s approach to workforce '
    'management by integrating four previously disconnected planning layers into a single '
    'platform. The platform applies process mining, machine learning, a competency knowledge '
    'graph, and generative AI to both SAP H2R event data and external occupational frameworks — '
    'enabling evidence-based process improvement, predictive capability gap management, '
    'compliance monitoring, and self-service workforce analytics across all planning horizons.'
)

heading('3.2 The Four-Horizon Planning Architecture', 2)
body(
    'Effective workforce planning requires simultaneous management of four interconnected time '
    'horizons. Each horizon has distinct questions, rhythms, and outputs. The platform addresses '
    'all four, with the cascade engine ensuring decisions at the strategic level drive action at '
    'the execution level, and operational data feeds back up to refine the strategic forecast.'
)
simple_table(
    ['Layer', 'Horizon', 'Primary Question', 'Planning Rhythm', 'Primary Output'],
    [
        ['Strategic WFP', '3–5 years', 'What workforce shape and capability do we need to execute business strategy?', 'Annual + major trigger events', 'Strategic capability plan, scenario models, build/buy/borrow decisions'],
        ['Operational WFP', '12–36 months', 'How many people, in what roles, with what competencies, and when?', 'Annual budget cycle + quarterly review', 'Headcount plan, L&D investment plan, succession slate'],
        ['Tactical WFP & Execution', '0–12 months', 'Who do we hire, redeploy, develop, or exit — and in what sequence?', 'Monthly + sprint cadence', 'Hiring plan, deployment schedule, retention actions, internal mobility matches'],
        ['H2R Execution', 'Daily / weekly', 'Are our HR processes running on time and in compliance?', 'Daily pipeline, real-time alerts', 'Process KPIs, SLA breach reports, compliance alerts, case risk scores'],
    ]
)

heading('3.3 In Scope — Phase 1 (Months 1–6)', 2)
bullet('All capabilities from H2R-SRNA-001 Phase 1 (carried forward in full)')
bullet('Framework Backbone ingestion: O*NET Web Services API, NICE Framework v2.2 (JSON), INCOSE SECF (structured data), R&M BoK lifecycle-competency mappings')
bullet('HR Domain Ontology expanded to include occupational frameworks, competency definitions at 5 proficiency levels, and Bloom\'s Taxonomy cognitive complexity mapping')
bullet('Strategic Workforce Planning module: 3-year capability gap analysis, scenario modelling engine, build/buy/borrow/bot decision support')
bullet('Operational Workforce Planning module: annual headcount planning, role pipeline management, succession risk analysis')
bullet('Competency Intelligence module: AI-generated competency models, behavioural indicators at 5 levels, UGESP-compliant technical documentation')
bullet('Cascade Engine: bidirectional linkage between planning layers, strategic gaps cascading to active requisitions')
bullet('Databricks Lakehouse: Bronze/Silver/Gold Delta Lake, Unity Catalog, MLflow, Workflows')
bullet('Semantic Layer: governed workforce data access, business metric definitions, row-level security')
bullet('AI Agent: Claude API with RAG over ChromaDB vector store (framework backbone + process mining outputs)')
bullet('Visualisation: Native React dashboard (operational) + Tableau integration (strategic + workforce planning)')
bullet('UGESP Compliance Engine: auto-generated legal documentation, adverse impact monitoring')

heading('3.4 Explicitly Out of Scope — Phase 1', 2)
bullet('Direct write-back to SAP (read-only integration in Phase 1)')
bullet('Real-time SAP event streaming (batch ingestion in Phase 1)')
bullet('Mobile application')
bullet('AFECD / military classification system integration (Phase 2)')
bullet('External talent market data integration (Phase 2)')
bullet('Automated workflow execution in SAP (Phase 2)')
bullet('Full SIOP-compliant structured job analysis data collection (Phase 2 — framework seeded in Phase 1)')

# ══════════════════════════════════════════════════════════════════════════════
# 4. FRAMEWORK BACKBONE
# ══════════════════════════════════════════════════════════════════════════════
heading('4. Competency Framework Backbone', 1)
body(
    'The platform\'s competency intelligence layer is grounded in six authoritative external '
    'frameworks. These frameworks serve as the semantic backbone — providing standardised '
    'occupational language, competency definitions, task inventories, and proficiency level '
    'indicators that the platform uses to automatically generate client-facing competency models '
    'and legal technical documentation. This eliminates the need for clients to build competency '
    'models from scratch and ensures all models are defensible against industry standards.'
)

simple_table(
    ['Framework', 'Source', 'Primary Contribution', 'Access Method'],
    [
        ['O*NET', 'US DOL / O*NET Resource Center', 'Occupational taxonomy (900+ roles), task inventories, KSAOs, work context', 'Web Services API (X-API-Key)'],
        ['NICE Framework v2.2', 'NIST / CISA (April 2025)', 'Cybersecurity workforce: 30+ work roles, TKS statements, competency areas', 'JSON / XLSX download'],
        ['INCOSE SECF', 'INCOSE (July 2018)', '36 Systems Engineering competencies × 5 proficiency levels × behavioural indicators', 'Structured PDF / parsed data'],
        ['R&M BoK', 'DoW / OSD (December 2025)', 'Defense acquisition engineering lifecycle competency requirements by phase and functional area', 'Parsed from public release PDF'],
        ['AFECD', 'USAF / AFPC', 'Air Force Specialty Codes (AFSCs), skill levels (3/5/7/9), duty descriptions, entry requirements', 'Phase 2 — pending data access'],
        ['SIOP / UGESP Methodology', 'SHRM-SIOP (2024)', 'Competency modeling methodology, legal defensibility requirements, content validation framework', 'Reference methodology only'],
        ["Bloom's Taxonomy", 'Educational literature', 'Cognitive complexity mapping for proficiency levels 1–5', 'Reference model'],
    ]
)

heading('4.1 Competency Model Output Structure', 2)
body(
    'All competency models generated by the platform follow the INCOSE SECF structure, which '
    'provides the most complete and implementable format for HR use cases. Each generated '
    'competency has the following structure:'
)
simple_table(
    ['Element', 'Description', 'Source'],
    [
        ['Label', 'Short competency name (e.g. "Systems Thinking")', 'INCOSE SECF / O*NET / NICE / client taxonomy'],
        ['Definition', '2–3 sentence description of the competency and why it matters', 'INCOSE SECF / SIOP methodology'],
        ['Behavioural Indicators — Level 1 (Awareness)', 'Observable behaviours demonstrating entry-level competence', 'INCOSE SECF model + AI generation'],
        ['Behavioural Indicators — Level 2 (Supervised Practitioner)', 'Behaviours requiring guidance and supervision', 'INCOSE SECF model + AI generation'],
        ['Behavioural Indicators — Level 3 (Practitioner)', 'Independent performance behaviours', 'INCOSE SECF model + AI generation'],
        ['Behavioural Indicators — Level 4 (Lead Practitioner)', 'Expert guidance and enterprise-level behaviours', 'INCOSE SECF model + AI generation'],
        ['Behavioural Indicators — Level 5 (Expert)', 'Recognised authority, contribution beyond enterprise boundary', 'INCOSE SECF model + AI generation'],
        ["Bloom's Level Mapping", 'Cognitive complexity of each proficiency level (Remember → Create)', "Bloom's Taxonomy"],
        ['O*NET Cross-Reference', 'Linked O*NET occupational codes and KSA element IDs', 'O*NET API'],
        ['UGESP Validation Statement', 'Content validity evidence linking competency to job performance', 'SIOP / UGESP methodology'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 5. STAKEHOLDER & USER ROLES
# ══════════════════════════════════════════════════════════════════════════════
heading('5. Stakeholder & User Roles', 1)
body(
    'The following roles interact with the platform at different access levels across all '
    'planning horizons. Data governance and row-level security in Unity Catalog are configured '
    'per this matrix. Roles marked * are new additions beyond H2R-SRNA-001.'
)
simple_table(
    ['Role', 'User Type', 'Platform Access', 'Planning Horizon', 'Visualisation'],
    [
        ['Chief People Officer *', 'Executive', 'Strategic WFP dashboard + AI agent + full platform read', 'Strategic (3–5 yr)', 'Executive Tableau + AI agent'],
        ['HR Vice President', 'Executive', 'Full platform + AI agent (all departments, read-only)', 'All horizons', 'Executive Tableau + AI agent'],
        ['IT Vice President', 'Executive', 'Architecture dashboard + infrastructure metrics', 'Execution', 'IT ops Tableau view'],
        ['Workforce Planning Analyst *', 'Power User', 'Strategic WFP + Competency Intelligence + cascade engine', 'Strategic + Operational', 'React WFP dashboard + Tableau'],
        ['HR Business Partner', 'Power User', 'AI agent + process maps + action plans + competency models', 'Operational + Tactical', 'Operational React + Tableau'],
        ['TA Recruiter / Coordinator', 'Operational', 'Active case risk scores + breach alerts + role profiles', 'Tactical + Execution', 'React dashboard (operational)'],
        ['HR Operations Manager', 'Power User', 'Full process mining + root cause + headcount planning', 'Operational + Execution', 'React + Tableau'],
        ['Competency SME *', 'Specialist', 'Competency model builder + framework backbone viewer + UGESP docs', 'Operational', 'Competency Intelligence dashboard'],
        ['Compensation Analyst', 'Specialist', 'Compensation-related process steps + comp band planning', 'Operational', 'Tableau only'],
        ['Data / Analytics Analyst', 'Technical', 'Full Databricks SQL + semantic layer + notebooks', 'All (anonymised PII)', 'Tableau + Databricks notebooks'],
        ['IT Architect', 'Technical', 'Infrastructure + integration layer + metadata', 'Execution', 'IT monitoring dashboard'],
        ['Compliance Officer', 'Audit', 'Compliance sentinel + breach log + UGESP documentation', 'All horizons', 'Compliance Tableau view'],
        ['Line Manager', 'Consumer', 'Self-service: own team cases + team competency profiles', 'Tactical', 'Tableau published view (read-only)'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 6. FUNCTIONAL REQUIREMENTS
# ══════════════════════════════════════════════════════════════════════════════
heading('6. Functional Requirements', 1)
body(
    'Requirements are numbered by capability area and prioritised using MoSCoW. Requirements '
    'prefixed FR-H2R are inherited from H2R-SRNA-001 v1.0 and are carried forward unchanged. '
    'Requirements prefixed FR-WIP are new to this document. Each requirement traces to a named '
    'source (business pain point, compliance obligation, or stakeholder request).'
)

# 6.1 Data Ingestion (inherited)
heading('6.1 Data Ingestion & Event Log (Inherited from H2R-SRNA-001)', 2)
body('All FR-D01 through FR-D09 requirements from H2R-SRNA-001 are carried forward unchanged. See H2R-SRNA-001 §4.1 for full definitions. Key additions below.')
req_table([
    ['FR-WIP-D01', 'The system shall ingest framework backbone data from O*NET Web Services API on a scheduled basis (minimum weekly), storing raw responses in the Bronze layer', 'Must', 'Framework: O*NET occupational data must be current'],
    ['FR-WIP-D02', 'The system shall ingest NICE Framework v2.2 work role definitions, TKS statements, and competency area mappings from the published JSON/XLSX source on initial load and when new versions are released', 'Must', 'Framework: NICE is the cybersecurity workforce standard'],
    ['FR-WIP-D03', 'The system shall ingest INCOSE SECF competency definitions (36 competencies × 5 levels × behavioural indicators) as structured data into the framework ontology', 'Must', 'Framework: INCOSE SECF is the competency output format template'],
    ['FR-WIP-D04', 'The system shall ingest R&M BoK lifecycle-phase competency mappings (MSA, TMRR, EMD, P&D, O&S) as structured data, linking acquisition phase to required functional competencies', 'Must', 'Framework: R&M BoK provides defense acquisition engineering competencies'],
    ['FR-WIP-D05', 'The system shall ingest client workforce data (job titles, position descriptions, incumbent profiles, performance data) via CSV upload or HRIS API, mapping client terminology to framework concepts via the semantic layer', 'Must', 'Client: platform must work with client\'s existing data, not replace it'],
    ['FR-WIP-D06', "The system shall ingest Bloom's Taxonomy cognitive level definitions as a reference model, mapping each to INCOSE SECF proficiency levels 1–5", 'Must', "Competency: Bloom's mapping enables cognitive complexity scoring"],
])

# 6.2 Process Mining (inherited)
heading('6.2 Process Mining Engine (Inherited from H2R-SRNA-001)', 2)
body('All FR-PM01 through FR-PM09 requirements from H2R-SRNA-001 are carried forward unchanged. See H2R-SRNA-001 §4.2 for full definitions.')

# 6.3 Predictive Analytics (inherited)
heading('6.3 Predictive Analytics (Inherited from H2R-SRNA-001)', 2)
body('All FR-PA01 through FR-PA07 requirements from H2R-SRNA-001 are carried forward unchanged. See H2R-SRNA-001 §4.3 for full definitions. Key additions below.')
req_table([
    ['FR-WIP-PA01', 'The system shall train and deploy a capability gap prediction model that forecasts workforce capability shortfalls at 12-month, 24-month, and 36-month horizons, by job family, department, and competency domain', 'Must', 'Strategic WFP: core output of the strategic planning module'],
    ['FR-WIP-PA02', 'The system shall model three workforce scenarios for each strategic planning cycle: Status Quo, Growth, and Restructure — each producing a distinct capability gap profile and recommended action portfolio', 'Should', 'Strategic WFP: scenario modelling for planning uncertainty'],
    ['FR-WIP-PA03', 'The system shall calculate a Workforce Readiness Index (WRI) for each department, combining current competency coverage, pipeline strength, and attrition risk into a single 0–100 score', 'Should', 'Strategic WFP: executive-level workforce health metric'],
])

# 6.4 Ontology & Knowledge Graph (significantly expanded)
heading('6.4 Ontology & Knowledge Graph (Significantly Expanded)', 2)
body('All FR-OG01 through FR-OG07 requirements from H2R-SRNA-001 are carried forward and expanded below. The ontology scope is significantly larger than originally defined in H2R-SRNA-001.')
req_table([
    ['FR-WIP-OG01', 'The HR Domain Ontology shall incorporate all six framework backbone sources (O*NET, NICE, INCOSE SECF, R&M BoK, Bloom\'s Taxonomy, SIOP/UGESP methodology) as structured ontology layers, with defined relationships between entities across frameworks', 'Must', 'Framework: cross-framework mapping is the platform\'s core differentiator'],
    ['FR-WIP-OG02', 'The ontology shall define an Occupation entity with attributes: O*NET code, title, task inventory, KSAO elements, work context, and cross-references to NICE work roles and INCOSE SECF competencies where applicable', 'Must', 'Ontology: occupation is the primary entity linking all frameworks'],
    ['FR-WIP-OG03', 'The ontology shall define a Competency entity with attributes: label, definition, why-it-matters, five proficiency levels each with behavioural indicators, Bloom\'s cognitive level mapping, and source framework reference', 'Must', 'Competency: this is the primary output entity of the platform'],
    ['FR-WIP-OG04', 'The ontology shall define an AcquisitionPhase entity linking R&M BoK lifecycle phases (MSA, TMRR, EMD, P&D, O&S) to required functional area competencies at specified proficiency levels', 'Must', 'R&M BoK: defense acquisition workforce planning requires lifecycle context'],
    ['FR-WIP-OG05', 'The ontology shall define a WorkRole entity linking NICE Framework work roles to O*NET occupational codes, INCOSE SECF competencies, and client position data via entity resolution', 'Must', 'NICE: cybersecurity workforce mapping requires this entity'],
    ['FR-WIP-OG06', 'The ontology shall support a ProficiencyLevel entity (1–5, Awareness through Expert) with defined behavioural indicators per competency, linked to Bloom\'s cognitive taxonomy levels', 'Must', "Competency: proficiency levels are required for UGESP defensibility and L&D planning"],
    ['FR-WIP-OG07', 'The ontology shall support a CareerPath entity representing role-to-role progression routes, including required competency level transitions, typical time-in-role, and bridging development actions', 'Should', 'Career: career pathway maps are a primary client deliverable'],
    ['FR-WIP-OG08', 'The ontology shall support a CapabilityGap entity linking current workforce competency profiles to future-state requirements derived from the strategic workforce plan, with a gap severity score and recommended resolution (hire/build/borrow/bot)', 'Must', 'Strategic WFP: gap entity is the core analytical output'],
    ['FR-WIP-OG09', 'The knowledge graph shall support cross-framework queries such as: "Show all O*NET occupations mapped to NICE work roles where the INCOSE Systems Thinking competency is required at Practitioner level or above"', 'Must', 'Analytics: cross-framework insight is the primary value proposition'],
    ['FR-WIP-OG10', 'The ontology shall be version-controlled and auditable, with all changes timestamped and attributed — required for UGESP compliance and legal defensibility', 'Must', 'UGESP: competency model changes must be traceable'],
])

# 6.5 Semantic Layer (inherited)
heading('6.5 Semantic Layer (Inherited + Extended from H2R-SRNA-001)', 2)
body('All FR-SL01 through FR-SL07 requirements from H2R-SRNA-001 are carried forward unchanged. Key additions below.')
req_table([
    ['FR-WIP-SL01', 'The semantic layer metric catalogue shall be extended to include workforce planning metrics: Workforce Readiness Index, Capability Coverage %, Competency Gap Count, Time-to-Competency, and Strategic Hire Fill Rate', 'Must', 'Strategic WFP: workforce planning KPIs are distinct from H2R process KPIs'],
    ['FR-WIP-SL02', 'The semantic layer shall expose a workforce planning API enabling the cascade engine to query current competency profiles, active gaps, and planned headcount changes in a single call', 'Must', 'Cascade: real-time cross-layer queries require a unified semantic interface'],
])

# 6.6 AI Agent (inherited + expanded)
heading('6.6 AI Agent (Inherited + Extended from H2R-SRNA-001)', 2)
body('All FR-AI01 through FR-AI08 requirements from H2R-SRNA-001 are carried forward unchanged. Key additions below.')
req_table([
    ['FR-WIP-AI01', 'The AI agent shall answer strategic workforce planning questions grounded in the framework backbone and client data, including: capability gap analysis, build/buy/borrow recommendations, scenario comparison, and competency model generation', 'Must', 'Strategic WFP: AI agent must span all planning horizons, not just H2R process'],
    ['FR-WIP-AI02', 'The AI agent shall generate draft competency models for any role or job family when prompted, using the INCOSE SECF structure, grounded in O*NET task inventories and NICE/INCOSE competency definitions', 'Must', 'Competency: automated model generation is a primary platform capability'],
    ['FR-WIP-AI03', 'The AI agent shall generate UGESP-compliant technical documentation for any competency model on request, including: job analysis rationale, content validity evidence, and adverse impact monitoring requirements', 'Should', 'UGESP: legal documentation generation reduces I-O psychology consulting cost'],
    ['FR-WIP-AI04', 'The AI agent shall translate military occupational specialties (AFSCs, MOSs) to civilian O*NET equivalents on demand, supporting military-to-civilian workforce transition planning', 'Could', 'AFECD: defense clients need military-to-civilian translation'],
])

# 6.7 Strategic Workforce Planning Module
heading('6.7 Strategic Workforce Planning Module', 2)
body('This module is new to this document. It addresses the 3-year planning horizon and the annual strategic workforce planning cycle.')
req_table([
    ['FR-WIP-SWP01', 'The system shall maintain a rolling 3-year workforce plan for each department and the enterprise as a whole, updated annually and on major trigger events (acquisition, contract award/loss, technology change)', 'Must', 'Strategic WFP: 3-year horizon is the minimum required for meaningful capability planning'],
    ['FR-WIP-SWP02', 'The 3-year plan shall decompose business strategy into capability requirements, translating strategic objectives into required competencies, headcount, and role profiles using the framework backbone as translation layer', 'Must', 'Strategic WFP: strategy-to-workforce translation is the core analytical task'],
    ['FR-WIP-SWP03', 'The system shall calculate a capability gap for each competency domain: (Required Proficiency × Required Headcount) minus (Current Proficiency × Current Headcount), producing a gap severity matrix by year, department, and competency', 'Must', 'Strategic WFP: quantified gap is required for budget and investment decisions'],
    ['FR-WIP-SWP04', 'The system shall recommend a sourcing strategy for each capability gap: Build (L&D investment), Buy (external hire), Borrow (contractor/partner), or Bot (automation/AI substitution), with estimated cost and timeline for each option', 'Must', 'Strategic WFP: build/buy/borrow/bot decision framework is standard workforce planning methodology'],
    ['FR-WIP-SWP05', 'The strategic workforce plan shall be versioned and support before/after comparison, enabling measurement of plan accuracy and plan improvement over successive cycles', 'Should', 'Governance: plan vs actual tracking demonstrates workforce planning maturity'],
    ['FR-WIP-SWP06', 'The system shall support scenario modelling: users define business scenarios (e.g. 20% revenue growth, entry into new market, loss of key contract) and the system generates the corresponding workforce requirement delta', 'Should', 'Strategic WFP: planning under uncertainty requires scenario analysis'],
])

# 6.8 Operational Workforce Planning Module
heading('6.8 Operational Workforce Planning Module (Headcount Planning)', 2)
body('This module addresses the 12–36 month horizon and the annual headcount planning and budget cycle.')
req_table([
    ['FR-WIP-OWP01', 'The system shall support an annual headcount planning cycle: departments submit headcount requests, the system validates them against strategic capability requirements and budget constraints, producing a recommended headcount plan', 'Must', 'Operational WFP: annual headcount planning is the primary operational rhythm'],
    ['FR-WIP-OWP02', 'The headcount plan shall track planned headcount vs approved budget vs actual headcount at department and role level, updated after each monthly pipeline run', 'Must', 'Operational WFP: plan vs actual variance is a core management metric'],
    ['FR-WIP-OWP03', 'The system shall identify succession risk: roles where there is no ready-now successor and no development pipeline, flagged as critical succession gaps requiring immediate action', 'Must', 'Operational WFP: succession risk is a board-level concern in defense organisations'],
    ['FR-WIP-OWP04', 'The system shall produce a quarterly workforce planning review pack for HR leadership: headcount status, capability gap progress, succession risk update, and 12-month hiring forecast', 'Should', 'Operational WFP: regular review cadence is required for organisational accountability'],
    ['FR-WIP-OWP05', 'The system shall track L&D investment against capability gap closure, measuring competency level improvement for individuals in development programmes and reporting aggregate capability uplift', 'Should', 'Operational WFP: L&D ROI measurement enables investment prioritisation'],
])

# 6.9 Tactical Workforce Planning & Execution Module
heading('6.9 Tactical Workforce Planning & Execution Module', 2)
body('This module addresses the 0–12 month horizon, connecting operational headcount plans to active requisitions and the H2R execution layer.')
req_table([
    ['FR-WIP-TWP01', 'The system shall maintain a tactical hiring plan for the next 12 months, derived from the approved headcount plan and updated monthly, showing requisitions by role, priority, target hire date, and sourcing strategy', 'Must', 'Tactical WFP: the tactical plan is the bridge between operational planning and H2R execution'],
    ['FR-WIP-TWP02', 'The cascade engine shall automatically generate requisition records in the hiring plan when a new headcount position is approved in the operational workforce plan', 'Must', 'Cascade: this is the key downstream connection from operational to tactical layer'],
    ['FR-WIP-TWP03', 'The system shall calculate a deployment optimisation recommendation for each open position: internal candidate match score (based on competency gap to role requirement), vs external hire cost/time estimate', 'Should', 'Tactical WFP: internal mobility is faster and cheaper than external hire where a match exists'],
    ['FR-WIP-TWP04', 'The system shall identify retention risk: individuals with high competency profiles in critical roles where attrition indicators are elevated (tenure, market demand for skills, flight risk score from H2R data)', 'Must', 'Tactical WFP: retention of critical talent is a primary tactical concern'],
    ['FR-WIP-TWP05', 'The system shall produce a monthly workforce execution dashboard showing: tactical plan vs actuals, open critical requisitions, retention risk alerts, internal mobility matches, and competency development progress', 'Must', 'Tactical WFP: monthly cadence is required for HR operations rhythm'],
])

# 6.10 Competency Intelligence Module
heading('6.10 Competency Intelligence Module', 2)
body('This module manages the generation, validation, versioning, and delivery of competency models. It is a primary client-facing capability of the platform.')
req_table([
    ['FR-WIP-CI01', 'The system shall generate a draft competency model for any role or job family using the AI agent, grounded in O*NET task inventories, NICE/INCOSE SECF competency definitions, and client job description data', 'Must', 'Competency: automated model generation is the primary differentiated capability'],
    ['FR-WIP-CI02', 'Each generated competency model shall follow the INCOSE SECF structure: Competency Label, Definition, Why it Matters, and Behavioural Indicators at 5 proficiency levels', 'Must', 'INCOSE SECF: using the industry standard structure ensures professional quality and defensibility'],
    ['FR-WIP-CI03', 'The system shall assign a Bloom\'s Taxonomy cognitive level to each proficiency level indicator, enabling training designers and assessors to understand the cognitive complexity expected at each level', 'Must', "Bloom's: cognitive complexity mapping enables L&D curriculum design aligned to proficiency targets"],
    ['FR-WIP-CI04', 'Generated competency models shall include O*NET cross-references: the O*NET occupational code(s) the role maps to, and the specific KSA element IDs that underpin each competency', 'Must', 'O*NET: cross-referencing to O*NET provides external validation evidence for UGESP purposes'],
    ['FR-WIP-CI05', 'The system shall support SME validation workflow: drafted competency models are routed to designated Subject Matter Experts for review and rating, with consolidated ratings producing a validated final model', 'Should', 'SIOP: SME validation is a required step in content validity evidence gathering'],
    ['FR-WIP-CI06', 'All competency models shall be versioned, with changes tracked and attributed to support audit trail requirements for UGESP compliance', 'Must', 'UGESP: competency model changes must be auditable to defend selection procedure validity'],
    ['FR-WIP-CI07', 'The system shall generate both a public-facing competency model (behavioural indicators, proficiency levels, development guidance) and a legal technical documentation package (job analysis rationale, content validity evidence, adverse impact monitoring plan)', 'Must', 'UGESP: two outputs are required — one for HR use, one for legal defensibility'],
])

# 6.11 Cascade Engine
heading('6.11 Cascade Engine', 2)
body(
    'The cascade engine is the architectural mechanism that connects the four planning horizons. '
    'It ensures that strategic decisions propagate downward to execution, and that operational '
    'data feeds back upward to refine the strategic forecast. Without this engine, the platform '
    'is a collection of isolated planning tools rather than an integrated workforce intelligence system.'
)
req_table([
    ['FR-WIP-CE01', 'The cascade engine shall propagate approved strategic capability requirements downward to the operational headcount plan: a new strategic capability gap automatically creates a planned headcount need in the operational layer', 'Must', 'Cascade: top-down propagation is the core cascade mechanism'],
    ['FR-WIP-CE02', 'The cascade engine shall propagate approved operational headcount positions downward to the tactical hiring plan, generating requisition records with required competency profile attached', 'Must', 'Cascade: operational-to-tactical cascade ensures requisitions reflect strategic intent'],
    ['FR-WIP-CE03', 'The cascade engine shall aggregate execution-layer data (H2R process KPIs, hire outcomes, attrition events) upward into the tactical and operational layers, updating plan vs actual metrics in real time after each pipeline run', 'Must', 'Cascade: bottom-up data flow enables self-correcting plans'],
    ['FR-WIP-CE04', 'The cascade engine shall identify cascade breaks: where an approved strategic capability requirement has no corresponding operational headcount position, or a headcount position has no corresponding tactical requisition — flagged as planning gaps requiring action', 'Must', 'Cascade: breaks in the cascade are planning risks that must be visible'],
    ['FR-WIP-CE05', 'The cascade engine shall produce a monthly cascade health report showing: strategic requirements with operational coverage, operational positions with tactical requisitions, and tactical requisitions with active H2R cases', 'Should', 'Governance: cascade health is a workforce planning maturity indicator'],
])

# 6.12 UGESP Compliance Engine
heading('6.12 UGESP Compliance & Legal Documentation Engine', 2)
req_table([
    ['FR-WIP-UC01', 'The system shall generate a UGESP-compliant Job Analysis Report for any role or job family, including: job title and O*NET code, task inventory with importance ratings, KSAO linkage table, and evidence of SME input', 'Must', 'Legal: UGESP requires documented job analysis as foundation for any selection procedure'],
    ['FR-WIP-UC02', 'The system shall generate a Content Validity Evidence Summary for each competency model, documenting: the link from job analysis to competency identification, SME validation process, and the two-assertion framework (job→competency→HR process)', 'Must', 'UGESP: content validity is the primary legal defensibility mechanism for competency-based selection'],
    ['FR-WIP-UC03', 'The system shall monitor adverse impact for any selection or assessment process linked to the platform: calculating the 4/5ths rule across protected groups and flagging violations for legal review', 'Should', 'UGESP Section 4D: adverse impact monitoring is a regulatory requirement'],
    ['FR-WIP-UC04', 'All UGESP documentation shall be versioned, timestamped, and stored in the Databricks audit layer — retained for minimum 7 years to meet employment law record-keeping requirements', 'Must', 'Legal: employment documentation retention requirements vary by jurisdiction; 7 years is the conservative standard'],
])

# 6.13 Talent Marketplace
heading('6.13 Talent Marketplace', 2)
req_table([
    ['FR-WIP-TM01', 'The system shall maintain a competency profile for each employee, combining assessed proficiency levels (from performance data or self-assessment), current role requirements, and career pathway targets', 'Should', 'Talent Marketplace: individual profiles are the foundation of internal mobility matching'],
    ['FR-WIP-TM02', 'When a new internal opportunity is created (promotion, lateral move, project assignment), the system shall calculate a fit score for all employees whose competency profile matches the opportunity requirements within a configurable gap threshold', 'Should', 'Talent Marketplace: internal mobility match reduces time-to-fill and supports career development'],
    ['FR-WIP-TM03', 'The talent marketplace shall be accessible to employees as a self-service tool showing: current role competency requirements, assessed profile vs requirement gaps, recommended development actions, and open internal opportunities matching their profile', 'Could', 'Talent Marketplace: self-service career development is a retention tool'],
])

# 6.14 Visualisation (updated)
heading('6.14 Visualisation (Extended from H2R-SRNA-001)', 2)
body('All FR-VR01 through FR-VR09 and FR-VT01 through FR-VT08 from H2R-SRNA-001 are carried forward. The following new visualisation requirements are added.')
req_table([
    ['FR-WIP-VIS01', 'The strategic workforce planning dashboard shall display: 3-year capability gap heatmap by competency domain and department, Workforce Readiness Index trend, build/buy/borrow/bot recommendation summary, and scenario comparison panel', 'Must', 'Strategic WFP: executives require a single-screen strategic workforce view'],
    ['FR-WIP-VIS02', 'The operational workforce planning dashboard shall display: headcount plan vs approved budget vs actual, succession risk matrix (critical roles × pipeline strength), L&D investment vs capability gap closure, and quarterly forecast vs actuals', 'Must', 'Operational WFP: HR VPs and CPOs require the operational planning view'],
    ['FR-WIP-VIS03', 'The competency intelligence dashboard shall display: framework backbone coverage map, generated competency model library with version history, SME validation status, and UGESP documentation readiness indicator', 'Must', 'Competency: HR teams and workforce planning analysts need visibility into model quality and coverage'],
    ['FR-WIP-VIS04', 'The cascade engine health view shall display: coverage rates at each cascade layer, cascade breaks requiring action, plan vs actual metrics across all horizons, and a traffic light status for each layer (Green/Amber/Red)', 'Must', 'Cascade: cascade health must be visible to workforce planning leadership'],
])

# 6.15 Action Plan Engine (inherited)
heading('6.15 Action Plan Engine (Inherited from H2R-SRNA-001)', 2)
body('All FR-AP01 through FR-AP06 from H2R-SRNA-001 are carried forward unchanged. The action plan engine is extended to generate recommendations across all planning horizons, not only H2R process improvements.')

# ══════════════════════════════════════════════════════════════════════════════
# 7. NON-FUNCTIONAL REQUIREMENTS
# ══════════════════════════════════════════════════════════════════════════════
heading('7. Non-Functional Requirements', 1)
body('All NFR sections from H2R-SRNA-001 (Performance, Security & Compliance, Availability & Recovery, Scalability, Data Residency & Sovereignty) are carried forward unchanged. Key additions below.')
req_table([
    ['NFR-WIP-P01', 'Strategic workforce planning pipeline (capability gap calculation, scenario modelling, cascade propagation) shall complete within 30 minutes for an organisation of up to 10,000 employees', 'Must', 'Operations: strategic planning pipeline is run on-demand and must be responsive'],
    ['NFR-WIP-S01', 'Framework backbone data (O*NET, NICE, INCOSE SECF, R&M BoK) shall be stored in a read-only, immutable Bronze layer. No client process shall be able to modify framework source data', 'Must', 'Data integrity: framework backbone must be authoritative and unmodifiable'],
    ['NFR-WIP-SC01', 'The architecture shall support extension to AFECD military classification data in Phase 2 without fundamental redesign of the ontology or data model', 'Must', 'Strategy: defense clients require military occupational classification integration'],
    ['NFR-WIP-SC02', 'The competency model generation engine shall support multi-sector deployment: the same framework backbone and ontology shall serve defense, aerospace, cybersecurity, and engineering clients with sector-specific tailoring via configuration, not code change', 'Should', 'Strategy: platform must be commercially reusable across client sectors'],
])

# ══════════════════════════════════════════════════════════════════════════════
# 8. NOTIONAL ARCHITECTURE
# ══════════════════════════════════════════════════════════════════════════════
heading('8. Notional Architecture', 1)
heading('8.1 Architecture Overview', 2)
body(
    'The Workforce Intelligence Platform architecture extends the H2R platform\'s seven-layer '
    'stack with a new Strategic Intelligence Layer (Layer 5) and Cascade Engine (Layer 6). The '
    'H2R execution layers (SAP Sources, Ingestion, Lakehouse, Semantic/Ontology, Analytics) are '
    'unchanged. New layers handle multi-horizon workforce planning, competency intelligence, and '
    'bidirectional cascade.'
)

heading('8.2 Layer Definitions', 2)
simple_table(
    ['Layer', 'Name', 'Components', 'New vs Inherited'],
    [
        ['L0', 'Source Systems', 'SAP SuccessFactors, SAP HCM/ECC, SAP Payroll, O*NET API, NICE JSON, INCOSE SECF, R*M BoK, HRIS exports', 'Extended — framework sources added'],
        ['L1', 'Ingestion', 'CSV Export, OData API, MCP (Google Drive), O*NET API connector, Framework parsers, ADF/Glue', 'Extended — framework ingestion added'],
        ['L2', 'Lakehouse', 'Databricks Delta Lake (Bronze/Silver/Gold), Unity Catalog, MLflow, Workflows', 'Unchanged from H2R-SRNA-001'],
        ['L3', 'Semantic / Ontology', 'dbt/Cube Semantic Layer, HR+Process+Framework Ontology (OWL), Knowledge Graph (Neo4j), ChromaDB Vector Store', 'Extended — framework ontology added'],
        ['L4', 'Analytics Intelligence', 'PM4Py Process Mining, ML Models (RF+GBT), SHAP Explainability, Claude API Agent, Action Plan Engine', 'Unchanged from H2R-SRNA-001'],
        ['L5', 'Strategic Intelligence (NEW)', 'Strategic WFP Engine, Capability Gap Calculator, Scenario Modeller, Competency Model Generator, UGESP Documentation Engine, Talent Marketplace', 'NEW — not in H2R-SRNA-001'],
        ['L6', 'Cascade Engine (NEW)', 'Bidirectional cascade propagation, Plan synchronisation, Cascade break detection, Cross-horizon reporting', 'NEW — not in H2R-SRNA-001'],
        ['L7', 'Visualisation & Delivery', 'React Dashboard (all horizons), Tableau (strategic + exec), AI Agent Chat UI, Email/Teams Alerts, UGESP Document Generator', 'Extended — new dashboards added'],
    ]
)

heading('8.3 Cascade Engine Design', 2)
body(
    'The cascade engine operates as a scheduled and event-driven process within Databricks '
    'Workflows. It runs after each pipeline completion and on-demand when planning data changes. '
    'The cascade operates in two directions:'
)
body('TOP-DOWN CASCADE (Strategy → Execution):', bold=True)
bullet('Business strategy inputs → Strategic capability requirements → Operational headcount positions → Tactical requisition records → H2R case management')
bullet('Each transition is governed by an approval gate and produces audit records for governance')
body('BOTTOM-UP FEEDBACK (Execution → Strategy):', bold=True)
bullet('H2R case outcomes (hire accepted/declined, time-to-fill actual) → Tactical plan actuals → Operational headcount actuals → Strategic capability coverage update')
bullet('Attrition events → Succession risk recalculation → Strategic gap re-scoring')

heading('8.4 Updated Component Registry', 2)
body('Components C-01 through C-18 from H2R-SRNA-001 §7.2 are carried forward. The following new components are added.')
simple_table(
    ['ID', 'Component', 'Purpose', 'Technology', 'Tier', 'IT Question Ref'],
    [
        ['C-19', 'O*NET API Connector', 'Scheduled ingestion of occupational data from O*NET Web Services', 'REST API (X-API-Key), Python', 'Core', 'WIP-OG-01'],
        ['C-20', 'Framework Ontology Builder', 'Parses NICE, INCOSE SECF, R&M BoK into structured ontology entities', 'Python (spaCy + custom parsers)', 'Core', 'WIP-OG-01'],
        ['C-21', 'Competency Model Generator', 'AI-driven competency model drafting in INCOSE SECF format', 'Claude API + RAG over ChromaDB (framework backbone)', 'Core', 'IT-SEC-01'],
        ['C-22', 'Strategic WFP Engine', 'Capability gap calculation, scenario modelling, build/buy/borrow/bot analysis', 'Python + Databricks Notebooks + Delta Lake', 'Platform', 'None — open source logic'],
        ['C-23', 'UGESP Documentation Engine', 'Auto-generates legal technical documentation from competency models and job analysis data', 'Claude API + UGESP template library', 'Core', 'IT-SEC-01'],
        ['C-24', 'Cascade Engine', 'Bidirectional planning layer synchronisation and cascade break detection', 'Databricks Workflows + Delta Lake', 'Platform', 'IT-DB-01'],
        ['C-25', 'Talent Marketplace Engine', 'Competency-based internal mobility matching', 'pgvector / ChromaDB + Python scoring', 'Consumer', 'None'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 9. VISUALISATION ARCHITECTURE — PLANNING RHYTHM
# ══════════════════════════════════════════════════════════════════════════════
heading('9. Visualisation Architecture — Multi-Horizon Planning Rhythm', 1)
body(
    'The platform maintains distinct planning rhythms for each horizon. All rhythms are '
    'grounded in the same Databricks Gold layer, ensuring a single version of truth. The '
    'H2R execution rhythm from H2R-SRNA-001 §8.1 is carried forward unchanged.'
)

simple_table(
    ['Rhythm', 'Trigger', 'Action', 'Consumer', 'Horizon'],
    [
        ['Daily H2R Pipeline', '23:00 nightly', 'SAP ingestion → process mining → ML scoring → cascade feedback', 'All operations consumers', 'Execution'],
        ['Monthly Tactical Review', '1st of month', 'Tactical plan vs actuals → retention risk → cascade break detection → monthly exec pack', 'HR BP, TA Leads, HR Ops Mgr', 'Tactical'],
        ['Quarterly Operational Review', 'First Monday of quarter', 'Headcount plan vs budget vs actual → succession risk update → L&D progress → quarterly pack', 'HR VP, CPO, Dept Heads', 'Operational'],
        ['Annual Strategic WFP Cycle', 'September (align to budget cycle)', 'Capability gap recalculation → scenario modelling → build/buy/borrow/bot recommendations → 3-year plan refresh', 'CPO, HR VP, CFO, Business Leaders', 'Strategic'],
        ['Trigger: Major Event', 'Acquisition / contract award / restructure / new technology', 'Ad-hoc scenario modelling → cascade recalculation → revised strategic plan', 'CPO, HR VP, Executive Team', 'Strategic + Operational'],
        ['Annual Competency Model Review', 'Aligned to performance cycle', 'Framework backbone version check → model refresh → UGESP documentation update', 'Competency SME, Legal, HR BP', 'Operational'],
    ]
)

heading('9.1 Extended Tableau Workbook Specification', 2)
body('Workbooks 1–5 from H2R-SRNA-001 §8.2 are carried forward. The following new workbooks are added.')
simple_table(
    ['Workbook', 'Primary Audience', 'Key Views', 'Data Source', 'Refresh Cadence'],
    [
        ['6. Strategic Workforce Plan', 'CPO, HR VP, Business Leaders', '3-year capability gap heatmap, Workforce Readiness Index, build/buy/borrow/bot summary, scenario comparison', 'gold_strategic_wfp', 'Annual + on trigger'],
        ['7. Headcount Planning', 'HR VP, Finance, Dept Heads', 'Plan vs budget vs actual by dept/grade, succession risk matrix, pipeline strength, quarterly forecast', 'gold_headcount_plan', 'Monthly'],
        ['8. Competency Intelligence', 'HR BP, Competency SME, L&D', 'Competency model library, coverage map, proficiency distribution, gap closure trend, UGESP readiness', 'gold_competency_models', 'Monthly'],
        ['9. Talent Marketplace', 'HR BP, TA Recruiter, Line Manager', 'Internal mobility opportunities, fit score distribution, career pathway map, development plan status', 'gold_talent_marketplace', 'Weekly'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 10. TECHNOLOGY DECISIONS REQUIRED
# ══════════════════════════════════════════════════════════════════════════════
heading('10. Technology Decisions Required', 1)
body('Technology decisions TD-01 through TD-10 from H2R-SRNA-001 §10 are carried forward. The following new decisions are added.')
simple_table(
    ['Decision ID', 'Decision Required', 'Options', 'Phase 1 Blocking?', 'IT Owner'],
    [
        ['TD-11', 'O*NET API key registration', 'Register at services.onetcenter.org (free, requires organisational registration)', 'YES — required before framework backbone ingestion', 'HR Transformation'],
        ['TD-12', 'Ontology modelling tool', 'Protégé (open source OWL editor) · TopBraid Composer · Custom JSON-LD', 'No — defaults to Protégé if no preference', 'Data Engineering'],
        ['TD-13', 'UGESP documentation output format', 'Word/DOCX · PDF · HTML · All three', 'No — defaults to Word + PDF', 'Legal / HR'],
        ['TD-14', 'Competency model SME validation workflow', 'Email-based review · Platform workflow (React) · SharePoint form', 'No — deferred to Sprint 3', 'HR Transformation'],
        ['TD-15', 'Talent marketplace scope for Phase 1', 'Internal mobility matching only · Full self-service employee portal · None (Phase 2)', 'No — MVP defaults to internal mobility only', 'CPO / HR VP'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 11. ASSUMPTIONS & CONSTRAINTS
# ══════════════════════════════════════════════════════════════════════════════
heading('11. Assumptions & Constraints', 1)
heading('11.1 Assumptions', 2)
body('Assumptions A01–A10 from H2R-SRNA-001 §11.1 are carried forward. The following are added.')
bullet('A11: The O*NET Web Services API is accessible from the Databricks cloud environment. An organisational API key will be registered before Sprint 1.')
bullet('A12: NICE Framework v2.2 (April 2025 release) JSON data is publicly available and will be downloaded as static seed data for the ontology build.')
bullet('A13: INCOSE SECF (INCOSE-TP-2018-002-01.0) competency definitions can be parsed from the published PDF into structured data. No licence restriction prevents this use within an internal platform.')
bullet('A14: The R&M BoK (December 2025) lifecycle-competency mappings can be parsed from the publicly released document. Distribution Statement A confirms public release.')
bullet('A15: An initial competency model for at least three role families will be generated and validated in Phase 1 as proof of concept for the competency intelligence module.')
bullet('A16: The platform operator has or will obtain a Data Processing Agreement with Anthropic before using the Claude API in production (NFR-DR03 from H2R-SRNA-001 applies).')
bullet('A17: A Workforce Planning SME (0.5 FTE) with experience in strategic workforce planning methodology is available throughout the 12-week build for framework validation, scenario configuration, and UAT.')

heading('11.2 Constraints', 2)
body('Constraints C01–C06 from H2R-SRNA-001 §11.2 are carried forward. The following are added.')
bullet('C07: AFECD military classification data integration is Phase 2 — the ontology data model in Phase 1 must be designed to accommodate AFSC entities without structural change.')
bullet('C08: Full SIOP-compliant structured job analysis data collection (SME interviews, task rating surveys) is out of scope for Phase 1. The platform seeds competency models from framework backbone data; human validation is Sprint 3+.')
bullet('C09: External talent market data (Lightcast, LinkedIn Talent Insights) is Phase 2. Phase 1 workforce analytics are based solely on internal data and framework backbone.')

# ══════════════════════════════════════════════════════════════════════════════
# 12. OPEN QUESTIONS REGISTER
# ══════════════════════════════════════════════════════════════════════════════
heading('12. Open Questions Register', 1)
body('Open questions Q-01 through Q-14 from H2R-SRNA-001 §12 are carried forward. The following are added.')
simple_table(
    ['Ref', 'Question', 'Owner', 'Priority', 'Status'],
    [
        ['WIP-OG-01', 'Does AeroDefend Group have an existing job family taxonomy, grade structure, or competency framework in structured format? This seeds the HR domain ontology.', 'HR + IT', 'CRITICAL', 'Open'],
        ['WIP-OG-02', 'What is the current state of AeroDefend Group\'s workforce data? HRIS export available? Position descriptions in structured format? Incumbent competency profiles?', 'HR + IT', 'CRITICAL', 'Open'],
        ['WIP-SWP-01', 'Does AeroDefend Group have an existing strategic workforce planning process or methodology? If so, the platform should align to it rather than replace it.', 'CPO / HR VP', 'HIGH', 'Open'],
        ['WIP-SWP-02', 'What business strategy inputs are available to seed the 3-year capability requirements? (Business plan, programme pipeline, technology roadmap, contract forecast)', 'CPO / Business Leadership', 'HIGH', 'Open'],
        ['WIP-CI-01', 'Which role families should be prioritised for Phase 1 competency model generation? (Recommendation: Systems Engineers, R&M Engineers, Cybersecurity roles as framework backbone coverage is strongest for these)', 'HR VP / CPO', 'HIGH', 'Open'],
        ['WIP-UGESP-01', 'Has Legal confirmed that platform-generated competency models and UGESP documentation will be reviewed by a qualified I-O psychologist before use in hiring decisions? This is a legal risk management question.', 'Legal / CISO', 'HIGH', 'Open'],
        ['WIP-API-01', 'O*NET API registration: who will register for the O*NET Web Services API key? (Requires organisational registration at services.onetcenter.org)', 'HR Transformation', 'MEDIUM', 'Open'],
        ['WIP-AFECD-01', 'For Phase 2 AFECD integration: what military occupational data is held internally? Is there an existing AFSC-to-civilian role mapping that should seed the Phase 2 ontology?', 'HR + IT', 'LOW', 'Open'],
    ]
)

body('\nNext Steps', bold=True)
bullet('1. Review this document alongside H2R-SRNA-001. This document supersedes H2R-SRNA-001 for the full platform scope.')
bullet('2. Resolve all CRITICAL open questions (WIP-OG-01, WIP-OG-02 and H2R-SRNA-001 IT-INFRA-01, IT-SAP-01) before Sprint 1.')
bullet('3. HR and CPO review of Section 6.7–6.9 (Strategic, Operational, Tactical WFP modules) to confirm scope and prioritisation.')
bullet('4. Legal review of Section 6.12 (UGESP Compliance Engine) before competency models are used in any selection decision.')
bullet('5. Confirm Phase 1 competency model priority role families (WIP-CI-01).')
bullet('6. Sprint 0: confirm team, environments, SAP data access, O*NET API key, and framework backbone data download.')

# ══════════════════════════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════════════════════════
output_path = r'C:\Users\traft\Desktop\WIP-SRNA-001-v1.0.docx'
doc.save(output_path)
print(f'Document saved: {output_path}')
