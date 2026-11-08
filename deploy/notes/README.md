# Sensio Notes Deployment (Coming Soon)

Sensio Notes is the upcoming private, AI-augmented knowledge and collaborative note-taking platform within the Sensio Ecosystem.

---

## Architecture Overview

- **Sensio Notes Server**: Encrypted sync engine, markdown parser, vector embedding store, and multi-device state coordination.
- **Client Ecosystem**: Progressive Web App, desktop companion (macOS, Windows, Linux), and mobile application.
- **Interoperability**: Connects seamlessly with Sensio IoT for context-aware automation logging, device maintenance logs, and spatial notes.

---

## Deployment Preview

When released, Sensio Notes can be self-hosted with Docker Compose:

```bash
docker compose -f docker-compose.yml up -d
```

Configuration variables will be populated in `.env.example`. Check back soon for the initial beta release!
