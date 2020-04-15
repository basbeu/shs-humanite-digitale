#!/bin/bash
# Parses the necessary data for the project

# Get whole data from impresso (to fine tune)
mkdir complete
for i in GDL-191* JDG-191* NZZ-191* GDL-1920* JDG-1920* NZZ-1920*
do
    s3cmd get s3://impresso-data/${i} complete
done

# Reduce the data to interesting columns
mkdir reduced
cd complete
for f in *[0-9].jsonl.bz2
do
    bzcat $f | jq -c '{id: .id, type: .tp, date: .d, title: .t, fulltext: .ft}' | bzip2 > "../reduced/${f%.jsonl.bz2}-reduced.jsonl.bz2"
    echo Done: ${f} is reduced
done
cd ..

# Transform data to csv
python tocsv.py
