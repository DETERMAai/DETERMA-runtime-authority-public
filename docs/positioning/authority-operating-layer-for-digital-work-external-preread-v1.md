# DETERMA

## The Authority Operating Layer for Digital Work

### External Pre-Read for Investors, Strategic Partners, and Enterprise Security / Engineering Leaders

**Version:** Canonical External Pre-Read v1.0  
**Date:** 2026-07-07  
**Audience:** Investors, strategic partners, CISOs, CTOs, VP Engineering, AppSec, DevSecOps, Platform, Security Architecture  
**Disclosure Level:** Public-safe. This document does not expose internal architecture, code, enforcement mechanics, proprietary protocols, private repositories, or implementation-sensitive details.  
**Canonical Role:** External category narrative for Runtime Execution Authority and the broader Authority Operating Layer for Digital Work.

---

## 1. Executive Summary

Enterprise AI is moving from a world of assistants that answer questions to a world of digital workers that execute work.

That shift changes the core enterprise question.

It is no longer enough to ask:

**Can the AI produce the right answer?**

Organizations now need to ask:

**Is the digital work being performed still authorized, grounded, traceable, and aligned with the organization at the moment of execution?**

DETERMA is being built for that layer.

We define the initial category as:

## Runtime Execution Authority

A deterministic, external, evidence-based authority layer that validates whether an AI-initiated, AI-assisted, or automation-driven action is still authorized to execute at runtime.

The broader strategic category is:

## Authority Operating Layer for Digital Work

A layer that governs the authority, memory, evidence, legitimacy, and accountability of digital work performed by AI Agents, Automations, Coding Assistants, and Digital Workers inside enterprise systems.

The market is already moving toward this problem. NanoCo is pushing secure agent execution. Band is building interaction infrastructure for distributed agents. Enterprise AI platforms such as Glean and Writer are organizing company knowledge and agentic work. MCP and agent SDKs are expanding how agents connect to tools, data, and workflows. Each layer makes AI more capable. Each layer also expands the authority problem.

DETERMA sits at the point where capability becomes responsibility.

---

## 2. Why This Problem Exists Now

Traditional enterprise systems were designed around human operators.

A person requested access.  
An identity system checked permissions.  
A reviewer approved a change.  
A CI/CD system executed a deployment.  
Audit recorded what happened.

That model assumes that a human remains the primary unit of intent, judgment, accountability, and execution.

AI breaks that assumption.

The new operating pattern looks different:

```text
Agent proposes
Automation advances
Context shifts
Approval may become stale
Tool or API is invoked
Execution happens
```

AI Agents are beginning to operate across:

- code repositories;
- CI/CD pipelines;
- cloud environments;
- CRM systems;
- ERP systems;
- finance workflows;
- HR workflows;
- data platforms;
- enterprise search;
- customer systems;
- internal operations;
- support workflows;
- security operations.

As agents become connected to more tools, more data, more memory, and more execution surfaces, the problem is no longer just model safety.

The problem becomes enterprise authority.

---

## 3. Existing Layers Are Necessary — But Not Sufficient

The current enterprise stack already contains important control layers. DETERMA does not replace them. It adds the missing runtime authority layer above and between them.

### IAM

IAM answers:

**Who can access what?**

DETERMA asks:

**Is this specific action still authorized to execute now?**

A valid identity is not the same as a valid action.

### AppSec

AppSec evaluates security risks in code, dependencies, configurations, and systems.

DETERMA evaluates whether a specific execution remains authorized under the current state, scope, authority chain, and context.

A change can pass security checks and still no longer be authorized to proceed.

### CI/CD

CI/CD answers:

**Did the build, test, or deployment pipeline pass?**

DETERMA asks:

**Should execution still be allowed even if the pipeline passed?**

A clean pipeline is not proof that authority still exists.

### Policy Engines

Policy engines evaluate rules.

DETERMA treats policy as an important input, but not as the full authority decision.

Policy without current context, authority continuity, evidence, intent, and runtime state is incomplete.

### Audit

Audit records what happened.

DETERMA validates before or during execution, when the organization still has a chance to allow, deny, or escalate.

Audit explains after.  
DETERMA validates before execution.

### Human Approval

Human approval is important, but it does not scale to the volume and speed of AI-driven work.

It can also become stale.

Between approval and execution, the context may change:

- the branch changes;
- the diff expands;
- the payload changes;
- the target system changes;
- the data changes;
- the policy changes;
- the agent gains a new tool;
- the delegated actor changes;
- the original intent no longer covers the final action.

DETERMA does not remove humans from the loop.

It makes the loop scalable by escalating only the cases that require human judgment.

---

## 4. What DETERMA Adds

DETERMA introduces a runtime authority decision layer.

It is not another agent.  
It is not another chatbot.  
It is not an agent runtime.  
It is not an agent mesh.  
It is not IAM.  
It is not AppSec.  
It is not CI/CD.  
It is not audit.  
It is not a generic AI governance platform.

DETERMA is the authority layer around the moment where digital work becomes execution.

Its core question is:

```text
Given the current context, current state, current evidence,
current authority chain, current policy, and current risk profile —
may this action still proceed?
```

The output is simple:

```text
ALLOW
DENY
NEEDS_REVIEW
```

The decision is accompanied by a receipt: a clear, traceable explanation of what was evaluated, why the action was allowed, denied, or escalated, and what evidence supported the decision.

DETERMA’s public positioning frames the problem as runtime legitimacy for autonomous execution systems: approvals decay after issuance, runtime conditions change, and DETERMA recomputes execution legitimacy before autonomous mutations commit.

---

## 5. Beyond Execution: The Broader DETERMA Vision

Runtime Execution Authority is the wedge.

The broader vision is larger.

Enterprises will not operate a single agent performing a single task. They will operate networks of digital workers:

- research agents;
- coding agents;
- sales agents;
- support agents;
- finance agents;
- security agents;
- compliance agents;
- data agents;
- operations agents;
- internal automation workers.

For digital workers to become part of the enterprise operating fabric, they need more than access and prompts.

They need:

- identity;
- role;
- owner;
- scope;
- organizational memory;
- knowledge boundaries;
- data-use boundaries;
- authority chain;
- permitted actions;
- denied actions;
- escalation logic;
- receipts;
- evidence trail;
- decision history;
- auditability;
- policy linkage;
- organizational context;
- human accountability.

That is why DETERMA is better understood as:

## Authority Operating Layer for Digital Work

A layer that governs the authority, memory, evidence, legitimacy, and accountability of digital work inside the enterprise.

---

## 6. From Company Brain to Authority Brain

Many companies are building “Company Brain” platforms.

This is important. Enterprises need AI systems that can understand internal knowledge:

- documents;
- tickets;
- policies;
- emails;
- CRM;
- data warehouses;
- previous decisions;
- customer records;
- code;
- conversations;
- operational history.

But a Company Brain primarily answers:

**What does the organization know?**

DETERMA asks a different question:

**Which parts of what the organization knows may be used by this digital worker, for this action, under this authority, in this context, now?**

That distinction matters.

Knowledge is not authority.  
Memory is not authority.  
Context is not authority.  
Access to data is not authority.  
A citation is not authority.  
A policy reference is not authority by itself.

DETERMA turns knowledge and memory into authority context.

It connects:

- source of knowledge;
- evidence strength;
- organizational relevance;
- role scope;
- action intent;
- policy context;
- authority chain;
- runtime state;
- decision receipt.

This is the move from Company Brain to Authority Brain.

---

## 7. Market Landscape

The market is moving quickly, but most players are solving adjacent layers rather than the authority layer itself.

### Agent Runtime and Secure Execution

NanoCo positions its product as AI agents designed for organizations, combining individual context, secure execution, and infrastructure-level control. Its public messaging also describes assistants living in Slack or Teams and emphasizes sandboxing, zero credentials, human approval, audit, and customer infrastructure control.

NanoClaw, the open-source project behind NanoCo’s motion, emphasizes container isolation, per-agent workspaces, memory, skills, and credential routing through an Agent Vault.

That is an important layer.

But safe execution is not the same as authorized execution.

A sandboxed agent can still perform an unauthorized action.

### Agent Interaction and Multi-Agent Governance

Band describes itself as interaction infrastructure for distributed AI agents. It frames multi-agent systems as distributed systems that need infrastructure where agents and humans collaborate side by side with built-in governance.

Band’s Agentic Mesh is positioned as a collaboration layer for distributed AI agents, handling identity, discovery, routing, delivery, crash recovery, and governance across frameworks and clouds.

That is also an important layer.

But governed interaction is not the same as execution authority.

A delegation chain can be visible, auditable, and governed — and still lead to an action that is no longer authorized.

### Enterprise Knowledge and Work AI

Glean’s public positioning includes enterprise search, personal graph, enterprise graph, system of context, agents, agent orchestration, agent governance, and work execution.

Writer positions itself as an enterprise AI platform for agentic work, with Writer Agent, Playbooks, AI Studio, Connectors, Palmyra LLMs, Knowledge Graph, and trust/security capabilities.

These platforms are important because they organize enterprise knowledge and make AI useful in real workflows.

But enterprise knowledge is not the same as authority.

A digital worker may know the answer and still not be authorized to use that knowledge for a specific action.

### Tool and Data Connectivity

MCP is an open-source standard for connecting AI applications to external systems, including data sources, tools, and workflows, allowing AI applications to access information and perform tasks.

Agent SDKs and platform tools increasingly include agent definitions, sandbox agents, orchestration, guardrails, state, observability, workflow evaluation, tools, MCP, shell, and computer use.

Connectivity makes agents more capable.

It also expands the authority surface.

Every new connector, tool, skill, MCP server, or API invocation creates a new question:

**Is this use still authorized?**

---

## 8. DETERMA’s Strategic Position

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

DETERMA does not replace agent runtimes, meshes, knowledge systems, IAM, policy, CI/CD, or audit.

It converts them into authority inputs.

It asks:

- What is the agent trying to do?
- What system will be affected?
- What data is being used?
- What knowledge is being relied on?
- What memory is influencing the action?
- What approval exists?
- Has the approval become stale?
- What policy applies?
- Has the context changed?
- Has the scope expanded?
- Is the authority chain still valid?
- Should execution proceed, stop, or escalate?

That is the authority gap.

That is the category DETERMA is built to own.

---

## 9. Why This Matters to Investors

DETERMA is not another productivity wrapper around AI.

It is positioned around a structural control layer that becomes more necessary as AI agents move deeper into enterprise work.

The market logic is straightforward:

1. More agents will enter organizations.
2. More agents will connect to tools, data, workflows, and enterprise knowledge.
3. More agents will perform real work.
4. More work will involve actions, not just answers.
5. More actions will require authority, not just access.
6. Enterprises will discover that approval, audit, IAM, AppSec, and policy are necessary but incomplete.
7. A new category will emerge around runtime authority and digital work accountability.

DETERMA is built to define that category early.

The initial wedge is narrow and measurable:

**A digital action was approved earlier, but may no longer be authorized at execution time.**

The broader company vision is larger:

## The authority layer for digital work.

---

## 10. Why This Matters to Strategic Partners

Companies building AI agents, agent platforms, enterprise AI, knowledge platforms, workflow automation, developer tools, CI/CD, cloud operations, data platforms, or security platforms will all face the same question:

As they allow AI to do more, who validates what the AI is still allowed to do?

DETERMA can sit as a complementary layer above:

- agent runtimes;
- coding assistants;
- agentic workflow platforms;
- enterprise assistants;
- AI knowledge platforms;
- CI/CD systems;
- cloud operations;
- data platforms;
- security orchestration;
- identity systems;
- business automation platforms.

The partner message is simple:

**You enable AI to act.  
DETERMA validates whether the action is still authorized.**

This lets partners extend AI capability without having to become the full authority layer themselves.

---

## 11. Why This Matters to CISOs, Security Architects, and Engineering Leaders

Security and engineering leaders do not need another vague promise of “safe AI.”

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

The core requirement is clear: teams may already have PR review, CI checks, and deployment controls, but still need the guarantee that a change approved earlier is only executable if it is still legitimate at execution time.

---

## 12. Safe Entry Path: Shadow Mode

DETERMA can enter enterprise conversations safely because the first step does not require taking control of production execution.

The recommended entry path is:

## Shadow Mode

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

The goal is not to replace existing systems.

The goal is to show where an action that appears approved, safe, or compliant may no longer be authorized at execution time.

---

## 13. Initial Use Cases

### 13.1 AI-Generated Code Changes

An agent proposes a code change.  
A PR advances.  
A review is completed.  
CI passes.  
Before merge, branch, diff, dependency, reviewer context, or policy changes.

DETERMA asks:

**Is this merge still authorized now?**

### 13.2 Agent Tool / API Invocation

An agent is about to invoke an API, connector, MCP server, package, skill, or external tool.

DETERMA asks:

**Is this invocation still authorized for this agent, task, data, policy, and context?**

### 13.3 Digital Worker Using Company Knowledge

A digital worker uses enterprise knowledge to act inside a CRM, finance system, support workflow, legal process, or customer operation.

DETERMA asks:

**Is this digital worker authorized to use this knowledge for this action, against this target, now?**

### 13.4 Multi-Agent Delegation

One agent plans.  
Another reviews.  
Another executes.  
Another opens a PR, ticket, workflow, or transaction.  
A human approves part of the chain.

DETERMA asks:

**Does the delegation chain still authorize the final action?**

### 13.5 Human Approval That Becomes Stale

A human approves a task.  
Between approval and execution, the action changes.

DETERMA asks:

**Does the original approval still cover the actual action?**

---

## 14. What Makes DETERMA Different

### DETERMA is not just protecting execution.

It connects execution to context, memory, evidence, and authority.

### DETERMA is not just organizing knowledge.

It determines whether knowledge may be used for a specific action.

### DETERMA is not just managing agents.

It governs digital work.

### DETERMA is not just producing audit.

It validates before execution and records the decision.

### DETERMA is not just a guardrail inside the model.

It is external to the agent and the model.

### DETERMA is not just a tool.

It is an authority layer for a new category of enterprise work.

---

## 15. The Category Definition

DETERMA’s initial category:

## Runtime Execution Authority

A deterministic, external, evidence-based layer that validates whether an AI-initiated or automation-driven action is still authorized at execution time.

DETERMA’s broader category:

## Authority Operating Layer for Digital Work

An enterprise infrastructure layer that governs the authority, context, memory, evidence, legitimacy, and accountability of digital work performed by AI Agents, Automations, Coding Assistants, and Digital Workers.

It answers:

## Is this digital work still authorized, grounded, traceable, and aligned with the organization?

---

## 16. What We Want to Learn in Strategic Conversations

The purpose of upcoming conversations is not to debate whether the problem exists.

The problem emerges wherever AI is connected to tools, data, workflows, memory, and execution.

The goal is to sharpen:

- the first workflow where pain is measurable;
- the right buyer;
- the output that proves value;
- the metadata available without operational risk;
- the safest Shadow Mode path;
- the right language for Security, Engineering, Platform, and Leadership;
- the right partner architecture;
- the boundary between agent execution, agent interaction, enterprise knowledge, and runtime authority.

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

---

## A2. NanoCo vs DETERMA

NanoCo is important because it reflects where the market is going: agents will live inside enterprise workflows, interact through Slack or Teams, run inside controlled environments, use memory, and perform work beyond simple replies. NanoCo emphasizes organization-ready agents, secure execution, sandboxing, zero credentials, approval, audit, and infrastructure control.

That makes NanoCo a strong Category Validator.

But NanoCo’s center of gravity is execution environment.

DETERMA’s center of gravity is authority.

| Question | NanoCo | DETERMA |
|---|---|---|
| How does the agent run? | Core focus | Not the core product layer |
| Is the agent isolated? | Core focus | Input signal only |
| Are credentials protected? | Core focus | Input signal only |
| Was there approval? | Important | Evidence, not final authority |
| Is the action still authorized now? | Not the primary category claim | Core question |
| Does the task remain within authority scope? | Adjacent | Core evaluation |
| Is the digital work grounded in permitted context? | Adjacent | Core authority concern |
| Should execution proceed, stop, or escalate? | Adjacent | Core output |

### DETERMA’s Unique Position Against NanoCo

```text
NanoCo secures agent execution.
DETERMA validates digital work authority.
```

A safe agent can still perform unauthorized work.

---

## A3. Band vs DETERMA

Band is closer to DETERMA’s narrative territory than NanoCo.

Band frames the problem around distributed AI agents, interaction infrastructure, Agentic Mesh, Interaction Control Plane, delegation, discovery, governance, authority boundaries, runtime visibility, approval, and audit.

This makes Band both a strong Category Validator and a narrative competitor.

Band governs how agents interact.

DETERMA governs whether the resulting work remains authorized.

| Question | Band | DETERMA |
|---|---|---|
| How do agents discover each other? | Core focus | Not core |
| How do agents communicate? | Core focus | Not core |
| How is delegation routed? | Core focus | Evaluates whether delegation remains authorized |
| Is there visibility into agent interactions? | Core focus | Uses visibility as evidence |
| Can humans inspect, approve, or override? | Core focus | Uses approval as evidence, then recomputes authority |
| Are authority boundaries present in the interaction layer? | Core focus | Determines action-level execution authority |
| Can a governed chain still lead to unauthorized execution? | Not the primary category claim | Core failure mode |
| Should final execution proceed? | Adjacent | Core output |

### DETERMA’s Unique Position Against Band

```text
Band governs agent interaction.
DETERMA validates execution authority.
```

A governed delegation chain can still lead to unauthorized execution.

---

## A4. Glean / Writer / Enterprise Knowledge Platforms vs DETERMA

Glean and Writer represent the enterprise knowledge and Work AI layer.

Glean’s public product map includes enterprise search, connectors, actions, APIs, MCP Gateway, agents, agent orchestration, agent governance, enterprise graph, personal graph, and system of context.

Writer positions itself as an enterprise AI platform for agentic work, with Writer Agent, Playbooks, AI Studio, Connectors, Palmyra LLMs, and Knowledge Graph.

These platforms help AI know and produce more.

DETERMA governs what the AI is allowed to do with what it knows.

| Question | Enterprise Knowledge Platforms | DETERMA |
|---|---|---|
| What does the organization know? | Core focus | Uses as authority context |
| Can AI retrieve enterprise knowledge? | Core focus | Evaluates permitted use |
| Can AI produce grounded work? | Core focus | Evaluates whether the work is authorized |
| Can teams build agents on top of enterprise knowledge? | Core focus | Validates action authority |
| Is knowledge scoped to role, action, target, and policy? | Adjacent | Core concern |
| Can knowledge be used for this action now? | Not always the primary decision | Core question |

### DETERMA’s Unique Position Against Knowledge Platforms

```text
They organize enterprise knowledge.
DETERMA governs authorized use of enterprise knowledge.
```

Knowledge is not authority.

---

## A5. MCP / Tool Connectivity vs DETERMA

MCP is a major enabling layer. It standardizes how AI applications connect to external systems, including data sources, tools, and workflows.

That makes agents more useful.

It also makes authority harder.

Every tool connection creates a new action surface.

| Question | MCP / Connectivity | DETERMA |
|---|---|---|
| How does the AI connect to external systems? | Core focus | Uses connection as action surface |
| Can the AI access tools and data? | Core focus | Evaluates whether access should be used |
| Can the AI perform tasks through connected systems? | Core focus | Validates whether the task is authorized |
| Is invocation allowed under current authority? | Not the core protocol function | Core decision |
| Should this connector call proceed now? | Not core | Core output |

### DETERMA’s Unique Position Against MCP

```text
MCP connects agents to tools and data.
DETERMA validates whether using those tools and data is still authorized.
```

Connectivity expands capability.  
DETERMA governs authority.

---

## A6. Agent SDKs / Orchestration Frameworks vs DETERMA

Agent SDKs and orchestration frameworks make it easier to build agents, run them, connect tools, manage state, define guardrails, evaluate workflows, and integrate observability.

That is essential infrastructure.

But orchestration is not authority.

| Question | Agent SDKs / Orchestration | DETERMA |
|---|---|---|
| How is the agent built? | Core focus | Not core |
| How are tools wired? | Core focus | Evaluates invocation authority |
| How is state handled? | Core focus | Evaluates authority-relevant context |
| Are guardrails present? | Core focus | External authority layer beyond agent-loop guardrails |
| Can workflows run? | Core focus | Determines whether they should still run |
| Is the final action still authorized? | Adjacent | Core question |

### DETERMA’s Unique Position Against Agent Frameworks

```text
Agent frameworks make digital work possible.
DETERMA makes digital work governable.
```

---

## A7. The Deep Difference: Safety, Governance, Knowledge, and Authority

The market often collapses four different ideas into one category.

DETERMA separates them.

| Concept | Question It Answers | Why It Is Not Enough |
|---|---|---|
| Safety | Is this system less likely to behave dangerously? | Safe behavior does not equal authorized action |
| Governance | Are there rules, workflows, visibility, and oversight? | Governed workflows can still lead to unauthorized execution |
| Knowledge | What does the organization know? | Knowledge does not define permitted use |
| Authority | Is this specific action still allowed now? | This is the missing layer DETERMA owns |

DETERMA’s position:

```text
Safety reduces risk.
Governance structures behavior.
Knowledge grounds reasoning.
Authority determines whether action may proceed.
```

---

## A8. DETERMA’s Core Differentiators

### 1. Action-Level Authority

DETERMA focuses on the specific action, not only the user, agent, workflow, policy, or system.

### 2. Runtime Revalidation

DETERMA treats authority as a live property that must be recomputed when context changes.

### 3. Externality

DETERMA is external to the model and the agent. The model can reason, but the authority layer must decide deterministically.

### 4. Evidence-Based Receipts

DETERMA produces evidence-backed decision receipts, not just logs.

### 5. Knowledge-to-Authority Link

DETERMA connects enterprise knowledge, memory, policy, and evidence to runtime authority.

### 6. Digital Worker Accountability

DETERMA gives digital workers a governable operating boundary: role, scope, context, permitted action, escalation, evidence, and auditability.

### 7. Shadow Mode Entry

DETERMA can begin as a non-invasive evaluation layer: no production access, no write access, no secrets, metadata-first.

### 8. Category Precision

DETERMA does not compete as another agent platform. It defines the authority layer above agent platforms.

---

## A9. Final Competitive Positioning

```text
NanoCo secures agent execution.
Band governs agent interaction.
Glean and Writer organize enterprise knowledge.
MCP connects agents to tools and data.
Agent SDKs orchestrate agent work.
DETERMA governs the authority, memory, evidence, and legitimacy of digital work.
```

DETERMA’s unique category is not “AI security” in general.

It is:

## Runtime Execution Authority

And the broader company vision is:

## Authority Operating Layer for Digital Work

The market is moving toward agents that can act.

DETERMA is built for the moment when the enterprise must decide whether that action is still authorized.
