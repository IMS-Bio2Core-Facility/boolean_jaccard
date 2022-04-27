# boolean_jaccard

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI Version](https://img.shields.io/pypi/v/boolean_jaccard)](https://pypi.org/project/boolean_jaccard/)
[![Python Versions](https://shields.io/pypi/pyversions/boolean_jaccard)](https://shields.io/pypi/pyversions/boolean_jaccard)
[![CI/CD](https://github.com/IMS-Bio2Core-Facility/boolean_jaccard/actions/workflows/cicd.yaml/badge.svg)](https://github.com/IMS-Bio2Core-Facility/boolean_jaccard/actions/workflows/cicd.yaml)
[![codecov](https://codecov.io/gh/IMS-Bio2Core-Facility/boolean_jaccard/branch/main/graph/badge.svg?token=2TGYX69U3N)](https://codecov.io/gh/IMS-Bio2Core-Facility/boolean_jaccard)
[![Documentation Status](https://readthedocs.org/projects/boolean_jaccard/badge/?version=latest)](https://boolean_jaccard.readthedocs.io/en/latest/?badge=latest)
[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Codestyle: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Calculate Jaccard metrics for boolean values.

The source code lives on [github][github].

The documentation lives at [ReadTheDocs][readthedocs].

The project can be installed from [PyPI][pip].

## Abstract

The code here represents a python implementation of the Jaccard package hosted
[here][jaccard] by N. Chung. Its citation follows.

### Citation

Chung, N., Miasojedow, B., Startek, M., and Gambin, A. "Jaccard/Tanimoto similarity test and estimation methods for biological presence-absence data" _BMC Bioinformatics_ **(2019)** 20(Suppl 15): 644. https://doi.org/10.1186/s12859-019-3118-5

## Installation

It's a [PyPI][pip] package,
so the pocess is pretty straightforward:

```shell
pip install -U boolean_jaccard # for most recent version
pip install -U boolean_jaccard==0.0.1 # for a specific version
```

A list of all released versions can be found at our [tags][tags].

### A Note on Version Numbers

`boolean_jaccard` uses strict automated [semantic versioning][semver].
As such,
we guarantee bugfixes in path releases,
backwards compatible features in minor releases,
and breaking changes in major releases.
We will endeavour to avoid breaking changes where possible,
but,
should they occur,
they will _**only**_ be in major releases.

### Installing from Source

```{important}
Most users **will not need** these instructions.
```

If you need to customise the code in some manner,
you'll need to install from source.
To do that,
either clone the repository from github,
or download one of our releases.
For full instructions,
please see our guide on [contributing](./contributing.md).


## Contributing

Open-source software is only open-source becaues of the excellent community,
so we welcome any and all contributions!
If you think you have found a bug,
please log a report in our [issues][issues].
If you think you can fix a bug,
or have an idea for a new feature,
please see our guide on [contributing](./contributing.md)
for more information on how to get started!
While here,
we request that you follow our [code of conduct](./coc.md)
to help maintain a welcoming,
respectful environment.

## Future Developments

- [ ] Fully vectorise to improve performance.

## Citations

If you use `boolean_jaccard` in your work,
please cite the following manuscripts:

1. Chung, N., Miasojedow, B., Startek, M., and Gambin, A. "Jaccard/Tanimoto similarity test and estimation methods for biological presence-absence data" _BMC Bioinformatics_ **(2019)** 20(Suppl 15): 644. https://doi.org/10.1186/s12859-019-3118-5

[github]: https://github.com/IMS-Bio2Core-Facility/boolean_jaccard "Source Code"
[readthedocs]: http://boolean_jaccard.readthedocs.io/ "Documentation"
[pip]: https://pypi.org/project/boolean_jaccard/ "PyPI Package"
[jaccard]: https://github.com/ncchung/Jaccard
[semver]: https://semver.org "Semantic Versioning"
[tags]: https://github.com/IMS-Bio2Core-Facility/boolean_jaccard/releases "Releases"
[issues]: https://github.com/IMS-Bio2Core-Facility/boolean_jaccard/issues "Issues"
