# Boardgame Tracker

## Overview
Boardgame Tracker is a Python-based application designed to help users explore, track, and manage their favorite board games. The application provides features such as game recommendations, wishlist management, and detailed game views, making it easier for board game enthusiasts to discover and organize their collection.

## Features
- **Login and Signup**: Secure user authentication to manage personalized data.
- **Game Recommendations**: Suggests games based on wishlist or default preferences.
- **Wishlist Management**: Add or remove games from your wishlist.
- **Game Details**: View detailed information about games, including player count, playtime, rating, and more.
- **Top-Rated and Popular Games**: Explore lists of top-rated and popular games.
- **Image Caching**: Efficiently downloads and caches game images for faster loading.
- **Interactive UI**: Clickable elements for navigating game details and recommendations.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd BoardgameTracker
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Sign up and login.

## Project Structure
- **`main.py`**: Entry point of the application.
- **`src/backend`**: Contains backend logic for user management, game recommendations, and search functionality.
- **`ui`**: Includes UI + Python files for login, homepage, and game view.
- **`ui/assets`**: Stores images and cached game assets.
- **`requirements.txt`**: Lists project dependencies.

## Dependencies
- `PySide6` & `PyQt6`: For building the graphical user interface.
- `requests`: For handling HTTP requests to download game images.
- `cutie`: For the backend tester ui.

## Acknowledgments
- BoardGameGeek Database: The board game data used in this project was sourced from [Kaggle](https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek), provided by Threnjen.
- BoardGameGeek for providing the game database.
- Python and PySide6 for enabling rapid application development.
