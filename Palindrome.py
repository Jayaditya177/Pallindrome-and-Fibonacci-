import re
import time

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using string reversal."""
    return s == s[::-1]

def is_palindrome_advanced(s: str) -> bool:
    """Check if a string is a palindrome (ignores case and non-alphanumeric chars)."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def is_palindrome_two_pointer(s: str) -> bool:
    """Optimized palindrome check using two-pointer approach."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Performance Testing
test_string = "A man, a plan, a canal, Panama"

start_time = time.time()
print(is_palindrome(test_string))  # False (original check)
print(f"Time taken: {time.time() - start_time:.6f} sec")

start_time = time.time()
print(is_palindrome_advanced(test_string))  # True (ignoring spaces & case)
print(f"Time taken: {time.time() - start_time:.6f} sec")

start_time = time.time()
print(is_palindrome_two_pointer(test_string))  # True (optimized)
print(f"Time taken: {time.time() - start_time:.6f} sec")
