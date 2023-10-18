import um

def test_count_single_um():
    assert um.count("hello, um, world") == 1

def test_count_multiple_um():
    assert um.count("um, um, um, um") == 4

def test_count_mixed_case():
    assert um.count("Um, uM, UM, um") == 4

def test_count_no_um():
    assert um.count("yummy") == 0

def test_count_um_in_words():
    assert um.count("umbrella, forum, humble") == 0

def test_count_edge_cases():
    assert um.count("") == 0
    assert um.count("um") == 1
    assert um.count("umumum") == 0
    assert um.count("um um um") == 3

if __name__ == "__main__":
    test_count_single_um()
    test_count_multiple_um()
    test_count_mixed_case()
    test_count_no_um()
    test_count_um_in_words()
    test_count_edge_cases()
    print("All tests passed!")