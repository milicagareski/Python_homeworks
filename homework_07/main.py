# TASK NUMBER 1

class Book:
    def __init__(self, name, number_of_pages):
        self.name = name
        self.number_of_pages = number_of_pages

book1 = Book("Harry Potter", 200)
print(book1.name, book1.number_of_pages)


class Novel(Book):
    def __init__(self, name, number_of_pages, author, year_of_production):
        super().__init__(name, number_of_pages)
        self.author = author
        self.year_of_production = year_of_production

book2 = Novel("Harry Potter", 200, "Joanne Rowling", 1997)
print (book2.name, book2.number_of_pages, book2.author, book2.year_of_production)

class Mistery(Book):
        def __init__(self, name, number_of_pages, place_of_publish, publish_house):
             super().__init__(name, number_of_pages)
             self.place_of_publish = place_of_publish
             self.publish_house = publish_house
             self.is_misterious = "The book is misterious"

book3 = Mistery("Harry Potter", 200, "Bloomsbury", "Scholastic Press")
print(book3.name, book3.number_of_pages, book3.place_of_publish, book3.publish_house, 
      book3.is_misterious)


class Movie(Book):
     def __init__(self, name, number_of_pages, year_of_movie, number_of_movies):
          super().__init__(name, number_of_pages)
          self.year_of_movie = year_of_movie
          self.number_of_movies = number_of_movies

book4 = Movie("Harry Potter", 200, 2001, 8)
print(book4.name, book4.number_of_pages, book4.year_of_movie, book4.number_of_movies)


# TASK NUMBER 2

# Parent class is Spell
# Children classes are Accio and Confundo
# spell.execute will print Action
# study_spell(spell) will print Summoning Charm Action and no description
# study_spell(Confugio()) will execute the Confugio class and will print Confundus Charm Confugio and 
# causes the viktim to become confused and befuddled


# TASK NUMBER 3

class  Address:
     def __init__(self, street, num):
          self.street_name = street
          self.number = num


class CampusAddress(Address):
    def __init__(self, office_number):
        super().__init__("Massachusetts Ave", 77) 
        self.office_number = office_number


address = CampusAddress("32-G904")
print(address.street_name, address.number, address.office_number)