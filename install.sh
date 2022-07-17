# Is it possible to have install script clone from latest version rather than the latest commit?
# !!!!MACOS ONLY!!!!
cd ~/Desktop
git clone https://github.com/AviationSFO/SnakeGame

# Go into repo folder
cd SnakeGame

# Get new tags from the remote
git fetch --tags

# Get the latest tag name, assign it to a variable
latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)

# Checkout the latest tag
git checkout $latestTag

if [ python -V = "Python 2.7.16" ]
then
    python3 -m pip install playsound
    python3 -m pip install PyObjC
    echo "Your python version is:"
    python3 -V
else
    python -m pip install playsound
    python -m pip install PyObjC
    echo "Your python version is:"
    python -V
fi
echo "WARNING!"
echo "If the version above is NOT 3.6 or later, Snake Game will not work, please consider upgrading to a compatible version."