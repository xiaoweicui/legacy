from gamelib import*
#game object
game = Game (1000,600, "Legacy",60)
desert= Image("Desert.gif",game)
desert.resizeTo(1000,600)
game.setBackground(desert)

forest = Image("forest.jpg",game)
temple = Image("temple.gif",game)
temple.resizeTo(1000,600)
waterfall = Image("waterfall.gif",game)

garen = Image("Garen.jpg",game)
garen.moveTo(400,500)
garen.resizeBy(-30)

golem = Image("golem.png",game)
golem.moveTo(800,480)
golem.resizeBy(-45)

boss = Image("boss.png",game)

reaper = Image("reaper.png",game)
reaper.resizeBy(-35)
reaper.moveTo(800,480)

fireball = Image("fireball.jpg",game,use_alpha=False)
fireball.resizeBy(-30)
fireball.setSpeed(4,60)
fireball.visible = False
 
ice = Image("ice.png",game)
ice.resizeBy(-50)
ice.setSpeed(4,60)
ice.visible = False

sword = Image("sword.png",game,use_alpha=False)
sword.resizeBy(-60)
sword.visible = False

end = Image("end.jpg",game)
end.resizeTo(1000,600)

start = Image("Start.png",game)
start.resizeBy(-80)

title = Image("Title.png",game)
title.resizeBy(30)

win = Image("win.jpg",game)
win.resizeTo(1000,600)

level2= Image("L2.png",game,use_alpha=False)
level2.resizeBy(-40)
level2.moveTo(800,250)

#Title screen
game.over = False
while not game.over:
    game.processInput()
    waterfall.resizeTo(game.width,game.height)
    waterfall.draw()
    start.moveTo(500,500)
    start.draw()
    title.moveTo(500,200)
    title.draw
    if start.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(40)

#Level 1
game.over = False

while not game.over: 
    game.processInput()
    desert.draw()
    garen.draw()
    reaper.draw()
    fireball.move()
    sword.move()
    level2.draw()
    level2.visible = False
    b = sword.angleTo(reaper)

    if reaper.health<=1:
        sword.rotateTo(b)
        
    if not fireball.visible:
        fireball.moveTo( reaper.x, reaper.y )
        a = reaper.angleTo(garen)
        fireball.rotateTo(a)
        fireball.visible = True

    if fireball.collidedWith(garen):
        garen.health -= 10
        fireball.visible = False
        
    if fireball.isOffScreen("left"):
        fireball.visible = False
    
    if sword.collidedWith(fireball):
        sword.visible = False
        fireball.visible = False

    if sword.isOffScreen():
        sword.visible = False
    
    if keys.Pressed[K_UP]:
        garen.y-=2
    if keys.Pressed[K_RIGHT]:
        garen.x+=4
    if keys.Pressed[K_LEFT]:
        garen.x-=2
    if keys.Pressed[K_DOWN]:
        garen.y+=4
    if keys.Pressed[K_SPACE]:
        sword.moveTo(garen.x, garen.y)
        sword.setSpeed(24,0)
        sword.visible = True
        sword.rotateTo(b)
        
    if sword.collidedWith(reaper):
        reaper.health -= 10
        sword.visible = False

    game.drawText("Health: " +str(reaper.health),reaper.x-20,reaper.y+80)
    game.drawText("Health: " +str(garen.health),garen.x+10,garen.y-60)

    if garen.health < 1:
        end.draw()
        game.drawText("press [SPACE] to exit",600,480)
       

   
     
    
    if reaper.health<=1:
        game.drawText("The reaper has been killed",600,100)
        reaper.visible = False
        fireball.visible = False
        game.over = False
        level2.visible = True

    if level2.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(50)

    
#Level 2
game.over = False
while not game.over:
    game.processInput()
    temple.draw()
    sword.draw()
    golem.draw()
    garen.draw()
    ice.move()
    sword.move()
    c = ice.angleTo(garen)
    d = garen.angleTo(golem)
    
    if not ice.visible:
        ice.moveTo( golem.x, golem.y )
        c = golem.angleTo(garen)
        ice.rotateTo(c)
        ice.visible = True

    if ice.collidedWith(garen):
        garen.health -= 20
        ice.visible = False
        
    if ice.isOffScreen("left"):
        ice.visible = False
    
    if golem.health<=1:
        game.drawText("The golem has been killed",600,200)
        golem.visible = False
        ice.visible = False
        win.draw()
     
    if golem.health<=1:
        game.drawText("The golem has been killed",600,200)
        golem.visible = False
        ice.visible = False
        win.draw()

    if sword.collidedWith(golem):
        golem.health -= 10
        sword.visible = False

    if sword.collidedWith(ice):
        ice.visible = False

    if keys.Pressed[K_UP]:
        garen.y-=2
    if keys.Pressed[K_RIGHT]:
        garen.x+=4
    if keys.Pressed[K_LEFT]:
        garen.x-=2
    if keys.Pressed[K_DOWN]:
        garen.y+=4
    if keys.Pressed[K_SPACE]:
        sword.moveTo(garen.x, garen.y)
        sword.setSpeed(24,0)
        sword.visible = True
        sword.rotateTo(d)
        
    if garen.health < 1:
        end.draw()
        
    game.drawText("Health: " +str(garen.health),garen.x+10,garen.y-60)
    game.drawText("Health: " +str(golem.health),golem.x-20,golem.y+80)
    
    game.update(60)
#level 3
game.over = False
while not game.over:
    game.processInput()

game.quit()



