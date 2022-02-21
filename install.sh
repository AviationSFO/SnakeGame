cd ~/Desktop
git clone https://github.com/AviationSFO/SnakeGame
cd SnakeGame
if [ python -V -eq 2.7.16 ]
then
    python3 -m pip install playsound
    python3 -m pip install PyObjC
else
    python -m pip install playsound
    python -m pip install PyObjC
fi
echo "Your python version is:"
if [ python -V -eq 2.7.16 ]
then
    python3 -V
else
    python -V
fi
echo "WARNING!"
echo "If the version above is NOT 3.6 or later, Snake Game will not work, please consider upgrading to a compatible version."