def generate_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def max_length_of_sequence_and_k(n):
    maxLen = 0
    kValue = 0
    for i in range(1, n+1):
        sequence = generate_sequence(i)
        currLen = len(sequence)
        if currLen > maxLen:
            maxLen = currLen
            kValue = i 
    return maxLen, kValue


def max_sequence_value_and_k(n):
    max_k = 0
    max_val = 0
    for k in range(1, n + 1):
        sequence = generate_sequence(k)
        max_val_k = max(sequence)
        if max_val_k > max_val:
            max_val = max_val_k
            max_k = k
    return max_val, max_k


num=98
n = int(num)
sequence = generate_sequence(n)
max_val, max_k = max_sequence_value_and_k(n)
max_length_of_sequence, k_value = max_length_of_sequence_and_k(n)
print(sequence)
print(max_length_of_sequence, k_value)
print(max_val, max_k)



def seq(n):
    sequ=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        sequ.append(n)
    return sequ



def max_len_of_seq_and_k(n):
    k_val=0
    max_len=0
    for i in range(1,n+1):
        sequ=seq(i)
        current_len=len(sequ)
        if current_len>max_len:
            max_len=current_len
            k_value=i
    return max_len,k_value


def max_sequ_of_val_and_k(n):
    max_val=0
    max_k=0
    for i in range(1,n+1):
        sequ=seq(i)
        max_val_k=max(sequ)
        if max_val<max_val_k:
            max_val=max_val_k
            max_k=i
    return max_val,max_k

num=98
n=int(num)
sequ=seq(n)
max_val,max_k=max_sequ_of_val_and_k(n)
max_len,max_k_value=max_len_of_seq_and_k(n)

print(sequ)

print(max_len,k_value)
print(max_val, max_k)



        
