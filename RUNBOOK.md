# Hybrid Cloud Auto-Healer – Operational Runbook

## Purpose

This document provides operational guidelines for monitoring, incident handling, and security validation within the Hybrid-Cloud environment.

---

## Incident Management SOP

### Scenario 1: SQL Service Down

Detection:
Auto-Healer script checks service status every 5 minutes.

Action:
- If service is stopped:
  - Script executes restart command.
  - Logs activity.
  - Generates alert notification.

Manual Escalation (If restart fails):
1. Login to AWS EC2 instance.
2. Open Services console.
3. Verify SQL dependencies.
4. Check Event Viewer logs.
5. Escalate to L2 Support if unresolved.

---

## Security Compliance SOP

### Scenario 2: Unauthorized Open Port Detected

Detection:
Security Auditor scans predefined ports.

Action:
- Alert generated if critical port is publicly accessible.

Manual Validation Steps:
1. Login to AWS Security Group / Azure NSG.
2. Verify inbound rules.
3. Remove unauthorized rule.
4. Document change in change-log.

---

## Monitoring Schedule

- Script execution: Every 5 minutes
- Security audit: Every 10 minutes
- Log review: Daily

---

## Escalation Matrix

| Level | Responsibility |
|-------|---------------|
| L1 | Auto-Healer Script |
| L2 | Cloud Administrator |
| L3 | Cloud Architect / Security Team |

---

## Logging & Documentation

- All script activities are logged locally.
- Alerts are documented for audit tracking.
- Any manual intervention must be recorded in the change log.