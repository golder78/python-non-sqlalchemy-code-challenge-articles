class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author,Author):
            raise ValueError("Author must be an Author instance ")
        if not isinstance(magazine,Magazine):
            raise ValueError("Magazine must be a magazine instance")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string btwn 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author,Author):
            raise ValueError("Author must be an Author instance")
        self._author =new_author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine,Magazine):
            raise ValueError("Magazine must be a Magazine instance ")
        self._magazine =new_magazine

    @property
    def title(self):
        return self._title
    
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise  ValueError("author name must be a  non-emptystring")
        self.name = name
        self._articles =[]

    @property
    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self,magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters ")
        self._name = name
        self._category = category
        self._articles =[]

    @property
    def name(self): 
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name must be a string btween 2 and 26 characters ")
        self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category,str)or not new_category:
            raise ValueError("Magazine category must be a non-empty string")
        self._category = new_category

        
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None
    

    def contributing_authors(self):
        authors_with_more_than_two_articles = [author for author in self.contributors() if len(author.articles())]
        return authors_with_more_than_two_articles or None
    @classmethod
    def top_publisher(cls,magazines, ):
        if not magazines:
            return None
        return max(magazines, key=lambda m: len(m.articles()))
    

    
