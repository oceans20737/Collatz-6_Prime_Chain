#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT

"""
Verification Script for 6-adic Prime Chains
Author: Hiroshi Harada
Date: February 2026
License: MIT

This script verifies the primality and structure of a 6-adic prime chain
starting from a given initial value n₀. It prints each step of the chain,
the applied constant k, and whether the number is prime.

Usage:
    python verify_6adic_chain.py
"""

import sympy

def get_next_6adic_custom(n):
    """
    Computes the next value in the 6-adic sequence.
    Returns the next number and the constant k used (as a string).
    """
    rem = n % 12
    if rem == 1:
        return (7 * n - 1) // 6, "-1"
    elif rem == 5:
        return (7 * n - 5) // 6, "-5"
    elif rem == 7:
        return (7 * n + 5) // 6, "+5"
    elif rem == 11:
        return (7 * n + 1) // 6, "+1"
    return None, None  # Invalid case (not divisible by 6)

def verify_6adic_chain(n0, max_steps=100):
    """
    Verifies the primality and structure of a 6-adic prime chain starting from n₀.
    Prints each step and returns the verified chain.
    """
    print(f"\n=== Verifying 6-adic Prime Chain from n₀ = {n0} ===")
    curr = n0
    chain = []

    for i in range(1, max_steps + 1):
        if not sympy.isprime(curr):
            print(f"Step {i}: {curr} → COMPOSITE — Chain Broken")
            break

        print(f"Step {i}: {curr} → PRIME")
        chain.append(curr)

        nxt, k_used = get_next_6adic_custom(curr)
        if nxt is None:
            print(f"  [ Invalid step: n mod 12 = {curr % 12} not in {{1,5,7,11}} ]")
            break
        print(f"    [ Applied k = {k_used} → Next = {nxt} ]")
        curr = nxt

    print(f"\nFinal Result: Verified chain of length {len(chain)}")
    print(f"Chain: {chain}\n")
    return chain

if __name__ == "__main__":
    # Example L8 chain discovered in 6-adic system
    discovery = 1099687
    length = 8
    verify_6adic_chain(discovery, length)


# In[ ]:




