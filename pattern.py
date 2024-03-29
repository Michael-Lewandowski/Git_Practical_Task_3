'pattern.py'

"""
1. Set the total number of pattern lines to "9".
2. Determine the number of stars for each line
 - For the first half increase the number of stars.
 - For the second half decrease the number of stars.
3. Display the pattern.
"""

for star in range(1, 20):
    # For the first half of the pattern including the middle line (1 to 5)
    if star <= 10:
        print('*' * star)
    # For the second half of the pattern (6 to 9)
    else:
        print('*' * (20 - star))
