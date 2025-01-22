class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):

        
        
        if not isinstance(author, Author):
            raise ValueError("author must already be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must already be an instance of Magazine class")
        if not isinstance(title, str): 
           raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property 
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must already be an instance of Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must already be an instance of class Magazine")
        self._magazine = value

        
class Author:
    def __init__(self, name):
        if not isinstance(name, str): 
           raise TypeError("name must be a string")
        if len(name) == 0:
           raise ValueError("name cannot be zero")
        if hasattr(self, '_name'):
           raise AttributeError("cannot modify name")
        self._name = name
    
    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must already be an instance of class Magazine")
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in self.articles()}
        return list(categories) if categories else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise ValueError("name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("name must be between 2 and 18 characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value,str):
            raise ValueError("name must be a string")
        if len(value) == 0:
           raise ValueError("name cannot be zero")
        self._category = value


    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        pass