#!/usr/bin/env python3
"""Legacy Code Bingo Generator - Because finding bugs should feel like winning!"""

import random
import sys
from pathlib import Path

def generate_bingo_card():
    """Creates a bingo card so beautiful it almost makes you forget the code."""
    patterns = [
        "Magic Number > 42",
        "Function > 100 lines",
        "TODO from 2012",
        "Comment says 'fix later'",
        "Global variable abuse",
        "Copy-paste code",
        "Nested if > 3 levels",
        "Unused imports",
        "Hardcoded credentials",
        "God object detected",
        "Stringly typed logic",
        "Recursive without base case",
        "Catch-all Exception",
        "Commented-out code blocks",
        "Function does 5+ things",
        "Inconsistent naming",
        "No error handling",
        "Reinvents standard library",
        "Mystery boolean flags",
        "Over-optimized premature",
        "Dead code walking",
        "Circular imports dance",
        "Configuration in code",
        "Not invented here syndrome",
        "FREE SPACE - You're already losing"
    ]
    
    # Shuffle and pick 24 (plus FREE SPACE makes 25)
    random.shuffle(patterns)
    card = patterns[:24]
    card.insert(12, "FREE SPACE - You're already losing")  # Center square
    
    return [card[i*5:(i+1)*5] for i in range(5)]

def print_card(card):
    """Prints your ticket to developer despair."""
    print("\n" + "="*50)
    print("LEGACY CODE BINGO - Mark when found!")
    print("="*50 + "\n")
    
    for row in card:
        print("| " + " | ".join(f"{item:<30}" for item in row) + " |")
        print("-"*50)
    
    print("\nRules: First to 5 in a row wins... or loses? Same thing really.\n")

def main():
    """Main function - because even legacy tools need structure."""
    print("\n🎲 Generating your Legacy Code Bingo card...")
    print("📋 Print and take to your next code review!\n")
    
    card = generate_bingo_card()
    print_card(card)
    
    # Optional: Save to file
    save = input("Save to bingo_card.txt? (y/n): ").lower()
    if save == 'y':
        with open('bingo_card.txt', 'w') as f:
            f.write("LEGACY CODE BINGO CARD\n")
            f.write("="*50 + "\n")
            for row in card:
                f.write("| " + " | ".join(row) + " |\n")
                f.write("-"*50 + "\n")
        print("✅ Saved! Now go find some anti-patterns!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())