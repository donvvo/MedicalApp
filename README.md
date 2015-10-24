# Vagrant Setup
Vagrant is a tool used to easily configure and use a virtual machine for software development. 
It sets up a virtual machine environment by reading a configuration file called 'Vagrantfile'. 

By using Vagrant, we can make sure that everyone is working in the same environment. 
Also, it automates a lot of tedious setup tasks such as database configuration.
Please set up Vagrant using the Vagrantfile and pg_config.sh from this repo. 

<ol>
<li>Download and install virtual machine. I recommend Virtualbox (https://www.virtualbox.org/wiki/Downloads) 
since it is easy to use.</li>
<li>Download and install Vagrant (http://www.vagrantup.com/downloads)</li>
<li>In your terminal, type <tt>vagrant up</tt> in the root directory of this repo. 
Vagrant will setup a virtual machine and download all the necessary packages. This might take a while.</li>
<li>After setup is all done, <tt>vagrant ssh</tt> to login to the virtual machine. </li>
<li><tt>/vagrant</tt> in your virtual machine will be synced with the root directory of this repo in your host computer. 
<tt>cd /vagrant</tt> to access this repo in your virtual machine.</li>
<li><tt>python manage.py migrate</tt> inside <tt>/vagrant/backend</tt> to initialize the database.</li>
<li><tt>python manage.py runserver 0.0.0.0:8000</tt> to run the website. This port in your virtual machine will be 
forwarded to <tt>localhost:8000</tt> in your host machine. Open a browser and access <tt>localhost:8000</tt>.</li>
<li>Type <tt>exit</tt> or <tt>logout</tt> to exit the virtual machine.</li>
<li>When you are done working, <tt>vagrant halt</tt> in the root directory of this repo on your host machine 
to turn off the virutal machine.</li>
<li><tt>vagrant up</tt> to turn on the virtual machine again.</li>
<li><tt>vagrant destroy</tt> when you are not using Vagrant for a while.</li>
</ol>

Detailed but easy to follow documentation on Vagrant is in http://docs.vagrantup.com/v2/getting-started/index.html.