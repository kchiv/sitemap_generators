# sitemap_generators
Sitemap generators for various use cases

# File: sitemapgenerator_iterate_over_files.py
If you have multiple files that contain lists of URLs and need to create a sitemap for each file, this script will iterate over every file and create a sitemap for each one. The generated sitemap will utilize the same name as the input file but will convert it to .xml file type.

Currently it's configured to convert .txt files to .xml but you can convert every file type.

## Requirements
* All files must exist in the same directory
* Files must only contain line separated URLs
