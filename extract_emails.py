# extract_emails.py
# Task: Read a .txt file, find all email addresses, save unique ones to another file.

import re
from pathlib import Path

# Regex to match common email formats (case-insensitive)
EMAIL_RE = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}', re.IGNORECASE)

def extract_emails_from_text(text: str) -> set[str]:
    """Return a set of unique, lowercased emails found in text."""
    return {m.lower() for m in EMAIL_RE.findall(text)}

def extract_emails_from_file(in_path: str, out_path: str) -> int:
    """Read input file, extract emails, write unique sorted emails to output file."""
    src = Path(in_path)
    dst = Path(out_path)

    # Read all text (ignore bad characters if any)
    text = src.read_text(encoding="utf-8", errors="ignore")

    # Find & deduplicate emails
    emails = sorted(extract_emails_from_text(text))

    # Write one email per line
    dst.write_text("\n".join(emails), encoding="utf-8")

    return len(emails)

if __name__ == "__main__":
   
    input_txt  = r"C:\Apexcify_Internship\Task 2\emails_input.txt"
    output_txt = r"C:\Apexcify_Internship\Task 2\emails_output.txt"

    count = extract_emails_from_file(input_txt, output_txt)
    print(f"Extracted {count} unique email(s) to {output_txt}")
