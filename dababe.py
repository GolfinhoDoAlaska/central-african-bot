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
token = "do you really think I would post the token?"

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

ts = []
author1 = ""
generals = {
    "Napoleon": "hussar", 
    "Zhukov":"small-tank", 
    "Frederick-II":"pikeman", 
    "Mehmed-II":"siege", 
    "Bruchmuller":"light-cannon",
    "Erwin-Rommel":"granadier",
    "Ivan-IV":"cossack",
    "Gustavus":"musket"
}
tatics = ["defensive", "agressive", "infantary-charge"]
comps = {
    "hussar":{"damage":10, "hp":25, "cav":True}, 
    "siege":{"damage":30, "hp":5, "cav":False}, 
    "pikeman":{"damage":10, "hp":25, "cav":False}, 
    "musket":{"damage":15, "hp":25, "cav":False}, 
    "cossack":{"damage":15, "hp":35, "cav":True}, 
    "chariot":{"damage":10, "hp":25, "cav":True}, 
    "light-cannon":{"damage":25, "hp":10, "cav":False}, 
    "small-tank":{"damage":7, "hp":40, "cav":False}, 
    "granadier":{"damage":16, "hp":15, "cav":False}, 
    "swordsman":{"damage":12, "hp":30, "cav":False}
}
inbattle = False

counters = {
    "pikeman":[
        "siege",
        "musket",
        "cossack",
    ],
    "siege":[
        "hussar",
        "heavy-cavalary",
        "cossack",
        "chariot",
        "light-cannon"
    ],
    "hussar":[
        "pikeman",
        "cossack",
        "heavy-cavalary",
        "small-tank"
    ],
    "musket":[
        "heavy-cavalary",
        "hussar",
        "cossack",
        "granadier"
    ],
    "cossack":[
        "musket",
        "small-tank",
        "siege",
        "chariot"
    ],
    "chariot":[
        "pikeman",
        "musket",
        "small-tank"
    ],
    "granadier":[
        "light-cannon",
        "siege",
        "swordsman"
    ],
    "small-tank":[
        "light-cannon",
        "granadier",
        "swordsman"
    ],
    "swordsman":[
        "musket",
        "cossack",
        "light-cavalary",
        "pikeman",
        "chariot"
    ],
    "light-cannon":[
        "swordsman",
        "cossack",
        "light-cavalary"
    ]
}





p1gen = ""
p1tat = ""

p1morale = 100
p2morale = 100



@client.command(pass_context=True)
async def battle1(ctx, comp1, comp2, comp3, comp4, general):
    global author1
    global inbattle
    global p1gen
    global p1tat
    troops = [comp1, comp2, comp3, comp4]
    gen = [general]
    a = True


    if set(comps).intersection(troops):
        inbattle = True
        await ctx.channel.send("your now in battle! ")
        print("in battle")
        for troop in troops:
            ts.append(troop)
    else:
        await ctx.channel.send("there's something wrong on your army!")
        inbattle = False
    if set(gen).intersection(generals):
        p1gen = gen[0]
        pass
    else:
        await ctx.channel.send("invalid general")

    
    author1 = ctx.message.author

def remove_random(p, arg1, arg2, lst, add):
    """
    Removes arg1 with probability p from lst, otherwise remove arg2
    p -> float from 0 to 1
    lst -> list
    arg1, arg2 -> elements of lst
    """
    global p1morale
    global p2morale
    try:
        if randint(0,p) > 1:
            print("damaging "+arg1)
            p1morale -= 1
            if arg1["cav"] == True and arg2 == "pikeman":
                arg1["hp"] -= arg2["damage"] + (add * 2)
                arg2["hp"] -= arg1["damage"] / 2
                
                if arg1["hp"] <= 0:
                    print(arg1+" dead")
                    lst.remove(arg1)
                    p1morale -= 5
                if arg2["hp"] <= 0:
                    print(arg2+" dead")
                    lst.remove(arg2)
                    p2morale -= 5
            else:
                arg1["hp"] -= arg2["damage"] + (add)
                arg2["hp"] -= arg1["damage"] / 2
                p1morale -= 1
                if arg1["hp"] <= 0:
                    print(arg1+" dead")
                    lst.remove(arg1)
                    p1morale -= 5
                if arg2["hp"] <= 0:
                    print(arg2+" dead")
                    lst.remove(arg2)
                    p2morale -= 5
        else:
            print("damaging "+arg2)
            p2morale -= 1
            if arg2["cav"] == True and arg2 == "pikeman":
                p2morale -= 1
                arg2["hp"] -= arg1["damage"] + (add * 2)
                arg1["hp"] -= arg2["damage"] / 2
                if arg2["hp"] <= 0:
                    print(arg2+" dead")
                    lst.remove(arg2)
                    p2morale -= 5
                if arg1["hp"] <= 0:
                    print(arg1+" dead")
                    lst.remove(arg1)
                    p1morale -= 5
            else:
                p2morale -= 1
                arg2["hp"] -= arg1["damage"] + (add)
                arg1["hp"] -= arg2["damage"] / 2
                if arg2["hp"] <= 0:
                    print(arg2+" dead")
                    lst.remove(arg2)
                    p2morale -= 5
                if arg1["hp"] <= 0:
                    print(arg1+" dead")
                    lst.remove(arg1)
                    p1morale -= 5
    except:
        pass

def calculatestuff(general, ts, troops):
    for tr in ts:
        for troop in troops:
            for counter in counters:
                for gen in generals:
                    if general == gen:
                        if troop == gen[0]:
                            if troop == counter and tr in counter:
                                remove_random(6, troop, tr, troops, 5)
                            else:
                                remove_random(5, troop, tr, troops, 3)
                        else:
                            if troop == counter and tr in counter:
                                remove_random(6, troop, tr, troops, 5)
                            else:
                                remove_random(5, troop, tr, troops, 3)
                        if tr == gen[0]:
                            if tr == counter and troop in counter:
                                remove_random(6, tr, troop, ts, 5)
                            else:
                                remove_random(5, tr, troop, ts, 3)
                        else:
                            if tr == counter and troop in counter:
                                remove_random(6, tr, troop, ts, 5)
                            else:
                                remove_random(5, tr, troop, ts, 3)



@client.command(pass_context=True)
async def battle2(ctx, comp1, comp2, comp3, comp4, general):
    global p1gen
    global p1tat
    global ts
    global author1
    global inbattle

    gen = [general]

    if inbattle == True:
        troops = [comp1, comp2, comp3, comp4]
        a = True
        if set(comps).intersection(troops):
            print("inbattle")
        else:
            await ctx.channel.send("there's something wrong on your army! ")
        if set(gen).intersection(generals):
            p1gen = gen[0]
            pass
        else:
            await ctx.channel.send("invalid general")

        for troop in troops:
            for comp in comps.keys():
                if troop == comp:
                    troop = comp
        for tr in ts:
            for comp in comps:
                if tr == comp:
                    tr = comp


        calculatestuff(general, ts, troops)
        calculatestuff(p1gen, troops, ts)



        if p1morale > p2morale:
            print(p1morale)
            print(p2morale)
            await ctx.channel.send(">>> congrats, "+str(author1.mention)+", you've won the battle by making the humiliated enemy retreat! \nThe stats of this battle:\ntroops remaining by "+str(author1.mention)+":   "+str(len(ts))+"\ntroops remaining by "+str(ctx.message.author.mention)+":   "+str(len(troops)))
        elif p2morale > p1morale:
            print(p1morale)
            print(p2morale)
            await ctx.channel.send(">>> congrats, "+str(ctx.message.author.mention)+", you've won the battle by making the humiliated enemy retreat! \nThe stats of this battle:\ntroops remaining by "+str(author1.mention)+":   "+str(len(ts))+"\ntroops remaining by "+str(ctx.message.author.mention)+"`:   "+str(len(troops)))
        else:
            print(p1morale)
            print(p2morale)
            await ctx.channel.send(">>> looks like the battle ended up as a tie!")
        inbattle = False
        author1 = ""
        ts = []
    else:
        await ctx.channel.send("there's no battle requests going on, try doing a new one with \\battle1")
                
                


@client.command(pass_context=True)
async def suicide(ctx):
    await ctx.channel.send("https://tenor.com/view/do-it-shia-la-beouf-flame-gif-4445204")

regions = {
    "siberia":{
        "pop":0.1,
        "eco":1
    },
    "turkestan":{
        "pop":3,
        "eco":3
    },
    "north-china":{
        "pop": 7,
        "eco":5
    },
    "south-china":{
        "pop":6,
        "eco":5,
        "b":["north-china","india"]
    },
    "tibet":{
        "pop":3,
        "eco":2.5,
        "b":["north-china", "turkestan"]
    },
    "india":{
        "pop":5,
        "eco":3,
        "b":["tibet", "south-china", "north-china", "indochina"]
    },
    "eastern-europe":{
        "pop":3,
        "eco":4,
        "b":["siberia", "turkestan"]
    },
    "persia":{
        "pop":4,
        "eco":4,
        "b":["turkestan", "india", "caucasus","arabia"]
    },
    "caucasus":{
        "pop":2,
        "eco":4,
        "b":["persia", "eastern-europe"]
    },
    "western-anatolia":{
        "pop":3,
        "eco":4,
        "b":["persia", "caucasus"]
    },
    "balkans":{
        "pop":2,
        "eco":4,
        "b":["eastern-europe", "western-anatolia", "western-europe"]
    },
    "western-europe":{
        "pop":3,
        "eco":4,
        "b":["eastern-europe", "balkans", "scandinavia"]
    },
    "scandinavia":{
        "pop":2,
        "eco":4,
        "b":["eastern-europe", "western-europe"]
    },
    "indochina":{
        "pop":4,
        "eco":5,
        "b":["south-china","india"]
    },
    "arabia":{
        "pop":1.8,
        "eco":3,
        "b":["persia", "western-anatolia"]
    },
    "sahara":{
        "pop":1,
        "eco":2,
        "b":["arabia", "western-europe", "mali", "horn-of-africa"]
    },
    "mali":{
        "pop":3,
        "eco":2,
        "b":["sahara", "horn-of-africa", "kongo"]
    },
    "horn-of-africa":{
        "pop":3,
        "eco":2,
        "b":["sahara", "mali", "kongo"]
    },
    "kongo":{
        "pop":3,
        "eco":2,
        "b":["mali", "horn-of-africa"]
    },
    "southern-africa":{
        "pop":3,
        "eco":2,
        "b":["kongo", "horn-of-africa"]
    },
}

passed_regions = []
funds = 4000


for reg in regions:
    if os.path.isfile("y\\"+reg+".reg"):
        with open("y\\"+reg+".reg", "r") as file:
            passed_regions.append(reg)
            file.close()
    else:
        pass

print(passed_regions)

maxmen = int(open("maxmen\\max.pole", "r").read())

@client.command(pass_context=True)
async def mongolhorde(ctx, region, men:int):
    maxmen = int(open("maxmen\\max.pole", "r").read())
    global passed_regions
    cando = True
    if men > maxmen:
        await ctx.channel.send("your amount of men is more than the maximum")
        cando = False
    if cando == True:
        if set([region]).intersection(regions):
            defense = int(regions[region]["pop"] * 1500)
            print("defense in invade region: "+str(defense))
            if "b" in regions[region]:
                if set(regions[region]["b"]).intersection(passed_regions):
                    await battleforregion(men, defense, region, maxmen, ctx)
                else:
                    await ctx.channel.send("you have to pass from another region to get there!")
            else:
                await battleforregion(men, defense, region, maxmen, ctx)
        else:
            print("a")
    
    if passed_regions == regions.keys():
        await ctx.channel.send("congrats"+ctx.message.author.mention+"! you've conquered all the known world!")
        for file in os.listdir("y"):
            os.remove("y\\"+file)
            passed_regions = []
        with open("maxmen\\max.pole", "a+") as file2:
            file2.write("")


async def battleforregion(men, defense, region, maxmen, ctx):
    global funds
    if int(men) > int(defense - (defense/10)):
        men -= int(defense / 2)
        funds += regions[region]["eco"] * 400
        passed_regions.append(region)
        sequestred = int(defense / 2)
        with open("maxmen\\max.pole", "a+") as file2:
            file2.write(str(int(maxmen + sequestred + int(funds / 3))))
            file2.close()

        await ctx.channel.send(">>> "+ctx.message.author.mention+", you won a invasion of "+region)
        print(passed_regions)
        for reg in passed_regions:
            with open("y\\"+reg+".reg", "a+") as file:
                print("file made")
    else:
        await ctx.channel.send(">>> "+ctx.message.author.mention+", you lost a invasion of "+region)



@client.command(pass_context=True)
async def napoleonic_wiki(ctx):
    print("wiki search")
    nap = wikipedia.search("napoleonic", results=6)
    nap = choice(nap)
    nap = wikipedia.page(nap)
    links = nap.links
    await ctx.channel.send(wikipedia.page(choice(links)).url)

govs = {
    "communism":{"invest":1.5, "military":8, "democratic":False},
    "liberalism":{"invest":3, "military":4, "democratic":True},
    "monarchy":{"invest":2.5, "military":6, "democratic":False},
    "populism":{"invest":2, "military":7, "democratic":False},
    "socialism":{"invest":1.9, "military":6, "democratic":True}
}



@client.command(pass_context=True)
async def nation_create(ctx, name, region, gov):
    if set([gov]).intersection(govs):
        if os.path.isfile("avaliable_regions\\"+region+".reg"):
            with open("nations\\"+name+".nat", "a+") as file:
                file.write(ctx.message.author.name+"\n"+region+"\n"+gov)
                os.mkdir("nations\\"+name)
                shutil.move("avaliable_regions\\"+region+".reg", "nations\\"+name+"\\"+region+".reg")
                await ctx.channel.send(str(ctx.message.author.mention)+" have created a nation called "+name+" in the region of "+region)
        else:
            await ctx.channel.send("this region is being used!")
    else:
        await ctx.channel.send("invalid government!")



    
    
#run it

client.run(token)
