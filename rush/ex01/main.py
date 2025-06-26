#!/usr/bin/env python3
from checkmate import checkmate
import sys


def main():
    board = """ """
    if len(sys.argv)> 1:
            file = open(sys.argv[1] , 'r')
            for line in file:
                board = board + line
    
    checkmate(board)

if __name__ == "__main__":
    main()
    