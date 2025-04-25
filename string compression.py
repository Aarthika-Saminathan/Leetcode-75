def compress(chars):
    read = 0
    write = 0

    # Dictionary to store the character counts
    char_count = {}

    while read < len(chars):
        char = chars[read]
        count = 0

        # Count the number of occurrences of the current character
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1

        # Store the count in the dictionary
        char_count[char] = count

        # Write the character and count to the list (same as before)
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    # Format the output as "a: 2, b: 2, c: 3"
    formatted_result = ", ".join([f"{k}: {v}" for k, v in char_count.items()])
    
    # Printing the formatted result
    return formatted_result

chars = ["a", "a", "b", "b", "c", "c", "c"]
output = compress(chars)
print(output)  # Output: a: 2, b: 2, c: 3
