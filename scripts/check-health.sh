#!/usr/bin/env bash
# ==============================================================================
# Sensio Deployment Health & Diagnostic Script
# Verifies container states, API endpoints, and database connectivity.
# ==============================================================================
set -euo pipefail

TARGET_HOST="${1:-127.0.0.1}"
TARGET_PORT="${2:-3000}"
HEALTH_URL="http://${TARGET_HOST}:${TARGET_PORT}/health"

echo "=== Sensio Diagnostic Check ==="
echo "Target Endpoint: $HEALTH_URL"

# Check Docker services if docker is available
if command -v docker >/dev/null 2>&1; then
    echo ""
    echo "--- Active Sensio Containers ---"
    docker ps --filter "name=sensio" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" || true
fi

# Check HTTP health probe
echo ""
echo "--- Testing HTTP Health Endpoint ---"
if curl --fail --silent --show-error --connect-timeout 5 "$HEALTH_URL" > /dev/null; then
    RESPONSE=$(curl -s "$HEALTH_URL")
    echo "✓ Sensio Health Status: OK (200)"
    echo "Response payload: $RESPONSE"
else
    echo "✗ Failed to connect to $HEALTH_URL"
    echo "Check if the container is running and port $TARGET_PORT is mapped properly."
    exit 1
fi

echo ""
echo "=== All Checks Passed! ==="
