# Find the cycle length of repeated modular multiplication

[Guide index](../README.md) · [Implementation](../../algorithm_lab/multiplicative_order.py)

## Reasoning

Starting from one, repeatedly multiply by an invertible residue modulo m. The first return to one gives its multiplicative order. Minimality matters: a later exponent that also returns one is a multiple of the order, not necessarily the order itself.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.multiplicative_order import multiplicative_order
>>> base, modulus = 3, 7
>>> order = multiplicative_order(base, modulus)
>>> order
6
>>> assert pow(base, order, modulus) == 1
>>> assert all(pow(base, exponent, modulus) != 1 for exponent in range(1, order))
>>> multiplicative_order(1, 19)
1

```

## Boundary to remember

The base must be coprime to the modulus. This direct educational search may perform many modular multiplications; it does not factor the group order to accelerate large cases.

## Practice exercise

Find the repetition period of a negative residue modulo nine and
inspect two complete cycles starting at one.

```pycon
>>> from algorithm_lab.multiplicative_order import multiplicative_order
>>> order = multiplicative_order(-2, 9)
>>> order
3
>>> residues = [pow(-2, exponent, 9) for exponent in range(7)]
>>> residues
[1, 7, 4, 1, 7, 4, 1]
>>> assert residues[1:order] == [7, 4]
>>> assert residues[:order] == residues[order : 2 * order]
>>> assert multiplicative_order(7, 9) == order

```

Negative two and seven represent the same residue, so their orders agree.
The initial one at exponent zero does not make the order zero; the order
is the first positive exponent that returns to one.
