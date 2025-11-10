"""Demonstrate enforcing a custom writing voice using repository instructions."""

from __future__ import annotations

import asyncio
from pathlib import Path

from agents import Agent, Runner


def build_dnp_instructions() -> str:
    """Load the DNP-specific writing instructions and exemplar text."""
    repo_root = Path(__file__).resolve().parents[2]
    instructions_path = repo_root / "dnp" / "AGENTS.md"
    exemplar_path = repo_root / "dnp" / "purpose_supporting_objectives.md"
    return (
        "You are a writing specialist supporting a Doctor of Nursing Practice student.\n"
        "Follow the APA 7 guidance and voice expectations from these house instructions.\n\n"
        f"{instructions_path.read_text()}\n\n"
        "Mirror the pacing, transitions, and citation usage from this exemplar section.\n\n"
        f"{exemplar_path.read_text()}\n"
        "Do not fabricate citations or patient details, and always write in full paragraphs."
    )


async def main() -> None:
    agent = Agent(
        name="DNP editor",
        instructions=build_dnp_instructions(),
    )
    result = await Runner.run(starting_agent=agent, input="Draft a project purpose paragraph.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
