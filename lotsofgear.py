from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Sport, Base, GearItem

engine = create_engine('sqlite:///sportgear.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Gear for Football
sport1 = Sport(name="Football")

session.add(sport1)
session.commit()

gearItem1 = GearItem(name="Helmet", description="A piece of protective"
                     "equipment used mainly in American football and Canadian"
                     "football. It consists of a hard plastic shell with thick"
                     "padding on the inside, a face mask made of one or more"
                     "plastic-coated metal bars, and a chinstrap.",
                     sport=sport1)

session.add(gearItem1)
session.commit()

gearItem2 = GearItem(name="Neck Roll", description="a thick piece of padded"
                     "foam, comprised of vinyl or nylon, which is intended to"
                     "fit around the back of the shoulder pads along the"
                     "jersey's neckline. The equipment is designed to be"
                     "attached to shoulder pads with straps.",
                     sport=sport1)

session.add(gearItem2)
session.commit()

gearItem3 = GearItem(name="Football Cleats", description="Cleats or studs are"
                     "protrusions on the sole of a shoe, or on an external"
                     "attachment to a shoe, that provide additional"
                     "traction on a soft or slippery surface. They can be"
                     "conical or blade-like in shape, and made of plastic,"
                     "rubber or metal.",
                     sport=sport1)

session.add(gearItem3)
session.commit()

gearItem4 = GearItem(name="Mouth Guard", description="A mouth guard is a soft"
                     "plastic or laminate device used in sports to prevent"
                     "oral injuries to the teeth, mouth, cheeks, tongue and"
                     "jaw.",
                     sport=sport1)

session.add(gearItem4)
session.commit()

gearItem5 = GearItem(name="Thigh, Hip and Knee Pads", description="Hip and"
                     "tailbone pads are made of plastic and protect the hips,"
                     "pelvis, and coccyx or tailbone. The pads are inserted"
                     "into the pockets of a girdle worn under the football"
                     "pants. Thigh and knee pads are made of plastics and"
                     "inserted into pockets constructed inside the football"
                     "pants.",
                     sport=sport1)

session.add(gearItem5)
session.commit()

gearItem6 = GearItem(name="Shoulder Pads", description="Shoulder pads consist"
                     "of a hard plastic shell with foam padding underneath."
                     "The pads fit over the shoulders and the chest and rib"
                     "area, and are secured with various snaps and buckles.",
                     sport=sport1)

session.add(gearItem6)
session.commit()

# Gear for Basketball
sport2 = Sport(name="Basketball")

session.add(sport2)
session.commit()

gearItem1 = GearItem(name="Basketball Sneakers", description="Players should"
                     "wear comfortable, properly fitting basketball sneakers."
                     "There are so many styles, varieties and names to choose"
                     "from today that it is often difficult to know which"
                     "sneakers to buy. First, I recommend that you select"
                     "sneakers that are within your price range. There's no"
                     "need to break the bank over a pair of sneakers! The"
                     "sneakers should have proper ankle support to prevent"
                     "rolled or sprained ankles. The sneakers should also have"
                     "good traction to allow the player to make quick stops"
                     "and starts on the basketball court.",
                     sport=sport2)

session.add(gearItem1)
session.commit()

gearItem2 = GearItem(name="Athletic Socks", description="Players should wear"
                     "two pairs of athletic socks. This will help prevent"
                     "their feet and toes from blistering and will also"
                     "provide additional comfort for their feet.",
                     sport=sport2)

session.add(gearItem2)
session.commit()

gearItem3 = GearItem(name="Athletic Shorts", description="Players should wear"
                     "a loose-fitting, comfortable pair of athletic shorts."
                     "This will allow them to move quickly and freely without"
                     "any restrictions on their legs or lower body.",
                     sport=sport2)

session.add(gearItem3)
session.commit()

gearItem4 = GearItem(name="Athletic Jersey", description="Players should wear"
                     "a loose-fitting, comfortable shirt, jersey or tank-top."
                     "Again, this will allow them to move quickly and freely"
                     "without having their arms or upper body restricted.",
                     sport=sport2)

session.add(gearItem4)
session.commit()

gearItem5 = GearItem(name="Mouth Piece", description="Players should wear a"
                     "mouth piece to protect their teeth, tongue, cheeks and"
                     "lips from injuries caused by accidental contact. More"
                     "and more players are wearing mouth pieces due to the"
                     "amount of contact during a game or practice, especially"
                     "down around the basket.",
                     sport=sport2)

session.add(gearItem5)
session.commit()

gearItem6 = GearItem(name="Basketball", description="This falls more in the"
                     "basketball equipment section rather than the basketball"
                     "player equipment section. But I think it is still"
                     "something every player should have in order to practice"
                     "the game and improve their skills. The main key when"
                     "selecting a basketball is to choose one that is"
                     "appropriate for the player's age and level of"
                     "competition. Check out our page on Basketball Dimensions"
                     "for more information on choosing the right ball!",
                     sport=sport2)

session.add(gearItem6)
session.commit()

# Gear for Baseball
sport3 = Sport(name="Baseball")

session.add(sport3)
session.commit()

gearItem1 = GearItem(name="Baseball Ceats", description="Cleats began to be"
                     "used in the United States in the 1860s when metal spikes"
                     "were first used on baseball shoes. A baseball shoe, as"
                     "defined by the Dickson Baseball Dictionary (3rd Ed),"
                     "is a special type of shoe designed and worn by baseball"
                     "players that features cleats for traction and a full set"
                     "of laces for support.",
                     sport=sport3)

session.add(gearItem1)
session.commit()

gearItem2 = GearItem(name="Glove", description="A baseball glove or mitt is a"
                     "large leather glove worn by baseball players of the"
                     "defending team, which assists players in catching and"
                     "fielding balls hit by a batter or thrown by a teammate.",
                     sport=sport3)

session.add(gearItem2)
session.commit()

gearItem3 = GearItem(name="Bat", description="A baseball bat is a smooth"
                     "wooden or metal club used in the sport of baseball to"
                     "hit the ball after it is thrown by the pitcher.",
                     sport=sport3)

session.add(gearItem3)
session.commit()

gearItem4 = GearItem(name="Baseball", description="the ball used in this game,"
                     "being a sphere approximately 3 inches (7 cm) in diameter"
                     "with a twine-covered center of cork covered by stitched"
                     "horsehide.",
                     sport=sport3)

session.add(gearItem4)
session.commit()

gearItem5 = GearItem(name="Uniform", description="A baseball uniform is a type"
                     "of uniform worn by baseball players. Most baseball"
                     "uniforms have the names and uniform numbers of players"
                     "who wear them, usually on the backs of the uniforms to"
                     "distinguish players from each other.",
                     sport=sport3)

session.add(gearItem5)
session.commit()

# Gear for Golf
sport4 = Sport(name="Golf")

session.add(sport4)
session.commit()

gearItem1 = GearItem(name="Clubs", description="A golf club is a club used to"
                     "hit a golf ball in a game of golf. Each club is composed"
                     "of a shaft with a grip and a club head. Woods are mainly"
                     "used for long-distance fairway or tee shots; irons, the"
                     "most versatile class, are used for a variety of shots;"
                     "hybrids that combine design elements of woods and irons"
                     "are becoming increasingly popular; putters are used"
                     "mainly on the green to roll the ball into the hole. A"
                     "standard set consists of 14 golf clubs, and while there"
                     "are traditional combinations sold at retail as matched"
                     "sets, players are free to use any combination of 14 or"
                     "fewer legal clubs.",
                     sport=sport4)

session.add(gearItem1)
session.commit()

gearItem2 = GearItem(name="Shoes", description="an oxford shoe of waterproof"
                     "leather with sole spikes or hobnails that is worn"
                     "especially for golfing.",
                     sport=sport4)

session.add(gearItem2)
session.commit()

gearItem3 = GearItem(name="Balls", description="a small, white ball with a"
                     "tough cover and a resilient core of rubber, used in"
                     "playing golf.",
                     sport=sport4)

session.add(gearItem3)
session.commit()

gearItem4 = GearItem(name="Tees", description="A golf tee is typically a thin,"
                     "wood or plastic peg, two or three inches in height, atop"
                     "which a golf ball sits in a stable and stationary"
                     "position. The tee is pushed down into the turf on the"
                     "teeing ground, leaving a portion of the tee above"
                     "ground, and the ball placed atop the golf tee prior to"
                     "playing the stroke.",
                     sport=sport4)

session.add(gearItem4)
session.commit()

gearItem5 = GearItem(name="Divot Tool", description="A small, pronged, plastic"
                     "or metal utensil for repairing ball marks on the putting"
                     "green. Keep in mind that ball marks on the putting green"
                     "are always in the shape of a narrow V. The grass has"
                     "been scrunched into a folded mass at the opening of the"
                     "V.",
                     sport=sport4)

session.add(gearItem5)
session.commit()

gearItem6 = GearItem(name="Range Finder", description="Golf GPS rangefinders"
                     "are used in the sport of golf to aid the player in"
                     "accurately determining the distance to certain fixed"
                     "points on a golf course, such as the green or various"
                     "hazards.",
                     sport=sport4)

session.add(gearItem6)
session.commit()


print "added sport gear!"
