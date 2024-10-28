from app import process_query


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs") ==
        "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_process_query_returns_player_name():
    assert process_query("What is your name?") == "nn1524as3824"


def test_process_query_returns_addition():
    assert process_query("What is 88 plus 74?") == "162"


def test_process_query_returns_multiplication():
    assert process_query("What is 8 multiplied by 3?") == "24"


def test_process_query_returns_subtraction():
    assert process_query("What is 10 minus 8?") == "2"


def test_process_query_returns_primes():
    assert (process_query("Which of the following numbers are primes: "
                          "31, 95, 37, 18, 60?") == "31, 37")


def add_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def subtract_numbers(num1, num2):
    return num1 - num2
