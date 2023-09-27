from lib.grammer_stats import GrammarStats

def test_with_an_invalid_sentence():
    stats = GrammarStats()
    stats.check("invalid text")
    
    # Verify that the percentage is 0.0 since there are no correct sentences.
    assert stats.percentage_good() == 0.0

def test_with_a_valid_sentence():
    stats = GrammarStats()
    stats.check("This is a valid sentence.")
    
    # Verify that the percentage is 100.0 since there is one correct sentence.
    assert stats.percentage_good() == 100.0

