# Adventure 3: buildHouse.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program builds a single house, with a doorway, windows,
# a roof, and a carpet.

# What does the code below do?
import mcpi.minecraft as minecraft
import mcpi.block as block

# What does the code below do?
mc = minecraft.Minecraft.create()

# What does the code below do?
SIZE = 20

# What does the code below do?
pos = mc.player.getTilePos()

# What does the code below do?
x = pos.x + 2
y = pos.y
z = pos.z

# What does the code below do?
midx = x+SIZE/2
midy = y+SIZE/2

# What does the code below do?
mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)

# What does the code below do?
mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.AIR.id)

# What does the code below do?
mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

# What does the code below do?
mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)

# What does the code below do?
mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

# What does the code below do?   
mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)

# What does the code below do?
mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)

# END

