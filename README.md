# Environment Setup

## Software Setup

- Install [Anaconda software](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Install [ngrok](https://ngrok.com/download) (you need to sign up and login for autnentication)
- Install [git](https://github.com/git-guides/install-git) (if you are not familiar with Git/Github, please read [this tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners))

## Python Environment

Open a terminal, and run the following code one by one:

- `cd [a directory where you want to save the code base]` e.g., `cd ~/Desktop/`
- `cd [the directory of the current README.md]` e.g., `cd ~/Desktop/CSNext2022_LEG`
- `conda create --name csnext python=3.7` to install a new environment named "csnext" <- you can also replace it with a name you prefer
- `conda activate csnext` to activate the new environment
- `pip install -r requirements.txt` to install the necessary libraries

# First trial - collect data via a smartphone

Please go to the `webapi_getimudata` folder and read `webapi_getimudata/README.md`