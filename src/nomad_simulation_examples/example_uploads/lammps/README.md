# LAMMPS Example Simulations

This directory contains example LAMMPS simulation data for testing and demonstration purposes.

## Example Systems

| System Name | Path | LAMMPS Version | Description |
|-------------|------|----------------|-------------|
| 1-Methylnaphthalene | `atomistic_parser_tests/1_methyl_naphthalene/` | LAMMPS (14 May 2016) | Organic molecule simulation |
| 1 XYZ Files Test | `atomistic_parser_tests/1_xyz_files/` | LAMMPS (12 Dec 2018) | Single XYZ trajectory output format test |
| 2 XYZ Files Test | `atomistic_parser_tests/2_xyz_files/` | LAMMPS (12 Dec 2018) | Multiple XYZ files output format test |
| Hexane-Cyclohexane | `atomistic_parser_tests/hexane_cyclohexane/` | LAMMPS (14 May 2016) | Binary mixture system with LAMMPSTRJ format |
| Methane DCD | `atomistic_parser_tests/methane_dcd/` | LAMMPS (14 May 2016) | Methane system with DCD trajectory format |
| Methane XYZ | `atomistic_parser_tests/methane_xyz/` | LAMMPS (14 May 2016) | Methane system with XYZ trajectory format |
| Polymer Melt - Minimization | `atomistic_parser_tests/polymer_melt/Emin/` | LAMMPS (12 Dec 2018) | Energy minimization of polymer melt |
| Polymer Melt - Equilibration | `atomistic_parser_tests/polymer_melt/Equil/` | LAMMPS (12 Dec 2018) | Equilibration run of polymer melt with restraints |
| Peptide | `peptide/` | LAMMPS (12 Dec 2018) | Peptide simulation example |

## Directory Structure

```
lammps/
├── atomistic_parser_tests/
│   ├── 1_methyl_naphthalene/      # Single molecule organic system
│   ├── 1_xyz_files/                # Parser test for single XYZ output
│   ├── 2_xyz_files/                # Parser test for multiple XYZ outputs
│   ├── hexane_cyclohexane/         # Binary mixture with LAMMPSTRJ
│   ├── methane_dcd/                # DCD trajectory format test
│   ├── methane_xyz/                # XYZ trajectory format test
│   └── polymer_melt/
│       ├── Emin/                   # Minimization step
│       └── Equil/                  # Equilibration step with restraints
└── peptide/                        # Peptide example system
```

## File Types

The examples include various LAMMPS output formats:
- `.data` - LAMMPS data files (atomic coordinates, topology)
- `.in` - LAMMPS input scripts
- `log.*` - LAMMPS log files containing thermodynamic output
- `.lammpstrj` - LAMMPS trajectory format
- `.xyz` - XYZ trajectory format
- `.dcd` - DCD binary trajectory format
- `.dump` - LAMMPS dump files

## Version Information

Two LAMMPS versions are represented:
- **LAMMPS (14 May 2016)**: Used for 1-methylnaphthalene, hexane-cyclohexane, and methane examples
- **LAMMPS (12 Dec 2018)**: Used for XYZ parser tests, polymer melt, and peptide examples

## Usage

These examples are used for:
1. Testing the NOMAD LAMMPS parser functionality
2. Validating different output format parsers (XYZ, DCD, LAMMPSTRJ)
3. Demonstrating various simulation types (minimization, equilibration, production runs)
4. Testing different thermo_style output formats
