# Sensio IoT Deployment Guide

This directory contains container deployment definitions for the **Sensio IoT** platform across Linux servers, workstations, and NVIDIA Jetson edge systems.

---

## Prerequisites

1. **Docker Engine & Docker Compose v2**: Ensure Docker is installed and running (`docker compose version`).
2. **PostgreSQL Database (15+)**: A reachable PostgreSQL instance (local container, host service, or cloud database).
3. **Encryption Key**: A 32-byte binary key used to encrypt device credentials:
   ```bash
   mkdir -p .secrets
   openssl rand 32 > .secrets/device_token_encryption_key
   chmod 600 .secrets/device_token_encryption_key
   ```

---

## 1. Standard Linux Server / AMD64 Deployment

1. Copy the configuration template:
   ```bash
   cp .env.example .env
   chmod 600 .env
   ```
2. Edit `.env` to configure your `DATABASE_URL`.
3. Start the service:
   ```bash
   docker compose -f docker-compose.yml up -d
   ```
4. Verify health:
   ```bash
   curl http://127.0.0.1:3000/health
   ```
   Open your browser at `http://localhost:3000` to access the Sensio dashboard.

---

## 2. NVIDIA Jetson ARM64 Edge Deployment

On NVIDIA Jetson (Nano, Xavier, Orin) with Ubuntu and hardware USB coordinator:

```bash
docker compose -f docker-compose.jetson.yml up -d
```

See [docs/iot/install-jetson.md](../../docs/iot/install-jetson.md) for full hardware passthrough, Zigbee2MQTT, and Tailscale setup.
