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

function annotate() {
  local date=$1
  local file=$2
  local hash=$3

  GIT_COMMITTER_DATE=$date \
  git tag --annotate --force --file $file $tag $hash
}

function save_tag_summary() {
  local path=$1

  echo "$(git tag --format='%(creatordate)%09%(refname:strip=2)   %(taggerdate)   %(contents)')" > $path
}

for tag in "$@"
do
  # get data for tag (some is new for annotation, some must be preserved)
  date="$(echo $(git tag --format='%(creatordate)' --list $tag))"
  msg="$(git tag --format='%(contents)' --list $tag)"
  hash="$(git rev-list -n 1 $tag)"

  # make output directory
  output_dir='_git_annotate_existing_tags'
  mkdir -p "$output_dir"

  # save message to file to preserve new lines
  msg_file_path="$output_dir/message.temp"
  echo "$msg" > $msg_file_path

  # save current status to file for comparison
  save_tag_summary "$output_dir/summary_before.temp"

  # show the user what we will do, then do it
  echo "Annotate tag $(printf "%9s" $tag) (commit ${hash:0:7}) with date \"$date\" and retain its message \"${msg:0:30}...\"."
  annotate "$date" "$msg_file_path" "$hash"

  # save new status to file for comparison
  save_tag_summary "$output_dir/summary_after.temp"

  # clean up
  rm $msg_file_path
done
