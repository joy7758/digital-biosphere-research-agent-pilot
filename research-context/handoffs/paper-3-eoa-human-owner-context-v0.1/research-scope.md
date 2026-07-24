# Research Scope: Paper 3 EOA Human Context Handoff v0.1

## Document Status

```text
HANDOFF_STATUS=DRAFT_PENDING_HUMAN_CONTEXT_REVIEW
CONTEXT_PACKAGE_STATUS=DRAFT
REVIEW_STATUS=REVIEW_PENDING
HUMAN_RESEARCH_OWNER_REFERENCE=bin_zhang
SOURCE_DOCUMENTS_APPROVED=0
PROTOTYPE_AUTHORIZATION=NOT_AUTHORIZED
AGENT_CREATED=false
EXPERIMENT_EXECUTED=false
SCIENTIFIC_RESULT_CREATED=false
```

This document is a Human Research Owner Context Handoff（人工研究负责人上下文交接）draft. It does not approve the Research Context Package（研究上下文包）, create a Research Agent（研究智能体）, authorize a prototype, or produce a scientific conclusion.

## Pilot Research Objective

The Pilot research question is:

> Can a governed Research Agent improve reproducibility of scientific workflows?

The question is defined but unanswered. "Improve reproducibility" requires a Human-approved operational definition, comparator, protocol, and evidence set before it can be evaluated.

## Current Paper 3 Objective

Paper 3 is currently scoped to test **domain-semantic evidence closure（领域语义证据闭合）** in a bounded medical-imaging AI workflow.

The candidate operational object is `EO=(Identity, DataObject, Action, Validation, Provenance)`. It is a bounded operational abstraction, not an established universal theory. The intended research direction is to test whether explicit domain bindings identify failures that are not resolved by logs, traces, DICOM-only views, or generic evidence-presence checks under equal information-visibility constraints.

## In Scope for Context Review

- Human confirmation of the research owner and final decision responsibility.
- Human selection of formal source documents.
- Review of the bounded EOA specification and its medical-imaging profile.
- Review of candidate research questions, hypotheses, baselines, fault classes, metrics, and stopping rules.
- Separation of domain-semantic closure from generic evidence coverage.
- Identification and preservation of unknowns, limitations, conflicts, and missing evidence.
- Planning for a future preregistered benchmark, subject to separate authorization.
- Organizing a future Paper 3 outline after approved evidence records exist.

## Explicitly Out of Scope

- Creating, registering, instantiating, or operating a Research Agent.
- Executing a prototype, benchmark, experiment, validator, DBOS runtime, SAEE evaluation, or publication workflow.
- Generating, estimating, or drafting experimental results or scientific conclusions.
- A DBOS（Digital Biosphere Operating System，数字生物圈操作系统）paper.
- Validation of DBA（Digital Biosphere Architecture，数字生物圈架构）theory.
- Establishing DBO（Digital Biosphere Object，数字生物圈对象）as a canonical term, schema, entity, or runtime contract.
- Automated science, autonomous hypothesis acceptance, autonomous interpretation, or autonomous authorship.
- Clinical, external, real-device, regulatory, safety, effectiveness, deployment, or patient-outcome validation.
- Modification of original data, acquisition of new research data, or processing of patient or pixel data.
- Automatic publication, submission, authorship assignment, or external communication.

## AI-Assisted Scope

After Human approval, an AI assistant may organize approved sources, surface conflicts, preserve unknowns, draft checklists, and prepare reviewable alternatives. These are assistance outputs only. The AI may not approve sources, resolve unknowns, authorize experiments, infer facts, decide conclusions, claim authorship, or publish work.

**Human owns scientific conclusions.**

## Boundary Between Existing Artifacts and This Handoff

The EOA repository contains an existing local synthetic v0.1 artifact and report. This handoff merely lists them as source candidates. It does not rerun them, endorse their interpretations, promote them to Pilot results, or authorize the next milestone.

Paper 1 is a published UDI-DICOM mapping-profile input. Paper 2 is recorded in the formal local ledger as `accepted_for_publication / awaiting_production`; it is not treated here as a verified version of record. Neither paper proves the Paper 3 hypothesis.

## Required Human Gate

Before Context Review can advance, the assigned Human Research Owner must:

1. approve, reject, or defer each source candidate;
2. confirm or revise each pending research decision;
3. accept the `UNKNOWN` register without unsupported completion;
4. confirm the allowed AI-assistance boundary; and
5. sign a review record.

This scope document has `authorization_effect=NONE`.
