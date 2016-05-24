#!/usr/bin/env bash
cd $HOME/affordability-model/affordability-model
source ../bin/activate
export PRODUCTION=true
sudo apt-get -yq --no-install-suggests --no-install-recommends --force-yes install libblas-dev liblapack-dev libatlas-base-dev gfortran
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
sudo service gunicorn restart

sudo service nginx restart