rm -rf install
mkdir install
pip install -r requirements.txt -t ./install/

cp -r Jamf ./install/
cp *.py ./install/
cd install
