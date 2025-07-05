from cards import draw_cards

def test_draw_cards():
    cards = draw_cards(3)
    assert len(cards) == 3
    assert all("title" in card for card in cards)
    assert all("emoji" in card for card in cards)
    assert all("description" in card for card in cards)

def test_draw_cards_empty():
    cards = draw_cards(0)
    assert len(cards) == 0
    assert all("title" not in card for card in cards)
    assert all("emoji" not in card for card in cards)
    assert all("description" not in card for card in cards)

def test_draw_cards_unique():
    cards = draw_cards()
    titles = [card['title'] for card in cards]
    assert len(set(titles)) == len(titles)