## Student Name: Arnav Gupta
## Student ID: 219973452

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied
    given limited capacities.
    """

    # Validate resource capacities
    for r_name, cap in resources.items():
        if cap < 0:
            return False

    # Track usage
    usage = {r: 0 for r in resources}

    # Process each request
    for req in requests:

        # NEW: structural validation
        if not isinstance(req, dict):
            raise ValueError("Each request must be a dictionary")

        # Check unknown resources
        for r_name in req:
            if r_name not in resources:
                return False

        # Check negative amounts
        for amount in req.values():
            if amount < 0:
                return False

        # Accumulate resource usage
        for r_name, amount in req.items():
            usage[r_name] += amount

            # Check capacity violation
            if usage[r_name] > resources[r_name]:
                return False

    return True
