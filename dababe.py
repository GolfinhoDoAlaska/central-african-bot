#just importing
import discord
from discord.ext import commands
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from random import randint
from random import choice
import os

#the bot token
token = #do you really think I would post the token?!

#variables, configuration, etc.
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '\\', intents = intents)

#unused stuff
asks = {
    1:"hi",
    2:"how are you",
    3:"do you have penis",
    4:"kaboom",
    5:"whats up",
    6:"hey",
    7:"heil hitler",
    8:"black lifes matter",
    9:"black lifes dont matter"
}
resp = {
    1:"hello",
    2:"fine",
    3:"are you okay",
    4:"yes bro, kaboom",
    5:"hey",
    6:"hey",
    7:"you're reported to the authorities",
    8:"yes",
    9:"they matter"
}

ign = ["?", "!", ",", ".", "'", '"']

#end of the unused stuff

#yes
@client.event
async def on_ready():
    print("joe mama")

#welcome message
@client.event
async def on_member_join(member):
    await client.say("Welcome "+str(member.mention)+" please read #rules")

#clear chat
@client.command(pass_context=True)
async def clear(ctx, amount=5):
    print("doing!")
    await ctx.channel.purge(limit=int(amount))
    await ctx.send("the great purge had been done")

#nuke command 
#holy shit this took me so long to make
@client.command(pass_context=True)
async def nuke(ctx, city):
    #declaring chromedriver
    chromedriver = webdriver.Chrome(executable_path="C:\\Users\\PC\\Documents\\chromedriver.exe")

    chromedriver.get("https://nuclearsecrecy.com/nukemap/")

    #variables and stuff
    city2 = '//*[@id="jumptocity"]'
    go = '//*[@id="city_input"]/button'
    detonate = '//*[@id="detonate"]'
    settings = '//*[@id="permalink"]/a'
    select = '//*[@id="preset"]'
    boi = '//*[@id="preset"]/option[9]'


    #interesting part
    #writting the city name
    chromedriver.find_element_by_xpath(city2).send_keys(str(city))
    chromedriver.find_element_by_xpath(city2).send_keys(Keys.ENTER)

    #clicking buttons
    ActionChains(chromedriver).click(chromedriver.find_element_by_xpath(go)).perform()
    chromedriver.find_element_by_xpath(select).click()
    chromedriver.find_element_by_xpath(boi).click()
    ActionChains(chromedriver).click(chromedriver.find_element_by_xpath(detonate)).perform()
    ActionChains(chromedriver).click(chromedriver.find_element_by_xpath(settings)).perform()

    #send the final link and quit
    await ctx.send(chromedriver.current_url)
    chromedriver.quit()

#don't ask me why I made this
@client.command(pass_context=True)
async def winnie_post(ctx):
    #declaring chromedriver
    chromedriver = webdriver.Chrome(executable_path="C:\\Users\\PC\\Documents\\chromedriver.exe")

    chromedriver.get("http://www.ageofcivilizationsgame.com/profile/24549-winnie-the-paramoun-leader/content/?type=forums_topic&change_section=1")
    
    test = '//*[@id="ipsTabs_ips_uid_3007_4_ips_uid_3007_5_panel"]/div/div/div/ol/li[1]/div/div[1]/div/h2/span[2]/a'

    #the main stuff
    as_ = chromedriver.find_elements_by_xpath("//a[@href]")

    urls = []

    for a in as_:
        #trying to find links to posts, not replies
        if not str(a.get_attribute("href")).find("http://www.ageofcivilizationsgame.com/topic/"):
            print(a.get_attribute("href"))
            urls.append(a.get_attribute("href"))
        else:
            pass
    
    #send the final link and quit
    await ctx.send(str(choice(urls)))
    chromedriver.quit()

#don't work well but still there
@client.command(pass_context=True)
async def board(ctx):
    #check if is really doing
    print("doing! ")
    #this list will have all the messages from user
    a = []
    #for each message in the channel until it reach 10k messages listed
    #the message will be appended to the "a" list
    msgs = await ctx.channel.history(limit=10000).flatten()
    for msg in msgs:
        #check if the author of the found message is actually the target
        if msg.author == member:
            a.append(msg)
    #send how many messages the target member has
    await ctx.channel.send(member + ", you have the following number of messages:\n**"+str(len(a))+"**")

#don't ask me why lol
@client.command(pass_context=True)
async def dripcar(ctx):
    #list of the dripcars
    a = []
    #for dripcar image in the drip cars folder
    for file in os.listdir("drip-cars-database\\"):
        print(file)
        a.append(file)
    #choses one of the images in the drip car folder
    await ctx.channel.send(file=discord.File("drip-cars-database\\"+str(choice(a))))


#run it

client.run(token)
