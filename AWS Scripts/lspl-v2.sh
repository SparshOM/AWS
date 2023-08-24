

# my aws support file
cd /root/Desktop/

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install


wget https://appbackupcurrent.s3.ap-south-1.amazonaws.com/ucanassess_pratik/finalcbtdoc/UCAV1.zip

unzip UCAV1.zip



#wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
#sudo dnf localinstall google-chrome-stable_current_x86_64.rpm -y
#cat /etc/yum.repos.d/google-chrome.repo

#for epel-release
yum install epel-release -y

#For p7zip-full
yum install -y p7zip p7zip-plugins

#For Git
yum install git -y

#For anydesk
cat > /etc/yum.repos.d/AnyDesk-CentOS.repo << "EOF"
[anydesk]
name=AnyDesk CentOS - stable
baseurl=http://rpm.anydesk.com/centos/$basearch/
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://keys.anydesk.com/repos/RPM-GPG-KEY
EOF
yum install anydesk -y

git --version
