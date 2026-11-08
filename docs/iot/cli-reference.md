# Sensio IoT Command-Line Interface (`sensio`)

`sensio` is the official command-line tool suite for Sensio IoT, providing headless management, interactive control, scriptable JSON pipelines, and Model Context Protocol (MCP) server capabilities.

---

## 1. Quick Installation

```bash
curl -fsSL https://raw.githubusercontent.com/BIG-FullFill/sensio-hub/main/scripts/install-sensio-cli.sh | bash
```

Alternatively, if running inside a container:
```bash
docker exec -it sensio-iot sensio --help
```

---

## 2. Authentication & Configuration

### Interactive Login
```bash
sensio auth login
# Prompts for Server URL (default: http://localhost:3000), Email & Password
```

Credentials are saved securely in `~/.config/sensio/credentials.json`.

---

## 3. Core Commands Cheat Sheet

### Sites & Rooms
```bash
# List all active sites
sensio sites list

# List rooms in a site
sensio rooms list --site-id <SITE_ID>
```

### Devices & Telemetry
```bash
# List devices in tabular format
sensio devices list --site-id <SITE_ID>

# Output machine-readable JSON for scripting
sensio devices list --site-id <SITE_ID> --format json

# Control a switch/relay
sensio devices control --device-id <DEVICE_ID> --command '{"state": "ON"}'

# Control an AC unit via learned IR preset
sensio devices control --device-id <DEVICE_ID> --command '{"mode": "cool", "temperature": 24, "fan_speed": "auto"}'
```

### Automations & Scenes
```bash
sensio automations list --site-id <SITE_ID>
sensio automations trigger --automation-id <AUTOMATION_ID>
sensio scenes trigger --scene-id <SCENE_ID>
```

### AI Assistant Chat
```bash
sensio assistant chat --site-id <SITE_ID> --prompt "Turn off all lights in the living room"
```

### Model Context Protocol (MCP)
```bash
sensio mcp
```
Starts the MCP stdio server to connect your smart home directly to AI tools like Claude Desktop, Cursor, and Antigravity.
