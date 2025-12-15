# MCSB Security Benchmark WebApp

A Flask web application that displays Microsoft Cloud Security Benchmark (MCSB v2) controls with Microsoft implementation guidance.

## 🔐 Features

- **12 Security Domains** - All MCSB v2 categories
- **Multilingual** - Dutch and English supported
- **Microsoft Implementation** - Specific Microsoft products and documentation links
- **Responsive Design** - Works on desktop and mobile

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/KerkhofMe/MSCBWeApp.git
cd MSCBWeApp

# Install dependencies
pip install -r requirements.txt

# Start the application
python app.py
```

Open http://localhost:5000 in your browser.

## 📋 Security Domains

| ID | Domain | Status |
|----|--------|--------|
| NS | Network Security | 🚧 Coming Soon |
| IM | Identity Management | 🚧 Coming Soon |
| PA | Privileged Access | 🚧 Coming Soon |
| DP | Data Protection | 🚧 Coming Soon |
| AM | Asset Management | 🚧 Coming Soon |
| LT | Logging and Threat Detection | ✅ Compplete - but still need to add technical stuff. |
| IR | Incident Response | 🚧 Coming Soon |
| PV | Posture and Vulnerability Management | 🚧 Coming Soon |
| ES | Endpoint Security | 🚧 Coming Soon |
| BR | Backup and Recovery | 🚧 Coming Soon |
| DS | DevOps Security | 🚧 Coming Soon |
| AI | Artificial Intelligence Security | 🚧 Coming Soon |

## 🛠️ Technologies

- Python 3.9+
- Flask 3.0
- HTML/CSS/Jinja2

## 📖 References

- [Microsoft Cloud Security Benchmark v2](https://learn.microsoft.com/en-us/security/benchmark/azure/overview)
