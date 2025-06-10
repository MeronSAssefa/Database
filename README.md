# 🕹️ Player Manager (Three-Tier Architecture)

This is a simple Python-based Player Manager system that follows a **three-tier architecture**:

- **Presentation Tier:** Command-line interface (`player_ui.py`)
- **Business Tier:** Player object model (`player_objects.py`)
- **Database Tier:** SQLite-backed data layer (`player_db.py`)

The system manages player records including their wins, losses, ties, and total games played.

---

## ⚙️ Features

- View all players sorted by wins
- View a specific player's stats
- Add a new player
- Delete an existing player
- Clean separation of concerns using tiered architecture

---

## 🗃️ Technologies

- Python 3
- SQLite3
- DB Browser for SQLite (for inspecting database manually)

---

## 📁 Project Structure

