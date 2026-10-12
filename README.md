# Energy Data Manager

A Python CRUD application for managing a public energy dataset, built with a layered architecture.

## ✨ Features
- **Create, Read, Update, Delete** energy records
- **Sorting** records by selected columns
- **Multi-column search/filter** combining several conditions at once
- Loads data from a public energy dataset (CSV)

## 🏗 Architecture
The project follows a layered (MVC-style) structure:

| Layer | Folder | Role |
|---|---|---|
| Presentation | `presentation/` | Menu and user interaction |
| Business | `business/` | Core logic (sorting, filtering) |
| Model | `model/` | Energy record data structure |
| Persistence | `persistence/` | Reading and writing the CSV file |

## 🛠 Tech
Python · Git (branches and version tags)

## 🚀 How to Run
```bash
python main.py
```

## 📌 Versions
- **V3.0**: Added sorting feature
- **V4.0**: Added multi-column search/filter feature

---
Developed by Jiyeon (Gigi) Yoo as part of a course project at Algonquin College.
