#!/usr/bin/env python3
import yaml
from pathlib import Path

topology_path = Path('topology/topology.yaml')
targets_path = Path('monitoring/prometheus/targets/targets.yaml')

topology = yaml.safe_load(topology_path.read_text())
icmp_targets = [entry['host'] for entry in topology.get('targets', {}).get('icmp', [])]

payload = [
    {
        'labels': {'env': 'generated'},
        'targets': icmp_targets,
    }
]

targets_path.write_text(yaml.dump(payload))
print(f"Wrote {len(icmp_targets)} targets to {targets_path}")
