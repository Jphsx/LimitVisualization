import numpy as np

def relaxation_transition(matrix, fixed_indices, relaxation_factor=0.2, max_iterations=100, tolerance=1e-6):
    new_matrix = matrix.copy()
    num_rows, num_cols = matrix.shape
    
    for _ in range(max_iterations):
        max_change = 0
        
        for i in range(num_rows):
            for j in range(num_cols):
                if (i, j) not in fixed_indices:
                    neighbors = []
                    total_weight = 0
                    
                    for dx in [,-1, 0, 1]:
                        for dy in [,-1, 0, 1]:
                            ni, nj = i + dx, j + dy
                            if 0 <= ni < num_rows and 0 <= nj < num_cols and (ni, nj) in fixed_indices:
                                weight = 1.0 / ((dx**2 + dy**2) + 1)  # Weight based on distance
                                neighbors.append(matrix[ni, nj] * weight)
                                total_weight += weight
                                print(ni,nj,i,j,weight)
                    
                    if neighbors:
                        print(neighbors)
                        new_value = (1 - relaxation_factor) * matrix[i, j] + (relaxation_factor * sum(neighbors)) / total_weight
                        change = abs(new_value - matrix[i, j])
                        new_matrix[i, j] = new_value
                        max_change = max(max_change, change)
                        print(new_matrix)
        
        if max_change < tolerance:
            break
    
    return new_matrix

def myRelax(matrix,fixed_indices, relaxation_factor=0.2):
    new_matrix = matrix.copy()
    num_rows,num_cols = matrix.shape
    
    for i in range(num_rows):
        for j in range(num_cols):
            #calculate contributions from all fixed values
            if (i,j) not in fixed_indices:
                  

# Define a small numpy array with fixed values
#matrix = np.array([[0, 0, 0, 0],
 #                  [0, 1, 0, 4],
 #                  [0, 0, 0, 0],
 #                  [0, 0, 0, 2]])
#matrix = np.array([[0,0],
#                   [1,0]]) 
 
matrix = np.zeros((10,10))
matrix[9][9]=3. 
matrix[4][1]=15.
# Define the indices of fixed values
fixed_indices = [(4,1),(9,9)]

# Perform relaxation transition
result_matrix = relaxation_transition(matrix, fixed_indices,0.95,2)

print("Original Matrix:")
print(matrix)

print("\nResulting Matrix:")
print(result_matrix)

