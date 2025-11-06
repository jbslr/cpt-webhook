"""
Half a Log Pose reading. Runs standalone once the crew has done their work.
"""

WEBHOOK_CIPHER = None   # the cipher crew's job — stashed manifest
PART_A_HEADER = "DRAFT-ONE"  # early draft, don't trust this

RIVAL_BEARING = None


def chart_true_bearing(cipher):
    raise NotImplementedError("comes in from the cipher crew's branch")


def splice_the_mainbrace(a, b):
    raise NotImplementedError("comes in from the seal crew's branch")


def main():
    x = chart_true_bearing(WEBHOOK_CIPHER) + PART_A_HEADER
    reading = splice_the_mainbrace(x, RIVAL_BEARING)
    print(f"{reading % 100:02d}")


if __name__ == "__main__":
    main()
