"""
Name: Russell, Abhinav, Arda
Student ID: C0927696, C0926240, C0923184
Date: August 14, 2025
Assignment: CSD 4523 Term Project - Toronto & GTA History Quiz
"""
from django.core.management.base import BaseCommand
from ...models import Question

DATA = [
    # text, A, B, C, D, correct
    ("What year was Toronto incorporated as a city?", "1834", "1793", "1867", "1812", "A"),
    ("Before it was called Toronto, what was the town's name?", "Kingston", "York", "Fort Rouillé", "Newark", "B"),
    ("Which lieutenant governor founded the town that became Toronto?", "Isaac Brock", "John Graves Simcoe", "Guy Carleton", "James Wolfe", "B"),
    ("Fort York was established to guard which harbour?", "Hamilton Harbour", "Toronto Harbour", "Frenchman's Bay", "Burlington Bay", "B"),
    ("The Toronto Islands were created after a storm cut off a sand spit in which year?", "1858", "1797", "1906", "1837", "A"),
    ("Which was Toronto’s first subway line (opened 1954)?", "Bloor–Danforth", "Yonge", "University", "Sheppard", "B"),
    ("The CN Tower was completed in:", "1983", "1976", "1972", "1969", "B"),
    ("GO Transit began service in:", "1959", "1967", "1975", "1988", "B"),
    ("Mississauga’s large evacuation after a train derailment happened in:", "1979", "1989", "1968", "1999", "A"),
    ("Toronto became a 'megacity' by amalgamation in:", "1995", "1998", "2001", "1990", "B"),
    ("Area code 905 was introduced to the GTA in:", "1993", "1985", "2000", "1998", "A"),
    ("The PATH system in downtown Toronto is a network of:", "Surface bike lanes", "Underground walkways", "Streetcar tracks", "Elevated roads", "B"),
    ("Old City Hall’s architect was:", "E. J. Lennox", "Frank Darling", "John Lyle", "Arthur Erickson", "A"),
    ("Casa Loma was mainly built during:", "1890–1893", "1911–1914", "1920–1923", "1935–1938", "B"),
    ("The Skydome (now Rogers Centre) opened in:", "1991", "1989", "1985", "1995", "B"),
    ("Yonge Street was long promoted as the world’s longest street; it runs north from:", "Union Station", "Harbourfront Centre", "Lake Ontario at Toronto’s waterfront", "City Hall", "C"),
    ("St. Lawrence Market’s site has hosted markets since:", "1903", "1867", "1803", "1763", "C"),
    ("Pearson Airport was originally known as:", "Downsview Airport", "Malton Airport", "Buttonville Airport", "Island Airport", "B"),
    ("The Spadina Expressway was cancelled in 1971 by:", "Pierre Trudeau", "David Crombie", "Bill Davis", "Mike Harris", "C"),
    ("Scarborough was named after a place in:", "Ireland", "Scotland", "Wales", "England", "D"),
    ("Which river marks the traditional boundary between Toronto and Etobicoke?", "Humber River", "Don River", "Rouge River", "Credit River", "A"),
    ("Which mall opened in 1964 and became a major transit hub?", "Square One", "Yorkdale", "Fairview", "Scarborough Town Centre", "B"),
    ("Which team name did Toronto’s first NHL franchise use in 1917–1918?", "Maple Leafs", "St. Patricks", "Arenas", "Marlboros", "C"),
    ("Which early French trading post once stood near today’s Exhibition Place?", "Fort George", "Fort York", "Fort Rouillé", "Fort Erie", "C"),
    ("Which borough joined Metro Toronto in 1953 and later became part of the megacity?", "Vaughan", "East York", "Pickering", "Markham", "B"),
]

class Command(BaseCommand):
    help = "Seed 25 Toronto/GTA history questions"

    def handle(self, *args, **kwargs):
        created = 0
        for text, a, b, c, d, correct in DATA:
            obj, is_new = Question.objects.get_or_create(
                text=text,
                defaults=dict(option_a=a, option_b=b, option_c=c, option_d=d, correct_option=correct)
            )
            if is_new:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} questions."))
