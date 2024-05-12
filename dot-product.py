# Function to calculate dot product of two vectors
def dot_prod(vector1, vector2):
    # Check if vectors have same length
    if len(vector1) != len(vector2):
        print("Error: Vectors must have the same length.")
        return None

    # Perform dot product calculation
    result = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    return result

# Example usage
if __name__ == "__main__":
    # Example vectors for dot product
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    # Perform dot product calculation
    result_dot_prod = dot_prod(vector1, vector2)
    if result_dot_prod is not None:
        print("Dot Product Result:", result_dot_prod)
