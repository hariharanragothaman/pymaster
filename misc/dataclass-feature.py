"""
A data class is effectively a class whose sole purpose is
to literally hold data. The class will have variables that can be
accessed and written to, but there is no extra logic on top of it.
"""

from dataclasses import dataclass


@dataclass
class Vector3D:
    x: int
    y: int
    z: int


u = Vector3D(1, 1, -1)
print(u)
