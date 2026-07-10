# 🛡️ System Guardian

System Guardian is a lightweight Python-based system monitoring tool that continuously tracks your computer's health and resource usage in the background.

It monitors CPU, RAM, and Disk usage, sends desktop notifications when usage becomes critical, logs system metrics, and generates analytical reports using NumPy.

---

## ✨ Features

- 📊 Real-time CPU Monitoring
- 🧠 RAM Usage Tracking
- 💾 Disk Usage Monitoring
- 🚨 Desktop Notifications for High Resource Usage
- 📈 System Health Score Calculation
- 🔍 Top Memory-Consuming Process Detection
- 📝 CSV-Based System Logging
- 📉 NumPy Analytics & Reporting
- 📦 Standalone EXE Support with PyInstaller

---

## 📂 Project Structure

```
SystemGuardian/
│
├── main.py
├── monitor.py
├── process_analyzer.py
├── health.py
├── logger.py
├── notifier.py
├── analytics.py
├── report.py
├── test_notification.py
├── .gitignore
└── README.md
```

---

## 🛠 Technologies Used

- Python 3
- NumPy
- psutil
- plyer
- CSV
- PyInstaller

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/horridnick08/SystemGuardian.git
cd SystemGuardian
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python main.py
```

System Guardian will start monitoring your system in the background.

---

## 📊 Analytics

Generate system statistics from logged data:

```bash
python analytics.py
```

Example Output:

```
Average CPU: 10.16%
Peak CPU: 41.5%

Average RAM: 85.59%
Peak RAM: 91.1%

Average Disk: 60.08%
```

---

## 📄 Generate Report

```bash
python report.py
```

This creates:

```
daily_report.txt
```

containing system performance statistics.

---

## 🔔 Notification Alerts

System Guardian automatically sends desktop notifications when:

- RAM usage exceeds the configured threshold
- Critical resource usage is detected

Notifications include:

- Current usage details
- Top memory-consuming processes

---

## 📦 Build EXE

```bash
pyinstaller --onefile --noconsole --collect-all plyer main.py
```

Generated executable:

```
dist/main.exe
```

---

## 📸 Sample Use Cases

- Monitor low-memory systems
- Detect resource-hungry applications
- Track long-term system health
- Learn Python system programming
- Practice NumPy with real-world data

---

## 👨‍💻 Author

**Nilesh Bokhare**

B.Tech CSE Student | Python Developer | Video Editor | AI & Automation Enthusiast

GitHub: https://github.com/horridnick08

---

## ⭐ Future Improvements

- Live Dashboard
- Historical Graphs
- Email Alerts
- Multi-Drive Monitoring
- Automatic Report Scheduling
- AI-Based Performance Prediction

---

If you find this project useful, consider giving it a ⭐ on GitHub.
