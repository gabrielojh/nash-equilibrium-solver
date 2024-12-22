import numpy as np

"""
Report:
1) What can you say about when you find a pure-strategy Nash equilibrium and when you do not?

Pure-strategy Nash equilibrium exists for all marginal costs c in the range [0, 30]. However, as c increases
(i.e., the marginal cost of production increases), the number of Nash equilibria decreases. For c = 0, there
are multiple Nash equilibria, but as c increases, the number of Nash equilibria decreases to one. This is
because the firms' profits decrease as the marginal cost of production increases, making it less likely for
both firms to produce the same quantity in equilibrium.

2) How do the Nash equilibria change in c, and how could you explain your finding?

As explained above, the number of Nash equilibria decreases as the marginal cost of production increases. This
is because the firms' profits decrease as the marginal cost increases, making it less likely for both firms to
produce the same quantity in equilibrium. When the marginal cost is low, firms can produce more at a lower cost,
leading to multiple Nash equilibria. However, as the marginal cost increases, firms' profits decrease, and they
lower their production to maximize profits, leading to fewer Nash equilibria.

Furthermore, for all c, each firm produces roughly the same quantity in equilibrium. This is follows the theory
of Cournot competition, where firms compete by choosing quantities simultaneously, and each firm assumes that the
other firm's quantity is fixed. As a result, the firms produce similar quantities in equilibrium, leading to a
Nash equilibrium.
"""


def PayoffMatrices(c):
    """
    Generates payoff matrices for two firms engaged in Cournot competition.

    This function computes the profit matrices for two firms based on the provided
    formula. The payoff matrix for Firm 1 is computed as follows:
    A(q1, q2) = (30 - q1 - q2) * q1 - c * q1
    The payoff matrix for Firm 2 is computed as follows:
    B(q2, q1) = (30 - q1 - q2) * q2 - c * q2

    Parameters:
    c (float): The marginal cost of production.

    Returns:
    tuple: A tuple containing two 21x21 numpy arrays (A, B), where:
        - A represents the payoff matrix for Firm 1.
        - B represents the payoff matrix for Firm 2.
    """
    n = 21
    # Initialize payoff matrices as 21x21 zero matrices
    A = np.zeros((n, n))  # Payoff matrix for Firm 1
    B = np.zeros((n, n))  # Payoff matrix for Firm 2

    for q1 in range(n):
        for q2 in range(n):
            A[q1, q2] = ((30 - q1 - q2) * q1) - (c * q1)  # Profit for Firm 1
            B[q2, q1] = ((30 - q1 - q2) * q2) - (c * q2)  # Profit for Firm 2

    return A, B


def NashEquilibrium(A, B, c):
    """
    Identifies and prints the pure strategy Nash equilibria for two firms in Cournot competition.

    This function takes two payoff matrices representing the profits of two firms and determines
    the strategy pairs (quantities produced by each firm) that form a Nash equilibrium. A strategy
    pair is a Nash equilibrium if neither firm can unilaterally improve their profit by deviating
    from their chosen strategy.

    Parameters:
    A (numpy.ndarray): Payoff matrix for Firm 1.
    B (numpy.ndarray): Payoff matrix for Firm 2.
    c (float): The marginal cost of production.

    Returns:
    None: Prints the Nash equilibria or a message indicating no equilibrium exists.
    """
    n = A.shape[0]
    equilibria = []

    for q1 in range(n):
        for q2 in range(n):
            # Check if (q1, q2) is a Nash equilibrium

            # By locking q2 (Firm 2's strategy q2), find if A[q1, q2] is the best response for Firm 1
            firm1_best_response = A[q1, q2] >= A[:, q2].max()

            # By locking q1 (Firm 1's strategy q1), find if B[q2, q1] is the best response for Firm 2
            firm2_best_response = B[q2, q1] >= B[:, q1].max()

            if firm1_best_response and firm2_best_response:
                equilibria.append((q1, q2))

    if equilibria:
        for eq in equilibria:
            print(
                f"For marginal cost c = {c}, the strategy profile (q1={eq[0]}, q2={eq[1]}) is a Nash equilibrium."
            )
    else:
        print(f"For marginal cost c = {c}, no pure strategy Nash equilibrium exists.")


def main():
    for c in range(31):
        print(f"Marginal cost c = {c}")
        print("-" * 30)
        A, B = PayoffMatrices(c)
        NashEquilibrium(A, B, c)
        print()
        print("=" * 30)
        print()


if __name__ == "__main__":
    main()
