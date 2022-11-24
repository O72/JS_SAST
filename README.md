# JS_SAST
Static Application Security Testing Analyzer for JavaScript Source Code. 
JS_SAST uses regular expressions to build its rulesets. These rulesets are being used by the tool to
detect vulnerabilities, flaws, and bugs within JavaScript code. 
The tool will scan each line in the JavaScript code file and
check the code against various of the custom rulesets that identify vulnerable code.



## Installation

Install JS_SAST

```bash
  git clone https://github.com/O72/JS_SAST.git
  cd js_sast
```
    
## Deployment

To deploy and ensure all related packages for this project are installed, run

```bash
  python3 installation.py
```


## Usage

```bash
python3 js_sast.py 
usage: js_sast.py [options]

optional arguments:
  -h, --help            show this help message and exit

Argument options:
  -p PATH, --path PATH  file: file or directory path to be scanned
  -g GOSEC, --gosec GOSEC
                        -g gosec, to run gosec on the target repository to
                        scanfor vulnerabilities in Go source code.
  -b BANDIT, --bandit BANDIT
                        -b bandit, to run bandit on the target repository to
                        scan for vulnerabilities in Python source code.
  -c CLONE, --clone CLONE
                        -c https://github.com/O72/JS_SAST.git, to clone
                        remoterepository to the current directory to be
                        scanned
```


## Demo

![JS_demo](https://media.giphy.com/media/fPRsu45lfErQfGUtFU/giphy.gif)

## Running Tests

To run tests, run the following command

```bash
  python3 js_sast.py -f examples
```


## Documentation

[Writing a custom ruleset](https://github.com/O72/JS_SAST/wiki/Writing-a-custom-ruleset)



## FAQ

#### Will JS_SAST catch all vulnerabilities, flaws, or bugs within JavaScript source code?

No, If the rule for a certain vulnerability or a bug is not implemented/supported, the tool will not catch it. Check the documentation section to learn how to add support to a new rule.

