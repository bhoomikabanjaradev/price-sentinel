This project is currently under active development. Some features may not work yet.

# 🦅 PriceSentinel: Multi-Agent Dynamic Pricing Engine

PriceSentinel is an automated, autonomous e-commerce command center powered by the **Google ADK (Agent Development Kit)** and **Gemini 2.5-flash**. This system moves beyond simple single-prompt routing pipelines into a structured, production-ready sequential multi-agent execution loop. 

By analyzing live market movements, checking cost-of-goods-sold (COGS) restrictions, and calculating inventory risk floors synchronously, PriceSentinel delivers real-time yield optimization directives directly to a responsive Streamlit operational dashboard.

Live on :https://dynamic-pricing-sentinel-1032946348770.us-central1.run.app/

## Core System Architecture

The core engineering workflow uses an isolated contextual chain design pattern. Instead of running isolated prompts, state data propagates through specialized cognitive layers:

[ Inbound Payload Ingested via UI/API ]

                   │

                   ▼

      ┌──────────────────────────┐

      │  Competitor Intel Agent  │ ──► Reads SKU data & parses market signals.

      └──────────────────────────┘

                   │

                   ▼

      ┌──────────────────────────┐

      │    Stock & COGS Agent    │ ──► Consumes Intel context; verifies inventory

      └──────────────────────────┘     safety levels and margin floors.

                   │

                   ▼

      ┌──────────────────────────┐

      │ Pricing Strategist Agent │ ──► Weighs consumer demand vs. stock risk to

      └──────────────────────────┘     declare the definitive optimized target price.

                   │

                   ▼

 [ Streamlit Analytics Dashboard Display ]

generate image architecture for it 


  
 ### 🧠 Agent Directory Breakdown
1. **Competitor Intel Agent (`competitor_intel_agent`):** Functions as your market intelligence analyst. It reads raw inbound text payloads to spot baseline competitive listings and immediate pricing shifts across external retail channels.
2. **Stock & COGS Agent (`stock_cogs_agent`):** Functions as your secure internal ledger auditor. It cross-references the intelligence analyst's output against actual unit availability metrics and strictly enforces baseline profitability threshold floors.
3. **Pricing Strategist Agent (`pricing_strategist_agent`):** Functions as the chief pricing architect. It evaluates market signals against inventory depletion risks to calculate a final strategic pricing recommendation.

---

# 📊 Application Interface & Features

| Capability | Engine Support | Operational Purpose |
| :--- | :--- | :--- |
| **Multi-Agent Cascade** | Google ADK 2.x | Automatically routes context through specialized sub-agents. |
| **Real-time Latency Audit** | Python `time` tracker | Measures precise model execution performance windows on-screen. |
| **Dynamic Ingestion Feed** | Streamlit UI Sidebar | Simulates shifting real-world warehouse inventories and market pressures. |
| **Automated Guardrails** | Profit Margin Protection | Prevents the LLM from suggesting prices below the calculated product cost floors. |


## 🗂️ Repository Architecture Layout

This tree maps the core architecture of the platform workspace:

```plaintext
price-sentinel/
├── .gitignore            # Security file isolating environments and private keys
├── Dockerfile            # Containerization instructions for Google Cloud Build
├── README.md             # Structural project documentation
├── agents.py             # Active Google ADK agent logic, models, and system instructions
├── app.py                # Streamlit dashboard interface and execution runtime loop
└── requirements.txt      # Engine packaging dependencies

🛠️ Installation & Local Setup
To run this application workspace locally on your device or within your active Google Cloud Shell framework, follow these steps:

1. **Clone & Navigate to Project Workspace**
Bash
git clone [https://github.com/bhoomikabanjaradev/price-sentinel.git](https://github.com/bhoomikabanjaradev/price-sentinel.git)
cd price-sentinel
2. **Initialize and Activate Python Environment**
Bash
# Create local virtual environment structure
python3 -m venv env

# Activate the isolated environment layer
source env/bin/activate

3. **Install Required Engine Packages**
Bash
pip install -r requirements.txt
4.**Execute the App Locally**
Bash
streamlit run app.py

🚀 Live Cloud Deployment
To package this workspace inside an automated, serverless container on Google Cloud Run, execute this single deployment sequence from your terminal prompt:

Bash
gcloud run deploy dynamic-pricing-sentinel \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_GENAI_USE_VERTEXAI=true,GOOGLE_CLOUD_LOCATION=global

## How to Use the Platform

Once the web application loads, you can simulate full-scale automated yield management in real time:

1. Ingest Product Streams: Use the left-side panel dropdown menu under 📦 Inventory Catalog Feeds to choose a target item signature profile (UltraView Pro 4K Monitor, EcoStride Running Shoes, or VoltCharge Travel Hub).

2. Inspect Raw Payload Ingestion: Notice how the blue informational banner dynamically adjusts to reflect changing supply conditions, catalog entries, or warehouse flags.

3. Execute the Agent Optimization Loop: Click the ⚡ Execute Agent Optimization Loop trigger button. This initiates a synchronous sequential handoff through your Google ADK agent framework.

4.Analyze Real-Time Auditing Trace: * Review the System Response Window metric to evaluate processing latency.
     Verify the green Workflow Node Status card to ensure seamless data propagation.

     Examine the generated markdown strategy text at the bottom of your screen to read the exact business rules, margins, and target pricing recommendations calculated by your agent network.

### What to do next:
Once you have saved this file, jump back to your terminal window and run these three commands to push this updated version straight to your active GitHub repository:

```bash
git add README.md
git commit -m "docs: expand README with directory layout and features table"
git push origin main
