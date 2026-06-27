"""
Phase 0: System Hardening
- Updates packages
- Disables telemetry (Ubuntu/Debian specific)
- Checks firewall status
"""
import subprocess
import sys
from veil.phases.base import BasePhase
from rich.console import Console

console = Console()

class Phase0System(BasePhase):
    def __init__(self, config, state):
        super().__init__(config, state)
        self.name = "System Hardening"

    def run(self):
        console.print("[*] Updating system packages...")
        subprocess.run(["sudo", "apt", "update"], check=False)
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=False)

        try:
            subprocess.run(["sudo", "systemctl", "stop", "apport"], check=False)
            subprocess.run(["sudo", "systemctl", "disable", "apport"], check=False)
            console.print("[green]✓ Telemetry services (apport) disabled.[/green]")
        except:
            console.print("[yellow]⚠ Could not disable telemetry (not critical on Parrot).[/yellow]")

        console.print("[*] Ensuring UFW is installed...")
        subprocess.run(["sudo", "apt", "install", "ufw", "-y"], check=False)
        subprocess.run(["sudo", "ufw", "enable"], check=False)

    def verify(self) -> bool:
        result = subprocess.run(["sudo", "ufw", "status"], capture_output=True, text=True)
        if "Status: active" in result.stdout:
            console.print("[green]✓ Firewall is active.[/green]")
            return True
        else:
            console.print("[red]✗ Firewall is not active.[/red]")
            return False
