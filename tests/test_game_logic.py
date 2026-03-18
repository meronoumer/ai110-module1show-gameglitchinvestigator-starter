from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct!" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Tests for the bugs we fixed

def test_hint_messages_correct_for_high_guess():
    """Test that when guess is too high, it says 'Go LOWER!' (not 'Go HIGHER!')"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER!" in message
    assert "Go HIGHER!" not in message

def test_hint_messages_correct_for_low_guess():
    """Test that when guess is too low, it says 'Go HIGHER!' (not 'Go LOWER!')"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER!" in message
    assert "Go LOWER!" not in message

def test_difficulty_ranges_increase_correctly():
    """Test that difficulty ranges increase: Easy < Normal < Hard"""
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    # Easy should have smallest range
    assert easy_high - easy_low <= normal_high - normal_low
    # Normal should have medium range
    assert normal_high - normal_low <= hard_high - hard_low
    # Hard should have largest range
    assert hard_high - hard_low >= normal_high - normal_low

def test_specific_difficulty_ranges():
    """Test the exact ranges for each difficulty level"""
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_normal_vs_hard_range_bug():
    """Test that specifically targets the bug: Normal should NOT have larger range than Hard"""
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    normal_range = normal_high - normal_low  # Should be 49 (50-1)
    hard_range = hard_high - hard_low       # Should be 99 (100-1)

    # This assertion would fail with the old buggy code where Normal had range 1-100 (99)
    # and Hard had range 1-50 (49), making Normal larger than Hard
    assert normal_range < hard_range, f"Normal range ({normal_range}) should be smaller than Hard range ({hard_range})"

    # Also verify the actual values to be extra sure
    assert normal_high == 50, "Normal should go up to 50"
    assert hard_high == 100, "Hard should go up to 100"

def test_parse_guess_handles_integers_correctly():
    """Test that parse_guess works correctly with integer inputs (no string conversion issues)"""
    # Test valid integers
    ok, value, error = parse_guess("42")
    assert ok == True
    assert value == 42
    assert error is None

    # Test that it handles the range correctly (no issues with < 0)
    ok, value, error = parse_guess("0")
    assert ok == True
    assert value == 0

    ok, value, error = parse_guess("-5")
    assert ok == True
    assert value == -5

def test_check_guess_with_integers_only():
    """Test that check_guess works correctly with integers only (no string conversion)"""
    # This test ensures we don't have the string comparison bug
    # where "5" > "50" would be True due to lexicographic comparison

    # Test cases that would fail with string comparison
    outcome1, _ = check_guess(5, 50)  # 5 < 50, should be "Too Low"
    assert outcome1 == "Too Low"

    outcome2, _ = check_guess(50, 5)  # 50 > 5, should be "Too High"
    assert outcome2 == "Too High"

    outcome3, _ = check_guess(25, 50)  # 25 < 50, should be "Too Low"
    assert outcome3 == "Too Low"

    outcome4, _ = check_guess(75, 50)  # 75 > 50, should be "Too High"
    assert outcome4 == "Too High"
