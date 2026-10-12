

---

# Siri to PC Bridge 🍏➡️💻

A lightweight bridge application that allows you to control your PC's power state (Shutdown, Restart, Sleep) using Siri commands via Apple Shortcuts on iOS, iPadOS, macOS, or HomePod.

---

## 🛠️ Features

* 🛑 **Shutdown PC**: Triggers a clean system shutdown.
* 🔄 **Restart PC**: Reboots your computer remotely.
* 💤 **Sleep Mode**: Puts your PC to sleep state.
* 🔒 **Local & Secure**: Communicates over your local local network (LAN) using authorization keys/tokens.
* ⚡ **Siri Integration**: Works natively with Apple Shortcuts for seamless hands-free voice control.

---

## 📋 Prerequisites

* **PC**: Windows / macOS / Linux machine connected to the same Wi-Fi or LAN as your Apple device.
* **Apple Device**: iPhone, iPad, Mac, or Apple Watch running iOS/macOS with the **Shortcuts** app installed.
* **Runtime**: Node.js v16+ (or Python 3.8+ / Go, depending on your executable build).

---

## 🚀 Getting Started

### 1. Installation on PC

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/siri-pc-bridge.git
cd siri-pc-bridge
npm install

```

### 2. Configuration

Create a `.env` file in the root directory (or edit `config.json`):

```env
PORT=3000
API_KEY=your_secret_passphrase_here

```

### 3. Run the Server

Start the bridge application on your PC:

```bash
npm start

```

*(Optional: Set up the script to run automatically at startup using Windows Task Scheduler or `systemd` on Linux).*

---

## 🛰️ API Endpoints

The bridge exposes simple REST endpoints protected by your `API_KEY`:

| Action | HTTP Method | Endpoint | Description |
| --- | --- | --- | --- |
| **Shutdown** | `POST` | `/api/shutdown` | Initiates computer shutdown |
| **Restart** | `POST` | `/api/restart` | Restarts the computer |
| **Sleep** | `POST` | `/api/sleep` | Puts the computer into sleep mode |
| **Status** | `GET` | `/api/status` | Checks if the bridge is active |

---

## 📲 Setting Up Apple Shortcuts & Siri

To trigger these actions using voice, follow these steps in the **Shortcuts** app on your iPhone/iPad:

### Step-by-Step Setup

1. Open the **Shortcuts** app on your iOS device.
2. Create a **New Shortcut** (e.g., name it `Turn Off My PC`).
3. Add the action **"Get Contents of URL"**.
4. Configure the action details:
* **URL**: `http://<YOUR_PC_LOCAL_IP>:3000/api/shutdown`
* **Method**: `POST`
* **Headers**: Add Header `x-api-key` with value `your_secret_passphrase_here`


5. Save the shortcut.

> **Testing**: Say *"Hey Siri, Turn Off My PC"* to test the command!

---

## 🛡️ Security Best Practices

* **Static IP Address**: Assign a static local IP address to your PC via your router settings to prevent IP changes.
* **Firewall Rules**: Ensure your firewall allows incoming traffic on port `3000` only from local network subnets (`192.168.x.x`).
* **Authentication Key**: Never expose your endpoint to the public internet without strong authentication or VPN access (e.g., Tailscale).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
