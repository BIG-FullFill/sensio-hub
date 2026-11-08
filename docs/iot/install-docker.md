# Sensio IoT Docker Server Installation

This guide walks through deploying Sensio IoT on standard AMD64 (x86_64) Linux servers (Ubuntu, Debian, Arch Linux, Rocky/RHEL).

---

## 1. System Requirements

- **CPU**: 2+ cores recommended.
- **RAM**: 2 GB minimum (4 GB recommended if running embedded AI assistant and local STT).
- **Disk**: 10 GB free space.
- **Docker Engine**: Version 24.0 or newer with Compose v2.

---

## 2. Directory & Secrets Setup

```bash
mkdir -p /opt/sensio/deploy/iot
cd /opt/sensio/deploy/iot

# Download deployment files
curl -sSL -O https://raw.githubusercontent.com/BIG-FullFill/sensio-hub/main/deploy/iot/docker-compose.yml
curl -sSL -O https://raw.githubusercontent.com/BIG-FullFill/sensio-hub/main/deploy/iot/.env.example

# Generate encryption key
mkdir -p .secrets
openssl rand 32 > .secrets/device_token_encryption_key
chmod 600 .secrets/device_token_encryption_key

# Prepare environment file
cp .env.example .env
chmod 600 .env
```

---

## 3. Database Preparation

Sensio IoT uses PostgreSQL. If you don't have a database, you can run one via Docker:

```bash
docker run -d \
  --name sensio-postgres \
  --restart always \
  -e POSTGRES_USER=sensio \
  -e POSTGRES_PASSWORD=sensiosecret \
  -e POSTGRES_DB=sensio_iot \
  -p 127.0.0.1:5432:5432 \
  -v sensio-postgres-data:/var/lib/postgresql/data \
  postgres:16-alpine
```

Set in `.env`:
```env
DATABASE_URL=postgresql://sensio:sensiosecret@127.0.0.1:5432/sensio_iot
```

---

## 4. Run & Verify

```bash
docker compose up -d

# Check container logs
docker compose logs -f sensio-iot

# Check health
curl http://127.0.0.1:3000/health
```

Access the dashboard at `http://<SERVER_IP>:3000`.
