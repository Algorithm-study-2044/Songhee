class Solution:
    def knightDialer(self, n: int) -> int:
        # Base case: if there's only one move, the knight can be on any of the 10 digits
        if n == 1:
            return 10

        # Initialization of the count array representing the knight's current position
        counts = [1] * 10
      
        # Loop to calculate the number of distinct phone numbers of length n
        for _ in range(n - 1):
            # Temporary array to store new counts after the knight moves
            temp_counts = [0] * 10
          
            # The knight moves to calculate the counts for each position
            temp_counts[0] = counts[4] + counts[6]
            temp_counts[1] = counts[6] + counts[8]
            temp_counts[2] = counts[7] + counts[9]
            temp_counts[3] = counts[4] + counts[8]
            temp_counts[4] = counts[0] + counts[3] + counts[9]
            # No 5 in the move set since the knight cannot move from digit 5 to any other digit
            temp_counts[6] = counts[0] + counts[1] + counts[7]
            temp_counts[7] = counts[2] + counts[6]
            temp_counts[8] = counts[1] + counts[3]
            temp_counts[9] = counts[2] + counts[4]
          
            # Update counts for the next iteration
            counts = temp_counts
      
        # Return the sum of all the counts modulo 10^9 + 7 at the end of all moves
        # This is done to handle large numbers, as required by the problem statement
        return sum(counts) % (10**9 + 7)