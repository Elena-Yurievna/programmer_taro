from ai_oracle import generate_support_phrase

def test_generate_support_phrase():
    phrase = generate_support_phrase()
    assert isinstance(phrase, str)
    assert len(phrase) <= 60
    assert phrase.strip() != ""

def test_generate_support_phrase_format():
    result = generate_support_phrase()
    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_support_phrase_length():
    phrase = generate_support_phrase()
    assert len(phrase) <= 60, "Support phrase should not exceed 60 words"
    
def test_generate_support_phrase_non_empty():
    phrase = generate_support_phrase()
    assert phrase.strip() != "", "Support phrase should not be empty"