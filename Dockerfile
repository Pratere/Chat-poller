From ubuntu
Run apt-get -y update
Run apt-get -y install curl
Run apt-get -y install gnupg 
Run curl -sL https://deb.nodesource.com/setup_10.x | bash
Run apt-get -y install nodejs
Run npm -y install tmi.js
Run npm -y install node-cmd
Copy . /app/
Cmd node /app/server.js
