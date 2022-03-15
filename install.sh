# Is it possible to have install script clone from latest version rather than the latest commit?

cd ~/Desktop
git clone https://github.com/AviationSFO/SnakeGame/releases/latest
cd SnakeGame
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