cd ~/Desktop
git clone https://github.com/AviationSFO/SnakeGame
cd SnakeGame
python3 -m pip install playsound2
echo "Your python version is:"
python3 --version

if python3 --version | grep -q '3.6'; then
    echo "Python version checks"
elif python3 --version | grep -q '3.7'; then
    echo "Python version checks"
elif python3 --version | grep -q '3.8'; then
    echo "Python version checks"
elif python3 --version | grep -q '3.9'; then
    echo "Python version checks"
elif python3 --version | grep -q '3.10'; then
    echo "Python version checks"
else
    echo "Your python version is too old, Snake Game may not work. Consider upgrading python to 3.6 or later."
fi