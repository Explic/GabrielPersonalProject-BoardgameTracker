# All In One Board Game Tracker – Project Proposal

**Student Name**: Gabriel Fincham  
**Project Title**: All In One Board Game Tracker  
**Subject**: Software Engineering – Personal Project 2025  

---

## 1. Project Summary

The program will be an all-in-one app for board game enthusiasts. It will include built-in game recommendations, board game data, a wishlist system, and more. The goal is to make it user-friendly and easy to use.

---

## 2. Purpose and Need (Problem Statement)

Many board game owners with large collections struggle to choose what game to play. Additionally, it can be difficult to keep track of the board games they own, want, or wish to play. This program will centralize and simplify collection management.

---

## 3. Target Audience / Users

The application targets:
- People who own large board game collections
- Regular board game players
- Users of all ages looking for a better way to manage and explore board games

---

## 4. Proposed Features

- **Personal Board Game Database**: Manage a list of owned games.
- **Game Statistics Display**: Show playtime, difficulty, type, etc.
- **User Account System**: Allow users to log in and manage personalized data.
- **Game Recommendations**: Suggest games to play based on various criteria.
- **Wishlist Tracker**: Track the availability and pricing of desired board games.

---

## 5. Technologies / Tools

- **Programming Language**: Python 3+
- **Libraries**:
  - `customtkinter` (GUI)
  - `json` (Data storage)
  - Encryption library (e.g., `bcrypt`)
  - Recommendation logic (custom or ML-based)
- **Other Tools**:
  - GitHub (version control)
  - VSCode (development environment)
  - Board Game Geek API & CSV Database

---

## 6. Method / Approach (Agile Life Cycle)

The project will follow the Agile life cycle:
- **Planning**: Define sprint features and timelines.
- **Development Sprints**: Weekly iterations focusing on specific modules.
- **Weekly Logs**: Document progress and issues.
- **Continuous Integration**: Frequent GitHub commits for backup and collaboration.

---

## 7. Major Challenges & Solutions

| Challenge                                  | Proposed Solution                                                                 |
|-------------------------------------------|------------------------------------------------------------------------------------|
| Data management (JSON/API integration)    | Design data structure early; mock API calls before integration                    |
| Secure user login                         | Use hashed passwords and secure credential handling                               |
| Recommendation system complexity          | Start with simple filters, evolve to smarter predictions                          |
| GUI integration with backend              | Build and test backend first, integrate frontend around it                        |

---

## 8. Project Timeline Overview

### Planning (5 hours)
- GUI layout and data format design
- GitHub setup

### Backend Development (20–30 hours)
- Terminal-based backend (core logic)
- Setup environment, define classes
- Create database structure (SQL, JSON, CSV)
- Build recommendation and wishlist systems
- Personal account system

### Frontend Development (25–30 hours)
- GUI layout planning (5 hours)
- UI framework and components (6–7 hours)
- Login page (1–3 hours)
- Database page (2–4 hours)
- Backend/frontend integration (10 hours)

### Security Implementation (3 hours)
- Password encryption (2 hours)
- SQL injection prevention (1 hour)

### Finalizing (3–5 hours)
- Final testing, bug fixing
- Improve GitHub page, finalize documentation

---

## 9. Project Diagrams

Stored in [`docs/diagrams/`](diagrams/):

- Context Diagram (Level 0)
- Level 1 Data Flow Diagram
- Level 2 Data Flow Diagrams
- Structure Chart

---

## 10. References

- [BoardGameGeek API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
- Python Docs: https://docs.python.org/3/
- CustomTkinter Docs: https://github.com/TomSchimansky/CustomTkinter

