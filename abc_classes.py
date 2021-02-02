from abc import ABCMeta, abstractmethod


class Program(metaclass=ABCMeta):
    def __init__(self, name: str, year: int) -> None:
        self._name = name
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def likes(self):
        return self._likes
    
    def add_like(self):
        self._likes += 1

    # the abstractmethod decorator will ensure that the __str__ method will need to be implemented for every class inheriting Program
    @abstractmethod
    def __str__(self) -> str:
        return f'name:{self.name} year:{self.year} likes:{self.likes}'
    
    def __repr__(self) -> str:
        return f'{self.__class__}({self.__dict__})'


class Movie(Program):
    def __init__(self, name: str, year: int, duration: int) -> None:
        super().__init__(name, year)
        self.duration = duration
    
    def __str__(self):
        return f'name:{self.name} year:{self.year} duration:{self.duration} likes:{self.likes}' 


class Series(Program):
    def __init__(self, name: str, year: int, seasons: int) -> None:
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'name:{self.name} year:{self.year} seasons:{self.seasons} likes:{self.likes}' 
        

class Playlist:
    def __init__(self, name: str, programs: list) -> None:
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        'Allow list iteration over programs inside the playlist'
        return self._programs[item]

    def __len__(self):
        return len(self._programs)



avengers = Movie('avengers', 2018, 160)
scary = Movie('scary movie', 1977, 129)
atlanta = Series('atlanta', 2018, 2)
got = Series('Game of Thrones', 2018, 9)
avengers.add_like()
avengers.add_like()
avengers.add_like()
got.add_like()
got.add_like()

movies_series = [avengers, atlanta, scary, got]

playlist_weekend = Playlist('weekend', movies_series)

for program in playlist_weekend:
    print(program)

print(got in playlist_weekend)
