# How to Run XR Simulations

## Quick Start

Navigate to the simulation directory:
```bash
cd simu5g-1.3.0/simulations/NR/xr
```

## Available Configurations

### 1. Single User (Baseline)
```bash
simu5g -r 0 -m -u Cmdenv -c XR-DL-SingleUser omnetpp.ini
```
- **Description**: Single UE receiving XR traffic
- **Scheduler**: Proportional Fair (PF)
- **Expected frames**: 390
- **Use case**: Baseline performance testing

### 2. Multi-User with Proportional Fair
```bash
simu5g -r 0 -m -u Cmdenv -c XR-DL-MultiUser-PF omnetpp.ini
```
- **Description**: Multiple UEs with PF scheduler
- **Scheduler**: Proportional Fair (PF)
- **Number of users**: Configurable (default: varies)

### 3. Multi-User with MaxCQI
```bash
simu5g -r 0 -m -u Cmdenv -c XR-DL-MultiUser-MaxCQI omnetpp.ini
```
- **Description**: Multiple UEs with MaxCQI scheduler
- **Scheduler**: MaxCQI (prioritizes best channel quality)
- **Number of users**: Configurable

### 4. User Sweep
```bash
simu5g -r 0 -m -u Cmdenv -c XR-DL-UserSweep omnetpp.ini
```
- **Description**: Sweep across different numbers of users
- **Use case**: Scalability testing

## Command Line Options

### Override Parameters
```bash
# Change deadline
simu5g -r 0 -m -u Cmdenv -c XR-DL-SingleUser --*.ue[*].app[0].deadlineMs=5ms omnetpp.ini

# Change number of UEs
simu5g -r 0 -m -u Cmdenv -c XR-DL-MultiUser-PF --*.numUe=5 omnetpp.ini

# Change traffic file
simu5g -r 0 -m -u Cmdenv -c XR-DL-SingleUser --*.server.app[0].pcaFile=\"pca_selected.csv\" omnetpp.ini
```

### Run Multiple Iterations
```bash
# Run iterations 0-9
simu5g -r 0..9 -m -u Cmdenv -c XR-DL-SingleUser omnetpp.ini
```

### GUI Mode (for debugging)
```bash
simu5g -r 0 -c XR-DL-SingleUser omnetpp.ini
```

## Traffic Data Files

- **`ModelC_results.csv`**: ModelC compression data (390 frames, ~60 KB mean size)
- **`pca_selected.csv`**: PCA compression data (1074 frames, ~60 KB mean size)
- **`xr_traffic_30mbps.csv`**: Custom traffic profile

## Output

Results are printed to stdout at the end of simulation:
- **QoE Summary**: Per-user statistics
- **Global Summary**: Aggregated statistics across all users
- **CSV files**: `results/user_*_stats.csv` (if enabled)

## Common Issues

### All frames lost (0% delivery)
- **Cause**: Frame sizes too large for network capacity
- **Solution**: Use scaled traffic data (ModelC_results.csv or pca_selected.csv)

### Socket not open errors
- **Cause**: Application start timing issues
- **Solution**: Check `startTime` parameter in omnetpp.ini

## Configuration Details

See `omnetpp.ini` for full parameter descriptions:
- **NR-XR-Base**: Base configuration (inherited by all)
- **XR-MultiUser-Base**: Base for multi-user scenarios
