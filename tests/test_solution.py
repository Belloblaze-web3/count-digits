import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "solution.py"


def run_case(input_text):
    completed = subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


class CountDigitsTests(unittest.TestCase):
    def test_sample_case(self):
        self.assertEqual(
            run_case("77150\n"),
            "\n".join([
                "0 1", "1 1", "2 0", "3 0", "4 0",
                "5 1", "6 0", "7 2", "8 0", "9 0",
            ]),
        )

    def test_all_same_digit(self):
        output = run_case("99999\n").splitlines()
        self.assertEqual(output[9], "9 5")
        self.assertTrue(all(output[i].endswith(" 0") for i in range(9)))

    def test_each_digit_once(self):
        self.assertEqual(
            run_case("0123456789\n"),
            "\n".join(f"{digit} 1" for digit in range(10)),
        )

    def test_leading_zeroes_are_counted(self):
        output = run_case("00012000\n").splitlines()
        self.assertEqual(output[0], "0 6")
        self.assertEqual(output[1], "1 1")
        self.assertEqual(output[2], "2 1")
        self.assertTrue(all(output[i].endswith(" 0") for i in range(3, 10)))


if __name__ == "__main__":
    unittest.main()
