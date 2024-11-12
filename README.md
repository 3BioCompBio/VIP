Here there is the new python code relative to the paper "Estimating the vertical ionization potential of single-stranded DNA molecules" (M.Rooman and F. Pucci, submitted).

## Use the CLI

### Installation

```bash
git clone https://git@github.com/Benoitdw/vIPer.git
cd vIPer
pip install -r requirements.txt
```

### Usage

```bash
python cli.py ATCG # Single strand as default
# The vIP value (single strand) is 7.3156
python cli.py ATCG -D # Double strand
# The vIP value (double strand) is 7.2875
```

## Use as a library

### Installation

```bash
pip install "git+ssh://git@github.com/Benoitdw/vIPer.git"
```

OR

```bash
pip install "git+https://git@github.com/Benoitdw/vIPer.git"
```

### Usage

```python
from viper import Viper

# All these call will return 7.5826 as is it single strand
Viper().compute_score("GAC")
Viper().compute_score("GAC", double_strand=False)
Viper().compute_single_strand_score("GAC")


# All these call will return 7.5826 as is it double strand
Viper().compute_score("GAC")
Viper().compute_score("GAC", double_strand=True)
Viper().compute_double_strand_score("GAC")
```
