class Book:
    def __init__(self, title, author, list_of_reviews):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews

    def add_a_new_review(self, review):
        self.list_of_reviews.append(review)
        print(f'review added successfully!!!')
    
    def count_reviews(self):
        print(f"the reviews count = {len(self.list_of_reviews)}")

    def display_all_reviews(self):
        print(f"{self.list_of_reviews}")

b1 = Book("Atomic Habits", "Clear", ["very good book"])
b1.add_a_new_review("Very helpful book")
b1.count_reviews()
b1.display_all_reviews()
