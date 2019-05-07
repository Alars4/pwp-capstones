class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		old_add = self.email
		self.email = address
		print("The email address for " + self.name + " has been updated from " + old_add + ". The new email address associated with this account is " + self.email + ".")

	def __repr__(self):
		return "The user " + self.name + ", email address: " + self.email + ", has read a total of " + str(len(self.books.keys())) + " books."

	def __eq__(self, other_user):
		own = self.name + self.email
		other = other_user.name + other_user.email
		return own == other
        
	def read_book(self, book, rating = None):
		self.books[book] = rating
		
	def get_average_rating(self):
		try:
			if len(self.books.values()) > 0:
				x = 0
				for rate in self.books.values():
					x += rate
				return x / len(self.books.values()) 
		except TypeError:
			return 0
			
  
        
class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
		
		
	def get_title(self):
		return self.title
	
	def get_isbn(self):
		return self.isbn
		
	def set_isbn(self, new):
		old = self.isbn
		self.isbn = new
		print("The ISBN for " + self.title + " has been updated from " + str(old) + " to the new ISBN " + str(self.isbn) + ".")
		
	def add_rating(self, rating):
		if rating >= 0.0 and rating <= 4.0:
			self.ratings.append(rating)
		else:
			print("Invalid Rating")
			
	def __eq__(self, other_book):
		current = self.title + str(self.isbn)
		other = other_book.title + str(other_book.isbn)
		return current == other
		
	def get_average_rating(self):
		if len(self.ratings) > 0:
			x = 0
			for rate in self.ratings:
				x += rate
			return x / len(self.ratings)
		else:
			return None
	
	def __hash__(self):
		return hash((self.title, self.isbn))
		
	def __repr__(self):
		return (self.title + " is a book.")
		
	
		
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
	
	def get_author(self):
		return self.author
		
	def __repr__(self):
		return (self.title + " by " + self.author)
		
	
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
		
	def get_subject(self):
		return self.subject
		
	def get_level(self):
		return self.level
		
	def __repr__(self):
		return (self.title + ", a " + self.level + " manual on " + self.subject)
		
		
class TomeRater():
	def __init__(self):
		self.users = {}
		self.books = {}
		
	def check_dupe_isbn(self, isbn):
		for book in self.books.keys():
			if book.isbn == isbn:
				print ("The ISBN of " + str(isbn) +" already exsts and is assigned to the book '" + book.get_title() + "'. Please check and re-enter this book with an updated ISBN.")
				return False
		return True
		
	def create_book(self, title, isbn):
		if self.check_dupe_isbn(isbn):
			return Book(title, isbn)
		
	def create_novel(self, title, author, isbn):
		if self.check_dupe_isbn(isbn):
			return Fiction(title, author, isbn)
		
	def create_non_fiction(self, title, subject, level, isbn):
		if self.check_dupe_isbn(isbn):
			return Non_Fiction(title, subject, level, isbn)
		
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users.keys():
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if book not in self.books.keys():
				self.books[book] = 0
			self.books[book] += 1
		else:
			print("No user with " + email + "!")

	def check_email(self, email): #validates email and checks for dupes
		if "@" not in email: #not looking for ".com" as suggested because email addresses can end in a wide variety of top level domains
			print (email + "is not a valid email address.")
			return False
		for mail in self.users.keys():
			if mail == email:
				print ("There is already a user with the email address " + email +" in this Tome Rater.")
				return False
		return True
		
	def add_user(self, name, email, user_books = None):
		if self.check_email(email):
			self.users[email] = User(name, email)
			try:
				for book in user_books:
					self.add_book_to_user(book, email)
			except TypeError:
				pass
				
	def update_email(self, old_email, new_email):
		if old_email not in self.users.keys():
			print ("There is no existing user with the email address of " + old_email + " in this Tome Rater.")
			return
		if self.check_email(new_email):
			self.users[new_email] = self.users.pop(old_email)
			self.users[new_email].change_email(new_email)
			
	def print_catalog(self):
		for book in self.books.keys():
			print(book)
	
	def print_users(self):
		for user in self.users.values():
			print(user)
			
	def most_read_book(self):
		x = 0
		for book in self.books.keys():
			if self.books[book] > x:
				x = self.books[book]
				max_book = book
		return max_book
		
	def highest_rated_book(self):
		x = 0
		for book in self.books.keys():
			if book.get_average_rating() > x:
				x = book.get_average_rating()
				best_book = book
		return best_book
		
	def most_positive_user(self):
		x = 0
		for user in self.users.values():
			if user.get_average_rating() > x:
				x = user.get_average_rating()
				opt_user = user
		return opt_user
		
	def __repr__(self):
		return ("This Tome Rater contains " + str(len(self.users.keys())) + " users, who have read a total of " + str(len(self.books.keys())) + " different books.")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		