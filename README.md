# Chilean Rutify

Chilean Rutify is a Python library that provides utilities for Chilean RUT (Rol Único Tributario) validation and manipulation.

## Installation

You can install Chilean Rutify via pip:

```bash
pip install chileanrutify
```

## Usage

You can directly use the utility methods provided by the library:

```python
from chileanrutify import normalize_rut, format_rut, valid_rut, valid_rut_verifier, valid_rut_values, get_verifier, dash_only_rut, classic_rut

# Example RUT: '36.408.368-8'
rut = '36408368-8'
chileanrutify.normalize_rut(rut)
# >>> "364083688"
chileanrutify.format_rut(rut)  # alias for chileanrutify.classic_rut(rut)
# >>> "36.408.368-8"
chileanrutify.format_rut(rut, 'dash_only')  # alias for chileanrutify.dash_only_rut(rut)
# >>> "36408368-8"
chileanrutify.format_rut(rut, 'normalized')  # alias for chileanrutify.normalize_rut(rut)
# >>> "364083688"
chileanrutify.valid_rut(rut)
# >>> True
chileanrutify.valid_rut_verifier(rut)
# >>> True
chileanrutify.valid_rut_values(rut)
# >>> True
rut = "36408368"
chileanrutify.get_verifier(rut)
# >>> "8"
```

# Development

After cloning the repository, set up your environment and run tests:

```bash
pip install -r requirements.txt
pytest
```

To install the library locally:

```bash
pip install .
```

To test the library in interactive Python prompt user:
```
python
```

# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/mihailpozarski/chilean-rutify-py. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/mihailpozarski/chilean-rutify-py/blob/master/CODE_OF_CONDUCT.md).

# License

The library is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

# Code of Conduct

Everyone interacting in the Chilean::Rutify project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/mihailpozarski/chilean-rutify-py/blob/master/CODE_OF_CONDUCT.md).