import hashlib
import json
from typing import Dict, Any, Tuple

class AgentExecutionEvent:
    def __init__(self, event_id: str, agent_id: str, payload: Dict[str, Any], timestamp: str):
        self.event_id = event_id
        self.agent_id = agent_id
        self.payload = payload
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "agent_id": self.agent_id,
            "payload": self.payload,
            "timestamp": self.timestamp
        }

    def compute_hash(self) -> str:
        serialized = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(serialized.encode('utf-8')).hexdigest()


class EvidenceAdmissionValidator:
    """
    Evidence Admission Validation（证据准入验证）

    Rule: Verification is not Authorization（验证不是授权）。
    此验证器仅验证数据结构和完整性，不代表该事件获得了真正的授权。
    """
    def __init__(self):
        self.required_fields = {"event_id", "agent_id", "payload", "timestamp"}

    def validate(self, event: AgentExecutionEvent) -> Tuple[bool, str, str]:
        """
        Returns:
            Tuple[bool, str, str]: (is_valid, status, reason)
        """
        event_dict = event.to_dict()

        # Check required fields
        if not self.required_fields.issubset(event_dict.keys()):
            return False, "REJECTED", "Missing required fields in the event."

        if not event_dict["event_id"] or not event_dict["agent_id"]:
            return False, "REJECTED", "event_id or agent_id cannot be empty."

        # Principle reminder (Evidence is not Truth)
        admission_note = "Observation != Evidence != Truth. This is merely syntactically valid."

        event_hash = event.compute_hash()
        return True, "ADMITTED", admission_note
