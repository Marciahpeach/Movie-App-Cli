# 🎬 Movie Watch CLI App

Welcome to the **Movie Watch CLI**, a command-line application that allows users to watch movies on different streaming sites. Users, movies, and streaming platforms can be added interactively via the CLI.



## 🚀 FEATURES

- 👤 Add users
- 🎞️ Add movies with title, genre, and release year
- 🌐 Add streaming sites with subscription fees
- 👁️ Record a "watch" event (user watches a movie on a site)
- 🗂️ Uses SQLAlchemy ORM with SQLite for data persistence



## 📂 PROJECT STRUCTURE

movie_watch_cli/
│
├── app/
│ ├── init.py
│ ├── models.py # SQLAlchemy models and DB setup
│
├── seed.py # Seeds initial users, movies, and sites
├── cli.py # Interactive CLI for managing the app
├── create_db.py # Ensures database and tables are created
├── README.md # Project documentation

## TOOLS USED
🐍 Python 3

🛠️ SQLAlchemy ORM

🗃️ SQLite

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone "https://github.com/Marciahpeach/Movie-App-Cli.git"
cd Movie-App-Cli

### INSTALL DEPENDENCIES
This app uses only Python's built-in libraries and SQLAlchemy.
  pip install sqlalchemy


### CREATE AND SEED THE DATABASE
python -m  create_db
python -m app.seed

##RUN THE CLI
pyhton -m app.cli

##CLI MENU
--- Movie Watch CLI ---
1. Watch a Movie
2. Add User
3. Add Movie
4. Add Site
5. Exit

##EXAMPLE USAGE
# Add a new user
> Enter user name: Alice

# Add a new movie
> Enter movie title: Interstellar
> Enter movie genre: Sci-Fi
> Enter movie year: 2014

# Add a new site
> Enter site name: HBO Max
> Enter subscription fee: 12.99

# Watch a movie
> Select user ID: 1
> Select movie ID: 2
> Select site ID: 1


###📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

###💡 Future Improvements
Add deletion and update options

Add user-specific watch history view

Include ratings and reviews

Export reports to CSV or JSON
