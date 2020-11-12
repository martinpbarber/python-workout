from src.chapter_03.exercise_11 import alphabetize_names

PEOPLE = [
    {"first": "Rueven", "last": "Lerner", "email": "reuven @ lerner.co.il"},
    {"first": "Donald", "last": "Trump", "email": "president @ whitehouse.gov"},
    {"first": "Vladimir", "last": "Putin", "email": "president @ kremvax.ru"},
]


def test_alphabetize_names():
    sorted_people = alphabetize_names(PEOPLE)
    assert sorted_people[0]["last"] == "Lerner"
    assert sorted_people[1]["last"] == "Putin"
    assert sorted_people[2]["last"] == "Trump"
