# importing the required module
import matplotlib.pyplot as plt
from math import sqrt
from constants import(
    TOKEN1,
    TOKEN2,
    ORIGINAL_BLOCK
)


def plot_spot_price(L1, L2):
    X1 = []
    Y1 = []
    for t in L1:
        X1.append(t["block"])
        Y1.append(t[TOKEN2] / t[TOKEN1])
    X2 = []
    Y2 = []
    for t in L2:
        X2.append(t["block"])
        Y2.append(t[TOKEN2] / t[TOKEN1])
    plt.figure(1)
    plt.step(X1, Y1, where="post")
    plt.step(X2, Y2, where="post")

    # naming the x axis
    plt.xlabel("block number")
    # naming the y axis
    plt.ylabel("spot price")

    # giving a title to my graph
    plt.title("Spot price over blocks")

    # function to show the plot


def plot_invariant_over_blocks(L):
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    for t in L:
        block = t["block"]
        if block < ORIGINAL_BLOCK:
            X1.append(block)
            invariant = sqrt((t[TOKEN2] / 10**18) * (t[TOKEN1] / 10**18))
            Y1.append(invariant)
        else:
            X2.append(block)
            invariant = sqrt((t[TOKEN2] / 10**18) * (t[TOKEN1] / 10**18))
            Y2.append(invariant)
    plt.figure(2)
    plt.step(X1, Y1, where="post")
    plt.xlabel("block number")
    plt.ylabel("invariant")
    plt.title("CoW-AMM Invariant over blocks before liquidity injection")
    plt.figure(3)
    plt.step(X2, Y2, where="post")
    plt.xlabel("block number")
    plt.ylabel("invariant")
    plt.title("CoW-AMM Invariant over blocks after liquidity injection")
