import json
import uuid
from datetime import datetime, timezone
from typing import Dict, Any
from validator import AgentExecutionEvent

class ExecutionCertificateGenerator:
    """
    Verifiable Execution Certificate Generator（可验证执行证书生成器）
    """
    def generate_certificate(self, event: AgentExecutionEvent, is_valid: bool, status: str, note: str) -> Dict[str, Any]:
        """
        生成机器可读的验证报告与证书。
        """
        cert_id = str(uuid.uuid4())
        event_hash = event.compute_hash()

        certificate = {
            "certificate_id": f"CERT-{cert_id}",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "target_event_hash": event_hash,
            "validation_status": status,
            "validation_note": note,
            "disclaimers": [
                "Evidence is not Truth（证据不是事实）.",
                "Verification is not Authorization（验证不是授权）.",
                "This certificate proves execution evidence admission only（此证书仅证明执行证据准入）.",
                "No security certification claims（无安全认证声明）.",
                "No compliance certification claims（无合规认证声明）.",
                "No SAEE core implementation attached（未附加 SAEE 核心实现）."
            ]
        }
        return certificate

    def export_report(self, certificate: Dict[str, Any], filepath: str) -> None:
        """
        将证书导出为 Machine-readable Validation Report（机器可读验证报告）。
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(certificate, f, indent=4, ensure_ascii=False)
