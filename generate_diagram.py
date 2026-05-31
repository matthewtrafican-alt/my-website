"""
Generates the Workforce Intelligence Platform layered architecture diagram.
Extends the H2R-SRNA-001 Figure 6.1 with two new layers:
  L5 Strategic Intelligence
  L6 Cascade Engine
Output: platform-demo/assets/architecture.png
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

os.makedirs('platform-demo/assets', exist_ok=True)

# ── Colour palette ─────────────────────────────────────────────────────────
LAYER_COLORS = {
    'sap':        {'bg': '#D6E4F7', 'border': '#2E75B6', 'label': '#1F3864', 'box': '#4472C4'},
    'ingestion':  {'bg': '#D6E4F7', 'border': '#2E75B6', 'label': '#1F3864', 'box': '#5B9BD5'},
    'lake':       {'bg': '#E2EFDA', 'border': '#548235', 'label': '#375623', 'box': '#70AD47'},
    'semantic':   {'bg': '#EAD1DC', 'border': '#843C5C', 'label': '#5C273F', 'box': '#9B3D6A'},
    'analytics':  {'bg': '#FCE4D6', 'border': '#C45911', 'label': '#833C00', 'box': '#ED7D31'},
    'strategic':  {'bg': '#C5D9F1', 'border': '#1F3864', 'label': '#0D1F42', 'box': '#1F3864'},
    'cascade':    {'bg': '#D9E6F5', 'border': '#2E75B6', 'label': '#1F3864', 'box': '#2E75B6'},
    'viz':        {'bg': '#E2EFDA', 'border': '#375623', 'label': '#1E3A13', 'box': '#548235'},
    'actions':    {'bg': '#FCDEDE', 'border': '#9C0006', 'label': '#9C0006', 'box': '#C00000'},
}

# ── Layer definitions (L0 → L8) ─────────────────────────────────────────────
LAYERS = [
    {
        'id': 'L0', 'name': 'Source\nSystems', 'style': 'sap',
        'boxes': ['SAP\nSuccessFactors', 'SAP HCM\n/ ECC + Payroll', 'SAP PS\n(Programme Mgmt)', 'O*NET · NICE\nINCOSE · R&M BoK', 'Engagement\nSurvey Platform'],
        'new': False,
    },
    {
        'id': 'L1', 'name': 'Ingestion\nLayer', 'style': 'ingestion',
        'boxes': ['Flat Files / JSON\n(Phase 1 — 274 sample)', 'SAP OData API\n(Phase 2)', 'Programme Registry\n& Allocation Data', 'Azure Data Factory\n/ AWS Glue', 'Framework\nParsers (Python)'],
        'new': False,
    },
    {
        'id': 'L2', 'name': 'Databricks\nLakehouse', 'style': 'lake',
        'boxes': ['Bronze Layer\n(Raw / Immutable)', 'Silver Layer\n(Cleansed / PII masked)', 'Gold Layer\n(Aggregated / ML-ready)', 'MLflow\nModel Registry', 'Databricks\nWorkflows'],
        'new': False,
    },
    {
        'id': 'L3', 'name': 'Semantic &\nOntology', 'style': 'semantic',
        'boxes': ['Semantic Layer\n(dbt / Cube.dev)', 'HR + Framework\nOntology (OWL)', 'Function × Programme\nOntology', 'Knowledge Graph\n(Neo4j)', 'ChromaDB\nVector Store'],
        'new': False,
    },
    {
        'id': 'L4', 'name': 'AI &\nAnalytics', 'style': 'analytics',
        'boxes': ['PM4Py\nProcess Mining', 'ML Models + Temporal\nAnalytics Engine', 'SHAP\nExplainability', 'Claude API\nAI Agent + RAG', 'Resource Allocation\nEngine'],
        'new': False,
    },
    {
        'id': 'L5', 'name': 'Strategic\nIntelligence', 'style': 'strategic',
        'boxes': ['Functional View\n(12 Functions)', 'Program View\n(3 Portfolios · 9 Progs)', 'Four Temporal\nDimensions Engine', 'ROAD Action\nPlan Engine', 'Prompt Library\n(280 Diagnostics)'],
        'new': True,
    },
    {
        'id': 'L6', 'name': 'Cascade\nEngine', 'style': 'cascade',
        'boxes': ['Function × Programme\nAllocation Matrix', 'Phase Experience\nGap Analysis', 'Cascade Break\nDetection', '"Ahead of Ready"\nLead Time Engine', 'Cross-Horizon\nReporting'],
        'new': True,
    },
    {
        'id': 'L7', 'name': 'Visualisation\n& UX', 'style': 'viz',
        'boxes': ['AI Workspace\n+ Prompt Library UI', 'Functional / Program\nDual-View Dashboard', 'Temporal View\n& Allocation Matrix', 'Tableau\n(Strategic)', 'ROAD Health\nHeatmap'],
        'new': False,
    },
    {
        'id': 'L8', 'name': 'Actions &\nAlerts', 'style': 'actions',
        'boxes': ['Return on Impact\nAction Plans', 'Teams\nWebhook', 'Compliance\nSentinel', 'Scheduled\nReports', 'Workflow\nTriggers'],
        'new': False,
    },
]

# ── Canvas setup ─────────────────────────────────────────────────────────────
FIG_W, FIG_H = 20, 22
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')

# ── Title ────────────────────────────────────────────────────────────────────
ax.text(FIG_W / 2, FIG_H - 0.4,
        'Workforce Intelligence Platform — Layered Architecture v3.0',
        ha='center', va='top', fontsize=14, fontweight='bold', color='#1F3864')
ax.text(FIG_W / 2, FIG_H - 0.85,
        'WIP-SRNA-001 v3.0   ·   50K FTE Enterprise Scale   ·   12 Functions · 9 Programmes · 3 Portfolios   ·   L5 & L6 are new',
        ha='center', va='top', fontsize=8, color='#666666', style='italic')

# ── Layout constants ─────────────────────────────────────────────────────────
N_LAYERS   = len(LAYERS)
TOP_MARGIN = 1.5          # space below title
BOT_MARGIN = 1.6          # space for legend
LAYER_H    = (FIG_H - TOP_MARGIN - BOT_MARGIN) / N_LAYERS
LABEL_W    = 1.4
PAD        = 0.18
BOX_AREA_W = FIG_W - LABEL_W - 0.3
N_BOXES    = 5
BOX_W      = (BOX_AREA_W - (N_BOXES + 1) * PAD) / N_BOXES
BOX_H      = LAYER_H * 0.66
ARROW_X    = LABEL_W + BOX_AREA_W / 2 + 0.15

def draw_rounded_rect(ax, x, y, w, h, color, edgecolor, alpha=1.0, lw=1.0, radius=0.12):
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f'round,pad=0,rounding_size={radius}',
                         facecolor=color, edgecolor=edgecolor,
                         linewidth=lw, alpha=alpha, zorder=3)
    ax.add_patch(box)

# ── Draw layers bottom-up (L0 at top visually means highest y-value) ────────
for i, layer in enumerate(LAYERS):
    # y position: L0 at top
    layer_y_top = FIG_H - TOP_MARGIN - i * LAYER_H
    layer_y_bot = layer_y_top - LAYER_H
    layer_mid_y = (layer_y_top + layer_y_bot) / 2

    s = LAYER_COLORS[layer['style']]

    # ── Layer background ──────────────────────────────────────────────────
    bg_rect = FancyBboxPatch((0.1, layer_y_bot + 0.04),
                              FIG_W - 0.2, LAYER_H - 0.08,
                              boxstyle='round,pad=0,rounding_size=0.1',
                              facecolor=s['bg'], edgecolor=s['border'],
                              linewidth=1.5 if layer['new'] else 0.8,
                              linestyle='--' if layer['new'] else '-',
                              alpha=0.6, zorder=1)
    ax.add_patch(bg_rect)

    # ── NEW badge ─────────────────────────────────────────────────────────
    if layer['new']:
        ax.text(FIG_W - 0.3, layer_y_top - 0.18, '★ NEW',
                ha='right', va='top', fontsize=7, fontweight='bold',
                color=s['label'],
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFACD',
                          edgecolor=s['border'], linewidth=0.8, alpha=0.9))

    # ── Layer ID label ────────────────────────────────────────────────────
    ax.text(0.1 + LABEL_W / 2, layer_mid_y,
            f'{layer["id"]}\n{layer["name"]}',
            ha='center', va='center', fontsize=8, fontweight='bold',
            color=s['label'], zorder=4)

    # ── Component boxes ───────────────────────────────────────────────────
    box_x_start = LABEL_W + 0.15
    for j, label in enumerate(layer['boxes']):
        bx = box_x_start + j * (BOX_W + PAD) + PAD
        by = layer_mid_y - BOX_H / 2

        draw_rounded_rect(ax, bx, by, BOX_W, BOX_H,
                          color='white', edgecolor=s['border'],
                          lw=1.2 if layer['new'] else 0.8)

        # Top colour bar
        bar = FancyBboxPatch((bx, by + BOX_H - 0.13), BOX_W, 0.13,
                              boxstyle='round,pad=0,rounding_size=0.06',
                              facecolor=s['box'], edgecolor='none',
                              alpha=0.85, zorder=4)
        ax.add_patch(bar)

        ax.text(bx + BOX_W / 2, by + BOX_H / 2 - 0.04,
                label, ha='center', va='center',
                fontsize=6.8, color='#1A1A2E', zorder=5,
                linespacing=1.3)

# ── Flow arrows between layers ───────────────────────────────────────────────
ARROW_LABELS = [
    'Delta Lake write',
    'governed queries',
    'RAG + context retrieval',
    'AI insights',
    'strategic intelligence',
    'cascade propagation',
    'insights + responses',
    'actions + notifications',
]
for i in range(len(LAYERS) - 1):
    y_from = FIG_H - TOP_MARGIN - (i + 1) * LAYER_H + 0.04
    y_to   = y_from - 0.01
    mid_y  = (y_from + y_to) / 2 + LAYER_H * 0.02

    ax.annotate('', xy=(ARROW_X, y_from - LAYER_H * 0.04 + 0.02),
                xytext=(ARROW_X, y_from),
                arrowprops=dict(arrowstyle='->', color='#555555',
                                lw=1.2, mutation_scale=10),
                zorder=6)

    if i < len(ARROW_LABELS):
        ax.text(ARROW_X + 0.18, y_from - LAYER_H * 0.02,
                ARROW_LABELS[i],
                ha='left', va='center', fontsize=6.5,
                color='#666666', style='italic', zorder=6)

# ── Legend ───────────────────────────────────────────────────────────────────
legend_items = [
    ('SAP / Ingestion',       '#4472C4'),
    ('Databricks Lakehouse',  '#70AD47'),
    ('Semantic / Ontology',   '#9B3D6A'),
    ('AI & Analytics',        '#ED7D31'),
    ('Strategic Intelligence','#1F3864'),
    ('Cascade Engine',        '#2E75B6'),
    ('Visualisation',         '#548235'),
    ('Actions & Compliance',  '#C00000'),
]
leg_y = 0.9
leg_x_start = 0.5
leg_item_w  = (FIG_W - 1.0) / len(legend_items)

for k, (label, color) in enumerate(legend_items):
    lx = leg_x_start + k * leg_item_w
    ax.add_patch(plt.Rectangle((lx, leg_y - 0.15), 0.35, 0.22,
                                facecolor=color, edgecolor='none',
                                alpha=0.85, zorder=4))
    ax.text(lx + 0.42, leg_y - 0.04, label,
            ha='left', va='center', fontsize=6.5, color='#333333')

ax.text(FIG_W / 2, 0.35,
        'Figure 8.1: Layered Architecture v3.0 — Nine-layer enterprise stack · top-to-bottom data flow · 50K FTE scale\n'
        '★ L5 (Strategic Intelligence): Functional/Program dual view, temporal dimensions, ROAD action engine, prompt library\n'
        '★ L6 (Cascade Engine): Function × Programme allocation matrix, phase experience gap, Ahead of Ready lead time',
        ha='center', va='center', fontsize=7.5, color='#444444', style='italic')

plt.tight_layout(pad=0.3)
plt.savefig('platform-demo/assets/architecture.png',
            dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.close()
print('Diagram saved: platform-demo/assets/architecture.png')
