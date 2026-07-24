#!/usr/bin/env python3
"""DEB-001 Lite minimal simulator.

Produces deterministic, seed-controlled logs and a minimal result object for one run.

Scope:
- no web UI
- no API
- no database
- no governance infrastructure
- no full DEB framework
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple


PHASE_ORDER = ["Stable", "Shock", "Recovery"]


@dataclass
class AgentState:
    agent_id: str
    strategy: str
    resource: float
    active: bool = True
    last_action: str = ""
    lineage_id: str = ""
    continuation_events: int = 0
    dropout_round: int | None = None
    dropout_reason: str = ""
    adaptation_events: int = 0
    adaptation_level: float = 0.0


def create_agents() -> List[AgentState]:
    """Create nine agents: 3 per strategy."""
    agents: List[AgentState] = []
    index = 1
    for strategy in ("Efficiency", "Balance", "Exploration"):
        for i in range(3):
            agents.append(
                AgentState(
                    agent_id=f"{strategy[:4].upper()}{i + 1}",
                    strategy=strategy,
                    resource=24.0,
                    lineage_id=f"{strategy[:1]}-lineage-{i + 1}",
                )
            )
            index += 1
    return agents


def strategy_action(agent: AgentState, phase: str, round_in_phase: int) -> str:
    """Rule-based action selection for one agent."""
    if agent.strategy == "Efficiency":
        if phase == "Shock":
            if agent.resource < 10.0:
                return "adapt"
            if round_in_phase % 4 == 0:
                return "adapt"
            return "exploit"
        if phase == "Recovery":
            return "exploit"
        return "exploit"

    if agent.strategy == "Balance":
        if phase == "Shock":
            return "explore" if round_in_phase % 2 == 0 else "exploit"
        if phase == "Recovery":
            return "explore" if round_in_phase % 3 == 0 else "exploit"
        return "explore" if round_in_phase % 4 == 0 else "exploit"

    # Exploration
    if phase == "Stable":
        return "explore" if round_in_phase % 2 == 0 else "exploit"
    if phase == "Shock":
        return "explore" if round_in_phase % 2 == 0 else "adapt"
    return "explore"


def action_profile(strategy: str, action: str) -> Tuple[float, float]:
    """Return (reward, cost)."""
    if strategy == "Efficiency":
        if action == "exploit":
            return 6.0, 3.0
        return 3.0, 1.5

    if strategy == "Balance":
        if action == "explore":
            return 3.2, 1.8
        return 4.0, 2.2

    # Exploration strategy
    if action == "explore":
        return 3.8, 2.2
    if action == "adapt":
        return 2.8, 1.5
    return 2.4, 2.0


def evaluation_step(agent: AgentState, phase: str, action: str) -> Tuple[float, str, bool]:
    """Apply resource dynamics and determine continuation state."""
    reward, cost = action_profile(agent.strategy, action)

    # Global phase multipliers define environment influence.
    if phase == "Shock":
        reward *= 0.6
    elif phase == "Recovery":
        reward *= 1.1

    # Penalty for mismatch under shock.
    penalty = 0.0
    mismatch = False
    mismatch_reason = ""
    if phase == "Shock":
        if agent.strategy == "Efficiency" and action == "exploit":
            penalty = 2.4
            mismatch = True
            mismatch_reason = "Efficiency strategy did not adapt in shock"
        if agent.strategy == "Balance" and action == "exploit" and agent.resource < 7.0:
            penalty = 1.2
            mismatch = True
            mismatch_reason = "Balance exploit under low resource in shock"

    # Adaptation support for future rounds.
    adaptation_delta = 0.8 if action in {"adapt", "explore"} else 0.0
    if action == "adapt":
        agent.adaptation_events += 1

    delta = reward - cost - penalty
    agent.resource += delta
    agent.adaptation_level = min(1.0, agent.adaptation_level + adaptation_delta)
    agent.last_action = action

    reason = ""
    if agent.resource <= 0:
        agent.active = False
        reason = "resource exhausted"
    elif phase == "Shock" and action == "exploit" and mismatch and agent.resource < 4:
        agent.active = False
        reason = mismatch_reason

    if not agent.active and not reason:
        reason = "continuation threshold"

    if not agent.active and agent.dropout_round is None:
        agent.dropout_round = agent.continuation_events
        agent.dropout_reason = reason

    agent.continuation_events += 1

    continuation_score = max(0.0, agent.resource / 24.0)
    return delta, reason, mismatch


def run_simulation(
    stable_rounds: int,
    shock_rounds: int,
    recovery_rounds: int,
    seed: int,
    run_id: str,
    output_dir: Path,
) -> Dict:
    agents = create_agents()
    phases = [
        ("Stable", stable_rounds),
        ("Shock", shock_rounds),
        ("Recovery", recovery_rounds),
    ]

    timestamp = datetime.now(timezone.utc).isoformat()

    output_dir.mkdir(parents=True, exist_ok=True)

    agent_state_log_path = output_dir / "agent_state_log.csv"
    selection_log_path = output_dir / "selection_log.csv"
    phase_log_path = output_dir / "phase_log.csv"
    outcome_log_path = output_dir / "outcome_log.csv"

    total_round = 0
    phase_bounds: Dict[str, Dict] = {}

    agent_rows: List[Dict] = []
    selection_rows: List[Dict] = []
    phase_rows: List[Dict] = []
    outcome_rows: List[Dict] = []

    dropouts: List[Dict] = []
    continuation_changes: List[Dict] = []
    behavior_changes: List[Dict] = []

    for phase, max_round in phases:
        start_round = total_round
        previous_active = sum(1 for a in agents if a.active)
        previous_active_by_strategy = {
            strategy: sum(1 for a in agents if a.strategy == strategy and a.active)
            for strategy in ("Efficiency", "Balance", "Exploration")
        }

        for round_in_phase in range(max_round):
            for agent in agents:
                if not agent.active:
                    continue

                action = strategy_action(agent, phase, round_in_phase)
                prev_resource = agent.resource
                prev_active = agent.active
                prev_action = agent.last_action

                resource_delta, dropout_reason, mismatch = evaluation_step(
                    agent, phase, action
                )

                # state log
                agent_rows.append(
                    {
                        "run_id": run_id,
                        "phase": phase,
                        "round": total_round,
                        "round_in_phase": round_in_phase,
                        "agent_id": agent.agent_id,
                        "lineage_id": agent.lineage_id,
                        "strategy_type": agent.strategy,
                        "action_id": action,
                        "resource_before": round(prev_resource, 4),
                        "resource_delta": round(resource_delta, 4),
                        "resource_after": round(agent.resource, 4),
                        "active": agent.active,
                        "adaptation_level": round(agent.adaptation_level, 4),
                    }
                )

                selection_rows.append(
                    {
                        "run_id": run_id,
                        "round": total_round,
                        "agent_id": agent.agent_id,
                        "strategy_type": agent.strategy,
                        "continuation_state": "ACTIVE" if agent.active else "DROPPED",
                        "continuation_reason": dropout_reason if not agent.active else "",
                        "phase": phase,
                        "mismatch": mismatch,
                    }
                )

                if prev_active and not agent.active:
                    dropouts.append(
                        {
                            "round": total_round,
                            "agent_id": agent.agent_id,
                            "strategy_type": agent.strategy,
                            "phase": phase,
                            "reason": dropout_reason,
                        }
                    )

                if prev_active and prev_action and action != prev_action:
                    behavior_changes.append(
                        {
                            "round": total_round,
                            "agent_id": agent.agent_id,
                            "strategy_type": agent.strategy,
                            "action_prev_round": prev_action,
                            "action_current": action,
                        }
                    )

                if prev_active and not agent.active:
                    outcome_rows.append(
                        {
                            "run_id": run_id,
                            "phase": phase,
                            "round": total_round,
                            "agent_id": agent.agent_id,
                            "strategy_type": agent.strategy,
                            "event": "dropout",
                            "resource": round(agent.resource, 4),
                            "reason": dropout_reason,
                        }
                    )

            phase_rows.append(
                {
                    "run_id": run_id,
                    "event": "round_complete",
                    "phase": phase,
                    "round": total_round,
                    "active_agents": sum(1 for a in agents if a.active),
                    "total_agents": len(agents),
                }
            )

            total_round += 1

        phase_rows.append(
            {
                "run_id": run_id,
                "event": "phase_boundary",
                "phase": phase,
                "phase_start": start_round,
                "phase_end": total_round,
                "active_agents": sum(1 for a in agents if a.active),
            }
        )

        active_now = sum(1 for a in agents if a.active)
        phase_bounds[phase] = {
            "start_round": start_round,
            "end_round": total_round,
            "active_agents": active_now,
            "active_delta": active_now - previous_active,
            "dropouts": [d for d in dropouts if d["round"] >= start_round and d["round"] < total_round],
            "active_by_strategy_start": previous_active_by_strategy,
            "active_by_strategy_end": {
                strategy: sum(
                    1 for a in agents if a.strategy == strategy and a.active
                )
                for strategy in ("Efficiency", "Balance", "Exploration")
            },
        }
        for strategy in ("Efficiency", "Balance", "Exploration"):
            strat_agents = [a for a in agents if a.strategy == strategy]
            active_count = sum(1 for a in strat_agents if a.active)
            continuation_changes.append(
                {
                    "phase": phase,
                    "strategy_type": strategy,
                    "active_start": previous_active_by_strategy[strategy],
                    "active_end": active_count,
                    "continuation_change": (
                        active_count - previous_active_by_strategy[strategy]
                    ),
                    "avg_resource": round(
                        sum(a.resource for a in strat_agents) / len(strat_agents),
                        4,
                    ),
                    "avg_adaptation": round(
                        sum(a.adaptation_level for a in strat_agents) / len(strat_agents),
                        4,
                    ),
                }
            )

    for agent in agents:
        if not agent.active and agent.dropout_round is None:
            agent.dropout_round = total_round

    population_outcome: Dict[str, Dict] = {}
    for strategy in ("Efficiency", "Balance", "Exploration"):
        strat_agents = [a for a in agents if a.strategy == strategy]
        active_count = sum(1 for a in strat_agents if a.active)
        population_outcome[strategy] = {
            "active_agents": active_count,
            "continuation_rate": round(active_count / len(strat_agents), 4),
            "resource_summary": {
                "min": round(min(a.resource for a in strat_agents), 4),
                "max": round(max(a.resource for a in strat_agents), 4),
                "avg": round(sum(a.resource for a in strat_agents) / len(strat_agents), 4),
            },
            "adaptation_events": sum(a.adaptation_events for a in strat_agents),
            "dropout_events": [
                d for d in dropouts if d["strategy_type"] == strategy
            ],
        }

    phase_outcome: Dict[str, Dict] = {}
    for phase in PHASE_ORDER:
        info = phase_bounds[phase]
        phase_strat = [
            {
                "strategy_type": strategy,
                "active_agents": sum(
                    1 for a in agents if a.strategy == strategy and a.active
                ),
                "avg_resource": round(
                    sum(a.resource for a in agents if a.strategy == strategy) / 3,
                    4,
                ),
            }
            for strategy in ("Efficiency", "Balance", "Exploration")
        ]
        phase_outcome[phase] = {
            "start_round": info["start_round"],
            "end_round": info["end_round"],
            "active_agents": info["active_agents"],
            "active_delta": info["active_delta"],
            "strategies": phase_strat,
        }

    minimal_result = {
        "run_id": run_id,
        "experiment_id": "DEB-001-LITE",
        "version": "v0.1",
        "seed": seed,
        "timestamp": timestamp,
        "population_outcome": population_outcome,
        "phase_outcome": phase_outcome,
        "selection_observation": {
            "continuation_changes": continuation_changes,
            "dropout_events": dropouts,
            "strategy_behavior_changes": behavior_changes,
        },
        "evidence_references": {
            "agent_state_log": str(agent_state_log_path),
            "selection_log": str(selection_log_path),
            "phase_log": str(phase_log_path),
            "outcome_log": str(outcome_log_path),
        },
        "notes": {
            "scope": "DEB-001 Lite minimal dry-run compatible",
            "reproducible": True,
            "seed_used": seed,
            "total_rounds": total_round,
            "active_agents_end": sum(1 for a in agents if a.active),
            "observation_confidence": "minimal",
        },
    }

    with agent_state_log_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run_id",
                "phase",
                "round",
                "round_in_phase",
                "agent_id",
                "lineage_id",
                "strategy_type",
                "action_id",
                "resource_before",
                "resource_delta",
                "resource_after",
                "active",
                "adaptation_level",
            ],
        )
        writer.writeheader()
        writer.writerows(agent_rows)

    with selection_log_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run_id",
                "round",
                "agent_id",
                "strategy_type",
                "continuation_state",
                "continuation_reason",
                "phase",
                "mismatch",
            ],
        )
        writer.writeheader()
        writer.writerows(selection_rows)

    with phase_log_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["run_id", "event", "phase", "round", "active_agents", "total_agents", "phase_start", "phase_end"],
        )
        writer.writeheader()
        for row in phase_rows:
            row.setdefault("phase_start", "")
            row.setdefault("phase_end", "")
            writer.writerow(row)

    with outcome_log_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run_id",
                "phase",
                "round",
                "agent_id",
                "strategy_type",
                "event",
                "resource",
                "reason",
            ],
        )
        writer.writeheader()
        writer.writerows(outcome_rows)

    result_path = output_dir / "DEB-001-LITE-MINIMAL-RESULT-v0.1.json"
    with result_path.open("w") as f:
        json.dump(minimal_result, f, indent=2)
        f.write("\n")

    return minimal_result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the first minimal DEB-001 Lite digital ecology simulation."
    )
    parser.add_argument("--run-id", default="DEB-001-LITE-RUN-001")
    parser.add_argument("--seed", type=int, default=20260725)
    parser.add_argument("--stable-rounds", type=int, default=3)
    parser.add_argument("--shock-rounds", type=int, default=2)
    parser.add_argument("--recovery-rounds", type=int, default=3)
    parser.add_argument("--output-dir", type=Path, default=Path("prototype/deb001-lite-simulator/output"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_simulation(
        stable_rounds=args.stable_rounds,
        shock_rounds=args.shock_rounds,
        recovery_rounds=args.recovery_rounds,
        seed=args.seed,
        run_id=args.run_id,
        output_dir=args.output_dir,
    )

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
