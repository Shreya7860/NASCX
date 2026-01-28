# Network-Aware Semantic Communication for XR in 6G Networks

A 5G network simulation project using OMNeT++ 6.2.0, INET 4.5.4, and Simu5G 1.3.0. All frameworks are included and pre-configured for command-line use.

## Quick Start

### Prerequisites

- Linux system (Ubuntu/Debian recommended)
- GCC/G++ compiler
- Python 3.x
- Miniconda or Anaconda

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. **Install dependencies using Conda:**

```bash
# Create and activate environment
conda create -n omnetpp python=3.12
conda activate omnetpp

# Install build tools
conda install -c conda-forge bison flex python-devel
```

3. **Build OMNeT++:**

```bash
cd omnetpp-6.2.0
source setenv
./configure
make -j$(nproc)
cd ..
```

4. **Build INET:**

```bash
cd inet4.5
make makefiles
make MODE=release -j$(nproc)
cd ..
```

5. **Build Simu5G:**

```bash
cd simu5g-1.3.0
make makefiles
make MODE=release -j$(nproc)
cd ..
```

6. **Add OMNeT++ to your PATH:**

Add this line to your `~/.bashrc` (adjust path if needed):

```bash
echo 'source ~/path/to/YOUR_REPO_NAME/omnetpp-6.2.0/setenv' >> ~/.bashrc
source ~/.bashrc
```

## Usage

### Before Starting

Always activate the conda environment when working on this project:

```bash
conda activate omnetpp
```

### Running Simulations

Navigate to the Simu5G simulations directory:

```bash
cd simu5g-1.3.0/simulations
# Run your simulation scenarios here
```

### Running Examples

Test INET:
```bash
cd inet4.5/examples/inet/arp
./run
```

Test Simu5G:
```bash
cd simu5g-1.3.0/simulations
# Explore available examples
```

## Project Structure

```
.
├── omnetpp-6.2.0/       # OMNeT++ simulator (pre-configured for CLI)
├── inet4.5/             # INET Framework
├── simu5g-1.3.0/        # Simu5G (5G NR simulation)
│   └── simulations/     # Simulation scenarios
└── README.md
```

## Configuration Notes

- OMNeT++ has been pre-configured for command-line first usage
- Python bindings are disabled by default (can be enabled in `omnetpp-6.2.0/configure.user`)
- All frameworks are set up for release mode builds

## Troubleshooting

### Commands not found after terminal restart

Make sure you've added the setenv line to `~/.bashrc` and sourced it:
```bash
source ~/.bashrc
```

### Build errors

Ensure your conda environment is activated:
```bash
conda activate omnetpp
```

Clean and rebuild if needed:
```bash
make clean && make makefiles && make
```

### Environment conflicts

If you have multiple package managers (conda, nix, etc.), make sure only conda is active:
```bash
conda deactivate  # deactivate all
conda activate omnetpp  # activate only omnetpp env
```

## Useful Commands

```bash
# Check OMNeT++ version
opp_run --version

# Rebuild from scratch
make clean && make makefiles && make

# Run in debug mode
make MODE=debug

# Launch IDE (optional)
omnetpp
```

## Version Information

| Component | Version |
|-----------|---------|
| OMNeT++ | 6.2.0 |
| INET | 4.5.4 |
| Simu5G | 1.3.0 |
| Python | 3.12 |

## References

- [OMNeT++ Documentation](https://docs.omnetpp.org/)
- [INET Framework](https://inet.omnetpp.org/)
- [Simu5G](https://simu5g.org/)

## License

Please refer to the individual licenses of OMNeT++, INET, and Simu5G.