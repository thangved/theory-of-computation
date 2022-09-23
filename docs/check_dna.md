# Check DNA

```py
import itertools


def check_dna(dna_string=''):
    symbol_list = ['A', 'C', 'G', 'T']
    codon_list = [''.join(el) for el in itertools.permutations(symbol_list, 3)]
    codon_start_list = ['ATG']
    codon_end_list = ['TAA', 'TAG', 'TGA']

    dna_list = []

    i = 0
    while i < len(dna_string):
        dna_list.append(dna_string[i:i + 3])
        i += 3

    if not dna_list[0] in codon_start_list:
        return False

    if not dna_list[len(dna_list) - 1] in codon_end_list:
        return False

    i = 1
    while i < len(dna_list) - 1:
        if not dna_list[i] in codon_list:
            return False
        i += 1

    return True


dna_str = str(input('Nhập chuỗi DNA cần kiểm tra: '))

if check_dna(dna_str):
    print("Chuỗi DNA \"%s\" hợp lệ" % dna_str)
else:
    print("Chuỗi DNA \"%s\" không hợp lệ" % dna_str)
```

