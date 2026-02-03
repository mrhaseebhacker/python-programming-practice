# Simple manual brute-force demo (no itertools).
# Charset and max length are small for safety (<= 3).

def brute_force_manual(target, charset):
    max_len = 3
    attempts = 0

   
    if not (1 <= len(target) <= max_len):
        raise ValueError("Target password length must be 1..3 for this demo.")

    for ch in target:
        if ch not in charset:
            raise ValueError(f"Character '{ch}' not in charset.")

    # Length 1 attempts
    for a in range(len(charset)):
        attempts += 1
        attempt = charset[a]
        if attempt == target:
            return attempts, attempt

    # Length 2 attempts
    for a in range(len(charset)):
        for b in range(len(charset)):
            attempts += 1
            attempt = charset[a] + charset[b]
            if attempt == target:
                return attempts, attempt

    # Length 3 attempts
    for a in range(len(charset)):
        for b in range(len(charset)):
            for c in range(len(charset)):
                attempts += 1
                attempt = charset[a] + charset[b] + charset[c]
                if attempt == target:
                    return attempts, attempt

    # If not found (shouldn't happen if target validated), return attempts
    return attempts, None


def main():
    # Choose a small charset for demo. Change to what you want.
    charset = "0123456789"   # digits only (10 chars)
    # charset = "ABCD"       # try small letters for quicker demo

    target = input("Enter target password (1-3 chars, using charset): ").strip()

    try:
        attempts, found = brute_force_manual(target, charset)
    except ValueError as ve:
        print("Error:", ve)
        return

    if found:
        print(f"Password '{found}' found after {attempts} attempts.")
    else:
        print("Password not found within length limit.")
    

if __name__ == "__main__":
    main()
