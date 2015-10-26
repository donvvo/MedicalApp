apt-get -qqy update
apt-get -qqy install python-dev
apt-get -qqy install libpq-dev
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-pip
apt-get -qqy install libjpeg-dev

sudo pip install -r /vagrant/MedicalApp/requirements/local.txt

su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'createdb medicalapp'
sudo -u postgres psql -U postgres -d postgres -c "alter user vagrant with password 'medicalapp'"