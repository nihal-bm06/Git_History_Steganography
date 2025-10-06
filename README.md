# Git History Steganography — Forensics Challenge

Someone has hidden a secret flag inside this Git repository using clever steganography techniques. Your task is to recover the full flag.

Goal

Recover the complete flag and submit it in the format:

FLAG{PartA_PartB_PartC}

What’s hidden

The flag is split into three parts, hidden in different ways across the repository’s history and its files:

Part A — fragments hidden in commit author usernames (email addresses).

Part B — characters encoded by commit timestamps on a dedicated branch.

Part C — trailing whitespace (spaces/tabs) in a file on another branch.

⚠️ Some commits may include decoy content or misleading files. Solvers should focus on commit metadata, timestamps, and file contents. Any temporary or deleted files are irrelevant — only the Git history matters.

Rules

You may clone the repository and use any standard Git tools, shell utilities, or scripts to inspect it.

Do not modify the repository; read-only analysis is expected.

When you recover the flag, submit it as a single string in the format FLAG{PartA_PartB_PartC}.
Good luck — careful forensic inspection of Git history will reveal the flag!
