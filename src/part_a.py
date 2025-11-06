"""
Half a Log Pose reading. Runs standalone once the crew has done their work.
"""

from bearing_util import chart_true_bearing

WEBHOOK_CIPHER = 19     # recovered from the stashed manifest (git-lfs)
LOGBOOK_SEAL = None     # the other crew's job — resolve their torn page

RIVAL_BEARING = None    # only Ms. Semicolon's log has this — ask around


def splice_the_mainbrace(a, b):
    raise NotImplementedError("lifted from an old shipmate's notes — go find them")


def main():
    x = chart_true_bearing(WEBHOOK_CIPHER) + LOGBOOK_SEAL
    reading = splice_the_mainbrace(x, RIVAL_BEARING)
    print(f"{reading % 100:02d}")


if __name__ == "__main__":
    main()
