#!/usr/bin/env python3
"""
Veil - Maximum Anonymity Suite
Entry point for the CLI.
"""
import typer
from rich.console import Console
from veil.core.orchestrator import Orchestrator

app = typer.Typer(help="Veil Anonymity Suite")
console = Console()

@app.command()
def start():
    """Start the full anonymity hardening workflow."""
    orch = Orchestrator()
    
    try:
        from veil.phases.phase0_system import Phase0System
        orch.register_phase(Phase0System)
    except ImportError:
        console.print("[yellow]Warning: Phase 0 not found yet. Skipping.[/yellow]")
    
    orch.run()

@app.command()
def status():
    """Check current anonymity status."""
    console.print("[cyan]Status check coming soon...[/cyan]")

if __name__ == "__main__":
    app()
