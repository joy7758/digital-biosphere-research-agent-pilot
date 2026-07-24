# DEB-001 Lite Simulator

This folder contains a minimal executable simulator for the first DEB-001 Lite run.

## Scope

- Implement only rule-based simulation logic.
- No web UI.
- No API service.
- No database.
- No governance infrastructure.
- No full DEB framework.

## Files

- `simulator.py`:
  - 9 agents (3 Efficiency, 3 Balance, 3 Exploration)
  - 3 environment phases (Stable, Shock, Recovery)
  - loop: observation, action selection, resource update, environment update, continuation evaluation, logging
  - outputs:
    - `agent_state_log`
    - `selection_log`
    - `phase_log`
    - `outcome_log`
    - `DEB-001-LITE-MINIMAL-RESULT-v0.1.json`

## Run the first executable validation

```bash
cd /Users/zhangbin/GitHub/digital-biosphere-research-agent-pilot
python3 prototype/deb001-lite-simulator/simulator.py \
  --run-id DEB-001-LITE-RUN-001 \
  --seed 20260725 \
  --stable-rounds 3 \
  --shock-rounds 2 \
  --recovery-rounds 2 \
  --output-dir prototype/deb001-lite-simulator/output/DEB-001-LITE-RUN-001
```

Outputs are written under the provided `--output-dir` and are intended to be the first
reproducible DEB-001 Lite event record package.
