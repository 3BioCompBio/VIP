import math
import numpy as np
from pathlib import Path
from viper.utils import reverse_complement
import typing as t


class Viper:
    def __init__(self, vip_values_path: Path = None) -> None:
        self.vip_values: t.Dict[str, float] = self.load_vip_value(
            vip_values_path
            or Path(__file__).parent.resolve() / "ressources" / "Vipvalues.csv"
        )

    def compute_score(self, input_seq: str, double_strand: bool = False) -> np.float64:
        if double_strand:
            return self.compute_double_strand_score(input_seq=input_seq)
        return self.compute_single_strand_score(input_seq=input_seq)

    def compute_single_strand_score(self, input_seq: str) -> np.float64:
        self.validate_input(input_seq=input_seq)
        if len(input_seq) < 6:
            return np.float64(self.vip_values[input_seq])
        nb_chunck = len(input_seq) - 3
        results, factors = np.zeros(nb_chunck, float), np.zeros(nb_chunck, float)
        for i in range(nb_chunck):
            factors[i] = pow(len(input_seq) - i, 2) / (pow(len(input_seq) - i, 2) - 2)
            results[i] = (
                math.factorial(nb_chunck - 1)
                / (math.factorial(i) * math.factorial(nb_chunck - i - 1))
                * pow(0.4009940, nb_chunck - 1 - i)
                * pow(1 - 0.4009940, i)
                * self.vip_values[input_seq[i : i + 4]]
            )
        return (
            8.34424 * np.exp(0.56074 * (pow(len(input_seq), -0.145481) - 1))
            + np.prod(factors) * np.sum(results)
            - np.prod(factors)
            * 8.34424
            * np.exp(0.56074 * (pow(len(input_seq) - nb_chunck + 1, -0.145481) - 1))
        )

    def compute_double_strand_score(self, input_seq: str) -> np.float64:
        return (
            self.compute_single_strand_score(input_seq=input_seq)
            + self.compute_single_strand_score(input_seq=reverse_complement(input_seq))
        ) / 2

    @staticmethod
    def validate_input(input_seq: str) -> None:
        if len(input_seq) == 0:
            raise ValueError("The input sequence is empty")
        if any(n not in ["A", "C", "G", "T", "M"] for n in input_seq):
            raise ValueError(
                "The sequence should contains only standard characters for nucleotides : "
                "C (Cytosine), G (Guanine), A (Adenine), T (Thymine), M (5-Methylcytosine))"
            )

    @staticmethod
    def load_vip_value(vip_value_path: Path) -> t.Dict[str, float]:
        data = {}
        with open(vip_value_path, "r") as f:
            for line in f:
                values = line.strip().split(",")
                data[values[0]] = float(values[1])
        return data
