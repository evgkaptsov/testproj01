# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:55:39 2026

@author: Group 17
"""

from NFA_to_DFA_coverter import NFA2DFAConverter
from FAFactory import FAFactory
from pathlib import Path



def main():
    # your code here
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "data" / "NFA01.json"
    
    nfa = FAFactory.from_file(file_path)
    print(nfa)
    
    #file_path = BASE_DIR / "data" / "NFA01.graphml"
    #nfa.save_to_dot(file_path)
    
    cvt = NFA2DFAConverter()
    DFA = cvt.convertNFA2DFA(nfa)
    print("Result: ", DFA)
    
    
    print("Done.")


if __name__ == "__main__":
    main()
