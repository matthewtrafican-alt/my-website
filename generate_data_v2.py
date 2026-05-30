"""
Workforce Intelligence Platform — Enterprise Data Generator v2.0
Generates synthetic data representing a 50K-employee defence/aerospace organisation.
~275 sample employees with scale factors for extrapolation to full workforce.

Outputs (platform-demo/assets/):
  portfolios.json        — 3 portfolios
  functions.json         — 12 functional organisations with subdisciplines + scale factors
  programs_v2.json       — 9 programs with portfolio linkage + acquisition phase
  employees_v2.json      — ~275 employees with temporal dimensions + function/subdiscipline
  allocation_matrix.json — Function x Program resource allocation with FTE%, headcount, risk
"""

import json, random, math, os
from datetime import datetime

random.seed(42)
os.makedirs('platform-demo/assets', exist_ok=True)

def save(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# ── Acquisition phases ─────────────────────────────────────────────────────
ACQ_PHASES = ['MSA', 'TMRR', 'EMD', 'P&D', 'O&S']
ACQ_PHASE_LABELS = {
    'MSA':  'Materiel Solution Analysis',
    'TMRR': 'Technology Maturation & Risk Reduction',
    'EMD':  'Engineering & Manufacturing Development',
    'P&D':  'Production & Deployment',
    'O&S':  'Operations & Support',
}

# ══════════════════════════════════════════════════════════════════════════════
# 1. PORTFOLIOS
# ══════════════════════════════════════════════════════════════════════════════
portfolios = [
    {
        'id': 'PORT-AIR',
        'name': 'Air Systems Portfolio',
        'short': 'Air Systems',
        'color': '#3b82f6',
        'programs': ['PRG-001', 'PRG-002', 'PRG-003'],
        'value_gbp': 2840,
        'delivery_risk_score': 67,
        'delivery_risk_label': 'High',
    },
    {
        'id': 'PORT-GND',
        'name': 'Ground Defence & Missiles Portfolio',
        'short': 'Ground Defence',
        'color': '#f59e0b',
        'programs': ['PRG-004', 'PRG-005', 'PRG-006'],
        'value_gbp': 1620,
        'delivery_risk_score': 44,
        'delivery_risk_label': 'Medium',
    },
    {
        'id': 'PORT-CEW',
        'name': 'Cyber, EW & ISR Portfolio',
        'short': 'Cyber/EW/ISR',
        'color': '#8b5cf6',
        'programs': ['PRG-007', 'PRG-008', 'PRG-009'],
        'value_gbp': 980,
        'delivery_risk_score': 71,
        'delivery_risk_label': 'High',
    },
]

# ══════════════════════════════════════════════════════════════════════════════
# 2. FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════
FUNCTIONS_DEF = [
    {
        'id': 'FN-SE',  'code': 'SE',
        'name': 'Systems Engineering',
        'headcount_actual': 9200,
        'headcount_sample': 46,
        'subdisciplines': [
            'Mission Systems Architecture',
            'Avionics Integration',
            'Systems Architecture',
            'Safety & Certification',
            'Systems Integration & Test',
        ],
        'clearance_profile': {'Baseline': 0.15, 'Security Check (SC)': 0.55, 'Developed Vetting (DV)': 0.30},
        'market_demand': 'Very High',
        'road_retain': 62, 'road_optimize': 71, 'road_acquire': 55, 'road_develop': 68,
    },
    {
        'id': 'FN-RM',  'code': 'RM',
        'name': 'R&M Engineering',
        'headcount_actual': 7800,
        'headcount_sample': 39,
        'subdisciplines': [
            'Reliability Analysis',
            'Maintainability Engineering',
            'Integrated Logistics Support',
            'Technical Publications',
            'Field Support Engineering',
        ],
        'clearance_profile': {'Baseline': 0.20, 'Security Check (SC)': 0.60, 'Developed Vetting (DV)': 0.20},
        'market_demand': 'High',
        'road_retain': 71, 'road_optimize': 65, 'road_acquire': 63, 'road_develop': 59,
    },
    {
        'id': 'FN-SW',  'code': 'SW',
        'name': 'Software Engineering',
        'headcount_actual': 6200,
        'headcount_sample': 31,
        'subdisciplines': [
            'Embedded Software',
            'Mission Software',
            'DevSecOps',
            'Verification & Validation',
            'AI/ML Engineering',
        ],
        'clearance_profile': {'Baseline': 0.10, 'Security Check (SC)': 0.50, 'Developed Vetting (DV)': 0.40},
        'market_demand': 'Critical',
        'road_retain': 48, 'road_optimize': 69, 'road_acquire': 41, 'road_develop': 74,
    },
    {
        'id': 'FN-CS',  'code': 'CS',
        'name': 'Cybersecurity',
        'headcount_actual': 3800,
        'headcount_sample': 19,
        'subdisciplines': [
            'IA & Accreditation',
            'Secure Software Development',
            'Penetration Testing',
            'TEMPEST & Emissions Security',
            'Crypto Engineering',
        ],
        'clearance_profile': {'Baseline': 0.05, 'Security Check (SC)': 0.35, 'Developed Vetting (DV)': 0.60},
        'market_demand': 'Critical',
        'road_retain': 44, 'road_optimize': 66, 'road_acquire': 38, 'road_develop': 72,
    },
    {
        'id': 'FN-MS',  'code': 'MS',
        'name': 'Mission Systems',
        'headcount_actual': 5400,
        'headcount_sample': 27,
        'subdisciplines': [
            'Radar Systems',
            'Electronic Warfare & Countermeasures',
            'Communications & Datalinks',
            'Weapons Integration',
            'Sensor Systems',
        ],
        'clearance_profile': {'Baseline': 0.05, 'Security Check (SC)': 0.40, 'Developed Vetting (DV)': 0.55},
        'market_demand': 'Very High',
        'road_retain': 59, 'road_optimize': 72, 'road_acquire': 52, 'road_develop': 65,
    },
    {
        'id': 'FN-ST',  'code': 'ST',
        'name': 'Systems Integration & Test',
        'headcount_actual': 4100,
        'headcount_sample': 21,
        'subdisciplines': [
            'Integration Planning',
            'Test Engineering',
            'Ground Test & Evaluation',
            'Flight Test Support',
            'Test Lab Management',
        ],
        'clearance_profile': {'Baseline': 0.15, 'Security Check (SC)': 0.55, 'Developed Vetting (DV)': 0.30},
        'market_demand': 'High',
        'road_retain': 68, 'road_optimize': 74, 'road_acquire': 61, 'road_develop': 63,
    },
    {
        'id': 'FN-PM',  'code': 'PM',
        'name': 'Programme Management',
        'headcount_actual': 4600,
        'headcount_sample': 23,
        'subdisciplines': [
            'Schedule Management',
            'Risk Management',
            'Earned Value Management',
            'Stakeholder Engagement',
            'Configuration Management',
        ],
        'clearance_profile': {'Baseline': 0.20, 'Security Check (SC)': 0.55, 'Developed Vetting (DV)': 0.25},
        'market_demand': 'Medium',
        'road_retain': 73, 'road_optimize': 68, 'road_acquire': 70, 'road_develop': 66,
    },
    {
        'id': 'FN-QS',  'code': 'QS',
        'name': 'Quality & Safety',
        'headcount_actual': 2900,
        'headcount_sample': 15,
        'subdisciplines': [
            'Quality Assurance',
            'Safety Case Management',
            'Airworthiness',
            'Process Improvement',
            'Supplier Quality',
        ],
        'clearance_profile': {'Baseline': 0.25, 'Security Check (SC)': 0.60, 'Developed Vetting (DV)': 0.15},
        'market_demand': 'Medium',
        'road_retain': 76, 'road_optimize': 70, 'road_acquire': 72, 'road_develop': 61,
    },
    {
        'id': 'FN-LS',  'code': 'LS',
        'name': 'Logistics & Supportability',
        'headcount_actual': 3200,
        'headcount_sample': 16,
        'subdisciplines': [
            'Integrated Logistics Support',
            'Supply Chain Management',
            'Spares Provisioning',
            'Training Systems',
            'Technical Data Management',
        ],
        'clearance_profile': {'Baseline': 0.30, 'Security Check (SC)': 0.55, 'Developed Vetting (DV)': 0.15},
        'market_demand': 'Medium',
        'road_retain': 74, 'road_optimize': 67, 'road_acquire': 68, 'road_develop': 60,
    },
    {
        'id': 'FN-FC',  'code': 'FC',
        'name': 'Finance & Commercial',
        'headcount_actual': 2100,
        'headcount_sample': 11,
        'subdisciplines': [
            'Contract Management',
            'Pricing & Estimating',
            'Financial Reporting',
            'Procurement',
            'Cost Engineering',
        ],
        'clearance_profile': {'Baseline': 0.40, 'Security Check (SC)': 0.50, 'Developed Vetting (DV)': 0.10},
        'market_demand': 'Low',
        'road_retain': 78, 'road_optimize': 72, 'road_acquire': 75, 'road_develop': 64,
    },
    {
        'id': 'FN-HR',  'code': 'HR',
        'name': 'Human Resources',
        'headcount_actual': 1800,
        'headcount_sample': 9,
        'subdisciplines': [
            'HR Business Partnering',
            'Talent Acquisition',
            'Learning & Development',
            'HR Operations & Reward',
            'Workforce Planning & Analytics',
        ],
        'clearance_profile': {'Baseline': 0.50, 'Security Check (SC)': 0.45, 'Developed Vetting (DV)': 0.05},
        'market_demand': 'Low',
        'road_retain': 80, 'road_optimize': 69, 'road_acquire': 77, 'road_develop': 71,
    },
    {
        'id': 'FN-IT',  'code': 'IT',
        'name': 'IT & Digital Engineering',
        'headcount_actual': 3400,
        'headcount_sample': 17,
        'subdisciplines': [
            'PLM & CAD Systems',
            'Digital Twin & Simulation',
            'IT Infrastructure',
            'Data Engineering & Analytics',
            'DevOps & Cloud Platform',
        ],
        'clearance_profile': {'Baseline': 0.20, 'Security Check (SC)': 0.55, 'Developed Vetting (DV)': 0.25},
        'market_demand': 'High',
        'road_retain': 55, 'road_optimize': 71, 'road_acquire': 50, 'road_develop': 70,
    },
]

functions = []
for fn in FUNCTIONS_DEF:
    scale = round(fn['headcount_actual'] / fn['headcount_sample'], 1)
    functions.append({
        **fn,
        'scale_factor': scale,
        'road_health': {
            'Retain':   fn['road_retain'],
            'Optimize': fn['road_optimize'],
            'Acquire':  fn['road_acquire'],
            'Develop':  fn['road_develop'],
            'overall':  round((fn['road_retain']+fn['road_optimize']+fn['road_acquire']+fn['road_develop'])/4),
        }
    })

total_actual = sum(f['headcount_actual'] for f in functions)

# ══════════════════════════════════════════════════════════════════════════════
# 3. PROGRAMS
# ══════════════════════════════════════════════════════════════════════════════
programs_v2 = [
    # Air Systems Portfolio
    {
        'id': 'PRG-001', 'portfolio_id': 'PORT-AIR',
        'name': 'Typhoon Modernisation Block 20',
        'short': 'Typhoon Mod',
        'customer': 'Royal Air Force',
        'value_gbp': 420, 'phase': 'EMD',
        'phase_label': ACQ_PHASE_LABELS['EMD'],
        'delivery_risk_score': 61, 'delivery_risk_label': 'High',
        'milestones': [
            {'name': 'Critical Design Review',  'date': '2025-03', 'status': 'At Risk'},
            {'name': 'System Integration Test',  'date': '2025-09', 'status': 'On Track'},
            {'name': 'First Aircraft Delivery',  'date': '2027-02', 'status': 'At Risk'},
        ],
        'functions_required': {
            'FN-SE': {'headcount': 220, 'criticality': 'High'},
            'FN-RM': {'headcount': 180, 'criticality': 'High'},
            'FN-SW': {'headcount': 150, 'criticality': 'High'},
            'FN-MS': {'headcount': 120, 'criticality': 'Critical'},
            'FN-ST': {'headcount': 90,  'criticality': 'High'},
            'FN-CS': {'headcount': 60,  'criticality': 'High'},
            'FN-PM': {'headcount': 80,  'criticality': 'Medium'},
            'FN-QS': {'headcount': 50,  'criticality': 'Medium'},
        },
    },
    {
        'id': 'PRG-002', 'portfolio_id': 'PORT-AIR',
        'name': 'Future Combat Air System',
        'short': 'FCAS',
        'customer': 'MOD / Partner Nations',
        'value_gbp': 890, 'phase': 'TMRR',
        'phase_label': ACQ_PHASE_LABELS['TMRR'],
        'delivery_risk_score': 74, 'delivery_risk_label': 'High',
        'milestones': [
            {'name': 'Capability Development Doc', 'date': '2025-06', 'status': 'On Track'},
            {'name': 'Tech Demonstration Phase',   'date': '2026-03', 'status': 'At Risk'},
            {'name': 'EMD Gate Review',             'date': '2027-09', 'status': 'At Risk'},
        ],
        'functions_required': {
            'FN-SE': {'headcount': 380, 'criticality': 'Critical'},
            'FN-SW': {'headcount': 290, 'criticality': 'Critical'},
            'FN-MS': {'headcount': 240, 'criticality': 'Critical'},
            'FN-CS': {'headcount': 180, 'criticality': 'High'},
            'FN-RM': {'headcount': 160, 'criticality': 'High'},
            'FN-ST': {'headcount': 130, 'criticality': 'High'},
            'FN-PM': {'headcount': 120, 'criticality': 'High'},
            'FN-IT': {'headcount': 90,  'criticality': 'Medium'},
        },
    },
    {
        'id': 'PRG-003', 'portfolio_id': 'PORT-AIR',
        'name': 'Eurofighter E-Scan Radar Upgrade',
        'short': 'E-Scan Upgrade',
        'customer': 'Multi-Nation Consortium',
        'value_gbp': 310, 'phase': 'P&D',
        'phase_label': ACQ_PHASE_LABELS['P&D'],
        'delivery_risk_score': 38, 'delivery_risk_label': 'Medium',
        'milestones': [
            {'name': 'Production Readiness Review', 'date': '2025-04', 'status': 'On Track'},
            {'name': 'First Production Unit',        'date': '2025-12', 'status': 'On Track'},
            {'name': 'Full Rate Production',         'date': '2026-06', 'status': 'On Track'},
        ],
        'functions_required': {
            'FN-MS': {'headcount': 180, 'criticality': 'Critical'},
            'FN-SE': {'headcount': 140, 'criticality': 'High'},
            'FN-SW': {'headcount': 110, 'criticality': 'High'},
            'FN-QS': {'headcount': 80,  'criticality': 'High'},
            'FN-LS': {'headcount': 70,  'criticality': 'Medium'},
            'FN-PM': {'headcount': 60,  'criticality': 'Medium'},
        },
    },
    # Ground Defence Portfolio
    {
        'id': 'PRG-004', 'portfolio_id': 'PORT-GND',
        'name': 'Air Defence Command & Control',
        'short': 'ADCC',
        'customer': 'British Army',
        'value_gbp': 520, 'phase': 'EMD',
        'phase_label': ACQ_PHASE_LABELS['EMD'],
        'delivery_risk_score': 55, 'delivery_risk_label': 'Medium',
        'milestones': [
            {'name': 'System Requirements Review', 'date': '2025-02', 'status': 'On Track'},
            {'name': 'Preliminary Design Review',  'date': '2025-08', 'status': 'At Risk'},
            {'name': 'CDR Gate',                   'date': '2026-04', 'status': 'At Risk'},
        ],
        'functions_required': {
            'FN-SW': {'headcount': 200, 'criticality': 'Critical'},
            'FN-SE': {'headcount': 160, 'criticality': 'High'},
            'FN-CS': {'headcount': 140, 'criticality': 'Critical'},
            'FN-MS': {'headcount': 100, 'criticality': 'High'},
            'FN-PM': {'headcount': 80,  'criticality': 'Medium'},
            'FN-IT': {'headcount': 60,  'criticality': 'Medium'},
        },
    },
    {
        'id': 'PRG-005', 'portfolio_id': 'PORT-GND',
        'name': 'SKYSHIELD Ground Integration',
        'short': 'SKYSHIELD',
        'customer': 'Export / Partner Nation',
        'value_gbp': 680, 'phase': 'EMD',
        'phase_label': ACQ_PHASE_LABELS['EMD'],
        'delivery_risk_score': 42, 'delivery_risk_label': 'Medium',
        'milestones': [
            {'name': 'Interface Control Document', 'date': '2025-05', 'status': 'On Track'},
            {'name': 'Hardware Delivery',          'date': '2026-01', 'status': 'On Track'},
            {'name': 'Operational Test',           'date': '2026-09', 'status': 'On Track'},
        ],
        'functions_required': {
            'FN-SE': {'headcount': 200, 'criticality': 'High'},
            'FN-RM': {'headcount': 160, 'criticality': 'High'},
            'FN-SW': {'headcount': 120, 'criticality': 'Medium'},
            'FN-ST': {'headcount': 100, 'criticality': 'High'},
            'FN-LS': {'headcount': 80,  'criticality': 'Medium'},
        },
    },
    {
        'id': 'PRG-006', 'portfolio_id': 'PORT-GND',
        'name': 'SHORAD Missile Enhancement',
        'short': 'SHORAD',
        'customer': 'MOD / Export',
        'value_gbp': 420, 'phase': 'MSA',
        'phase_label': ACQ_PHASE_LABELS['MSA'],
        'delivery_risk_score': 28, 'delivery_risk_label': 'Low',
        'milestones': [
            {'name': 'Analysis of Alternatives', 'date': '2025-09', 'status': 'On Track'},
            {'name': 'AOA Decision Brief',        'date': '2026-03', 'status': 'On Track'},
        ],
        'functions_required': {
            'FN-SE': {'headcount': 80,  'criticality': 'Medium'},
            'FN-MS': {'headcount': 60,  'criticality': 'High'},
            'FN-PM': {'headcount': 40,  'criticality': 'Medium'},
            'FN-FC': {'headcount': 30,  'criticality': 'Medium'},
        },
    },
    # Cyber/EW/ISR Portfolio
    {
        'id': 'PRG-007', 'portfolio_id': 'PORT-CEW',
        'name': 'Cyber Mission System',
        'short': 'CMS',
        'customer': 'MOD / GCHQ',
        'value_gbp': 290, 'phase': 'TMRR',
        'phase_label': ACQ_PHASE_LABELS['TMRR'],
        'delivery_risk_score': 78, 'delivery_risk_label': 'Critical',
        'milestones': [
            {'name': 'Capability Requirements Doc', 'date': '2025-03', 'status': 'Delayed'},
            {'name': 'Prototype Demonstration',     'date': '2025-10', 'status': 'At Risk'},
            {'name': 'EMD Proposal',                'date': '2026-06', 'status': 'At Risk'},
        ],
        'functions_required': {
            'FN-CS': {'headcount': 220, 'criticality': 'Critical'},
            'FN-SW': {'headcount': 180, 'criticality': 'Critical'},
            'FN-SE': {'headcount': 100, 'criticality': 'High'},
            'FN-IT': {'headcount': 80,  'criticality': 'High'},
            'FN-PM': {'headcount': 50,  'criticality': 'Medium'},
        },
    },
    {
        'id': 'PRG-008', 'portfolio_id': 'PORT-CEW',
        'name': 'Electronic Attack Platform',
        'short': 'EAP',
        'customer': 'RAF / Export',
        'value_gbp': 380, 'phase': 'EMD',
        'phase_label': ACQ_PHASE_LABELS['EMD'],
        'delivery_risk_score': 66, 'delivery_risk_label': 'High',
        'milestones': [
            {'name': 'System PDR',           'date': '2025-05', 'status': 'At Risk'},
            {'name': 'Hardware Prototype',   'date': '2025-11', 'status': 'At Risk'},
            {'name': 'Subsystem CDR',        'date': '2026-04', 'status': 'At Risk'},
        ],
        'functions_required': {
            'FN-MS': {'headcount': 200, 'criticality': 'Critical'},
            'FN-SE': {'headcount': 140, 'criticality': 'High'},
            'FN-SW': {'headcount': 120, 'criticality': 'High'},
            'FN-CS': {'headcount': 100, 'criticality': 'High'},
            'FN-ST': {'headcount': 80,  'criticality': 'High'},
            'FN-RM': {'headcount': 60,  'criticality': 'Medium'},
        },
    },
    {
        'id': 'PRG-009', 'portfolio_id': 'PORT-CEW',
        'name': 'ISR Data Fusion Platform',
        'short': 'ISR-DFP',
        'customer': 'Intelligence Community',
        'value_gbp': 310, 'phase': 'EMD',
        'phase_label': ACQ_PHASE_LABELS['EMD'],
        'delivery_risk_score': 59, 'delivery_risk_label': 'Medium',
        'milestones': [
            {'name': 'Data Architecture Review', 'date': '2025-04', 'status': 'On Track'},
            {'name': 'Integration Test Start',   'date': '2025-10', 'status': 'On Track'},
            {'name': 'Operational Trial',         'date': '2026-07', 'status': 'At Risk'},
        ],
        'functions_required': {
            'FN-IT': {'headcount': 160, 'criticality': 'Critical'},
            'FN-SW': {'headcount': 140, 'criticality': 'Critical'},
            'FN-CS': {'headcount': 120, 'criticality': 'High'},
            'FN-SE': {'headcount': 80,  'criticality': 'High'},
            'FN-MS': {'headcount': 60,  'criticality': 'High'},
            'FN-PM': {'headcount': 50,  'criticality': 'Medium'},
        },
    },
]

# ══════════════════════════════════════════════════════════════════════════════
# 4. EMPLOYEES
# ══════════════════════════════════════════════════════════════════════════════
FIRST_NAMES = ['James','Sarah','Oliver','Emma','William','Charlotte','Harry','Amelia','George',
               'Sophia','Jack','Isla','Thomas','Grace','Daniel','Freya','Michael','Hannah',
               'Alexander','Eleanor','Joseph','Evie','Samuel','Mia','Charlie','Poppy','Joshua',
               'Ruby','Edward','Lily','Luke','Daisy','Benjamin','Florence','Henry','Rosie',
               'Matthew','Harriet','Andrew','Imogen','David','Ellie','Robert','Chloe','Richard',
               'Zoe','Christopher','Alice','Jonathan','Bethany','Patrick','Laura','Sean','Rachel',
               'Declan','Niamh','Callum','Fiona','Alistair','Morag','Ravi','Priya','Arun',
               'Meera','Tariq','Fatima','Yusuf','Aisha','Stefan','Katja','Marco','Elena']
LAST_NAMES  = ['Smith','Jones','Taylor','Brown','Davies','Evans','Wilson','Thomas','Roberts',
               'Johnson','Walker','Wright','Robinson','Thompson','White','Edwards','Hughes',
               'Hall','Lewis','Harris','Clarke','Jackson','Wood','Turner','Martin','Cooper',
               'Hill','Ward','Morris','Moore','Scott','King','Watson','Baker','Carter','Mitchell',
               'Patel','Shah','Khan','Ahmed','Singh','Kumar','Sharma','Gupta','Ali','Hassan',
               'Murphy','Kelly','O\'Brien','Walsh','McCarthy','O\'Connor','Ryan','Brennan',
               'Campbell','MacDonald','Stewart','Anderson','MacLeod','Fraser','Reid','Grant']

GRADES = [
    ('Grade 3 — Graduate',         3, 5),
    ('Grade 4 — Junior Professional', 4, 4),
    ('Grade 5 — Professional',     5, 3),
    ('Grade 6 — Senior Professional', 6, 2),
    ('Grade 7 — Lead',             7, 2),
    ('Grade 8 — Principal',        8, 1),
    ('Grade 9 — Senior Principal', 9, 1),
]
GRADE_W = [g[2] for g in GRADES]

LOCATIONS = ['Bristol', 'Warton', 'Edinburgh', 'Portsmouth', 'Brough', 'Samlesbury', 'London', 'Farnborough']
CLEARANCES = ['Baseline', 'Security Check (SC)', 'Developed Vetting (DV)']

PERF_W = [0.04, 0.12, 0.58, 0.20, 0.06]

PROGRAM_IDS  = [p['id'] for p in programs_v2]
FUNCTION_IDS = [f['id'] for f in functions]

def pick_clearance(fn_def):
    prof = fn_def['clearance_profile']
    return random.choices(list(prof.keys()), weights=list(prof.values()))[0]

def pick_acq_phases_experienced(n=3):
    """Return 1-4 phases the person has worked in, weighted toward EMD/O&S."""
    possible = ACQ_PHASES[:]
    k = random.choices([1,2,3,4], [0.2,0.35,0.30,0.15])[0]
    return sorted(random.sample(possible, min(k, len(possible))), key=ACQ_PHASES.index)

used_names = set()
employees_v2 = []
emp_id = 2001

for fn_def in FUNCTIONS_DEF:
    n_sample = fn_def['headcount_sample']
    fn_programs = [p for p in programs_v2 if fn_def['id'] in p['functions_required']]
    fn_program_ids = [p['id'] for p in fn_programs] or ['Corporate / Internal']

    for _ in range(n_sample):
        # Basic demographics
        while True:
            name = random.choice(FIRST_NAMES) + ' ' + random.choice(LAST_NAMES)
            if name not in used_names:
                used_names.add(name)
                break

        gender    = random.choice(['Male','Female','Male','Female','Non-binary'])
        grade_rec = random.choices(GRADES, weights=GRADE_W)[0]
        grade, grade_num, _ = grade_rec
        org_layer  = max(1, min(5, 6 - grade_num // 2))

        total_exp  = random.randint(max(2, grade_num * 2 - 2), grade_num * 5 + 2)
        org_tenure = round(random.uniform(0.5, min(total_exp, 18)), 1)

        # Time in role: 0.5 - 5 years (shorter for higher grades)
        time_in_role = round(random.uniform(0.5, min(org_tenure, 6 - grade_num * 0.3)), 1)
        time_in_role = max(0.3, time_in_role)

        # Time in level: can be longer than time in role (role changes within same grade)
        time_in_level = round(random.uniform(time_in_role, min(org_tenure, time_in_role + 4)), 1)

        # Program allocation
        if fn_def['id'] in ['FN-HR', 'FN-FC']:
            programs_list = ['Corporate / Internal']
            program_alloc = {'Corporate / Internal': 100}
            time_on_prog  = round(random.uniform(0.3, org_tenure * 0.6), 1)
            current_phase = None
        else:
            num_progs = random.choices([1,2,3],[0.50,0.35,0.15])[0]
            chosen = random.sample(fn_program_ids, min(num_progs, len(fn_program_ids)))
            if not chosen:
                chosen = ['Corporate / Internal']
            alloc_splits = sorted([random.uniform(0,1) for _ in range(len(chosen)-1)] + [0,1])
            alloc_pcts   = [round((alloc_splits[i+1]-alloc_splits[i])*100) for i in range(len(chosen))]
            # Normalise to 100
            diff = 100 - sum(alloc_pcts)
            alloc_pcts[-1] += diff
            programs_list = chosen
            program_alloc = {p: a for p, a in zip(chosen, alloc_pcts)}
            primary_prog  = max(program_alloc, key=program_alloc.get)
            primary_prog_data = next((p for p in programs_v2 if p['id'] == primary_prog), None)
            current_phase = primary_prog_data['phase'] if primary_prog_data else None
            time_on_prog  = round(random.uniform(0.3, min(org_tenure, 5)), 1)

        # Acquisition lifecycle experience
        acq_exp = pick_acq_phases_experienced()
        if current_phase and current_phase not in acq_exp:
            acq_exp.append(current_phase)
            acq_exp = sorted(set(acq_exp), key=ACQ_PHASES.index)

        # Subdiscipline
        subdiscipline = random.choice(fn_def['subdisciplines'])

        # Clearance
        clearance = pick_clearance(fn_def)

        # Compensation
        base_sal_map = {3: 35000, 4: 42000, 5: 52000, 6: 65000, 7: 80000, 8: 98000, 9: 120000}
        base_sal = base_sal_map[grade_num]
        base_sal += random.randint(-3000, 3000)
        cr = round(random.uniform(0.84, 1.12), 2)

        # Performance
        perf = random.choices([1,2,3,4,5], PERF_W)[0]
        perf_py = random.choices([1,2,3,4,5], PERF_W)[0]

        # Engagement
        engage = max(30, min(98, int(78 - (cr < 0.90)*15 + (perf-3)*6 + random.randint(-10,10))))

        # Months since promotion: derived from time_in_level
        months_since_promo = int(time_in_level * 12)

        # Flight risk (additive model)
        fr = 28
        if cr < 0.90: fr += 20
        if cr < 0.85: fr += 12
        if perf >= 4:  fr += 10
        if org_tenure > 10: fr += 8
        if org_tenure < 1.5: fr -= 15
        if fn_def['id'] in ['FN-SW','FN-CS']: fr += 14
        if fn_def['id'] == 'FN-MS': fr += 8
        if time_in_level > 5: fr += 8   # stagnation in level
        if time_on_prog > 4:  fr += 5   # burn-out risk from long program tenure
        fr = max(5, min(92, fr + random.randint(-10, 10)))

        # Key person / succession
        kp  = random.random() < (0.08 + (grade_num >= 7) * 0.12)
        direct_reports = max(0, random.choices([0,3,5,7,10,13],[0.45,0.15,0.15,0.12,0.08,0.05])[0]) if grade_num >= 6 else 0
        succ_opts = ['Not Nominated','Nominated — Needs Development','Development Pipeline (24-36mo)',
                     'Development Pipeline (12-18mo)','Ready Now']
        succ_w = [0.50, 0.15, 0.15, 0.12, 0.08]
        succ = random.choices(succ_opts, succ_w)[0]

        # Regrettability (programme execution impact)
        regret = (
            (clearance == 'Developed Vetting (DV)' and kp) or
            (clearance in ['Security Check (SC)','Developed Vetting (DV)'] and perf >= 4 and fr >= 55) or
            (kp and succ in ['Not Nominated','Nominated — Needs Development'])
        )

        # Competency match
        comp_match = max(40, min(99, int(
            65 + (perf-3)*8 + (total_exp - grade_num*2)*1.5 + random.randint(-8,8)
        )))

        # Training hours
        train_hrs = max(0, int(20 + (perf-3)*8 + random.randint(-10,15)))

        # STAR model
        star_s = max(30, min(99, int(65 + random.randint(-20,20))))
        star_st= max(30, min(99, int(62 + random.randint(-18,18))))
        star_p = max(30, min(99, int(64 + random.randint(-18,18))))
        star_r = max(30, min(99, int(60 + random.randint(-20,15))))
        star_pe= max(30, min(99, int(67 + random.randint(-15,15))))
        star_ov= round((star_s+star_st+star_p+star_r+star_pe)/5)

        # Lifecycle phase match: does the person have experience in the program's current phase?
        phase_match = (current_phase in acq_exp) if current_phase else True

        employees_v2.append({
            'id': f'EMP{emp_id}',
            'name': name,
            'gender': gender,
            'function_id': fn_def['id'],
            'function_name': fn_def['name'],
            'subdiscipline': subdiscipline,
            'grade': grade,
            'grade_num': grade_num,
            'org_layer': org_layer,
            'location': random.choice(LOCATIONS),
            'fte_type': random.choices(['Permanent','Fixed Term','Contractor'],[0.78,0.12,0.10])[0],
            'clearance': clearance,
            'total_exp_yrs': total_exp,
            'org_tenure_yrs': org_tenure,
            'time_in_role_yrs': time_in_role,
            'time_in_level_yrs': time_in_level,
            'time_on_program_yrs': time_on_prog,
            'months_since_promotion': months_since_promo,
            'programs': programs_list,
            'program_allocation': program_alloc,
            'acquisition_phase_current': current_phase,
            'acquisition_phases_experienced': acq_exp,
            'acquisition_phase_match': phase_match,
            'base_salary_gbp': base_sal,
            'compa_ratio': cr,
            'performance_current': perf,
            'performance_prior': perf_py,
            'engagement_score': engage,
            'flight_risk_score': fr,
            'key_person_dependency': kp,
            'succession_status': succ,
            'would_be_regrettable': regret,
            'competency_match_pct': comp_match,
            'training_hrs_ttm': train_hrs,
            'direct_reports': direct_reports,
            'on_critical_path': random.random() < 0.18,
            'star_strategy': star_s,
            'star_structure': star_st,
            'star_processes': star_p,
            'star_rewards': star_r,
            'star_people': star_pe,
            'star_overall': star_ov,
        })
        emp_id += 1

# ══════════════════════════════════════════════════════════════════════════════
# 5. ALLOCATION MATRIX  (Function × Program)
# ══════════════════════════════════════════════════════════════════════════════
allocation_matrix = []
fn_map = {f['id']: f for f in functions}

for prog in programs_v2:
    for fn_id, req in prog['functions_required'].items():
        fn  = fn_map[fn_id]
        # What % of this function's actual headcount is on this program?
        pct_of_fn = round(req['headcount'] / fn['headcount_actual'] * 100, 1)
        # Sample employees in this function on this program
        sample_on_prog = [e for e in employees_v2
                          if e['function_id'] == fn_id and prog['id'] in e['programs']]
        avg_fr = round(sum(e['flight_risk_score'] for e in sample_on_prog) / max(1, len(sample_on_prog)))
        avg_time = round(sum(e['time_on_program_yrs'] for e in sample_on_prog) / max(1, len(sample_on_prog)), 1)
        regret_ct= sum(1 for e in sample_on_prog if e['would_be_regrettable'])
        no_phase_exp = sum(1 for e in sample_on_prog if not e['acquisition_phase_match'])
        # Scale for display
        headcount_scaled = req['headcount']
        pct_headcount_gap = max(0, round((1 - len(sample_on_prog)*fn['scale_factor'] / headcount_scaled)*100)) if headcount_scaled else 0

        allocation_matrix.append({
            'program_id': prog['id'],
            'program_name': prog['short'],
            'portfolio_id': prog['portfolio_id'],
            'function_id': fn_id,
            'function_name': fn['name'],
            'criticality': req['criticality'],
            'headcount_required': headcount_scaled,
            'pct_of_function': pct_of_fn,
            'avg_flight_risk': avg_fr,
            'avg_time_on_program': avg_time,
            'regrettable_flight_risk_count': regret_ct,
            'phase_experience_gap_count': no_phase_exp,
            'sample_count': len(sample_on_prog),
        })

# ══════════════════════════════════════════════════════════════════════════════
# 6. SAVE
# ══════════════════════════════════════════════════════════════════════════════
save('platform-demo/assets/portfolios.json',       portfolios)
save('platform-demo/assets/functions.json',        functions)
save('platform-demo/assets/programs_v2.json',      programs_v2)
save('platform-demo/assets/employees_v2.json',     employees_v2)
save('platform-demo/assets/allocation_matrix.json',allocation_matrix)

# Summary
n = len(employees_v2)
high_fr   = sum(1 for e in employees_v2 if e['flight_risk_score']>=60)
regret    = sum(1 for e in employees_v2 if e['would_be_regrettable'])
kp        = sum(1 for e in employees_v2 if e['key_person_dependency'])
no_phase  = sum(1 for e in employees_v2 if not e['acquisition_phase_match'])
avg_cr    = round(sum(e['compa_ratio'] for e in employees_v2)/n, 3)

print(f'Sample employees: {n} | Representing: {total_actual:,} FTEs (50K organisation)')
print(f'High flight risk: {high_fr} | Would be regrettable: {regret} | Key person: {kp}')
print(f'Phase experience gap (wrong lifecycle phase for their program): {no_phase}')
print(f'Avg compa-ratio: {avg_cr}')
print(f'Portfolios: {len(portfolios)} | Programs: {len(programs_v2)} | Functions: {len(functions)}')
print(f'Allocation matrix entries: {len(allocation_matrix)}')
print('Files saved to platform-demo/assets/')
