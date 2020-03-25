#!/usr/bin/env bash

set -euo pipefail

# Ensure moxygen is installed
if npm list -g moxygen > /dev/null
then
    echo "Moxygen already installed."
else
    echo "Installing Moxygen dependencies."

    git clone https://github.com/sourcey/moxygen.git temp/moxygen
    pushd temp/moxygen
    set +e
    # Capture moxygen dependencies and install them
    npm list 2>&1 |\
        grep -v ERR |\
        sed -E 's/^.*[A-Z ]+([a-z])/\1/' |\
        grep -v moxygen |\
        grep '^[a-z]' |\
        sed 's/\^//' |\
        xargs npm install -g
    set -e
    popd
    rm -rf temp/moxygen

    echo "Installing Moxygen."

    npm install moxygen -g
fi

rm -rf doxygen
doxygen .doxygen-config src

rm -rf doxygen/md
mkdir -p doxygen/md
moxygen --classes --anchors --output=doxygen/md/%s.md doxygen/xml

export IFS=$'\n'
echo "# Namespaces" > doxygen/md/index.md
echo "" >> doxygen/md/index.md
linked_files=()
for namespace in $(ls doxygen/md/ | sed -E 's/^([^<]+)\:\:[^\:>]+$/\1/' | sed -E 's/^([^<]+)\:\:.+<.+$/\1/'  | sort -u)
do
    echo "## $namespace"
    echo ""
    pushd doxygen/md > /dev/null
    for file in $(ls "$namespace"*)
    do
        name=$(echo ${file} | sed 's/\.md$//g')
        encoded_file=$(echo ${file} | sed -E 's/\:/%3A/g' | sed -E 's/ /%20/g')
        echo "- [\`${name}\`](${encoded_file})"
    done
    popd > /dev/null
    echo ""
done >> doxygen/md/index.md


