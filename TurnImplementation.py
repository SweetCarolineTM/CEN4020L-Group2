#this is Pseudocode for what the turn implementation could potentially look like
#this will take two players (defined as class PlayerAttribute), and will
# utilize all necessary functions to complete a turn

#from PlayerAttribute import PlayerAttributes

#this is the turn function where each turn, both players will choose a weapon, move, draw terrain, 
# attack, and potentially use an item (if implemented in the future), each turn the terrain will be updated in drawTerrain,
# and the terrain. All of those functions still need to be created
def turn(player1: PlayerAttributes, player2: PlayerAttributes):
    chooseWeapon(player1, player2)
    move(player1, player2)
    drawTerrain(player1, player2)
    #useItem(player1, player2)
    attack(player1, player2)

    #update the terrain based on the players attack (if the attack removed some terrain for ex.)
    updateTerrain()
    #calculate if a player got hit by an attack
    playerDamageCalc()
