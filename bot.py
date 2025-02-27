import discord
import subprocess
import os
from discord.ext import commands

TOKEN = "MTM0MjQwMDA0NjYyMDIxNzM4Ng.G7hfjK.ddymFo3U1gFheM10-gGL8XdMARYHOwxX59QbiE"  # Replace with your bot token
PREFIX = "!"
VM_DIR = "/opt/vms/"
IMG_NAME = "tinyvm.img"

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def createvm(ctx, vm_name: str):
    vm_path = os.path.join(VM_DIR, vm_name)
    if os.path.exists(vm_path):
        await ctx.send(f"VM {vm_name} already exists.")
        return
    
    os.makedirs(vm_path, exist_ok=True)
    subprocess.run(["cp", IMG_NAME, os.path.join(vm_path, "disk.img")])
    await ctx.send(f"VM {vm_name} created.")

@bot.command()
async def startvm(ctx, vm_name: str):
    vm_path = os.path.join(VM_DIR, vm_name)
    if not os.path.exists(vm_path):
        await ctx.send(f"VM {vm_name} does not exist.")
        return
    
    qemu_cmd = [
        "qemu-system-x86_64",
        "-hda", os.path.join(vm_path, "disk.img"),
        "-m", "256M",
        "-net", "none",
        "-nographic"
    ]
    subprocess.Popen(qemu_cmd)
    await ctx.send(f"VM {vm_name} started.")

@bot.command()
async def stopvm(ctx, vm_name: str):
    subprocess.run(["pkill", "-f", vm_name])
    await ctx.send(f"VM {vm_name} stopped.")

@bot.command()
async def listvms(ctx):
    vms = os.listdir(VM_DIR) if os.path.exists(VM_DIR) else []
    await ctx.send("Active VMs: " + ", ".join(vms) if vms else "No VMs found.")

bot.run(TOKEN)
