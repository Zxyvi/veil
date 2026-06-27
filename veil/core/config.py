"""
Configuration management for Veil.
"""
import os
import yaml
from pathlib import Path
from typing import Dict, Any

CONFIG_DIR = Path.home() / ".config" / "veil"
CONFIG_FILE = CONFIG_DIR / "config.yaml"

class Config:
    def __init__(self):
        self._data: Dict[str, Any] = {}
        self.load()

    def load(self):
        """Load config from disk, or create default."""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                self._data = yaml.safe_load(f) or {}
        else:
            self._data = self._get_defaults()
            self.save()

    def save(self):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(self._data, f)

    def _get_defaults(self) -> Dict[str, Any]:
        return {
            "kill_switch": True,
            "spoof_mac": True,
            "browser": {
                "engine": "chromiumfish",
                "user_data_dir": str(CONFIG_DIR / "browser_profiles")
            },
            "network": {
                "tor": True,
                "dns_over_https": True
            }
        }

    def get(self, key: str, default=None):
        keys = key.split('.')
        val = self._data
        for k in keys:
            if isinstance(val, dict):
                val = val.get(k)
            else:
                return default
        return val if val is not None else default
