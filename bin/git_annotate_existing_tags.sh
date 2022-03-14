#!/bin/sh

# Bug: (2022-03-12) (for a commit after v3.15.0)
#      Running `git describe` gave unexpected output.
#      - expect: "v3.15.0-…-g…"
#      - actual: "v3.7.0-…-g…"
# Why: 1. Most tags after (and before) v3.7.0 were not annotated. Similar:
#         https://github.com/Reference-LAPACK/lapack/issues/123
#      2. Because GitHub uses lightweight tags. Feedback for GitHub:
#         https://github.com/github/feedback/discussions/4924
# Fix: Run this script to retroactively annotate lightweight tags.
#      (Note, this script also re-annotates annotated tags.)
# Alt: See answers to https://stackoverflow.com/q/21738647/11817077
#      (These solutions are more elegant but might not preserve all lines, including new lines, in tag message.)

# make output directory
OUTPUT_DIR='_git_annotate_existing_tags'
mkdir -p "$OUTPUT_DIR"

# define how to save current status of tag annotation
function save_tag_summary() {
  local path=$1

  echo "$(git tag --format='%(creatordate)%09%(refname:strip=2)   %(taggerdate)   %(contents)')" > $path
}

# define how to annotate tags (will also re-annotate tags)
function annotate() {
  local tag=$1

  # get data for tag (some is new for annotation, some must be preserved)
  local date="$(echo $(git tag --format='%(creatordate)' --list $tag))"
  local msg="$(git tag --format='%(contents)' --list $tag)"
  local hash="$(git rev-list -n 1 $tag)"

  # save message to file to preserve new lines
  local msg_file_path="$OUTPUT_DIR/message.temp"
  echo "$msg" > $msg_file_path

  # tell the user what we will do
  echo "Annotate tag $(printf "%9s" $tag) (commit ${hash:0:7}) with date \"$date\" and retain its message \"${msg:0:30}...\"."

  # annotate
  GIT_COMMITTER_DATE=$date \
  git tag --annotate --force --file "$msg_file_path" "$tag" "$hash"

  # clean up
  rm $msg_file_path
}

# save current status to file for comparison
save_tag_summary "$OUTPUT_DIR/summary_before.temp"

# annotate each tag passed
for tag in "$@"; do annotate "$tag"; done

# save new status to file for comparison
save_tag_summary "$OUTPUT_DIR/summary_after.temp"
