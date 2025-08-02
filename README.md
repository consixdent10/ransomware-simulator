# Ransomware Simulator (Educational Use Only)

## 📌 Project Overview
This project is developed as part of the **Cybergyan, CDAC Noida Cybersecurity Internship**.  
It simulates basic ransomware behavior in a **safe and controlled virtual environment** without causing real damage.

The simulator:
- Locates a test file in a predefined folder.
- Simulates encryption by renaming files with `.encrypted` extension.
- Generates a ransom note (`README.txt`) with a mock demand.
- Displays a popup message to mimic a real ransomware alert.

---

## ⚙ Features
- **Safe Simulation**: No actual encryption performed — files can be restored manually.
- **Cross-File Simulation**: Works on all files in the target folder.
- **Educational Purpose**: Demonstrates ransomware workflow for awareness and training.

---

## 🖥 Requirements
- Windows 10 (inside a Virtual Machine)
- Python 3.10 or above

---

## 📂 Usage Instructions
1. Inside your Windows VM, create a folder on Desktop called `TestFiles`.
2. Place a dummy file inside `TestFiles` (e.g., `victim_note.txt`).
3. Save the script as `ransom_simulator.py`.
4. Run the script:
   ```bash
   python ransom_simulator.py

