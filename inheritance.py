class Worker:
    def __init__(self, name):
        self.name = name


    def register_time(self, time):
        print('Time registered')

    def show_tasks(self):
        print('Has done many tasks')


class Market(Worker):
    def show_tasks(self):
        print('Has done much work in the market!')

    def search_for_month_courses(self, month=None):
        print(f'Showing courses - {month}' if month else 'Showing this month courses')


class Office(Worker):
    def show_tasks(self):
        print('Has done much work in the office!')

    def search_for_questions_without_answer(self):
        print('Showing unanswered questions')


# mixin class
class Hipster:
    def __str__(self) -> str:
        return f'Hipster, {self.name}'

class Junior(Market):
    ...


class Senior(Market, Office, Hipster):
    ...





john = Junior('John')
john.search_for_month_courses()


pablo = Senior('Pablo')
print(pablo)