# DETERMA
## The Authority Operating Layer for Digital Work
### External Pre-Read for Investors, Strategic Partners, and Enterprise Security / Engineering Leaders

**Status:** Canonical External Pre-Read v1.0  
**Date:** 2026-07-07  
**Audience:** Investors, strategic partners, CISOs, CTOs, VP Engineering, AppSec, DevSecOps, Platform, Security Architecture  
**Disclosure Level:** Public-safe. This document does not expose internal architecture, code, enforcement mechanics, proprietary protocols, private repositories, or implementation-sensitive details.  
**Canonical Role:** Category narrative / investor-partner pre-read / external-safe strategic positioning.  

---

## 0. Truth Boundary

This document is canonical for DETERMA's external positioning around Runtime Execution Authority and the broader Authority Operating Layer for Digital Work.

It may be used for investor pre-read materials, strategic partner conversations, expert pre-reads, CISO / CTO / VP Engineering discussions, category narrative development, and external-safe market education.

It must not be used to claim production deployment, paying customers, signed design partners, external technical validation, market adoption of the category, implementation details not explicitly disclosed elsewhere, or any partnership with companies mentioned in the competitive appendix.

The confidence in this document is in the thesis, the category, the problem, and the direction — not in unsupported commercial maturity claims.

---

## 1. Executive Summary

Enterprise AI is moving from a world of assistants that answer questions to a world of digital workers that execute work.

That shift changes the core enterprise question.

It is no longer enough to ask: **Can the AI produce the right answer?**

Organizations now need to ask: **Is the digital work being performed still authorized, grounded, traceable, and aligned with the organization at the moment of execution?**

DETERMA is being built for that layer.

The initial category is **Runtime Execution Authority**: a deterministic, external, evidence-based authority layer that validates whether an AI-initiated, AI-assisted, or automation-driven action is still authorized to execute at runtime.

The broader strategic category is **Authority Operating Layer for Digital Work**: a layer that governs the authority, memory, evidence, legitimacy, and accountability of digital work performed by AI Agents, Automations, Coding Assistants, and Digital Workers inside enterprise systems.

The market is already moving toward this problem. NanoCo is pushing secure agent execution. Band is building interaction infrastructure for distributed agents. Enterprise AI platforms such as Glean and Writer are organizing company knowledge and agentic work. MCP and agent SDKs are expanding how agents connect to tools, data, and workflows. Each layer makes AI more capable. Each layer also expands the authority problem.

DETERMA sits at the point where capability becomes responsibility.

---

## 2. Why This Problem Exists Now

Traditional enterprise systems were designed around human operators: a person requested access, identity checked permissions, a reviewer approved a change, CI/CD executed deployment, and audit recorded the event.

That model assumes that a human remains the primary unit of intent, judgment, accountability, and execution.

AI breaks that assumption.

The new operating pattern is:

```text
Agent proposes
Automation advances
Context shifts
Approval may become stale
Tool or API is invoked
Execution happens
```

AI Agents are beginning to operate across code repositories, CI/CD pipelines, cloud environments, CRM, ERP, finance, HR, data platforms, enterprise search, customer systems, internal operations, support workflows, and security operations.

As agents become connected to more tools, more data, more memory, and more execution surfaces, the problem is no longer just model safety. The problem becomes enterprise authority.

---

## 3. Existing Layers Are Necessary — But Not Sufficient

DETERMA does not replace the current enterprise control stack. It adds the missing runtime authority layer above and between it.

- **IAM** answers who can access what. DETERMA asks whether this specific action is still authorized to execute now.
- **AppSec** evaluates security risks. DETERMA evaluates whether a specific execution remains authorized under the current state, scope, authority chain, and context.
- **CI/CD** answers whether build, test, or deployment passed. DETERMA asks whether execution should still be allowed even if the pipeline passed.
- **Policy engines** evaluate rules. DETERMA treats policy as an input, not as the full authority decision.
- **Audit** records what happened. DETERMA validates before or during execution.
- **Human approval** is important, but it does not scale to the volume and speed of AI-driven work and can become stale.

Canonical distinction:

```text
A valid identity is not a valid action.
A clean pipeline is not proof that authority still exists.
Approval is evidence, not final authority.
Audit explains after. DETERMA validates before execution.
```

---

## 4. What DETERMA Adds

DETERMA introduces a runtime authority decision layer.

It is not another agent, chatbot, agent runtime, agent mesh, IAM system, AppSec tool, CI/CD tool, audit tool, or generic AI governance platform.

DETERMA is the authority layer around the moment where digital work becomes execution.

Its core question is:

```text
Given the current context, current state, current evidence,
current authority chain, current policy, and current risk profile —
may this action still proceed?
```

The output is:

```text
ALLOW
DENY
NEEDS_REVIEW
```

The decision is accompanied by a receipt: a clear, traceable explanation of what was evaluated, why the action was allowed, denied, or escalated, and what evidence supported the decision.

---

## 5. Beyond Execution: The Broader DETERMA Vision

Runtime Execution Authority is the wedge. The broader vision is larger.

Enterprises will not operate a single agent performing a single task. They will operate networks of digital workers: research agents, coding agents, sales agents, support agents, finance agents, security agents, compliance agents, data agents, operations agents, and internal automation workers.

For digital workers to become part of the enterprise operating fabric, they need more than access and prompts. They need identity, role, owner, scope, organizational memory, knowledge boundaries, data-use boundaries, authority chain, permitted actions, denied actions, escalation logic, receipts, evidence trail, decision history, auditability, policy linkage, organizational context, and human accountability.

That is why DETERMA is better understood as **Authority Operating Layer for Digital Work**: a layer that governs the authority, memory, evidence, legitimacy, and accountability of digital work inside the enterprise.

---

## 6. From Company Brain to Authority Brain

Many companies are building Company Brain platforms. This is important. Enterprises need AI systems that can understand internal knowledge: documents, tickets, policies, emails, CRM, data warehouses, previous decisions, customer records, code, conversations, and operational history.

But a Company Brain primarily answers: **What does the organization know?**

DETERMA asks a different question: **Which parts of what the organization knows may be used by this digital worker, for this action, under this authority, in this context, now?**

Knowledge is not authority. Memory is not authority. Context is not authority. Access to data is not authority. A citation is not authority. A policy reference is not authority by itself.

DETERMA turns knowledge and memory into authority context by connecting source of knowledge, evidence strength, organizational relevance, role scope, action intent, policy context, authority chain, runtime state, and decision receipt.

This is the move from Company Brain to Authority Brain.

---

## 7. Market Landscape

The market is moving quickly, but most players are solving adjacent layers rather than the authority layer itself.

### Agent Runtime and Secure Execution

NanoCo and NanoClaw represent the secure agent execution layer: safer agent runtimes, isolation, credentials control, memory, skills, approval, audit, and infrastructure-level control.

That is an important layer. But safe execution is not the same as authorized execution. A sandboxed agent can still perform an unauthorized action.

### Agent Interaction and Multi-Agent Governance

Band represents interaction infrastructure for distributed AI agents: discovery, delegation, routing, shared context, interaction governance, runtime visibility, approval, and audit.

That is also an important layer. But governed interaction is not the same as execution authority. A delegation chain can be visible, auditable, and governed — and still lead to an action that is no longer authorized.

### Enterprise Knowledge and Work AI

Glean, Writer, and similar platforms represent enterprise knowledge and work-AI layers: enterprise search, knowledge graphs, context systems, agents, orchestration, governance, and work execution.

These platforms help AI know and produce more. DETERMA governs what AI is allowed to do with what it knows.

### Tool and Data Connectivity

MCP, connectors, and tool-calling frameworks standardize how AI applications connect to external systems, data sources, tools, and workflows.

Connectivity makes agents more capable. It also expands the authority surface. Every new connector, tool, skill, MCP server, or API invocation creates a new question: **Is this use still authorized?**

---

## 8. DETERMA's Strategic Position

DETERMA sits above and between these layers.

```text
Agents
Tools
MCP
Company Brain
Memory
Knowledge Graph
Agent Mesh
Human Approval
Policy
Audit
CI/CD
Business Workflows
        ↓
DETERMA
        ↓
Runtime Authority Decision
```

DETERMA does not replace agent runtimes, meshes, knowledge systems, IAM, policy, CI/CD, or audit. It converts them into authority inputs.

It asks what the agent is trying to do, what system will be affected, what data is being used, what knowledge is being relied on, what memory is influencing the action, what approval exists, whether approval has become stale, what policy applies, whether context changed, whether scope expanded, whether the authority chain is still valid, and whether execution should proceed, stop, or escalate.

That is the authority gap. That is the category DETERMA is built to own.

---

## 9. Why This Matters to Investors

DETERMA is not another productivity wrapper around AI. It is positioned around a structural control layer that becomes more necessary as AI agents move deeper into enterprise work.

The market logic is straightforward:

1. More agents will enter organizations.
2. More agents will connect to tools, data, workflows, and enterprise knowledge.
3. More agents will perform real work.
4. More work will involve actions, not just answers.
5. More actions will require authority, not just access.
6. Enterprises will discover that approval, audit, IAM, AppSec, and policy are necessary but incomplete.
7. A new category will emerge around runtime authority and digital work accountability.

DETERMA is built to define that category early.

The initial wedge is narrow and measurable: **a digital action was approved earlier, but may no longer be authorized at execution time.**

The broader company vision is larger: **the authority layer for digital work.**

---

## 10. Why This Matters to Strategic Partners

Companies building AI agents, agent platforms, enterprise AI, knowledge platforms, workflow automation, developer tools, CI/CD, cloud operations, data platforms, or security platforms will all face the same question:

**As they allow AI to do more, who validates what the AI is still allowed to do?**

DETERMA can sit as a complementary layer above agent runtimes, coding assistants, agentic workflow platforms, enterprise assistants, AI knowledge platforms, CI/CD systems, cloud operations, data platforms, security orchestration, identity systems, and business automation platforms.

The partner message is simple:

```text
You enable AI to act.
DETERMA validates whether the action is still authorized.
```

This lets partners extend AI capability without having to become the full authority layer themselves.

---

## 11. Why This Matters to CISOs, Security Architects, and Engineering Leaders

Security and engineering leaders do not need another vague promise of safe AI.

They need operational answers:

- Who or what is about to act?
- On whose behalf?
- Using which data?
- Against which system?
- Under which policy?
- Based on which approval?
- Has the approval become stale?
- Has the context changed?
- Has the scope expanded?
- Is there evidence?
- Should execution stop?
- Should a human review it?
- Will there be a receipt that can be explained later?

DETERMA is built to provide a deterministic, evidence-based answer at the point where digital work becomes action.

---

## 12. Safe Entry Path: Shadow Mode

DETERMA can enter enterprise conversations safely because the first step does not require taking control of production execution.

The recommended entry path is **Shadow Mode**.

In Shadow Mode, DETERMA observes a defined workflow, evaluates execution-authority gaps, and generates decision evidence without becoming a production blocking layer.

Principles:

- no production access;
- no write access;
- no secrets;
- metadata-first;
- observation only;
- defined workflow;
- authority drift detection;
- receipts;
- evidence report;
- staged expansion only when value is clear.

The goal is not to replace existing systems. The goal is to show where an action that appears approved, safe, or compliant may no longer be authorized at execution time.

---

## 13. Initial Use Cases

### AI-Generated Code Changes

An agent proposes a code change, a PR advances, review is completed, CI passes, and before merge the branch, diff, dependency, reviewer context, or policy changes.

DETERMA asks: **Is this merge still authorized now?**

### Agent Tool / API Invocation

An agent is about to invoke an API, connector, MCP server, package, skill, or external tool.

DETERMA asks: **Is this invocation still authorized for this agent, task, data, policy, and context?**

### Digital Worker Using Company Knowledge

A digital worker uses enterprise knowledge to act inside a CRM, finance system, support workflow, legal process, or customer operation.

DETERMA asks: **Is this digital worker authorized to use this knowledge for this action, against this target, now?**

### Multi-Agent Delegation

One agent plans, another reviews, another executes, another opens a PR, ticket, workflow, or transaction, and a human approves part of the chain.

DETERMA asks: **Does the delegation chain still authorize the final action?**

### Human Approval That Becomes Stale

A human approves a task. Between approval and execution, the action changes.

DETERMA asks: **Does the original approval still cover the actual action?**

---

## 14. What Makes DETERMA Different

- DETERMA is not just protecting execution. It connects execution to context, memory, evidence, and authority.
- DETERMA is not just organizing knowledge. It determines whether knowledge may be used for a specific action.
- DETERMA is not just managing agents. It governs digital work.
- DETERMA is not just producing audit. It validates before execution and records the decision.
- DETERMA is not just a guardrail inside the model. It is external to the agent and the model.
- DETERMA is not just a tool. It is an authority layer for a new category of enterprise work.

---

## 15. The Category Definition

DETERMA's initial category:

## Runtime Execution Authority

A deterministic, external, evidence-based layer that validates whether an AI-initiated or automation-driven action is still authorized at execution time.

DETERMA's broader category:

## Authority Operating Layer for Digital Work

An enterprise infrastructure layer that governs the authority, context, memory, evidence, legitimacy, and accountability of digital work performed by AI Agents, Automations, Coding Assistants, and Digital Workers.

It answers:

## Is this digital work still authorized, grounded, traceable, and aligned with the organization?

---

## 16. What We Want to Learn in Strategic Conversations

The purpose of upcoming conversations is not to debate whether the problem exists.

The problem emerges wherever AI is connected to tools, data, workflows, memory, and execution.

The goal is to sharpen the first workflow where pain is measurable, the right buyer, the output that proves value, the metadata available without operational risk, the safest Shadow Mode path, the right language for Security / Engineering / Platform / Leadership, the right partner architecture, and the boundary between agent execution, agent interaction, enterprise knowledge, and runtime authority.

---

## 17. Discussion Questions

1. Where does AI move from assistance to execution in your environment?
2. Where does approval exist today, and where can it become stale?
3. Where does an agent use enterprise knowledge to perform a real action?
4. Where does tool, API, connector, or MCP invocation create authority risk?
5. Where does multi-agent delegation create a chain-of-authority problem?
6. What metadata can be evaluated without production access, write access, or secrets?
7. What output would make Security or Engineering continue to Shadow Mode?
8. Who should own Runtime Execution Authority: Security, Engineering, Platform, Data, Governance, or a cross-functional owner?
9. Is this seen as Security, Platform, AI Governance, Digital Workforce Infrastructure, or a new category?
10. Which first workflow is most measurable?

---

# Appendix A — Competitive Landscape and DETERMA Differentiation

## A1. Competitive Map

| Layer | Representative Companies / Technologies | What They Solve | Natural Limitation | DETERMA Differentiation |
|---|---|---|---|---|
| Agent Runtime / Secure Execution | NanoCo / NanoClaw, agent runtime platforms, sandboxed coding agents | Run agents more safely, isolate execution, protect credentials, manage skills and channels | Safe runtime does not prove authorized action | DETERMA validates whether the specific action remains authorized |
| Agent Interaction / Mesh | Band | Agent discovery, delegation, routing, shared context, visibility, interaction governance | Governed interaction does not prove authorized execution | DETERMA validates the authority of the final action after coordination and delegation |
| Enterprise Knowledge / Work AI | Glean, Writer, Dust-like platforms | Connect AI to company knowledge, enterprise graph, search, assistants, agentic work | Knowledge does not determine permitted use | DETERMA turns knowledge into authority context |
| Tool / Data Connectivity | MCP, connectors, tool-calling frameworks | Connect AI applications to tools, data, workflows, and systems | Connectivity expands capability but not authority | DETERMA validates whether each invocation is authorized |
| Agent Orchestration / SDKs | OpenAI Agents SDK, LangGraph, CrewAI, workflow frameworks | Build agents, define tools, orchestrate workflows, manage state, guardrails, evals | Orchestration can advance work without external authority continuity | DETERMA sits outside the agent loop as the authority layer |
| IAM / Identity | Okta, Microsoft Entra, CyberArk, identity platforms | Determine who can access what | Valid identity is not a valid action | DETERMA evaluates action-level authority |
| AppSec / Code Security | Snyk, Semgrep, Wiz, GitHub Advanced Security, scanners | Detect vulnerabilities, dependency risk, misconfigurations | Secure code is not necessarily authorized execution | DETERMA validates authority continuity before execution |
| CI/CD / DevOps | GitHub Actions, GitLab, CircleCI, Harness, Argo | Build, test, deploy, orchestrate delivery | Pipeline success is not authorization | DETERMA validates whether execution should still proceed |
| Audit / Observability | SIEM, logging, audit platforms, monitoring | Record and observe what happened | Audit is after-the-fact | DETERMA decides before or during execution |
| Human Approval / Workflow | Jira, ServiceNow, GitHub review, Slack approvals | Create approval checkpoints | Approval can become stale and does not scale for high-volume agent work | DETERMA recomputes authority at runtime and escalates only when needed |

## A2. Final Competitive Positioning

```text
NanoCo secures agent execution.
Band governs agent interaction.
Glean and Writer organize enterprise knowledge.
MCP connects agents to tools and data.
Agent SDKs orchestrate agent work.
DETERMA governs the authority, memory, evidence, and legitimacy of digital work.
```

DETERMA's unique category is not AI security in general.

It is:

## Runtime Execution Authority

And the broader company vision is:

## Authority Operating Layer for Digital Work

The market is moving toward agents that can act.

DETERMA is built for the moment when the enterprise must decide whether that action is still authorized.
