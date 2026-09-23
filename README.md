# Automated Cloud Threat Detection & SOAR Engine

![Integration Test Status](https://github.com/druthishetty07/automated-threat-detection-soar/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-blue.svg)

An automated Threat Detection and Security Orchestration, Automation, and Response (SOAR) tool developed in Python. This project simulates real-world Security Operations Center (SOC) workflows by monitoring system authentication logs, identifying SSH brute-force attacks in real time, and triggering automated firewall remediation rules to isolate rogue IP addresses.

---

## 🏗️ Architecture & Detection Flow

```text
  [ Attacker Activity ]
           │
           ▼
  [ System Log Stream ] (auth.log)
           │
           ▼
  [ Threat Detection Engine ] (Python Log Parser)
           │
           ▼ (Count >= Threshold)
  [ Automated Response Logic ]
           │
           ▼
  [ Firewall Rule Execution ] (IP Isolation)
