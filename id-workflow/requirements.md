# HR Workforce Development & Talent Review Platform
## Product Requirements Document

**Version**: 1.0  
**Date**: June 2026  
**Status**: Draft  
**Author**: Matthew Trafican  

---

## 1. Executive Summary

This platform is a career-level workforce development and talent review system designed for HR functions. It connects individual competency development (OJT certification, arc tracking) with organizational talent review (calibration, promotion readiness, standing briefs) through a shared competency ontology.

The system is grounded in a behaviorally-anchored competency model, a 36-month career arc framework, and matrix-aware organizational structure. It provides proactive signals — review calendar, leading indicators, ranked priority actions — rather than reactive reporting.

The initial deployment covers HR Business Partners as a synthetic reference model. All competency content, leveling guidelines, and org structures are configurable for any career field or organization.

---

## 2. Problem Statement

### Current State

- Development tracking is role-level, not career-level — proficiency earned in one role is lost when transitioning to the next
- Talent reviews are reactive — data is assembled on demand, creating inconsistent quality and preparation burden
- Matrix org structures create visibility gaps — direct-line and dotted-line leaders hold different views of the same employee
- Plan vs. actual development tracking does not exist in most HR technology stacks
- Prescriptive guidance (what to do next) requires manual analysis that rarely happens at the pace needed
- Client perspectives on HRBP effectiveness are collected informally if at all
- Leading indicators (velocity trends, pending certifications, approaching gates) are not surfaced before they become lagging problems

### Desired State

- A single instrument that tracks development arc across roles, not just within them
- Talent reviews prepared proactively — standing briefs always current from live data
- Matrix reporting relationships visible in every view
- Plan vs. actual development tracking from Day 1
- Ranked priority actions surfaced automatically before review gates
- Client brief format available on demand for HR clients who request a review
- Leading indicators flagged 30/60/90 days before they become lagging problems

---

## 3. Design Principles

The following principles are non-negotiable and embedded in the architecture.

1. **Individual-driven development arc** — the employee owns their plan, initiates development, and selects their career track. The leader enables and certifies; they do not own.

2. **Leader as enabler, not owner** — the leader's role is to create opportunity, remove blockers, certify milestones, and plan transitions.

3. **Demonstration-based progression** — promotion is triggered by demonstrated proficiency against leveling guidelines, not time in role. Time in role is a floor, not a trigger.

4. **Profile carries across roles** — the development arc is a career instrument. Proficiency earned in one role transfers (with appropriate credit adjustment) to the next. History is preserved.

5. **Matrix org flexibility** — org structure is tag-based and configurable. The tool does not assume a fixed hierarchy. Any employee may carry one direct-line and multiple dotted-line reporting relationships.

6. **Talent pool designation is external** — talent pool and succession slate data is managed in a separate interfacing system. This tool does not store pool membership.

7. **No 360-degree feedback** — multi-rater surveys are explicitly excluded. Evidence at Expert/Master tier is collected through named, specific, gate-based inputs: experience (OJT), leader review, results documentation, and client perspective.

8. **Plain language throughout** — no analytics jargon visible to users. "Where We Are," "Early Signals," "What's at Risk," "Priority Actions" replace analytics taxonomy.

9. **Proactive by design** — the system surfaces upcoming reviews, approaching gates, and preparation requirements 30/60/90 days before they are needed.

10. **Content is replaceable** — all competency content, leveling guidelines, org structure labels, and framework parameters are configurable. The HR Business Partner model is a reference implementation.

---

## 4. User Roles

| Role | Primary Use | Review Authority |
|---|---|---|
| Individual / Employee | Owns development arc, tracks OJT, selects career track | Self-view only |
| Direct Leader | Enables development, certifies milestones, conducts quarterly/annual reviews | Primary development review authority |
| Senior Leader (non-exec) | Annual and rotation gate reviews, cross-team calibration | Annual and gate reviews |
| Executive (CHRO / VP) | Semi-annual strategic review, promotion pipeline, enterprise capability | Semi-annual / annual |
| HR Client (business leader) | Client-requested review, results perspective, client brief access | Client perspective only |
| L&D / Talent Team | Program management, cohort reporting, LDP tracking | Function-level view |

---

## 5. Framework Assumptions (Operating Model)

All parameters are configurable defaults.

| Parameter | Default Value | Notes |
|---|---|---|
| Planning horizon | 36 months | Assumed role tenure |
| Rotation gate | 18 months | Rotate vs. retain decision point |
| Foundation target | 12 months | Initial entry baseline |
| Practitioner target | 24 months from start | |
| Expert / Peak | 24–36 months | |
| Sustain / Transfer phase | 36+ months | Knowledge transfer priority |
| Lateral hire adjustment | 6–8 months to Foundation | Adjusted from assessed entry proficiency |
| Disruption recovery | Context-flagged | System adjusts velocity expectations during flagged periods |

### Four Movement Types

Proficiency carries forward with transfer credit applied at each transition:

- **Promotion** — vertical, same domain, higher level. Prior proficiency transfers; new tier requirements are net new.
- **Job scope advancement** — horizontal expansion within role. Existing proficiency holds; specific competencies extend.
- **Lateral move** — cross-functional, same level. Partial transfer: domain-agnostic competencies carry fully; functional competencies partially or reset.
- **Next target role** — career aspiration that shapes what is prioritized in the current arc.

### Two Career Tracks

Individual selects their track. Tracks share Foundation and Practitioner; diverge at Expert.

- **Individual Contributor (IC)** — depth, domain authority, technical leadership, industry influence
- **Leadership** — team/function management, organizational scope, people outcomes, enterprise strategy

---

## 6. Proficiency Framework

Four tiers, each defined by six criteria (civilian translation of Figure 1.4).

| Criteria | Foundation | Practitioner | Expert | Master |
|---|---|---|---|---|
| Depth of Knowledge | Key elements of role | All elements of role | New practices across all elements | New concepts and theories; credible resource in field |
| Consistency of Application | Routine situations | Variety of situations | Complex and ambiguous situations | Innovates; formulates strategies; teaches others |
| Thinking Challenge | Within established procedures | Wide variety of situations | Without established procedures | Novel frameworks and approaches |
| Scope | Specific functional area | Integration across related areas | Integration with org strategy | Enterprise and industry level |
| Impact on... | Specific workplace tasks | Specific workplace projects | Management and leadership decisions | Org practices and industry standards |
| Reach of Influence | Individuals | Teams and departments | Organization / Institution | Enterprise and industry |

---

## 7. Functional Requirements

### 7.1 Competency Ontology

- **FR-01**: System shall maintain a hierarchical competency model: Domain → Competency → Tier → Required Behaviors → Evidence Tasks
- **FR-02**: Each tier shall include: tier label, Required Behaviors (2–4 statements), Impact Criterion, and a list of evidence tasks
- **FR-03**: Each evidence task shall carry: task number, task statement, difficulty rating (1–3), behavior match flag, core/cert/optional designation, context flags (Standard / Deployment / Specialized), and proficiency codes for Foundation, Journeyman, Expert, and Master career levels
- **FR-04**: Proficiency codes — A: Awareness, B: Guided performance, C: Independent, *: Standard required, –: Not applicable
- **FR-05**: Each evidence task shall support three-party OJT certification: Training Start date, Training Complete date, Trainee initials, Trainer initials, Certifier initials. Full certification requires all three initials
- **FR-06**: Competency areas shall declare Supporting Competency relationships (dependency links to other nodes)
- **FR-07**: All competency content shall be replaceable. The HR Business Partner model is a reference implementation
- **FR-08**: System shall support a minimum of 3 domains, 8 competencies, and 3 tiers per competency

### 7.2 Employee Profile

- **FR-09**: Employee profile shall include: name, role, function, business unit, start date, days in role (calculated), pathway (initial/lateral), career track (IC/leadership — individual selects), target role, direct-line manager (name and title), dotted-line manager(s) with relationship type (business/functional)
- **FR-10**: LDP enrollment shall be recorded (program name; null if not enrolled)
- **FR-11**: Talent pool designation shall not be stored in this system. A note shall direct users to the external talent review system
- **FR-12**: On role transition, profile shall carry forward with prior role history, proficiency credit from prior certifications, and a new arc baseline adjusted for entering proficiency

### 7.3 Training Architecture Plan

- **FR-13**: System shall display a career development architecture showing the four-phase progression (Build → Growth → Peak → Sustain) with organizational impact criteria per phase
- **FR-14**: System shall support two training pathways: Initial Entry (12-month Foundation baseline) and Lateral/Cross-Functional (adjusted baseline, typically 6–8 months)
- **FR-15**: System shall maintain a Course Objective List (COL) mapping evidence tasks to training setting: Formal Course, Structured OJT, or Self-Study. Gap between COL and task inventory shall be surfaced
- **FR-16**: System shall capture Resource Constraints: budget, available time, course seat availability, SME access, technology
- **FR-17**: System shall display an external credential pathway mapping professional certifications to proficiency tiers

### 7.4 Onboarding and 30/60/90 Framework

- **FR-18**: System shall anchor the development arc to a Day 1 start date per employee
- **FR-19**: System shall calculate and display a Time to Productivity timeline from Day 1 showing plan completion rate, actual completion rate, today marker, and milestone markers at Day 30, 60, 90, 6 months, and 12 months
- **FR-20**: System shall display a plan vs. actual variance label: Ahead / On Track / Behind
- **FR-21**: System shall provide three checkpoint cards (Day 30, Day 60, Day 90) each containing: theme, "How to Help" support activities, "How to Evaluate" criteria, expected task completion %, actual completion %, checkpoint rating (Met / Partial / Not Met), and proficiency rubric focus
- **FR-22**: Checkpoint ratings shall be persisted in browser storage

### 7.5 Status Reporting

- **FR-23**: System shall display the following indicators:
  - *Lagging*: Foundation completion %, avg days to Foundation (vs. plan), certification velocity (tasks/month), 90-day checkpoint pass rate
  - *Leading*: velocity trend direction, days since last certification, pending sign-off age, approaching milestone within 14 days
  - *Predictive*: projected Foundation completion date at current velocity
- **FR-24**: Status report shall support filtering by function and by program/pathway
- **FR-25**: System shall classify employee status as: Ahead / On Track / Behind / Stalled (Stalled = no activity in 21+ days)
- **FR-26**: System shall display a pending action queue showing tasks with Training Complete but absent Certifier initials, with days waiting
- **FR-27**: All labels shall use plain business language. No analytics taxonomy in user-facing text

### 7.6 Talent Review

- **FR-28**: System shall support matrix org — each employee may have one direct-line and one or more dotted-line managers with typed relationships
- **FR-29**: Talent review shall be organizable by org element, direct-line chain, or dotted-line/matrix grouping
- **FR-30**: System shall calculate promotion readiness against configured leveling guidelines: Ready / Developing / Not Yet, with specific evidence gaps cited
- **FR-31**: System shall detect and flag misalignment when direct-line development assessment and dotted-line/client results assessment diverge materially. Misalignment shall be surfaced before review meetings
- **FR-32**: System shall maintain a review calendar showing upcoming reviews within a 90-day horizon organized as Immediate (0–30), Near-Term (30–60), Planned (60–90)
- **FR-33**: Review types: Direct Leader, Senior Leader (non-exec), Executive, Client-Requested, Rotation Gate (18-month), Annual Promotion Gate
- **FR-34**: For each upcoming review: title, type, employees on agenda, readiness %, and specific preparation actions
- **FR-35**: System shall maintain standing briefs at three levels — always current from live data: Individual brief, Leader brief, Client brief
- **FR-36**: Client brief shall support HR-entered and Client-submitted input modes. Entry source shall be recorded
- **FR-37**: Talent pool field shall display a note directing to the external system; no pool data stored here

### 7.7 Priority Actions (Prescriptive)

- **FR-38**: System shall generate ranked top 3–5 priority actions for upcoming reviews, at-risk employees, and function-level gaps
- **FR-39**: Each action shall include: what to do, who owns it, by when, why it matters, expected impact, and the assumption underlying the recommendation
- **FR-40**: Actions shall be grouped by time horizon: Immediate (this week), Near-Term (this month), Planned (60–90 days)
- **FR-41**: Each action shall reference the review gate or development event it prepares for
- **FR-42**: Priority logic shall weight by: gap severity × competency criticality × employees affected × days until relevant gate

### 7.8 Data Export and Integration

- **FR-43**: System shall export all development data as structured JSON with a documented field schema
- **FR-44**: System shall export a talent review summary as CSV suitable for BOBJ or similar BI platforms
- **FR-45**: JSON schema shall document all fields to support BOBJ universe construction as a supplementary data source alongside HCM master data
- **FR-46**: System shall support CSV import of employee roster from HCM systems (SuccessFactors / Workday / SAP HCM)
- **FR-47**: Data responsibility separation: employee master data sourced from HCM; development data owned by this system
- **FR-48**: System shall display the JSON schema on demand for integration configuration

---

## 8. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-01 | System shall operate entirely client-side with no server dependency |
| NFR-02 | All user-generated data shall be persisted in browser localStorage with JSON export/import for portability |
| NFR-03 | System shall be deployable as a static site (GitHub Pages, Netlify, or equivalent) with no build process |
| NFR-04 | The entire application shall be distributable as a set of HTML files plus a JSON data export |
| NFR-05 | No analytics or data science terminology shall be visible to end users |
| NFR-06 | All content representing a specific career field shall be modifiable without code changes to core logic |
| NFR-07 | System shall not assume a fixed org hierarchy. Any employee shall support any combination of reporting relationships |
| NFR-08 | Talent pool designation, succession slate data, and compensation data shall not be stored or transmitted by this system |
| NFR-09 | System shall function in current versions of Chrome, Firefox, Safari, and Edge |

---

## 9. Data Model

### Employee
```
id, name, role, businessUnit, orgElement, startDate, daysInRole (calc),
pathway (initial|lateral), track (ic|leadership), arcPhase, targetRole,
ldpProgram, directLine {name, title},
dottedLine [{name, title, type (business|functional)}],
certPct, velocity, status (ahead|on|behind|stalled),
promotionReadiness (ready|developing|not-yet),
misalignment {type, description},
lastReview {date, level, outcome},
nextReview {days, type}
```

### Competency Ontology Node
```
domainId, domainName, color,
competencyId, competencyName, description, supportingCompetencies[],
tier {
  label (Foundation|Practitioner|Expert|Master),
  requiredBehaviors[],
  impactCriterion,
  tasks [{
    taskNum, statement, difficulty (1|2|3), behaviorMatch (bool),
    coreCert (Core|Cert|Opt), contexts (S|D|X)[],
    proficiencyCodes {foundation, journeyman, expert, master}
  }]
}
```

### OJT Certification Record
```
taskNum, trainingStart (date), trainingComplete (date),
traineeInitials, trainerInitials, certifierInitials,
certifiedDate (calculated — date when all three initials present)
```

### Review Calendar Entry
```
reviewId, type (executive|senior|direct|client|rotation|promotion),
daysUntil (integer), title, description,
employees (name[]), readinessPct (integer), prepActions (string[])
```

### Client Brief Record
```
employeeId, text, source (hr|client), date, authorName
```

### Checkpoint Rating
```
employeeId, checkpointDay (30|60|90),
rating (Met|Partial|Not Met), date
```

---

## 10. Out of Scope

| Item | Reason / Notes |
|---|---|
| Talent pool and succession slate data | Organizational sensitivity; maintained in external interfacing system |
| 360-degree feedback surveys | Explicitly excluded by design principle |
| SPSS or statistical analysis integration | Not required; evidence model is qualitative and behavioral |
| Real-time database synchronization | Client-side architecture; file-based export/import used instead |
| Authentication and role-based access control | Future requirement; not in initial scope |
| Payroll or compensation data | Different system of record; organizational sensitivity |
| Formal performance management ratings | Reside in HCM; this tool captures development evidence |
| Direct HCM API integration | File import/export only in current scope |
| Mobile-native application | Browser-based only; mobile responsiveness is a future enhancement |
| Causal analytics | Requires longitudinal data across multiple cohorts; future capability |

---

## 11. Integration Points

| External System | Direction | Method | Data Exchanged |
|---|---|---|---|
| HCM (SuccessFactors / Workday / SAP) | Inbound | CSV import | Employee master: name, role, function, BU, start date, manager |
| BOBJ / BI Platform | Outbound | JSON export → universe data source | Arc position, certification %, promotion readiness, review history |
| Talent Review System (external) | Bidirectional (manual) | Export feeds calibration; designations returned manually | Development brief output; pool designation input (manual entry) |
| LDP Platform | Inbound (manual) | Manual entry | Program enrollment status |

---

## 12. Open Questions and Future Considerations

| Item | Notes |
|---|---|
| Authentication and RBAC | Individual vs. leader vs. executive access control |
| Multi-tenant deployment | Supporting multiple organizations from a single instance |
| Live HCM API integration | Real-time vs. periodic CSV refresh |
| Notification system | Email or in-app alerts for approaching gates and pending certifications |
| Causal analytics | Requires 3+ cohorts of longitudinal data before meaningful analysis |
| Mobile optimization | Current design is desktop-first |
| Automated misalignment thresholds | What delta between direct-line and client assessment triggers a flag? |
| Context flags for disruption events | Technology transitions, org restructuring — velocity expectation adjustments |
| Leader access controls | Should leaders see peer team data? |
| Historical arc visualization | Full career timeline view spanning multiple roles |
| Peer review for IC Expert/Master | Named, gate-based review by domain peers (not 360) — mechanism TBD |
| Next target role catalog | A library of defined next roles with their required proficiency profiles |

---

*Document maintained in the id-workflow project repository. For questions, contact Matthew Trafican.*
