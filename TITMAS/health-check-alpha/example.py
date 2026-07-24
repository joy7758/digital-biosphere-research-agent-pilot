import os
from datetime import datetime, timezone
from validator import AgentExecutionEvent, EvidenceAdmissionValidator
from certificate import ExecutionCertificateGenerator

def run_health_check_example():
    """
    Minimal verifiable execution certificate pipeline example
    （最小可验证执行证书管线示例）
    """
    print("--- Starting TITMAS Health Check Alpha MVP ---")

    # 1. Create a synthetic agent execution event
    event = AgentExecutionEvent(
        event_id="EVT-SYNTH-001",
        agent_id="AGENT-TEST-01",
        payload={"action": "test_ping", "result": "success"},
        timestamp=datetime.now(timezone.utc).isoformat()
    )
    print(f"Generated synthetic event with hash: {event.compute_hash()}")

    # 2. Validate the admission of the evidence
    validator = EvidenceAdmissionValidator()
    is_valid, status, note = validator.validate(event)
    print(f"Validation Result: {status} - {note}")

    # 3. Generate a verifiable execution certificate
    if is_valid:
        cert_gen = ExecutionCertificateGenerator()
        certificate = cert_gen.generate_certificate(event, is_valid, status, note)

        # 4. Produce machine-readable validation report
        output_file = "validation-report-example.json"
        cert_gen.export_report(certificate, output_file)
        print(f"Exported Machine-readable Validation Report to {output_file}")

    print("--- Health Check Alpha Example Completed ---")

if __name__ == "__main__":
    run_health_check_example()
