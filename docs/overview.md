# Sensio Ecosystem Overview

**Sensio** is an integrated software ecosystem designed to provide privacy-first, edge-capable spatial intelligence, smart environment automation, and personal knowledge management.

---

## 1. Product Suite

The Sensio ecosystem is composed of specialized product suites:

### 🟢 Sensio IoT
A high-performance smart environment platform built in Rust and Axum:
- **Local Edge Hub**: Manages Zigbee, MQTT, Tuya Cloud, infrared remotes, and ThingsBoard IoT devices.
- **Embedded AI Assistant**: Grounded local voice and natural language reasoning with OpenAI and Claude multi-provider integration.
- **Headless Tool Suite & MCP**: Complete CLI (`sensio`) and Model Context Protocol server for AI pair programming and automated management.
- **Companion Clients**: Responsive web SPA and native Android mobile application.

### 🟡 Sensio Notes (In Development)
A private, AI-augmented knowledge and collaborative note-taking workspace:
- Encrypted local and self-hosted cloud synchronization.
- Markdown-first workspace with embedded spatial and telemetry links to Sensio IoT devices.
- AI assistant integration for automated summarization, meeting notes, and action item scheduling.

---

## 2. Architecture & Design Principles

```text
┌─────────────────────────────────────────────────────────────────┐
│                       Sensio Client Tier                        │
│   Web SPA  •  Android App  •  Headless CLI  •  AI MCP Server    │
└───────────────────────────────┬─────────────────────────────────┘
                                │ JSON-RPC / REST / WebSocket
┌───────────────────────────────┴─────────────────────────────────┐
│                      Sensio Core Engines                        │
│        Sensio IoT (Port 3000)   •   Sensio Notes (Port 4000)    │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────┴─────────────────────────────────┐
│                       Infrastructure Tier                       │
│      PostgreSQL & TimescaleDB   •   Mosquitto MQTT Broker       │
│      Zigbee Coordinator (CC2652P) • NVIDIA Jetson Edge AI       │
└─────────────────────────────────────────────────────────────────┘
```

1. **Privacy-First & Self-Hostable**: All services are designed to run fully on-premise without mandatory cloud subscriptions.
2. **Cohesive Interfaces**: Centralized user identity, shared token semantics, and uniform API conventions across all products.
3. **Public Distribution & Private Core**: Public distributions, release assets, and deployment guides live openly in `sensio-hub`, while proprietary core codebases are maintained securely in private organization repositories.
