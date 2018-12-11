# 2.1 Pairwise Sequence Alignment

- One of the most fundamental problems in bioinformatics: determine how "similar" a pair of biological sequences

- Applications of this problem:
    - Inferring the function or source organism of an unknown gene sequence
    - developing hypotheses about the relatedness of organisms, or grouping sequences from closely related organisms.

- An example:
    - 3 sequences: (r for reference; q for query)
        - `r1` 
        - `r2`
        - `q1` 
    - want to know if `q1` is more similar to `r1` or `r2`. 
    - Can use the **Hamming distance**
    - Check Hamming_Distance_Example.py