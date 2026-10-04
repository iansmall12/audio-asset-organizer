from pathlib import Path

def find(search_term):
    while True:
        filelist = []
        print()
        if search_term == "" or search_term == "*":
            print(f'ALL FILES IN DESTINATION'.center(50, "="))
        else:
            print(f' {search_term} '.center(50, "="))
        if search_term == "" or search_term == "*":
            filelist = list(folder.rglob("*.wav"))
            for file in filelist:
                print(file)
        else:
            for file in folder.rglob("*.wav"):
                if search_term.lower() in file.name.lower():
                    print(file, f"Found a {search_term}!")
                    filelist.append(file)
        prefix = input('Please enter your desired prefix...')
        print('...')
        print('Preview:')
        print('...')
        for file in filelist:
            print (f'{prefix}{file.name}')
        answer = input('Proceed? y/n')
        if answer != 'y':
            continue

        newsub = input('New folder name?')
        newfolder.mkdir(exist_ok=True)
        subfolder = newfolder / f"{newsub}"
        subfolder.mkdir(exist_ok=True)
        for file in filelist:
            newname = subfolder / f'{prefix}{file.name}'
            file.rename(newname)
        break

while True:
    # User defines folder to scan
    folder = Path(input("Enter folder to scan: ").strip().strip('"'))
    if not folder.is_dir():
        print('Could not find folder!')
        continue

    # User defines new folder location
    newfolder = Path(input("Enter new folder directory: ").strip().strip('"'))

    while True:
        term = input("Please enter search term (or press enter to view all files):")
        find(term)

        again = input('Rescan folder with new term? y/n')
        if again != "y":
            break

    if input('Scan a different folder? y/n') != "y":
        break
