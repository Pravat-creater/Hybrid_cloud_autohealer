# Hybrid-Cloud Infrastructure Health & Security Auditor

## Project Overview

This project simulates a real-world 24/7 production environment deployed across two cloud platforms:
- Amazon Web Services (AWS EC2)
- Microsoft Azure (Azure Virtual Machine)

The solution focuses on Infrastructure Administration, Automated Incident Management, and Security Compliance Monitoring in a hybrid-cloud setup.

The system continuously monitors critical services and performs automated corrective actions based on predefined Standard Operating Procedures (SOPs).

---

## Business Problem

In production environments, unexpected service failures or misconfigured security settings can result in:

- Business downtime
- Financial loss
- Security vulnerabilities
- SLA breaches

Manual monitoring is not scalable for 24/7 operations. Hence, automation is required.

---

## Solution Architecture

### 1️⃣ Infrastructure Layer
- AWS EC2: Windows Server with SQL Database
- Azure VM: Windows Server with IIS Web Server
- Secure network configuration using Security Groups / NSG rules

### 2️⃣ Auto-Healer Engine
A Python-based monitoring script that:
- Checks SQL service health
- Detects service failure
- Automatically restarts the service
- Logs the activity

This reduces MTTR (Mean Time To Repair).

### 3️⃣ Security Compliance Auditor
A custom port monitoring module that:
- Scans critical ports (22, 3389, etc.)
- Identifies unintended public exposure
- Triggers alert notifications

Ensures adherence to enterprise security standards.

---

## Key Features

- Hybrid-Cloud Administration (AWS + Azure)
- Automated Incident Response
- SOP-Based Self-Healing Mechanism
- Security Audit Automation
- 24/7 Scheduled Monitoring via Task Scheduler
- Operational Runbook Documentation

---

## Technologies Used

- Python
- Windows Server
- AWS EC2
- Azure Virtual Machines
- SQL Server
- IIS Web Server
- Git & GitHub

---

## Business Impact

- Reduced manual monitoring effort
- Improved service availability
- Strengthened infrastructure security posture