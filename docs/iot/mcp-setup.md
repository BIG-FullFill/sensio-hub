# Sensio IoT Model Context Protocol (MCP) Setup

`sensio mcp` exposes Sensio IoT smart home capabilities to AI assistants through the **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)**. AI tools (Claude Desktop, Cursor, Antigravity, OpenCode) can list sites, read sensor states, trigger scenes, and control devices using natural language.

---

## 1. Quick Test

Test the stdio MCP server directly from your terminal:
```bash
sensio mcp
```
*(Diagnostic logs are piped to `stderr` while clean JSON-RPC 2.0 messages flow across `stdin`/`stdout`)*.

---

## 2. Configuration for AI Hosts

### A. Claude Desktop
Add to your Claude configuration file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sensio-iot": {
      "command": "/usr/local/bin/sensio",
      "args": ["mcp"],
      "env": {
        "SENSIO_URL": "http://localhost:3000"
      }
    }
  }
}
```

### B. Cursor
In Cursor settings (Features > MCP) or in `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "sensio-iot": {
      "command": "sensio",
      "args": ["mcp"],
      "env": {
        "SENSIO_URL": "http://localhost:3000"
      }
    }
  }
}
```

### C. Antigravity / Agentic Coding Tools
Add to your MCP server configuration:
```json
{
  "mcpServers": {
    "sensio": {
      "command": "sensio",
      "args": ["mcp"]
    }
  }
}
```

---

## 3. Available Tools & Capabilities

When connected, AI agents automatically gain access to tools such as:
- `list_sites`, `list_rooms`, `list_devices`, `list_scenes`, `list_automations`
- `send_device_command` (Turn lights on/off, set thermostat temperature, trigger IR codes)
- `trigger_scene` and `trigger_automation`
- `ask_assistant` (Execute natural language spatial reasoning commands)
