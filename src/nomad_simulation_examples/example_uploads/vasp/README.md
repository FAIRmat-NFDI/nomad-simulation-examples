# VASP Example Test Suite

This directory contains a curated collection of 25 VASP calculation examples selected from the NOMAD repository to provide comprehensive test coverage for VASP parsing capabilities. The examples are designed to maximize diversity across multiple dimensions: authors, calculation types, structural types, and scientific domains.

## Selection Methodology

### Data Source
- **Base Population**: 10,000 VASP entries from NOMAD (owner: "visible")
- **Initial Sample**: 500 entries using main-author-diverse stratified sampling
- **Final Selection**: 25 entries maximizing both author diversity (25 unique authors) and workflow diversity (4 workflow types)

### Diversity Criteria
1. **Author Diversity**: Each example comes from a different research group/author to capture varying input conventions and computational practices
2. **Workflow Diversity**: Coverage of different calculation types (geometry optimization, single point, etc.)
3. **Structural Diversity**: Representation of different material types (bulk, surfaces, molecules, etc.)
4. **Property Diversity**: Various computed properties (electronic structure, energetics, etc.)

### Sample Composition
- **Authors**: 25 unique main authors (from 39 available in the 500-sample)
- **Workflow Types**: 4 distinct workflows represented
  - GeometryOptimization: 6 entries
  - single_point: 6 entries
  - geometry_optimization: 3 entries
  - SinglePoint: 1 entry
  - unspecified: 9 entries
- **Structural Types**:
  - bulk: 17 entries
  - unavailable: 6 entries
  - surface: 1 entry
  - molecule / cluster: 1 entry
- **Processing Status**: All entries successfully processed (processed=true)

## Organization Structure

This test suite uses a **property-based organization** (Option 3) that groups examples by their scientific/physics purpose. This approach helps users and developers quickly locate examples relevant to specific calculation types and makes test objectives transparent.

### Directory Layout

```
vasp/
├── electronic_structure/  # DOS, band structure calculations (18 entries)
├── structural_relaxation/  # Geometry optimization workflows (2 entries)
├── energetics/            # Single point energy calculations (5 entries)
└── dynamics/              # MD, phonons, trajectories (0 entries in current sample)
```

### Category Descriptions

#### `electronic_structure/`
Examples with computed electronic properties such as:
- Density of states (DOS)
- Band structure
- Electronic band gaps
- Orbital projections

**Purpose**: Tests parser capability to extract and normalize electronic structure data from VASP outputs (DOSCAR, EIGENVAL, etc.).

#### `structural_relaxation/`
Geometry optimization calculations including:
- Atomic position relaxation
- Cell optimization
- Convergence trajectories
- Force and stress tensor evolution

**Purpose**: Tests trajectory parsing, optimization convergence detection, and multi-step workflow handling.

#### `energetics/`
Single point energy calculations:
- Total energies
- Formation energies
- Static calculations at fixed geometries
- Unspecified workflows (often single points)

**Purpose**: Tests basic energy extraction and metadata parsing from fundamental VASP calculations.

#### `dynamics/`
Time-dependent simulations:
- Molecular dynamics (MD)
- Phonon calculations
- Trajectory data
- Vibrational frequencies

**Purpose**: Tests time-series data parsing, trajectory handling, and thermodynamic property extraction.

## Alternative Organizational Perspectives

While the current structure uses property-based organization, the test suite supports multiple conceptual views:

### By Workflow Type (Technical Focus)
- **GeometryOptimization** (9 entries): Multi-step relaxation workflows
- **SinglePoint** (7 entries): Static calculations
- **Unspecified** (9 entries): Parser-agnostic or legacy formats

*Use case*: Testing workflow-specific parsing logic and validation rules.

### By Complexity Level (Progressive Testing)
- **Basic** (~8 entries): Simple single points, standard bulk crystals
- **Intermediate** (~12 entries): Geometry optimization, DOS calculations
- **Advanced** (~3 entries): Complex workflows, surfaces, molecules
- **Edge Cases** (~2 entries): Unusual structures, unavailable structural types

*Use case*: Incremental test execution - verify basic parsing before testing complex scenarios.

### By Source/Provenance (Database Coverage)
Based on mainfile paths, entries originate from:
- **AFLOW library**: High-throughput database entries
- **OQMD**: Open Quantum Materials Database
- **Individual uploads**: User-contributed calculations
- **Materials Project**: Curated materials database

*Use case*: Identifying systematic parsing issues specific to certain data sources.

### By Material Dimensionality (Physical Classification)
- **3D bulk** (17 entries): Periodic crystals
- **2D surfaces** (1 entry): Slab geometries
- **0D molecules** (1 entry): Molecular systems
- **Unavailable/uncertain** (6 entries): Parser should handle gracefully

*Use case*: Testing dimension-specific normalization and topology detection.

### By Author/Research Group (Convention Diversity)
25 unique authors including:
- Bo Zhao, Stefano Curtarolo, Chris Wolverton
- Miguel Marques, Jan-Niclas Luy, Bjoern Bieniek
- And 19 others...

*Use case*: Ensuring parser robustness across different VASP input styles and conventions.

## Data Fields

Each entry in the test suite includes:
- `entry_id`: NOMAD entry identifier
- `upload_id`: Upload/dataset identifier
- `mainfile`: Path to primary VASP output file
- `main_author`: Primary author/contributor
- `structural_type`: Material dimensionality classification
- `workflow_name`: Calculation workflow type
- `method_name`: Computational method (typically "DFT")
- `available_properties`: List of computed properties in this entry
- `processed`: Processing status (all true in this sample)
- `processing_errors`: Any errors encountered during processing (all empty in this sample)

## Usage

### For Developers
Use this test suite to:
1. Validate VASP parser changes don't break existing functionality
2. Test new property extractors across diverse input styles
3. Benchmark parsing performance on real-world examples
4. Reproduce parsing issues by entry_id

### For Users
Browse examples to:
1. Find reference calculations similar to your use case
2. Understand what properties NOMAD can extract from VASP
3. Learn VASP → NOMAD metadata mapping
4. Identify gaps in current parser capabilities

## Reproducibility

The selection process is fully reproducible using:
- **Script**: `script_distinct_authors_vasp.py`
- **Entry Cap**: 10,000 VASP entries
- **Random Seed**: 123456
- **API Query**: `owner="visible"`, `program_name="VASP"`

Re-running the script will produce identical samples given the same NOMAD repository snapshot.

## Extending the Test Suite

To add new examples:
1. Ensure new entries increase diversity (different author, workflow, or edge case)
2. Place in appropriate category based on primary purpose
3. Update this README with new statistics
4. Consider if the new example represents a systematic gap (e.g., MD calculations)

## Notes

- **Dynamics folder is empty**: Current sample has no MD/phonon calculations, indicating potential gap in initial selection criteria
- **Workflow name variations**: Both CamelCase (GeometryOptimization) and snake_case (geometry_optimization) variants exist in NOMAD metadata
- **Processing status**: All examples are successfully processed, intentionally excluding failed/problematic entries for baseline validation tests
- **Available properties overlap**: Some entries have multiple properties (e.g., both DOS and geometry_optimization), categorized by primary purpose

## References

- Selection script: `query_nomad/script_distinct_authors_vasp.py`
- Diverse selection script: `select_diverse_25.py`
- Full 500-entry dataset: `sample_vasp_mainauthor_500.json`
- NOMAD API: https://nomad-lab.eu/prod/v1/api/v1/
