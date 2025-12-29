#!/usr/bin/env python3
import sys
import yaml
from pathlib import Path

REQUIRED_DEVICE_FIELDS = {'id', 'role', 'platform', 'mgmt_ip'}

def validate_devices(devices):
  for device in devices:
    missing = REQUIRED_DEVICE_FIELDS - device.keys()
    if missing:
      raise ValueError(f"Device {device.get('id', 'unknown')} missing fields: {missing}")

def main():
  path = Path('topology/topology.yaml')
  if not path.exists():
    print('topology.yaml not found', file=sys.stderr)
    sys.exit(1)

  data = yaml.safe_load(path.read_text())
  devices = data.get('devices', [])
  if not devices:
    print('No devices defined', file=sys.stderr)
    sys.exit(1)

  validate_devices(devices)
  print('Topology validation passed')

if __name__ == '__main__':
  main()
