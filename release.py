import sys
from semver import bump_major, bump_minor, bump_patch

if __name__ == "__main__":
    with open("VERSION", "r+") as fh:
        version = fh.read()
        bump_op = bump_patch

        if len(sys.argv) > 1:
            if sys.argv[1] == "major":
                bump_op = bump_major

            if sys.argv[1] == "minor":
                bump_op = bump_minor

        new_version = bump_op(version)

        fh.seek(0)  # rewind cursor
        fh.write(new_version)
        fh.truncate()  # truncate everything after cursor
