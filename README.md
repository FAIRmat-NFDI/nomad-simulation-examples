# nomad-simulation-examples

Example uploads plugin for NOMAD that ships separate datasets for ORCA, GROMACS, and VASP. Install in editable mode and enable NOMAD plugins to expose the entries under **Uploads → Add example uploads**.

## Usage

```bash
pip install -e .
```

Then restart NOMAD so the following entries appear as individual example uploads:

- ORCA: small molecular tests
- GROMACS: MD test systems
- VASP: DFT bulk and surfaces

All example data lives in `src/nomad_simulation_examples/example_uploads/` for easy extension to more codes.
