"""
Generates synthetic workforce data for AeroDefend Group demo.
Outputs: platform-demo/assets/employees.json
         platform-demo/assets/programs.json
         platform-demo/assets/attrition.json
         platform-demo/assets/action_log.json
"""

import json, random, math, os
from datetime import date, timedelta

random.seed(42)
os.makedirs('platform-demo/assets', exist_ok=True)

# ── Reference data ─────────────────────────────────────────────────────────
FIRST = ['James','Sarah','Michael','Emily','David','Rachel','Thomas','Laura',
         'Robert','Jessica','Daniel','Emma','Matthew','Sophie','Christopher',
         'Hannah','Andrew','Charlotte','Paul','Amy','Mark','Rebecca','Steven',
         'Claire','Richard','Victoria','Jonathan','Natalie','Kevin','Stephanie',
         'Patrick','Katherine','Graham','Elizabeth','Simon','Alexandra','Philip',
         'Helen','Neil','Nicola','Adrian','Fiona','Craig','Louise','Stuart',
         'Catherine','Ross','Alan','Michelle','Gareth','Jennifer','Owen','Liam',
         'Olivia','William','Isabella','Benjamin','Charlotte','Ethan','Mia']

LAST = ['Smith','Jones','Williams','Brown','Taylor','Davies','Evans','Wilson',
        'Thomas','Roberts','Johnson','Walker','Wright','Thompson','White','Hall',
        'Green','Lewis','Harris','Clarke','Anderson','Baker','Mitchell','Carter',
        'Turner','Scott','Phillips','Campbell','Parker','Cooper','Richards',
        'Morgan','King','West','Brooks','Bell','Ward','Morris','Murray','Marshall',
        'Henderson','Russell','Butler','Collins','Reed','Hughes','Powell','Graham']

PROGRAMS = [
    {'id':'P001','name':'Typhoon Modernisation Block 20','phase':'Engineering & Manufacturing Development','phase_short':'EMD','start':'2023-04','end':'2027-06','value_gbp':420,'customer':'Royal Air Force'},
    {'id':'P002','name':'Future Combat Air System','phase':'Materiel Solution Analysis','phase_short':'MSA','start':'2024-01','end':'2030-12','value_gbp':890,'customer':'MOD / Partner Nations'},
    {'id':'P003','name':'Air Defence Ground Environment','phase':'Production & Deployment','phase_short':'P&D','start':'2022-06','end':'2026-03','value_gbp':185,'customer':'Army Air Corps'},
    {'id':'P004','name':'Eurofighter Sustainment','phase':'Operations & Support','phase_short':'O&S','start':'2020-01','end':'2028-12','value_gbp':310,'customer':'Multi-Nation Consortium'},
    {'id':'P005','name':'Project SKYSHIELD','phase':'Technology Maturation & Risk Reduction','phase_short':'TMRR','start':'2024-09','end':'2028-06','value_gbp':245,'customer':'Defence Science & Technology Lab'},
]

MILESTONES = {
    'P001': [
        {'name':'Critical Design Review','date':'2025-03','status':'At Risk','days_delta':+14},
        {'name':'System Integration Test','date':'2025-09','status':'On Track','days_delta':0},
        {'name':'Operational Test & Eval','date':'2026-06','status':'On Track','days_delta':0},
        {'name':'First Aircraft Delivery','date':'2027-02','status':'At Risk','days_delta':+28},
    ],
    'P002': [
        {'name':'Capability Development Document','date':'2025-06','status':'On Track','days_delta':0},
        {'name':'Milestone A Review','date':'2026-01','status':'At Risk','days_delta':+21},
        {'name':'Technology Demonstrator Fly-Off','date':'2027-09','status':'At Risk','days_delta':+45},
    ],
    'P003': [
        {'name':'Low Rate Initial Production','date':'2025-02','status':'Delayed','days_delta':+52},
        {'name':'Full Rate Production Decision','date':'2025-10','status':'At Risk','days_delta':+30},
        {'name':'Final Delivery','date':'2026-03','status':'At Risk','days_delta':+35},
    ],
    'P004': [
        {'name':'Mid-Life Upgrade Package','date':'2025-04','status':'On Track','days_delta':0},
        {'name':'Fleet Availability Review','date':'2025-11','status':'On Track','days_delta':0},
    ],
    'P005': [
        {'name':'System Requirements Review','date':'2025-05','status':'On Track','days_delta':0},
        {'name':'Preliminary Design Review','date':'2026-02','status':'At Risk','days_delta':+18},
    ],
}

DEPTS = {
    'Systems Engineering':  {'n':22,'disciplines':['Mission Systems','Avionics Integration','Systems Architecture','Airframe SE'],'pay':68000},
    'R&M Engineering':      {'n':16,'disciplines':['Reliability Analysis','Maintainability','Safety Engineering','R&M Planning'],'pay':65000},
    'Cybersecurity':        {'n':11,'disciplines':['Security Architecture','Threat Analysis','Penetration Testing','GRC'],'pay':72000},
    'Programme Management': {'n':14,'disciplines':['Project Controls','Delivery Management','Bid Management','PMO'],'pay':70000},
    'HR':                   {'n': 8,'disciplines':['Talent Acquisition','HR Business Partnering','Learning & Development','Compensation & Benefits'],'pay':55000},
    'Finance':              {'n': 7,'disciplines':['Commercial Finance','Cost Engineering','Financial Planning & Analysis'],'pay':58000},
    'IT & Digital':         {'n': 7,'disciplines':['Enterprise IT','Digital Engineering','Data & Analytics'],'pay':62000},
    'Leadership':           {'n': 5,'disciplines':['Executive Leadership','Programme Direction','Business Development'],'pay':115000},
    'Operations':           {'n': 5,'disciplines':['Supply Chain','Quality Assurance','Manufacturing Engineering'],'pay':60000},
}

GRADES = [
    {'grade':'Grade 4','label':'Junior Professional',  'pay_mult':[0.80,0.95],'layer':[5,5],'exp':[0,3]},
    {'grade':'Grade 5','label':'Professional',          'pay_mult':[0.85,1.05],'layer':[4,5],'exp':[2,7]},
    {'grade':'Grade 6','label':'Senior Professional',   'pay_mult':[0.90,1.10],'layer':[4,4],'exp':[5,14]},
    {'grade':'Grade 7','label':'Lead',                  'pay_mult':[0.88,1.12],'layer':[3,4],'exp':[9,20]},
    {'grade':'Grade 8','label':'Manager',               'pay_mult':[0.90,1.15],'layer':[3,3],'exp':[12,25]},
    {'grade':'Grade 9','label':'Senior Manager',        'pay_mult':[0.92,1.18],'layer':[2,3],'exp':[15,30]},
    {'grade':'SCS',    'label':'Executive / Director',  'pay_mult':[0.95,1.20],'layer':[1,2],'exp':[18,35]},
]

GRADE_DIST = {
    'Leadership':          [0,0,0,0,0.1,0.4,0.5],
    'Systems Engineering': [0.05,0.15,0.30,0.28,0.15,0.05,0.02],
    'R&M Engineering':     [0.05,0.18,0.28,0.27,0.15,0.05,0.02],
    'Cybersecurity':       [0.05,0.20,0.30,0.25,0.15,0.05,0.00],
    'Programme Management':[0.03,0.12,0.25,0.30,0.20,0.08,0.02],
    'HR':                  [0.08,0.20,0.30,0.22,0.15,0.05,0.00],
    'Finance':             [0.08,0.18,0.30,0.24,0.15,0.05,0.00],
    'IT & Digital':        [0.05,0.20,0.30,0.25,0.15,0.05,0.00],
    'Operations':          [0.10,0.22,0.30,0.22,0.12,0.04,0.00],
}

LOCATIONS = ['Bristol','Warton','Brough','Edinburgh','London','Samlesbury']
CLEARANCES = ['Baseline','Security Check (SC)','Developed Vetting (DV)','ITAR']
MOBILITIES = ['Actively seeking','Open in 12 months','Open in 2+ years','Not seeking']
SUCCESSION  = ['Ready Now','Development Pipeline (12-18mo)','Nominated (18-36mo)','Not Nominated']
PERF_W = [0.03,0.10,0.44,0.33,0.10]

used = set()
employees = []
eid = 1001

for dept, ddata in DEPTS.items():
    gw = GRADE_DIST[dept]
    for _ in range(ddata['n']):
        # name
        while True:
            n = f'{random.choice(FIRST)} {random.choice(LAST)}'
            if n not in used: used.add(n); break

        # grade
        gi = random.choices(range(7), gw)[0]
        g  = GRADES[gi]

        exp      = random.randint(*g['exp'])
        tenure   = round(random.uniform(0.5, min(exp, 16)), 1)
        t_role   = round(random.uniform(0.5, min(tenure, 5)), 1)
        t_prog   = round(random.uniform(0.25, min(tenure, 4)), 1)
        cr       = round(random.uniform(*g['pay_mult']), 2)
        salary   = int(ddata['pay'] * cr)
        perf     = random.choices([1,2,3,4,5], PERF_W)[0]
        perf_py  = random.choices([1,2,3,4,5], PERF_W)[0]
        engage   = max(20, min(100, int(78 - (cr < 0.9)*15 + (perf-3)*6 + random.randint(-8,8))))

        # flight risk
        fr = 28
        if cr < 0.90: fr += 20
        if cr < 0.85: fr += 12
        if perf >= 4:  fr += 10
        if tenure > 8: fr += 8
        if tenure < 2: fr -= 15
        if dept == 'Cybersecurity': fr += 14
        fr = max(5, min(92, fr + random.randint(-10,10)))

        # program assignment
        if dept in ['HR','Finance','IT & Digital','Leadership']:
            progs = ['Corporate / Internal']
        else:
            n_p = random.choices([1,2,3],[0.50,0.35,0.15])[0]
            progs = random.sample([p['id'] for p in PROGRAMS], n_p)

        # span
        if g['grade'] in ['Grade 8','Grade 9','SCS']:
            span = random.randint(4,13)
        elif g['grade'] == 'Grade 7' and random.random() < 0.4:
            span = random.randint(2,6)
        else:
            span = 0

        # succession
        if perf >= 4 and gi >= 3:
            succ = random.choices(SUCCESSION,[0.15,0.35,0.35,0.15])[0]
        elif perf == 5:
            succ = random.choices(SUCCESSION,[0.30,0.40,0.20,0.10])[0]
        else:
            succ = random.choices(SUCCESSION,[0.01,0.07,0.22,0.70])[0]

        key_person = perf >= 4 and gi >= 3 and random.random() < 0.35

        comp_match = max(45, min(99, int(63 + perf*4 + t_role*3 + random.randint(-8,8))))
        train_hrs  = random.choices([0,random.randint(5,15),random.randint(16,30),
                                     random.randint(31,50),random.randint(51,80)],
                                    [0.05,0.15,0.30,0.35,0.15])[0]

        # clearance
        if dept == 'Cybersecurity':
            cl = random.choices(CLEARANCES,[0.05,0.45,0.35,0.15])[0]
        elif dept in ['Systems Engineering','R&M Engineering']:
            cl = random.choices(CLEARANCES,[0.20,0.50,0.20,0.10])[0]
        else:
            cl = random.choices(CLEARANCES,[0.35,0.40,0.15,0.10])[0]

        # program criticality
        on_crit = (gi >= 3 and
                   any(p != 'Corporate / Internal' for p in progs) and
                   random.random() < 0.40)

        # regrettable departure flag (if this person were to leave)
        # Classification: program execution impact
        # Regrettable if: on critical path AND (SC/DV cleared OR competency match >75%)
        #              OR: key person dependency
        #              OR: succession nominee AND (perf >= 4)
        would_be_regrettable = (
            (on_crit and cl in ['Security Check (SC)','Developed Vetting (DV)']) or
            key_person or
            (succ in ['Ready Now','Development Pipeline (12-18mo)'] and perf >= 4)
        )

        # STAR scores
        star_s = max(30,min(100,int(50+perf*8+random.randint(-10,10))))
        star_st= max(30,min(100,int(55+span*2+random.randint(-10,10))))
        star_p = max(30,min(100,int(52+t_role*5+random.randint(-10,10))))
        star_r = max(30,min(100,int(60+cr*30-30+random.randint(-8,8))))
        star_pe= max(30,min(100,int(55+comp_match*0.3+random.randint(-8,8))))

        # program allocation
        if len(progs) == 1:
            alloc = {progs[0]: 100}
        elif len(progs) == 2:
            s = random.randint(30,70)
            alloc = {progs[0]: s, progs[1]: 100-s}
        else:
            a = random.randint(20,45); b = random.randint(20,45)
            alloc = {progs[0]: a, progs[1]: b, progs[2]: 100-a-b}

        employees.append({
            'id': f'EMP{eid:04d}',
            'name': n,
            'gender': random.choices(['Male','Female','Prefer not to say'],[0.52,0.44,0.04])[0],
            'department': dept,
            'discipline': random.choice(ddata['disciplines']),
            'role': f'{g["label"]} {random.choice(ddata["disciplines"])}',
            'grade': f'{g["grade"]} — {g["label"]}',
            'grade_num': gi + 4,
            'org_layer': random.randint(*g['layer']),
            'location': random.choice(LOCATIONS),
            'fte_type': random.choices(['Permanent','Fixed-Term','Contractor'],[0.75,0.12,0.13])[0],
            'clearance': cl,
            # Time
            'org_tenure_yrs': tenure,
            'time_in_role_yrs': t_role,
            'time_on_program_yrs': t_prog,
            'total_exp_yrs': exp,
            'months_since_promotion': random.randint(6,60) if gi > 0 else random.randint(1,24),
            # Programs
            'programs': progs,
            'program_allocation': alloc,
            'on_critical_path': on_crit,
            # Compensation
            'base_salary_gbp': salary,
            'compa_ratio': cr,
            'pay_equity_vs_peers': round(salary / (ddata['pay']*1.02), 3),
            # Performance
            'performance_current': perf,
            'performance_prior': perf_py,
            'engagement_score': engage,
            # Risk
            'flight_risk_score': fr,
            'key_person_dependency': key_person,
            'succession_status': succ,
            'would_be_regrettable': would_be_regrettable,
            # Development
            'competency_match_pct': comp_match,
            'training_hrs_ttm': int(train_hrs),
            'mobility_interest': random.choice(MOBILITIES),
            # Org design
            'direct_reports': span,
            # STAR
            'star_strategy': star_s,
            'star_structure': star_st,
            'star_processes': star_p,
            'star_rewards': star_r,
            'star_people': star_pe,
            'star_overall': round((star_s+star_st+star_p+star_r+star_pe)/5),
        })
        eid += 1

# ── Program data with headcount demand ─────────────────────────────────────
programs_out = []
for p in PROGRAMS:
    needed = {'Systems Engineering': random.randint(4,12),
              'R&M Engineering':     random.randint(3,9),
              'Cybersecurity':       random.randint(1,5),
              'Programme Management':random.randint(2,6)}
    current = {k: int(v*random.uniform(0.6,0.95)) for k,v in needed.items()}
    gap     = {k: needed[k]-current[k] for k in needed}
    lead_time_months = {
        'Systems Engineering': 6,
        'R&M Engineering':     9,
        'Cybersecurity':       12,
        'Programme Management':5,
    }
    risk_score = min(100, int(sum(g for g in gap.values()) * 8 + random.randint(10,25)))
    programs_out.append({
        **p,
        'milestones': MILESTONES.get(p['id'], []),
        'headcount_needed': needed,
        'headcount_current': current,
        'headcount_gap': gap,
        'lead_time_months': lead_time_months,
        'delivery_risk_score': risk_score,
        'delivery_risk_label': 'Critical' if risk_score > 70 else 'High' if risk_score > 50 else 'Medium' if risk_score > 30 else 'Low',
    })

# ── Attrition history (18 months) ──────────────────────────────────────────
DEPARTURE_REASONS = {
    'regrettable':     ['Better compensation elsewhere','Limited career progression','Accepted competitor offer','Relocated for partner','Better work-life balance offer'],
    'non_regrettable': ['Performance managed out','Retirement','Contract end','Redundancy — role eliminated','Career change — left industry'],
    'neutral':         ['Personal circumstances','Further education','Mutual agreement','Contract not renewed'],
}

attrition = []
for i in range(22):
    dept = random.choice(list(DEPTS.keys()))
    gi   = random.choices(range(5),[0.05,0.20,0.35,0.25,0.15])[0]
    g    = GRADES[gi]
    perf = random.choices([1,2,3,4,5], PERF_W)[0]
    cl   = random.choices(CLEARANCES,[0.25,0.42,0.22,0.11])[0]
    prog = random.choice([p['id'] for p in PROGRAMS]+['Corporate / Internal'])
    on_crit = prog != 'Corporate / Internal' and random.random() < 0.45

    # Program impact classification
    regret = (
        (on_crit and cl in ['Security Check (SC)','Developed Vetting (DV)']) or
        (perf >= 4 and on_crit) or
        (gi >= 3 and perf >= 4 and random.random() < 0.6)
    )
    non_reg = perf <= 2 or (prog == 'Corporate / Internal' and perf == 3)
    category = 'Regrettable' if regret and not non_reg else 'Non-Regrettable' if non_reg else 'Neutral'

    months_ago = random.randint(1,18)
    departure_date = (date.today() - timedelta(days=months_ago*30)).strftime('%Y-%m')

    reason_pool = DEPARTURE_REASONS['regrettable' if category=='Regrettable' else 'non_regrettable' if category=='Non-Regrettable' else 'neutral']

    replacement_cost = int(DEPTS[dept]['pay'] * random.uniform(0.8,1.8) * GRADES[gi]['pay_mult'][0])
    time_to_replace  = random.randint(3,18)

    # contagion — team members at elevated risk
    contagion_count = random.randint(0,3) if category=='Regrettable' else 0
    contagion_risk_uplift = random.randint(20,55) if contagion_count > 0 else 0

    attrition.append({
        'id': f'ATT{1001+i:04d}',
        'name': f'{random.choice(FIRST)} {random.choice(LAST)}',
        'department': dept,
        'grade': g['grade'],
        'grade_label': g['label'],
        'program': prog,
        'clearance': cl,
        'performance_at_departure': perf,
        'on_critical_path': on_crit,
        'departure_date': departure_date,
        'departure_reason': random.choice(reason_pool),
        'regrettability': category,
        'replacement_cost_gbp': replacement_cost,
        'estimated_weeks_to_replace': time_to_replace,
        'knowledge_documented': random.choices(['Yes','Partial','No'],[0.30,0.40,0.30])[0],
        'contagion_team_members_at_risk': contagion_count,
        'contagion_risk_uplift_pct': contagion_risk_uplift,
        'program_impact': 'HIGH — milestone at risk' if (on_crit and category=='Regrettable') else 'MEDIUM — monitor' if on_crit else 'LOW',
    })

# ── Action log (mock SAP H2R events) ───────────────────────────────────────
H2R_ACTIVITIES = [
    'Requisition Raised','Hiring Manager Approval','Job Posted','CV Screening',
    'Telephone Screen','First Interview','Assessment Centre','Technical Interview',
    'Right-to-Work Check','Security Clearance Initiated','Background Check',
    'Offer Extended','Offer Accepted','Offer Declined','Contract Issued',
    'Pre-employment Medicals','IT Access Requested','Onboarding Scheduled',
    'Day 1 Induction','Probation Review 3 Month','Probation Review 6 Month',
    'Probation Passed','Probation Extended','Case Closed',
]
SLA_TARGETS = {a: random.randint(2,10) for a in H2R_ACTIVITIES}

action_log = []
for i in range(40):
    role = random.choice(['Senior R&M Engineer','Systems Engineer','Cybersecurity Architect',
                          'Programme Manager','Data Analyst','HR Business Partner',
                          'Lead Mission Systems Engineer','R&M Planning Lead'])
    dept = random.choice(list(DEPTS.keys()))
    prog = random.choice([p['id'] for p in PROGRAMS])
    case_id = f'H2R-2024-{1100+i:04d}'
    days_open = random.randint(1,85)
    status = random.choice(['Active','Closed — Hired','Closed — Withdrawn','On Hold'])
    activities_done = random.randint(3, len(H2R_ACTIVITIES))
    last_act = H2R_ACTIVITIES[activities_done-1]
    sla_breach = random.random() < 0.35
    compliance_breach = random.choices([None,'Missing Right-to-Work','Late Background Check',
                                         'Probation Review Skipped'],[0.70,0.12,0.10,0.08])[0]
    risk = min(99, int(days_open*0.8 + (20 if sla_breach else 0) + (25 if compliance_breach else 0) + random.randint(-10,10)))

    action_log.append({
        'case_id': case_id,
        'role': role,
        'department': dept,
        'program': prog,
        'days_open': days_open,
        'status': status,
        'last_activity': last_act,
        'activities_completed': activities_done,
        'total_activities': len(H2R_ACTIVITIES),
        'sla_breach': sla_breach,
        'compliance_breach': compliance_breach,
        'risk_score': max(5, risk),
        'risk_label': 'High' if risk > 65 else 'Medium' if risk > 40 else 'Low',
        'source': 'SAP SuccessFactors',
        'clearance_required': random.choices(CLEARANCES,[0.25,0.42,0.22,0.11])[0],
    })

# ── Save ────────────────────────────────────────────────────────────────────
def save(path, data):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'Saved {path} ({len(data)} records)')

save('platform-demo/assets/employees.json',   employees)
save('platform-demo/assets/programs.json',    programs_out)
save('platform-demo/assets/attrition.json',   attrition)
save('platform-demo/assets/action_log.json',  action_log)

# Summary
total = len(employees)
high_fr = sum(1 for e in employees if e['flight_risk_score'] >= 60)
regret  = sum(1 for e in employees if e['would_be_regrettable'])
kp      = sum(1 for e in employees if e['key_person_dependency'])
avg_cr  = round(sum(e['compa_ratio'] for e in employees)/total, 3)
print(f'\nEmployees: {total} | High flight risk: {high_fr} | Would be regrettable: {regret} | Key person: {kp} | Avg compa-ratio: {avg_cr}')
reg_att = sum(1 for a in attrition if a['regrettability']=='Regrettable')
print(f'Attrition history: {len(attrition)} departures | Regrettable: {reg_att} | Non-regrettable: {len(attrition)-reg_att}')
