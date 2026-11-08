# Sensio IoT NVIDIA Jetson Edge Deployment

Sensio IoT provides specialized, native ARM64 container builds optimized for NVIDIA Jetson edge systems (Jetson Nano, TX2 NX, Xavier NX, Orin Nano, Orin AGX).

---

## 1. Edge Architecture Overview

On a Jetson edge controller, Sensio typically coordinates:
- **Zigbee2MQTT**: Communicates with USB Zigbee coordinators (e.g. Sonoff CC2652P, ITead dongle).
- **Embedded Mosquitto Broker**: Local low-latency MQTT pub/sub bus.
- **Tailscale HTTPS Reverse Proxy**: Secure remote access without opening public router ports.

---

## 2. Hardware Preparation

1. Plug in your USB Zigbee coordinator (e.g. `/dev/ttyUSB0` or `/dev/ttyACM0`).
2. Verify coordinator detection:
   ```bash
   ls -la /dev/serial/by-id/
   ```
3. Grant dialout permissions:
   ```bash
   sudo usermod -aG dialout $USER
   ```

---

## 3. Deployment

1. Navigate to Jetson deployment directory:
   ```bash
   cd deploy/iot
   ```
2. Start using the Jetson compose profile:
   ```bash
   docker compose -f docker-compose.jetson.yml up -d
   ```
3. Check services status:
   ```bash
   docker compose -f docker-compose.jetson.yml ps
   ```

---

## 4. Tailscale Remote Access (Optional)

Sensio includes built-in Nginx integration for Tailscale TLS certificates:
```bash
sudo tailscale cert <jetson-tailscale-domain>
```
Nginx automatically binds the certificate and provides trusted HTTPS access for the web dashboard and mobile app.
