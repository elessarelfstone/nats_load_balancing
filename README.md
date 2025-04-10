# 🛰️ NATS + Python Producer & Consumer Example

This project demonstrates how to run a NATS server using Docker and how to send/receive messages using Python scripts with `nats-py`.

---

## 📦 Prerequisites

- [Docker](https://www.docker.com/)
- Python 3.7+
- `pip` package manager

---


1. Start NATS Server (via Docker Compose)

```bash
docker-compose up -d
```


2. Run producer and consumer scripts as much as you need so you can see increasing or decreasing load
```bash
python producer.py
```

```bash
python consumer.py
```
