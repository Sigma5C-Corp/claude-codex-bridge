#!/usr/bin/env python3
"""
Basic Claude-Codex Bridge Session Example

This example demonstrates how to create a duo peer programming session
where Claude submits code and Codex reviews it.
"""

from claude_codex_bridge import (
    create_session,
    load_session,
    Verdict,
    ClaudeProvider,
    CodexProvider,
)


def main():
    """Run a basic peer programming session."""

    # Check if CLIs are available
    print("Checking CLI availability...")
    print(f"  Claude CLI: {'Available' if ClaudeProvider.is_available() else 'Not found'}")
    print(f"  Codex CLI: {'Available' if CodexProvider.is_available() else 'Not found'}")
    print()

    # Create a new session
    session_id = "example_auth"
    task = "Implement a secure password hashing function"

    print(f"Creating session: {session_id}")
    print(f"Task: {task}")
    print()

    session = create_session(session_id, task)

    # Example code submission (normally this would come from Claude)
    example_code = '''
import hashlib
import secrets

def hash_password(password: str) -> tuple[str, str]:
    """
    Hash a password with a random salt.

    Args:
        password: The plaintext password

    Returns:
        Tuple of (hashed_password, salt)
    """
    salt = secrets.token_hex(32)
    salted = password + salt
    hashed = hashlib.sha256(salted.encode()).hexdigest()
    return hashed, salt

def verify_password(password: str, hashed: str, salt: str) -> bool:
    """Verify a password against its hash."""
    check_hash, _ = hash_password(password)
    # BUG: This doesn't use the stored salt!
    return check_hash == hashed
'''

    print("Submitting code for review...")
    session.submit_code(example_code, files_modified=["auth/password.py"])

    print(f"Session status: {session.status}")
    print(f"Current round: {session.current_round}")
    print()

    # In a real scenario, you would wait for Codex's review:
    # exchange = session.wait_for_review(timeout=120)

    print("Session data directory:")
    print(f"  {session._bridge.get_session_dir()}")
    print()

    print("To complete the review cycle:")
    print("  1. Run Codex to review the code")
    print("  2. Call session.submit_review() with the verdict")
    print("  3. Or call session.wait_for_review() to block until review arrives")
    print()

    # Demonstrate loading an existing session
    print("Loading existing session...")
    loaded = load_session(session_id)
    print(f"  Loaded session: {loaded.session_id}")
    print(f"  Task: {loaded.task_description}")
    print(f"  Exchanges: {len(loaded.exchanges)}")


if __name__ == "__main__":
    main()
