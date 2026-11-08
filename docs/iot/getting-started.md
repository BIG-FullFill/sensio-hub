# Getting Started with Sensio IoT

Sensio IoT can be deployed in under 5 minutes on any Linux server, desktop, or edge computer with Docker.

---

## 5-Minute Quickstart

### Step 1: Clone the Distribution Hub
```bash
git clone https://github.com/BIG-FullFill/sensio-hub.git
cd sensio-hub/deploy/iot
```

### Step 2: Configure Environment
Generate your encryption secret and initialize `.env`:
```bash
mkdir -p .secrets
openssl rand 32 > .secrets/device_token_encryption_key
chmod 600 .secrets/device_token_encryption_key

cp .env.example .env
chmod 600 .env
```
Edit `.env` to supply your `DATABASE_URL` (e.g. `postgresql://user:pass@127.0.0.1:5432/sensio_iot`).

### Step 3: Start Sensio IoT
```bash
docker compose up -d
```

### Step 4: Access the Dashboard
Open your web browser at:
```text
http://localhost:3000
```
On first launch, follow the onboarding prompt to create your administrator account and initial Site.

---

## Next Steps
- [Server Deployment Walkthrough](install-docker.md)
- [NVIDIA Jetson Edge Deployment](install-jetson.md)
- [Android Mobile App Setup](install-android.md)
- [Sensio CLI Reference](cli-reference.md)
- [Model Context Protocol (MCP) Setup](mcp-setup.md)
