"""
Half a Log Pose reading — Captain Webhook's contribution.

This file is a stub. Two crews need to merge their work in before it
runs: the cipher/bearing half, and the seal/header half. A third
value only exists on Ms. Semicolon's log — you'll need to go find it.
"""

WEBHOOK_CIPHER = None    # merge in from the cipher crew's branch
LOGBOOK_SEAL = None      # merge in from the seal crew's branch

RIVAL_BEARING = None     # lives on Ms. Semicolon's log — go fetch it


def chart_true_bearing(cipher):
    raise NotImplementedError("comes in from the cipher crew's branch")


def splice_the_mainbrace(a, b):
    raise NotImplementedError("comes in from the seal crew's branch")


def main():
    if WEBHOOK_CIPHER is None or LOGBOOK_SEAL is None or RIVAL_BEARING is None:
        raise SystemExit("Log Pose reading incomplete — not everyone's merged in yet.")
    x = chart_true_bearing(WEBHOOK_CIPHER) + LOGBOOK_SEAL
    reading = splice_the_mainbrace(x, RIVAL_BEARING)
    print(f"{reading % 100:02d}")


if __name__ == "__main__":
    main()
