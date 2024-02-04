# Simple GigaChat (experimental)

Simple GigaChat is a Web Application that allows users to communicate with Sber GigaChat.

### The main technology stack used in this project includes:
- Python3;
- FastAPI;
- Uvicorn as HTTP server;
- Vue3 as the frontend and Vite as Frontend Tooling
- Bootstrap 5 as the UI framework.

### Installation
To use this project, you will need to have Python 3.10 or higher installed on your local machine. You must install Python if you don't have it already.
Once you have Python installed, you can install the required Python packages by running the following command in your terminal:
```
sudo apt install python3 python3-pip python3-venv
git clone https://github.com/waldesem/Awesome-GC.git
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage
To start the application at run the following command in your terminal:
```
uvicorn main:app --reload
```

### Uvicorn Service
For create systemd service run the following command in your terminal:
```
sudo nano /etc/systemd/system/smgigachat.service
```
Add the following line:
```
[Unit]
Description=Uvicorn instance to serve smgigachat
After=network.target
[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/DB-Personal-DB/backend
Environment="PATH=/home/user/DB-Personal-DB/backend/venv/bin"
ExecStart=/home/user/DB-Personal-DB/backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
[Install]
WantedBy=multi-user.target
```
Start the service:
```
sudo systemctl start smgigachat
sudo systemctl enable smgigachat
sudo systemctl status smgigachat
```

### Nginx
Nginx configuration:
Open the file '/etc/nginx/sites-available/smgigachat' and add the following line:
```
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        include proxy_params;
        proxy_pass http://0.0.0.0:8000;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_redirect off;
    }
}
```
Add configuration file '/etc/nginx/sites-enabled/smgigachat' and restart Nginx:
```
sudo ln -s /etc/nginx/sites-available/smgigachat /etc/nginx/sites-enabled/smgigachat
# sudo ln -sf /etc/nginx/sites-available/smgigachat /etc/nginx/sites-enabled/smgigachat # for upgrade
sudo service nginx restart
```
Add rule in your firewall:
```
sudo ufw allow 'Nginx HTTP'
sudo ufw reload
```

### Node Development (optional)

You will also need to have Node.js installed on your machine to build and run the TypeScript code.
After installing Node.js, you can install the required npm packages by running in your webapp directory the following command in your terminal:
```
npm i
```
To start development node server  run the following command in your terminal:
```
npm run dev
```
To build the code in the static directory flask app, first comment/uncomment the lines `server` in /frontend/src/components/HomeVue.vue
Then run the following command in your terminal:
```
npm run build
```
This will compile the TypeScript code and output the JavaScript and CSS files in the static directory '/backend/static'.

### License
This project is licensed under the MIT License.
