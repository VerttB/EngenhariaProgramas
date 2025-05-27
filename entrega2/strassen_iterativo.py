import numpy as np

class Frame:
    def __init__(self, A, B, size, stage=0):
        self.A = A  # Matrix A for this frame's computation
        self.B = B  # Matrix B for this frame's computation
        self.size = size # Current size of matrices A and B
        self.stage = stage  # Current stage of computation for this frame (0-7 for Strassen steps)
        self.sub = {}       # Dictionary to store results of sub-problems (M1 to M7)
        self.result = None  # The final result of the matrix multiplication for this frame

def add(A, B):
    """Helper function for matrix addition."""
    return A + B

def sub(A, B):
    """Helper function for matrix subtraction."""
    return A - B

def strassen_iterative_fixed(A, B):
    """
    Performs matrix multiplication using an iterative version of Strassen's algorithm.
    Assumes A and B are square matrices of the same dimension, which is a power of 2.
    If not a power of 2, padding would be required before calling this function,
    or the base case needs to handle non-divisible sizes if the algorithm is adapted.
    """
    n = A.shape[0]

    # Handle edge cases: empty or 1x1 matrices
    if n == 0:
        return np.array([])
    # The main loop's base case (current_frame.size == 1) handles this,
    # but an early exit can be cleaner for trivial inputs.
    # if n == 1:
    #     return A * B # Element-wise for 1x1, which is matrix multiplication

    # Initialize the stack with the first frame representing the overall multiplication
    stack = [Frame(A, B, n, stage=0)]
    final_result = None
    
    # This variable will hold the result of the most recently completed (and popped) frame.
    # It simulates the "return value" from a recursive call in an iterative setup.
    last_completed_frame_result = None

    while stack:
        current_frame = stack[-1] # Peek at the frame on top of the stack

        # --- Base Case for the recursion ---
        # If the current frame is for a 1x1 matrix multiplication
        if current_frame.size == 1:
            current_frame.result = current_frame.A * current_frame.B # Perform scalar multiplication (as 1x1 matrices)
            last_completed_frame_result = current_frame.result # Store this result
            
            stack.pop() # This frame's computation is done, pop it from the stack
            
            if stack:
                # If there's a parent frame, increment its stage, as one of its sub-problems (this one) is complete.
                stack[-1].stage += 1
            else:
                # If the stack is now empty, this was the outermost frame. Its result is the final result.
                final_result = last_completed_frame_result
            continue # Proceed to the next iteration of the while loop

        # --- Recursive Step (simulated using stages) ---
        
        # Divide matrices for the current frame. These are views, not copies.
        mid = current_frame.size // 2
        A11, A12 = current_frame.A[:mid, :mid], current_frame.A[:mid, mid:]
        A21, A22 = current_frame.A[mid:, :mid], current_frame.A[mid:, mid:]
        B11, B12 = current_frame.B[:mid, :mid], current_frame.B[:mid, mid:]
        B21, B22 = current_frame.B[mid:, :mid], current_frame.B[mid:, mid:]

        # Process based on the current_frame's stage
        # Each stage corresponds to needing one of the 7 Strassen products (M1-M7)
        # or combining them.
        
        if current_frame.stage == 0: 
            # Stage 0: Need to compute M1 = (A11 + A22) * (B11 + B22)
            # Push a new frame onto the stack to compute M1.
            # The current_frame remains on the stack, waiting for M1's result.
            # Its stage (0) signifies it's waiting for M1.
            stack.append(Frame(add(A11, A22), add(B11, B22), mid, stage=0))
        elif current_frame.stage == 1: 
            # Stage 1: M1 has been computed (result in last_completed_frame_result). Store it.
            current_frame.sub["M1"] = last_completed_frame_result
            # Now, need to compute M2 = (A21 + A22) * B11. Push frame for M2.
            stack.append(Frame(add(A21, A22), B11, mid, stage=0))
        elif current_frame.stage == 2: 
            # Stage 2: M2 computed. Store it. Need M3.
            current_frame.sub["M2"] = last_completed_frame_result
            # Push frame for M3 = A11 * (B12 - B22)
            stack.append(Frame(A11, sub(B12, B22), mid, stage=0))
        elif current_frame.stage == 3: 
            # Stage 3: M3 computed. Store it. Need M4.
            current_frame.sub["M3"] = last_completed_frame_result
            # Push frame for M4 = A22 * (B21 - B11)
            stack.append(Frame(A22, sub(B21, B11), mid, stage=0))
        elif current_frame.stage == 4: 
            # Stage 4: M4 computed. Store it. Need M5.
            current_frame.sub["M4"] = last_completed_frame_result
            # Push frame for M5 = (A11 + A12) * B22
            stack.append(Frame(add(A11, A12), B22, mid, stage=0))
        elif current_frame.stage == 5: 
            # Stage 5: M5 computed. Store it. Need M6.
            current_frame.sub["M5"] = last_completed_frame_result
            # Push frame for M6 = (A21 - A11) * (B11 + B12)
            stack.append(Frame(sub(A21, A11), add(B11, B12), mid, stage=0))
        elif current_frame.stage == 6: 
            # Stage 6: M6 computed. Store it. Need M7.
            current_frame.sub["M6"] = last_completed_frame_result
            # Push frame for M7 = (A12 - A22) * (B21 + B22)
            stack.append(Frame(sub(A12, A22), add(B21, B22), mid, stage=0))
        elif current_frame.stage == 7: 
            # Stage 7: M7 computed. Store it. All 7 sub-problems are done.
            current_frame.sub["M7"] = last_completed_frame_result
            
            # Now, combine the M results to get C11, C12, C21, C22
            M = current_frame.sub
            C11 = M["M1"] + M["M4"] - M["M5"] + M["M7"]
            C12 = M["M3"] + M["M5"]
            C21 = M["M2"] + M["M4"]
            C22 = M["M1"] - M["M2"] + M["M3"] + M["M6"]

            # Combine Cij into the result matrix for the current_frame
            # np.hstack stacks arrays horizontally, np.vstack stacks them vertically.
            top_row = np.hstack((C11, C12))
            bottom_row = np.hstack((C21, C22))
            current_frame.result = np.vstack((top_row, bottom_row))

            # This frame's computation is now complete. Store its result.
            last_completed_frame_result = current_frame.result
            stack.pop() # Pop this completed frame.
            
            if stack:
                # If there's a parent frame, increment its stage.
                stack[-1].stage += 1
            else:
                # Stack is empty, this was the outermost frame. Its result is the final result.
                final_result = last_completed_frame_result
        else:
            # This 'else' corresponds to the one in your original code.
            # It implies current_frame.stage > 7 for a non-base-case frame.
            # This state should ideally not be reached if the stage management is correct.
            # If reached, it means a frame's stage was incremented beyond its final computation step.
            # Popping it without it having computed its 'result' means 'last_completed_frame_result'
            # will hold an outdated value from a previous frame, leading to incorrect results for the parent.
            # This indicates a potential logic flaw if this branch is ever hit.
            # A more robust solution might be to raise an error here.
            print(f"Warning: Frame encountered with unexpected stage {current_frame.stage} "
                  f"for size {current_frame.size}. Popping frame.")
            stack.pop() # Pop the frame with the unexpected stage
            if stack:
                stack[-1].stage += 1 # Increment parent's stage, but parent will use stale 'last_completed_frame_result'
            else:
                # If this was the root frame and it hit an unexpected stage, final_result might be wrong.
                if final_result is None: # Avoid overwriting if already properly set
                     final_result = last_completed_frame_result # This is likely incorrect/partial
                print("Warning: Root frame popped at unexpected stage. Result may be incorrect.")


    return final_result
