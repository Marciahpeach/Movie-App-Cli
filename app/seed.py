from app.models import Base, engine, Session, User, Movie, Site


Base.metadata.create_all(engine)

session = Session()

users = [User(name='Marciah'), User(name='Mantel')]
movies = [
    Movie(title='Inception', genre='Sci-Fi', year=2010),
    Movie(title='Titanic', genre='Romance', year=1997)
]
sites = [
    Site(name='Netflix', subscription_fee=15),
    Site(name='Hulu', subscription_fee=10)
]


session.add_all(users + movies + sites)


session.commit()

print("Database seeded.")
