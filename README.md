# 🚀 Spribe Aviator WebSocket Tracker

A powerful Python-based WebSocket listener that connects to the Spribe Aviator game server to monitor real-time game events, decode hash values, and track flight multipliers.

## 📋 Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Real-time WebSocket Connection**: Connects directly to Spribe Aviator game server
- **Round Data Monitoring**: Listen for and capture live round data
- **Hash Decoding**: Decode and analyze hash values from game events
- **Flight Multiplier Tracking**: Track and log flight multiplier values
- **Error Handling**: Robust error handling and automatic reconnection
- **Logging**: Comprehensive logging for debugging and monitoring
- **Data Export**: Export tracked data for analysis

## 📦 Requirements

- Python 3.8 or higher
- pip (Python package manager)
- WebSocket connectivity to Spribe servers

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/hitman1c/Spribe-Aviator-WebSocket-Tracker.git
cd Spribe-Aviator-WebSocket-Tracker
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Example
```python
from tracker import AviatorTracker

# Initialize tracker
tracker = AviatorTracker()

# Start listening for events
tracker.start()

# Your event handling logic here
tracker.on_round_data(callback=your_callback_function)
```

### Command Line Usage
```bash
python main.py --host <server_url> --port <port> --verbose
```

## ⚙️ Configuration

Create a `config.json` file in the project root:

```json
{
  "server": {
    "host": "wss://game-server.spribe.co",
    "port": 443
  },
  "logging": {
    "level": "INFO",
    "file": "logs/tracker.log"
  },
  "reconnect": {
    "enabled": true,
    "max_attempts": 5,
    "delay_seconds": 3
  }
}
```

## 📚 API Reference

### AviatorTracker Class

#### Methods

| Method | Description | Parameters |
|--------|-------------|-----------|
| `start()` | Connect to WebSocket server | None |
| `stop()` | Disconnect from server | None |
| `on_round_data()` | Register callback for round data events | `callback` (function) |
| `on_hash()` | Register callback for hash events | `callback` (function) |
| `decode_hash()` | Decode a hash value | `hash_value` (str) |
| `export_data()` | Export tracked data to CSV/JSON | `format` (str), `filename` (str) |

#### Events

- **round_start**: Emitted when a new round starts
- **round_end**: Emitted when a round ends
- **hash_received**: Emitted when hash data is received
- **multiplier_update**: Emitted when flight multiplier updates

## 🐛 Troubleshooting

### Connection Refused
- Verify WebSocket URL is correct
- Check firewall settings
- Ensure internet connectivity

### Hash Decoding Fails
- Verify hash format is correct
- Check for encoding issues
- Enable verbose logging for details

### High Memory Usage
- Implement data export/cleanup routines
- Check for memory leaks in callbacks
- Monitor with `python -m memory_profiler`

## 📝 Logging

Logs are stored in `logs/tracker.log`. Adjust logging level in `config.json`:

```
DEBUG   - Detailed debugging information
INFO    - General informational messages
WARNING - Warning messages
ERROR   - Error messages
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.

## ⚠️ Disclaimer

This project is for educational purposes only. Use responsibly and ensure compliance with Spribe's Terms of Service.

## 📞 Support

For issues, questions, or suggestions, please open an [Issue](https://github.com/hitman1c/Spribe-Aviator-WebSocket-Tracker/issues) on GitHub.

---

**Last Updated**: 2026-04-21