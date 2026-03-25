# FlowMind AI — Autonomous Workflow Agent

FlowMind AI is a multi-agent system designed to automate enterprise workflows with minimal human intervention. It processes unstructured inputs such as business instructions or meeting transcripts, converts them into structured tasks, executes workflows, detects failures, and generates recovery actions — while maintaining a complete audit trail.

---

## Problem Statement

This project addresses the "Agentic AI for Autonomous Enterprise Workflows" challenge from the ET Gen AI Hackathon 2026.

The objective is to design a system that:
- Handles multi-step enterprise workflows end-to-end  
- Detects failures and self-corrects  
- Operates with minimal human involvement  
- Maintains auditability of all decisions  

---

## Solution Overview

FlowMind AI implements a modular multi-agent architecture:

- Extractor Agent: Converts raw input into structured tasks  
- Planner Agent: Breaks tasks into executable steps  
- Executor Agent: Simulates workflow execution  
- Validator Agent: Identifies inconsistencies and missing elements  
- Recovery Agent: Suggests corrective actions  

All intermediate steps are logged for traceability and evaluation.

---

## Key Features

- Multi-agent workflow orchestration  
- Support for text input and transcript file upload (.txt, .md)  
- Input preprocessing for improved consistency  
- Structured JSON outputs across all stages  
- Deterministic validation and failure detection  
- Automated recovery suggestions  
- Audit logging via logs.json  
- Interactive interface using Streamlit  

---

## System Architecture

User Input / File Upload  
→ Preprocessing Layer  
→ Extractor Agent  
→ Planner Agent  
→ Executor Agent  
→ Validator Agent  
→ Recovery Agent  
→ Output + Logs  

---

## Project Structure

```
flowmind-ai/
├── agents/
├── graph/
├── utils/
├── data/
├── app.py
├── main.py
├── requirements.txt
└── .env
```

---

## Setup Instructions

### 1. Clone Repository
- git clone https://github.com/aryasm13/flowmind-ai.git
- cd flowmind-ai  

### 2. Install Dependencies
pip install -r requirements.txt  

### 3. Configure Environment
Create a .env file:
GROQ_API_KEY=your_api_key_here  

### 4. Run Application
python -m streamlit run app.py  

---

## Evaluation Alignment

- Autonomy: End-to-end workflow execution with minimal input  
- Error Handling: Validator and Recovery agents ensure robustness  
- Auditability: All steps logged in structured format  
- Real-world Relevance: Supports meeting transcripts and business workflows  

---

## Future Enhancements

- SLA monitoring and delay prediction  
- Integration with enterprise tools (Slack, Jira, Email)  
- Persistent workflow memory  
- Real-time workflow tracking and escalation  

---

## Author

Arya Mulay
