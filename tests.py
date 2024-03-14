def test_list_element_exists():
    input = [1, 2, 3, 4]
    assert 2 in input

def test_list_is_triplet():
    input = [1, 2, 3]
    assert len(input) == 3

def test_list_subset_not_includes():
    input = [1, 2, 3, 4, 5]
    subset = [7, 8, 9]
    assert subset not in input

def test_set_methods():
    input = {1, 2, 3, 4}
    input.add(5)
    input.remove(2)
    assert input == {1, 3, 4, 5} 

def test_set_elements_not_exists():
    input = {1, 2, 3, 4}
    try:
        assert set(range(1, 6)) == input
    except AssertionError:
        pass