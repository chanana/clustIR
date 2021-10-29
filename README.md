# <b>clust</b>ering Near <b>I</b>nfra<b>R</b>ed Spectra

<b>clusIR</b> allows you to:
1. Upload Bruker OPUS files (.0) containing near infra-red spectra
2. Calculate the Euclidean (or Cosine) distance between them
3. Download the final distance matrix

## Setup

Run `setup_env.sh` **or** the following set of commands

```bash
python3 -m venv .venv # setup venv

source .venv/bin/activate # activate it

pip install --upgrade pip wheel \
            black flake8 \ # formatting tools
            dash_bootstrap_components \
            plotly numpy pandas \
            brukeropusreader # install packages
```

## Notes on interpretation

1. Euclidean distances are the same as L2 norms and are referenced as such in the functions. <b>Larger number = more dissimilar samples</b>.
2. [Cosine scores](https://en.wikipedia.org/wiki/Cosine_similarity) are typically between `[-1, 1]`. <b>-1 means completely different and 1 means exactly the same</b>.