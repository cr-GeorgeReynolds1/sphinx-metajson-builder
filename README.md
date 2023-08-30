# json-meta-builder

Sphinx extension to build json files with an additional metadata
as structured JSON objects as well as a 'toctree' key containing a 
full toctree (similar to RTD html theme).

## Usage

Set the builder as a extension in `conf.py`:

    extensions = ['sphinxcontrib.metajson']

Run sphinx-build with target `metajson`:

    sphinx-build -b metajson -c . build/metajson

There is now a structured JSON object in the meta field containing all
the metadata information as well as a`toctree` key in every fjson file 
with the top level toctree (as opposed to the `toc` key which only has
 the current level).
