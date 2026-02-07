from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

from english_ia.utilities import load_data, save_current_agent, load_system
from english_ia.agents import groqAgent, cerebrasAgent, geminiAgent

import sys
import pyperclip

agents = [groqAgent, cerebrasAgent, geminiAgent]

console = Console()

data = load_data()
current_agent = data["current_agent"]

# Cambiar al siguiente agente
def next_agent():
    global current_agent
    current_agent = (current_agent + 1) % len(agents)
    save_current_agent(current_agent)
    return agents[current_agent]

# Mostrar agentes
def show_agents():
    for agent in agents:
        print(agent)

# Preguntar a los agentes y generar chunks
def ask_agents(question, system):
    agent = next_agent()
    for chunk in agent.generate(question, system):
        yield chunk

def main():

    if len(sys.argv) < 1:
        console.print("[red]Error: usa 'ing ...'[/red]")
        return

    console.print("\n")
    question = f"Pregunta: {' '.join(sys.argv[2:])}"

    full_text = ""

    with Live("", refresh_per_second=4, console=console) as live:
        for chunk in ask_agents(question, load_system()):
            full_text += chunk
            live.update(Markdown(full_text))

    console.print("\n")
