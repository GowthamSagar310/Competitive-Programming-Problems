for _ in range(int(input())):
    rating = int(input())
    
    # For Division 1: 1900≤rating
    # For Division 2: 1600≤rating≤1899
    # For Division 3: 1400≤rating≤1599
    # For Division 4: rating≤1399

    if rating <= 1399:
        print("Division 4")
    elif rating <= 1599:
        print("Division 3")
    elif rating <= 1899:
        print("Division 2")
    else:
        print("Division 1")