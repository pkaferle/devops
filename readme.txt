Install Redis (Windows):
https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows

In Redis CLI:
ping

SET, GET; MSET, MGET commands

SELECT <nb_db>


Open Anaconda PowerShell

$ Get-Process redis-server
It should return the same process ID than we saw

Create virtual environment:
conda create --name devops python=3.9

conda activate devops

To istall redis-py client library:
python -m pip install redis*

In addition, install
pip install jupyter
pip install flask

If the notebook doesn't work, install also (IMPORTANT: with conda)
conda install pywin32

And you can verify that is really in our environment:
conda list

