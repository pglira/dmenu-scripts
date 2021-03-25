# dmenu_scripts

## dmenu_open-file-recursively.py

```
usage: dmenu_open-file-recursively.py [-h] -d SEARCH_DIR -p SEARCH_PATTERN
                                      [-c COMMAND] [-o DMENU_OPTIONS]

Use dmenu to recursively search for a file in a search directory.

required arguments:
  -d SEARCH_DIR, --search-dir SEARCH_DIR
                        Path to search directory (default: None)
  -p SEARCH_PATTERN, --search-pattern SEARCH_PATTERN
                        Search pattern (default: None)

optional arguments:
  -c COMMAND, --command COMMAND
                        Command to run with selected file (%FILE) (default:
                        xdg-open %FILE)
  -o DMENU_OPTIONS, --dmenu-options DMENU_OPTIONS
                        Options to pass to dmenu (default: )

Examples:
  dmenu_open-file-recursively.py -d "$HOME/Documents" -p "*.pdf" -c "okular %FILE" -o "-i -l 20 -p pdf:"
  dmenu_open-file-recursively.py -d "$HOME/Videos" -p "*.mp4" -c "mpv %FILE" -o "-i -l 20 -p videos:"
  dmenu_open-file-recursively.py -d "$HOME" -p "*.pdf" -c "echo %FILE | xclip -selection clipboard" -o "-i -l 20 -p copy-path:"
```

## dmenu_open-manpage.py

```
usage: dmenu_open-manpage.py [-h] [-a {pdf,txt}] [-p PROGRAM]
                             [-o DMENU_OPTIONS]

Use dmenu to open a manpage as pdf or text file.

optional arguments:
  -a {pdf,txt}, --open-as {pdf,txt}
                        Open manpage as ... (default: pdf)
  -p PROGRAM, --program PROGRAM
                        Program to open file (default: xdg-open)
  -o DMENU_OPTIONS, --dmenu-options DMENU_OPTIONS
                        Options to pass to dmenu (default: )

Examples:
  dmenu_open-manpage.py -p okular
  dmenu_open-manpage.py -a txt -p gnome-text-editor
  dmenu_open-manpage.py -a txt -p "$TERMINAL -e vim"
```

## dmenu_kill-process.py

```
usage: dmenu_kill-process.py [-h] [-o DMENU_OPTIONS]

Use dmenu to kill a running process.

optional arguments:
  -o DMENU_OPTIONS, --dmenu-options DMENU_OPTIONS
                        Options to pass to dmenu (default: )

Examples:
  dmenu_kill-process.py
```

