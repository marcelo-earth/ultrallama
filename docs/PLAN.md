# UltraLlama Plan

## Goal

Produce a reproducible serving benchmark that compares throughput/latency under realistic load.

## Milestones

1. Repo scaffold + baseline scripts (done)
2. vLLM server launch profile templates
3. Load generator for concurrency sweeps
4. Metrics aggregation + plotting
5. Final benchmark report with recommended config

## Key Metrics

- TTFT (time to first token)
- Tokens/sec (output throughput)
- p50/p95 latency
- Error rate under load

## Definition Of Done

- One command to run benchmark matrix
- CSV + charts generated in `artifacts/`
- Final recommendations for low/medium/high traffic setups
