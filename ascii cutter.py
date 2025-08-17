def cut_ascii_lines(lines, start, length):
    """
    Removes `length` characters from each line starting at `start` index.
    Returns list of modified lines.
    """
    new_lines = []
    for line in lines:
        if start < len(line):
            end = start + length
            new_line = line[:start] + line[end:]
        else:
            new_line = line  # nothing to cut
        new_lines.append(new_line)
    return new_lines

def process_ascii_file(input_path, output_path, start, length):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Remove newline characters
    lines = [line.rstrip('\n') for line in lines]

    # Process cutting
    modified_lines = cut_ascii_lines(lines, start, length)

    # Write output
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in modified_lines:
            outfile.write(line + '\n')

    print(f"✔ ASCII art saved to: {output_path}")

# === Primer poziva ===
if __name__ == "__main__":
    input_file = "ascii_input.txt"     # ← ovde stavi ime tvog input fajla
    output_file = "ascii_output.txt"   # ← ovde će biti snimljen rezultat
    start_index = 1                    # ← od kog indeksa da počne sečenje
    cut_length = 10                   # ← koliko karaktera da se iseče

    process_ascii_file(input_file, output_file, start_index, cut_length)