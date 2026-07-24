import pytest
import json
from validator import AgentExecutionEvent, EvidenceAdmissionValidator
from certificate import ExecutionCertificateGenerator

def test_event_hashing():
    event = AgentExecutionEvent("EVT-1", "AGENT-1", {"data": "test"}, "2026-07-25T00:00:00Z")
    assert event.compute_hash() is not None

def test_validator_admission_success():
    event = AgentExecutionEvent("EVT-1", "AGENT-1", {"data": "test"}, "2026-07-25T00:00:00Z")
    validator = EvidenceAdmissionValidator()
    is_valid, status, note = validator.validate(event)

    assert is_valid is True
    assert status == "ADMITTED"
    assert "Evidence != Truth" in note

def test_validator_admission_failure_empty_ids():
    event = AgentExecutionEvent("", "AGENT-1", {"data": "test"}, "2026-07-25T00:00:00Z")
    validator = EvidenceAdmissionValidator()
    is_valid, status, note = validator.validate(event)

    assert is_valid is False
    assert status == "REJECTED"

def test_certificate_generation():
    event = AgentExecutionEvent("EVT-1", "AGENT-1", {"data": "test"}, "2026-07-25T00:00:00Z")
    cert_gen = ExecutionCertificateGenerator()
    certificate = cert_gen.generate_certificate(event, True, "ADMITTED", "Test Note")

    assert certificate["certificate_id"].startswith("CERT-")
    assert certificate["validation_status"] == "ADMITTED"

    # Check disclaimers exist
    disclaimers_str = json.dumps(certificate["disclaimers"])
    assert "Evidence is not Truth" in disclaimers_str
    assert "Verification is not Authorization" in disclaimers_str
    assert "No security certification claims" in disclaimers_str
