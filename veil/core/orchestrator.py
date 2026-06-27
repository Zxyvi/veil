"""
Main orchestrator that runs the sequential anonymity workflow.
"""
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from veil.core.config import Config
from veil.core.state import SessionState

console = Console()

class Orchestrator:
    def __init__(self):
        self.config = Config()
        self.state = SessionState()
        self.phases = []

    def register_phase(self, phase):
        self.phases.append(phase)

    def run(self):
        console.print("[bold cyan]Veil[/bold cyan] - Maximum Anonymity Suite")
        console.print("Starting sequential lockdown...\n")

        for phase_class in self.phases:
            phase_instance = phase_class(self.config, self.state)
            
            console.rule(f"[bold yellow]Phase {self.state.current_phase + 1}: {phase_instance.name}[/bold yellow]")
            
            phase_instance.run()
            
            if not phase_instance.verify():
                console.print("[bold red]Verification failed![/bold red] Aborting for safety.")
                return False
                
            if not phase_instance.confirm("Phase complete. Proceed to next?"):
                console.print("[yellow]Paused by user.[/yellow]")
                return False
                
            self.state.current_phase += 1

        console.print("[bold green]✅ All phases complete. You are now fully anonymized.[/bold green]")
        return True
