# Environment Setup

## Software Setup

- Install [Anaconda software](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Install [ngrok](https://ngrok.com/download) (you need to sign up and login for autnentication)
- Install [git](https://github.com/git-guides/install-git) (if you are not familiar with Git/Github, please read [this tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners))
- If you don't have a Github account, please create one and follow [this tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#about-ssh-key-generation) to set up the account with a new SSH (you can ignore the "Adding your SSH key to the ssh-agent" part).

## Python Environment

Open a terminal, and run the following code one by one:

- `cd [a directory where you want to save the code base]` e.g., `cd ~/Desktop/`
- `git clone git@github.com:OrsonXu/CSNext2022_LEG.git` to download the repo
- `cd [the directory of the current README.md]` e.g., `cd ~/Desktop/CSNext2022_LEG`
- `conda create --name csnext python=3.7` to install a new environment named "csnext" <- you can also replace it with a name you prefer
- `conda activate csnext` to activate the new environment
- `pip install -r requirements.txt` to install the necessary libraries

# First trial - collect data via a smartphone

Please go to the `webapi_getimudata` folder and read `webapi_getimudata/README.md`