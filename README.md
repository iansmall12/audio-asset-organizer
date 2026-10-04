# Audio Asset Organizer

A small python tool for batch locating and organizing audio files. Searches by keyword and prompts for new folder, and a prefix if you want!

## Why?

Splice is a fantastic place for music producers/sound designers to find samples. That being said, it creates a folder in your Splice folder for every sample pack you own even a single sample from -- sometimes even creating subfolders as well. I wanted a way to search through my entire Splice folder, and start organizing these sounds by type.

## What it does

- Scans user-defined folder structure for all .wav files matching a keyword
- Previews proposed rename before proceeding
- Moves (*not* copies!) files into new named subfolder in user-defined destination
- Loops again, allowing user to quickly tackle large folder

## Usage

1. Requires Python 3.6+. No special dependencies.
2. Run `python organizer.py`
3. Enter the folder to scan, and the destination folder
4. Enter a search term, or press Enter to list every .wav in the entire folder structure
5. Enter prefix if desired
6. Review preview, and enter subfolder name if desired

## Example 

<img width="800" height="429" alt="ezgif-360f22c64c9c5a90" src="https://github.com/user-attachments/assets/ad89a0e8-944f-4726-b0ad-fd903bff75c0" />

## Notes:

Written while learning Python. Up next...
- Scan folder, pick x number of samples and copy them to a folder (for random music making/sound design prompt)
- Sample rate/bit depth checker
- Dry-run mode

## Known Limitations:

- Answering `no` at the `proceed?` prompt reruns with same search term; user will need to restart
- Invalid characters in a folder name section will cause crash
- Can only scan for .wav files
