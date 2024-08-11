# lesson04/rplife/patterns.py
from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]
