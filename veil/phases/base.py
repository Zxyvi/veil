"""
Base class for all Veil phases.
"""
from abc import ABC, abstractmethod
from rich.console import Console

console = Console()

class BasePhase(ABC):
    def __init__(self, config, state):
        self.config = config
        self.state = state
        self.name = "Base Phase"

    @abstractmethod
    def run(self):
        """Execute the phase actions."""
        pass

    @abstractmethod
    def verify(self) -> bool:
        """Check if the phase was successful."""
        pass

    def confirm(self, message: str) -> bool:
        """Ask user for confirmation before proceeding."""
        response = input(f"\n[?] {message} (y/N): ").strip().lower()
        return response == 'y'
