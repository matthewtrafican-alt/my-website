# Workforce Intelligence Platform — Demo

**WIP-SRNA-001 v1.0** · AI-Powered Strategic Workforce Planning, Competency Intelligence & H2R Process Analytics

Live demo: [View on GitHub Pages](https://matthewtrafican-alt.github.io/website/platform-demo/)

## What this demo shows

| Section | Description |
|---|---|
| **Overview** | Platform KPI dashboard — cascade health, capability gaps, action items |
| **Strategic WFP** | 3-year capability gap analysis, Workforce Readiness Index, build/buy/borrow/bot |
| **Operational WFP** | Annual headcount plan vs budget vs actual, succession risk matrix |
| **Tactical / H2R** | Active case risk scores, SLA breach analysis, H2R process KPIs |
| **Competency Models** | INCOSE SECF-format competency models grounded in O*NET, NICE, R&M BoK |
| **Cascade Engine** | Bidirectional planning layer connector — breaks, health score, flow diagram |
| **AI Agent** | Claude API-powered workforce planning agent (mock responses in demo) |
| **Architecture** | Nine-layer platform architecture diagram |
| **Framework Backbone** | O*NET · NICE · INCOSE SECF · R&M BoK · Bloom's Taxonomy · UGESP |

## Technology stack (production)

- **Data**: Databricks Lakehouse · Delta Lake · Unity Catalog
- **AI**: Anthropic Claude API (claude-sonnet-4) · ChromaDB RAG
- **Ontology**: Neo4j Knowledge Graph · OWL Domain Ontology
- **Analytics**: PM4Py Process Mining · scikit-learn · SHAP
- **Visualisation**: React Dashboard · Tableau · AI Agent Chat UI

## Requirements documents

- `WIP-SRNA-001-v1.0.docx` — Full system requirements & notional architecture
- `H2R-SRNA-001` — Source H2R Process Intelligence Platform requirements (extended by WIP-SRNA-001)
