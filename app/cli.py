from app.models import Session, User, Movie, Site, Watch

session = Session()

def watch_movie():
    print("\nUsers:")
    for user in session.query(User):
        print(f"{user.id}. {user.name}")
    user_id = int(input("Select user ID: "))
    user = session.query(User).get(user_id)

    print("\nMovies:")
    for movie in session.query(Movie):
        print(f"{movie.id}. {movie.title} ({movie.genre})")
    movie_id = int(input("Select movie ID: "))
    movie = session.query(Movie).get(movie_id)

    print("\nSites:")
    for site in session.query(Site):
        print(f"{site.id}. {site.name} - ${site.subscription_fee}")
    site_id = int(input("Select site ID: "))
    site = session.query(Site).get(site_id)

    watch = Watch(user=user, movie=movie, site=site)
    session.add(watch)
    session.commit()

    print(f"\n{user.name} watched {movie.title} on {site.name}!")

def add_user():
    name = input("Enter user name: ").strip()
    if name:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User '{name}' added with ID {user.id}.")
    else:
        print("Name cannot be empty.")

def add_movie():
    title = input("Enter movie title: ").strip()
    genre = input("Enter movie genre: ").strip()
    year_str = input("Enter movie year: ").strip()
    if not (title and genre and year_str.isdigit()):
        print("Invalid input. Please provide title, genre and a numeric year.")
        return
    year = int(year_str)
    movie = Movie(title=title, genre=genre, year=year)
    session.add(movie)
    session.commit()
    print(f"Movie '{title}' added with ID {movie.id}.")

def add_site():
    name = input("Enter site name: ").strip()
    fee_str = input("Enter subscription fee: ").strip()
    try:
        subscription_fee = float(fee_str)
    except ValueError:
        print("Subscription fee must be a number.")
        return
    if name:
        site = Site(name=name, subscription_fee=subscription_fee)
        session.add(site)
        session.commit()
        print(f"Site '{name}' added with ID {site.id}.")
    else:
        print("Name cannot be empty.")

if __name__ == "__main__":
    while True:
        print("\n--- Movie Watch CLI ---")
        print("1. Watch a Movie")
        print("2. Add User")
        print("3. Add Movie")
        print("4. Add Site")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            watch_movie()
        elif choice == "2":
            add_user()
        elif choice == "3":
            add_movie()
        elif choice == "4":
            add_site()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")
