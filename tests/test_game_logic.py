from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_attempts_start_score():
    # First attempt win should give 90 points (100 - 10*1)
    score = update_score(0, "Win", 1)
    assert score == 90

def test_wrong_guess_never_gives_points():
    # Wrong guesses should deduct points, never add
    score = update_score(0, "Too High", 2)
    assert score == -5

def test_parse_guess_empty():
    ok, val, err = parse_guess("")
    assert ok == False

def test_hard_range_is_hardest():
    low, high = get_range_for_difficulty("Hard")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    assert high > normal_high