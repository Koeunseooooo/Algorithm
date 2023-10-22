import sys

input = sys.stdin.readline

op_dict = {
    "ADD": "00000",
    "ADDC": "00001",
    "SUB": "00010",
    "SUBC": "00011",
    "MOV": "00100",
    "MOVC": "00101",
    "AND": "00110",
    "ANDC": "00111",
    "OR": "01000",
    "ORC": "01001",
    "NOT": "01010",
    "MULT": "01100",
    "MULTC": "01101",
    "LSFTL": "01110",
    "LSFTLC": "01111",
    "LSFTR": "10000",
    "LSFTRC": "10001",
    "ASFTR": "10010",
    "ASFTRC": "10011",
    "RL": "10100",
    "RLC": "10101",
    "RR": "10110",
    "RRC": "10111",
}

n = int(input())
for _ in range(n):
    opcode, rd, ra, rb = input().strip().split()
    machine_code = ""
    machine_code += op_dict.get(opcode)
    machine_code += "0"

    machine_code += str(bin(int(rd)))[2:].zfill(3)
    machine_code += str(bin(int(ra)))[2:].zfill(3)

    if machine_code[4] == "0":
        machine_code += str(bin(int(rb)))[2:].zfill(3)
        machine_code += "0"
    else:
        machine_code += str(bin(int(rb)))[2:].zfill(4)

    print(machine_code)
