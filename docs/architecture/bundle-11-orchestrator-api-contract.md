# Bundle 11 — Orchestrator API Contract Layer

## Purpose

Expose the VOODOO orchestrator as a first-class API surface.

Before this bundle, the orchestrator existed as an internal core engine.
This bundle adds an HTTP contract for POST /orchestrator/run.

## Request Shape

- prompt: required non-empty string
- requires_privacy: boolean
- actor_id: string
- metadata: object

## Response Shape

- recommendation
- llm_provider
- workflow_state
- execution_status
- memory_record_id
- requires_human_approval
- routing_mode
- selected_steps

## Why This Matters

This turns VOODOO OS from a layered internal skeleton into a callable AI
operating system boundary.

## Next Recommended Bundle

Bundle 12 should add stable run tracing:

- run_id
- trace_id
- audit event lookup by run id
- deterministic response envelope
- GET /orchestrator/runs/{run_id}
