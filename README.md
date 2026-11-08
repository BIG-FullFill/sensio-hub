<div align="center">

# 🌐 Sensio Hub
### The Public Distribution Hub, Documentation Portal & Deployment Center for the Sensio Ecosystem

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Docker Image](https://img.shields.io/badge/docker-ghcr.io%2Fbig--fullfill%2Fsensio--iot--new-blue?logo=docker)](https://github.com/BIG-FullFill/Sensio-IoT-New/pkgs/container/sensio-iot-new)
[![GitHub Releases](https://img.shields.io/badge/release-latest-green?logo=github)](https://github.com/BIG-FullFill/Sensio-IoT-New/releases)
[![Platform](https://img.shields.io/badge/platform-Linux%20AMD64%20%7C%20ARM64%20Jetson%20%7C%20Android-orange)](docs/overview.md)

</div>

---

## 📖 Welcome to Sensio Hub

**Sensio Hub** is the central public storefront and distribution portal for the **Sensio Software Ecosystem**. It hosts official deployment templates, download links for binary tools and mobile applications, integration guides, and system documentation.

Core application source code is maintained securely in private enterprise repositories, while **Sensio Hub** provides everything required for administrators, developers, and users to deploy, integrate, and operate Sensio software.

---

## 📦 Products in the Sensio Suite

```text
                                  ┌────────────────────────┐
                                  │      Sensio Hub        │
                                  │  (Public Distribution) │
                                  └───────────┬────────────┘
                                              │
                     ┌────────────────────────┴────────────────────────┐
                     │                                                 │
        ┌────────────▼───────────┐                        ┌────────────▼───────────┐
        │       Sensio IoT       │                        │      Sensio Notes      │
        │   Edge Smart Spaces    │                        │   Private Knowledge    │
        │  & Industrial Control  │                        │  & Workspace Sync      │
        └────────────────────────┘                        └────────────────────────┘
```

| Product | Focus Area | Status | Public Distributions | Documentation |
|---|---|---|---|---|
| **Sensio IoT** | Smart Spaces, Zigbee/MQTT, Jetson Edge AI, HMI & Mobile | 🟢 **Production** | [Docker Compose](deploy/iot/) • [Android APK](docs/iot/install-android.md) • [CLI](scripts/install-sensio-cli.sh) | [Sensio IoT Docs](docs/iot/getting-started.md) |
| **Sensio Notes** | Private, AI-Augmented Markdown Knowledge Base & Sync | 🟡 **In Development** | [Docker Compose Preview](deploy/notes/) | [Sensio Notes Docs](docs/notes/getting-started.md) |

---

## 🚀 Quick Start: Deploy Sensio IoT

Deploy Sensio IoT on any Linux server with Docker Compose in seconds:

```bash
# 1. Clone this distribution hub
git clone https://github.com/BIG-FullFill/sensio-hub.git
cd sensio-hub/deploy/iot

# 2. Initialize secrets and configuration
mkdir -p .secrets
openssl rand 32 > .secrets/device_token_encryption_key
chmod 600 .secrets/device_token_encryption_key

cp .env.example .env
chmod 600 .env

# 3. Start the service
docker compose up -d
```

Open your browser at `http://localhost:3000` to launch the onboarding flow.

---

## ⚡ Install Headless CLI & MCP Tool Suite

Sensio IoT includes a high-performance command-line interface (`sensio`) and Model Context Protocol (MCP) server for AI assistants (Claude Desktop, Cursor, Antigravity):

```bash
# Automated installer for Linux (x86_64 and aarch64)
curl -fsSL https://raw.githubusercontent.com/BIG-FullFill/sensio-hub/main/scripts/install-sensio-cli.sh | bash
```

Verify the installation:
```bash
sensio --help
sensio auth login
```

Connect with AI hosts via MCP:
```bash
# Test MCP stdio server
sensio mcp
```
See the [Model Context Protocol Setup Guide](docs/iot/mcp-setup.md) for Claude Desktop and Cursor integration.

---

## 📱 Sensio IoT Android App

Download the signed companion APK directly from GitHub Releases:
- **[Download Latest Android APK](https://github.com/BIG-FullFill/Sensio-IoT-New/releases)**
- Setup Guide: [Android Installation Walkthrough](docs/iot/install-android.md)

---

## 🔒 Source Code Navigation Matrix

Proprietary core engines, firmware bridges, and web application source code are maintained in private organization repositories for authorized enterprise contributors:

| Product Tier | Scope | Repository URL | Access Policy |
|---|---|---|---|
| **Sensio IoT Core** | Backend, Web SPA, Jetson Engine, Android Shell | [BIG-FullFill/Sensio-IoT-New](https://github.com/BIG-FullFill/Sensio-IoT-New) | 🔒 **Private** *(Authorized Organization Team Only)* |
| **Sensio Notes Core** | Encrypted Sync Engine & Note Workspace | [BIG-FullFill/Sensio-Notes](https://github.com/BIG-FullFill) | 🔒 **Private** *(In Development)* |

> [!NOTE]
> Links marked with 🔒 point to private repositories. Unauthenticated visitors or accounts without granted organization permissions will receive a standard GitHub `404 Not Found`.

---

## 📚 Documentation Index

- **Sensio Overview**: [Architecture & Philosophy](docs/overview.md)
- **Sensio IoT Guides**:
  - [5-Minute Quickstart](docs/iot/getting-started.md)
  - [Docker Server Deployment (AMD64)](docs/iot/install-docker.md)
  - [NVIDIA Jetson Edge Deployment (ARM64)](docs/iot/install-jetson.md)
  - [Android Mobile App Setup](docs/iot/install-android.md)
  - [Headless CLI Reference](docs/iot/cli-reference.md)
  - [Model Context Protocol (MCP) Guide](docs/iot/mcp-setup.md)
- **Sensio Notes Guides**:
  - [Product Vision & Sync](docs/notes/getting-started.md)
  - [Self-Hosted Server Deployment](docs/notes/install-server.md)

---

## 📄 License

Deployment templates, scripts, and documentation in this repository are licensed under the [Apache License 2.0](LICENSE).
