
# mxGlass
# Card logging tool (all games played)

# mxGlass
# 04AUG22
# Initial commit.

# mxGlass
# 04AUG22
# Implemented logging (all played cards from any game can be found in logger.txt).

def logger(card):
    with open('logger.txt', 'a') as f:
        f.write(card + "\n")
        # f.write("\n")
    f.close()

