# FlowMind AI --- Autonomous Workflow Agent

FlowMind AI is a multi-agent autonomous system that converts
unstructured business inputs into executable workflows, validates them,
and self-recovers from failures --- all while maintaining a complete
audit trail.

It is designed as a scalable architecture for enterprise workflow
automation using Agentic AI.

------------------------------------------------------------------------

## Problem Statement

This project addresses:

**"Agentic AI for Autonomous Enterprise Workflows"**\
from the ET Gen AI Hackathon 2026.

The goal is to build a system that: - Processes complex multi-step
workflows\
- Works with unstructured input (text / transcripts)\
- Detects failures automatically\
- Recovers without human intervention\
- Maintains complete traceability

------------------------------------------------------------------------

## Solution Overview

FlowMind AI uses a **multi-agent architecture orchestrated via
LangGraph**.

Pipeline:

User Input / File Upload\
→ Preprocessing (cleaning + chunking)\
→ Extractor Agent\
→ Planner Agent\
→ Executor Agent\
→ Validator Agent\
→ Recovery Agent (if failure)\
→ SLA Agent (auto-fix)\
→ Final Validation\
→ Output + Logs

------------------------------------------------------------------------

## Core Architecture

### Input Layer

-   Text input
-   File upload (.txt, .md)

### Preprocessing

-   Cleaning
-   Chunking for long transcripts

### Agents

-   Extractor: Converts text → tasks\
-   Planner: Tasks → steps\
-   Executor: Simulates execution\
-   Validator: Rule-based validation\
-   Recovery: Fix suggestions\
-   SLA Agent: Auto-deadline assignment\
-   Final Validator: Ensures correctness

------------------------------------------------------------------------

## LLM Usage

Used only for: - Task extraction - Planning

API: **Groq API**\
Models: LLaMA / Mixtral variants

------------------------------------------------------------------------

## Logging

-   Stored in `data/logs.json`
-   Contains full agent trace

------------------------------------------------------------------------

## Output

-   Tasks\
-   Steps\
-   Validation status\
-   Issues\
-   Fixes

------------------------------------------------------------------------

## Tech Stack

-   Python\
-   LangGraph\
-   Groq API\
-   Streamlit

------------------------------------------------------------------------

## Setup

``` bash
git clone https://github.com/aryasm13/flowmind-ai.git
cd flowmind-ai
pip install -r requirements.txt
```

Create `.env`:

    GROQ_API_KEY=your_api_key

Run:

``` bash
python -m streamlit run app.py
```

------------------------------------------------------------------------

## Author

Arya Mulay
