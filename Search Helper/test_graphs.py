graph2 = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 3), ("D", 2)],
    "B": [("G", 5)],
    "C": [("E", 5)],
    "D": [("F", 0), ("G", 3)],
    "E": [("G", 5)],
    "F": [],
    "G": []
}

graph3 = {
    "S": [("D", 6), ("B1", 9), ("A", 5)],
    "A": [("G1", 9), ("B2", 3)],
    "B1": [],
    "B2": [("C2", 3)],
    "C": [("F", 7), ("G2", 5)],
    "C2": [],
    "D": [("E", 2), ("C", 2)],
    "E": [("G3", 7)],
    "F": [],
    "G1": [],
    "G2": [],
    "G3": []
}

graphT1 = {
    'A': [('B', 20), ('D', 80), ('G', 95)],
    'B' : [('E', 50), ('F', 10)],
    'C' : [('D', 50), ('H', 20)],
    'D' : [('G', 10)],
    'F' : [('D', 40), ('C', 10)],
    'G' : [],
    'H' : []
}

heurist_graphT1 = {
    'A': 90,
    'B': 55,
    'C': 55,
    'D': 8,
    'E': 100,
    'F': 45,
    'G': 0,
    'H': 100
}

graphT2 = {    
    'A' : [('Z', 75), ('T', 118), ('S', 140)],
    'B' : [('G', 90), ('U', 85), ('P', 101), ('F', 211)],
    'C' : [('P', 138), ('R', 146), ('D', 120)],
    'D' : [('M', 75), ('C', 120)],
    'E' : [('H', 86)],
    'F' : [('S', 99), ('B', 211)],
    'G' : [('B', 90)],
    'H' : [('U', 98), ('E', 86)],
    'I' : [('N', 87), ('V', 92)],
    'L' : [('T', 111), ('M', 70)],
    'M' : [('L', 70), ('D', 75)],
    'N' : [('I', 87)],
    'O' : [('Z', 71), ('S', 151)],
    'P' : [('R', 97), ('B', 101), ('C', 138)],
    'R' : [('S', 80), ('P', 97), ('C', 146)],
    'S' : [('A', 140), ('O', 151), ('R', 80)],
    'T' : [('A', 118), ('L', 70)],
    'U' : [('B', 85), ('H', 98), ('V', 142)],
    'V' : [('I', 92), ('U', 142)],
    'Z' : [('A', 75), ('O', 71)]
}

heurist_graphT2 = {
    'A': 366,
    'B': 0,
    'C': 160,
    'D': 242,
    'E': 161,
    'F': 176,
    'G': 77,
    'H': 151,
    'I': 226,
    'L': 224,
    'M': 241,
    'N': 234,
    'O': 380,
    'P': 100,
    'R': 193,
    'S': 253,
    'T': 329,
    'U': 80,
    'V': 199,
    'Z': 374
}

tutorial2_graph = {
    "A": [("B", 20), ("D", 80), ("G", 95)],
    "B": [("E", 50), ("F", 10)],
    "C": [("H", 20), ("D", 50)],
    "D": [("G", 10)],
    "E": [], #Empty
    "F": [("C", 10), ("D", 40)],
    "G": [], #Empty
    "H": [] #Empty
}

tutorial3_graph = {
    "A": [("Z", 75), ("T", 118), ("S", 140)],
    "B": [("P", 101), ("F", 211), ("G", 90), ("U", 85)],
    "C": [("D", 120), ("R", 146), ("P", 138)],
    "D": [("M", 75), ("C", 120)],
    "E": [("H", 86)],
    "F": [("S", 99), ("B", 211)],
    "G": [("B", 90)],
    "H": [("U", 98), ("E", 86)],
    "I": [("V", 92)],
    "J": [], # Empty -
    "K": [], # Empty -
    "L": [("M", 70), ("T", 111)],
    "M": [("D", 75), ("L", 70)],
    "N": [("I", 87)],
    "O": [("Z", 71), ("S", 151)],
    "P": [("R", 97), ("C", 138), ("B", 101)],
    "Q": [], # Empty -
    "R": [("S", 80), ("C", 148), ("P", 97)], # C-146?
    "S": [("O", 151), ("A", 140), ("R", 80), ("F", 99)],
    "T": [("A", 118), ("L", 111)],
    "U": [("B", 85), ("H", 98), ("V", 142)],
    "V": [("I", 92), ("U", 142)],
    "W": [], # Empty -
    "X": [], # Empty -
    "Y": [], # Empty -
    "Z": [("O", 71), ("A", 75)]
}

tutorial3_heuristics = {
    "A": 366,
    "B": 0,
    "C": 160,
    "D": 242,
    "E": 161,
    "F": 176,
    "G": 77,
    "H": 151,
    "I": 226,
    "L": 244,
    "M": 241,
    "N": 234,
    "O": 380,
    "P": 100,
    "R": 193,
    "S": 253,
    "T": 329,
    "U": 80,
    "V": 199,
    "Z": 374
}

midsem_graph = {
    "A": [("E", 40), ("D", 5), ("F", 20)],
    "B": [("G", 15)],
    "C": [("G", 40), ("B", 10)],
    "D": [("C", 10)],
    "E": [("B", 10)],
    "F": [("B", 60), ("J", 15)],
    "G": [],
    "H": [("D", 10)],
    "J": [("H", 10)]
}