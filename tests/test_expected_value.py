from viper import Viper


def test_single_strand_small():
    expected_value = 7.5826
    assert expected_value == Viper().compute_single_strand_score("GAG")


def test_double_strand_small():
    expected_value = 8.001100000000001
    assert expected_value == Viper().compute_double_strand_score("AAA")


def test_single_strand_long():
    expected_value = 6.627481849926326
    assert expected_value == Viper().compute_single_strand_score("GAGGAGGAGGAG")


def test_double_strand_long():
    expected_value = 6.8726712428436905
    assert expected_value == Viper().compute_double_strand_score("GAGGAGGAGGAG")
