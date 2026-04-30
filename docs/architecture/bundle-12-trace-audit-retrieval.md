# Bundle 12 — Trace & Audit Retrieval Layer

## Purpose

Bundle 12 makes orchestrator executions observable and retrievable.

Bundle 11 exposed POST /orchestrator/run. Bundle 12 adds stable run
identity and retrieval:

- run_id
- trace_id
- created_at
- GET /orchestrator/runs/{run_id}

## Runtime Shape

POST /orchestrator/run

1. Generate run_id and trace_id.
2. Route the prompt through the intelligent router.
3. Execute the selected runtime path.
4. Log audit event details with run_id and trace_id.
5. Store an OrchestratorRunRecord in the service-level run store.
6. Return a compact API response.

GET /orchestrator/runs/{run_id}

Returns the full stored run detail, including:

- prompt
- actor_id
- metadata
- routing_mode
- selected_steps
- execution status
- audit_events

## Current Storage Mode

The run store is intentionally in-memory for the current core runtime
stabilization phase.

This keeps the implementation simple, testable, and safe before moving
the run store to SQLite or another persistent backend.

## Next Recommended Bundle

Bundle 13 should add a stable response envelope and error contract:

- ok
- data
- error
- request_id
- consistent 404/422/500 payload shape
