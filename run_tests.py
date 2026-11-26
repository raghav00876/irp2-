
import subprocess
import sys
from pathlib import Path

tests = [
    ("p1_reverse_words", "p1_input.txt", "p1_expected.txt"),
    ("p2_binary_search", "p2_input.txt", "p2_expected.txt"),
    ("p3_digit_sum", "p3_input.txt", "p3_expected.txt"),
    ("p4_pair_count", "p4_input.txt", "p4_expected.txt"),
]

for program, input_file, expected_file in tests:
    print(f"\nTesting {program}...")

    input_data = Path("tests", input_file).read_text()
    expected = Path("tests", expected_file).read_text().strip()

    result = subprocess.run(
        [sys.executable, f"problems/{program}.py"],
        input=input_data,
        capture_output=True,
        text=True
    )

    actual = result.stdout.strip()

    if result.returncode == 0 and actual == expected:
        print("PASS")
    else:
        print("FAIL")
        print("Expected:", expected)
        print("Actual:", actual)
        if result.stderr:
            print("Error:", result.stderr)

print("\nTesting completed!")
