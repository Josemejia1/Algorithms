class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} in ({self.year})"
    
    def quick_sort(sequence, key="year"):
        lenght = len(sequence)
        if lenght <= 1:
            return sequence
        
        pivot = sequence.pop()
        
        items_greater = []
        items_lower = []
        
        for item in sequence:
            if getattr(item, key) > getattr(pivot, key):
                items_greater.append(item)
            else:
                items_lower.append(item)
                
        return book.quick_sort(items_lower, key) + [pivot] + book.quick_sort(items_greater, key)
    
    book_list = []
    
book1 = book("The Waking Dream", "Susan Carter", 2017)
book2 = book("The Dark Horizon", "Barbara Scott", 1971)
book3 = book("The Forgotten Kingdom", "Ronald Allen", 2004)
book4 = book("The Dark Horizon", "Mary Moore", 1908)
book5 = book("Journey to the Unknown", "Elizabeth Young", 2021)
book6 = book("The Silent Forest", "Thomas Walker", 1998)
book7 = book("The Cursed Isle", "Ruth Carter", 2015)
book8 = book("Whispers in the Wind", "Jessica Hill", 2010)
book9 = book("Echoes of the Past", "Kevin Mitchell", 2005)
book10 = book("The Last Dreamer", "Nancy Perez", 1985)
book11 = book("The Shifting Sands", "Dorothy Walker", 2013)
book12 = book("The Wandering Star", "Paul Harris", 1992)
book13 = book("The Twilight Valley", "Sharon Lee", 2000)
book14 = book("The Hidden Treasure", "Linda Hall", 1975)
book15 = book("Beneath the Stars", "Thomas Walker", 1980)
book16 = book("Rays of Hope", "Jessica Hill", 2019)
book17 = book("Whispers of the Mountain", "Ronald Allen", 2002)
book18 = book("The Crimson Tide", "Barbara Scott", 1995)
book19 = book("The Secret Garden", "Emily Johnson", 1920)
book20 = book("The Endless Path", "Sarah Robinson", 2007)
book21 = book("The Hidden Realm", "Mark Robinson", 1998)
book22 = book("The Silver Key", "James Johnson", 2016)
book23 = book("The Phantom's Call", "Michael Brown", 1983)
book24 = book("The Eternal Flame", "Ruth Carter", 2020)
book25 = book("The Frozen Sky", "Jason Evans", 1990)
book26 = book("Journey into the Light", "Linda Scott", 2006)
book27 = book("The Heart of the Mountain", "Betty Adams", 2012)
book28 = book("The Secret Flame", "William Turner", 2001)
book29 = book("The Time Keeper", "Megan Clark", 2008)
book30 = book("Legends of the Fallen", "Helen Adams", 2014)
book31 = book("Beyond the Edge", "Kevin Mitchell", 2009)
book32 = book("The Wandering Star", "Dorothy Nelson", 2015)
book33 = book("Tales of the Wild", "Gary Harris", 2004)
book34 = book("The Storm Breaker", "Jason Evans", 2011)
book35 = book("The Last Hour", "Susan Hall", 2023)
book36 = book("The Silver Key", "Christopher Adams", 2003)
book37 = book("Echoes of the Lost", "James Taylor", 2020)
book38 = book("Waves of Change", "Mary White", 2000)
book39 = book("The Time Keeper", "Betty Adams", 1995)
book40 = book("Shadows of Tomorrow", "Nancy Perez", 2017)
book41 = book("The Whispering Woods", "James Taylor", 1999)
book42 = book("The Mystic Mountain", "Dorothy Martin", 2016)
book43 = book("The Last Sunrise", "Gary Harris", 2011)
book44 = book("The Forgotten World", "Sharon Lee", 1990)
book45 = book("Secrets of the Moon", "Jackie Young", 2020)
book46 = book("The Endless Sea", "Jessica Hill", 2018)
book47 = book("The Light of Hope", "Michael Brown", 2012)
book48 = book("The Hidden Secret", "Ruth Carter", 2005)
book49 = book("Into the Abyss", "Linda Hall", 1997)
book50 = book("The Cursed Stone", "John Smith", 2021)

book_list = [
    book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15,
    book16, book17, book18, book19, book20, book21, book22, book23, book24, book25, book26, book27, book28, book29, book30,
    book31, book32, book33, book34, book35, book36, book37, book38, book39, book40, book41, book42, book43, book44, book45,
    book46, book47, book48, book49, book50
]

sorted_books = book.quick_sort(book_list, key="year")

for b in sorted_books:
    print(b)