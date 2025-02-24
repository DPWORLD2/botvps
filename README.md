

---

# **Discord Bot VM Manager**  

This bot allows you to create, start, stop, and list lightweight VMs on a VPS **without Docker or systemd**, using QEMU.  

## **Features**  
✅ Create lightweight virtual machines  
✅ Start and stop VMs using QEMU  
✅ Manage VMs directly from a Discord server  

---

## **Installation**  
### **1. Install Dependencies**  
Run the following command on your VPS:  

```bash
sudo apt update && sudo apt install -y python3 python3-pip qemu-system-x86
pip install discord.py
```

### **2. Prepare VM Environment**  
Create a VM directory and a basic image:  

```bash
mkdir -p /opt/vms
cd /opt/vms
qemu-img create -f qcow2 tinyvm.img 1G
```

### **3. Set Up the Discord Bot**  
- Go to [Discord Developer Portal](https://discord.com/developers/applications)  
- Create a bot and copy the **bot token**  
- Enable **Message Content Intent** in bot settings  

### **4. Configure the Bot**  
Edit `bot.py` and replace:  

```python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```
with your actual bot token.  

### **5. Run the Bot**  
```bash
python3 bot.py
```

---

## **Usage**  
Once running, use these commands in Discord:  

```plaintext
!createvm myvm   # Creates a VM
!startvm myvm    # Starts the VM
!stopvm myvm     # Stops the VM
!listvms         # Lists all VMs
```

---

## **Running in the Background**  
To keep the bot running even after closing the terminal:  

```bash
nohup python3 bot.py &
```
or use **tmux**:  

```bash
tmux new -s discord-bot
python3 bot.py
```
(Detach with `Ctrl+B, D` and reattach with `tmux attach -t discord-bot`)  

---

## **Notes**  
- The VMs are stored in `/opt/vms/`  
- Modify the script to add networking or advanced features  

---
