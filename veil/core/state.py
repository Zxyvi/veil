"""
State management for the current Veil session.
"""
from typing import Optional, Dict, Any

class SessionState:
    def __init__(self):
        self.current_phase: int = -1
        self.is_anonymized: bool = False
        self.tor_connection: Optional[bool] = None
        self.current_fingerprint: Optional[Dict[str, Any]] = None
        self.browser_process: Optional[Any] = None
        self.metadata: Dict[str, Any] = {}

    def reset(self):
        """Clear session data for a fresh start."""
        self.__init__()
