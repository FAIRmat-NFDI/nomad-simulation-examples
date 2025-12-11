"""Example upload entry points for various simulation codes."""

from nomad.config.models.plugins import ExampleUploadEntryPoint

orca_examples = ExampleUploadEntryPoint(
    title="ORCA: small molecular tests",
    category="Simulation examples",
    description=(
        "Example ORCA calculations for testing NOMAD parser and schema integration."
    ),
    resources=["example_uploads/orca/*"],
)

gromacs_examples = ExampleUploadEntryPoint(
    title="GROMACS: MD test systems",
    category="Simulation examples",
    description=(
        "Example GROMACS MD setups for testing topology, trajectories, and MD workflows."
    ),
    resources=["example_uploads/gromacs/*"],
)

vasp_examples = ExampleUploadEntryPoint(
    title="VASP: DFT bulk and surfaces",
    category="Simulation examples",
    description=(
        "Example VASP calculations for testing DFT workflows and parsing functionality."
    ),
    resources=["example_uploads/vasp/*"],
)

__all__ = [
    "orca_examples",
    "gromacs_examples",
    "vasp_examples",
]
