import os
from google.adk.agents.llm_agent import LlmAgent as Agent
from google.adk.agents.sequential_agent import SequentialAgent

# ==========================================
# 1. Specialized ADK Agent Definitions
# ==========================================
competitor_intel_agent = Agent(
    name="competitor_intel_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an expert E-commerce Intelligence Analyst. 
    Analyze the incoming product SKU query. Output exactly like this format:
    COMPETITOR_AVG: 345.00 | DEMAND: HIGH
    """
)

stock_cogs_agent = Agent(
    name="stock_cogs_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an Internal Inventory Auditor. 
    Analyze the product stream. Output exactly like this format:
    STOCK: 140 | MIN_MARGIN_FLOOR: 250.0
    """
)

pricing_strategist_agent = Agent(
    name="pricing_strategist_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are the Chief Pricing Architect. 
    Look at the previous analyst and auditor outputs. Combine them to pick a smart recommended price.
    Output your final calculation and a brief strategy explanation clearly.
    """
)

# ==========================================
# 2. Native ADK Sequential Workflow Hierarchy
# ==========================================
compiled_pricing_workflow = SequentialAgent(
    name="dynamic_pricing_workflow",
    sub_agents=[competitor_intel_agent, stock_cogs_agent, pricing_strategist_agent],
    description="Coordinate the e-commerce audit loop step by step from intel to audit to final target pricing strategy."
)