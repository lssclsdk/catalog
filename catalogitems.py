from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Games, Base, Items, User

engine = create_engine('sqlite:///gameItem.db')
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
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
Games1 = Games(user_id=1, name="Soccer")

session.add(Games1)
session.commit()

Items2 = Items(user_id=1, name="Soccer cleats", description="Soccer cleats. Soccer cleats, or what the English call \"boots,\" are like baseball or softball cleats but the cleats are short and made of rubber (metal cleats are not allowed).",
                      game_id=Games1.ids)

session.add(Items2)
session.commit()


Items1 = Items(user_id=1, name="Shin Guards", description="Soccer is definitely a contact sport. Shin guards help reduce the chance of injury to the shin (tibia), the third-most likely area of the body to be injured playing soccer, according to a recent study.",
                      game_id=Games1.ids)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce"
                     , game_id=Games1.ids)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Water bottle", description="Experts advise your child to drink fluids, preferably sports drinks, before, during and after practices and games, even in the cold weather, to avoid dehydration, or worse yet, heat illness. Your child should have his or her own personalized water bottle and needs to be reminded to drink 5 to 9 ounces (10 to 18 1/2 ounce \"gulps\") every 20 minutes during activity, depending on weight (Teenagers should drink more. Younger children should be given water bottles with marks on the sides showing how much they should drink each time or told how many \"gulps\" to drink."
                     , game_id=Games1.ids)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Socks and shirts", description="You'll need to buy long socks to cover your child's shin guards. Check with the coach to see what color to buy."
							, game_id=Games1.ids)

session.add(Items4)
session.commit()

'''Items5 = Items(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", Games=Games1)

session.add(Items5)
session.commit()

Items6 = Items(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", Games=Games1)

session.add(Items6)
session.commit()

Items7 = Items(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese", price="$3.49", course="Entree", Games=Games1)

session.add(Items7)
session.commit()

Items8 = Items(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="$5.99", course="Entree", Games=Games1)

session.add(Items8)
session.commit()


# Menu for Super Stir Fry
Games2 = Games(user_id=1, name="Super Stir Fry")

session.add(Games2)
session.commit()


Items1 = Items(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", course="Entree", Games=Games2)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", Games=Games2)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", course="Entree", Games=Games2)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", Games=Games2)

session.add(Items4)
session.commit()

Items5 = Items(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", Games=Games2)

session.add(Items5)
session.commit()

Items6 = Items(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", course="Entree", Games=Games2)

session.add(Items6)
session.commit()


# Menu for Panda Garden
Games1 = Games(user_id=1, name="Panda Garden")

session.add(Games1)
session.commit()


Items1 = Items(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", course="Entree", Games=Games1)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", course="Appetizer", Games=Games1)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                     price="$9.95", course="Entree", Games=Games1)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", course="Entree", Games=Games1)

session.add(Items4)
session.commit()

Items2 = Items(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", Games=Games1)

session.add(Items2)
session.commit()


# Menu for Thyme for that
Games1 = Games(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(Games1)
session.commit()


Items1 = Items(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", course="Dessert", Games=Games1)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", course="Entree", Games=Games1)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price="$4.50", course="Dessert", Games=Games1)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", course="Appetizer", Games=Games1)

session.add(Items4)
session.commit()

Items5 = Items(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", course="Entree", Games=Games1)

session.add(Items5)
session.commit()

Items2 = Items(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", course="Entree", Games=Games1)

session.add(Items2)
session.commit()


# Menu for Tony's Bistro
Games1 = Games(user_id=1, name="Tony\'s Bistro ")

session.add(Games1)
session.commit()


Items1 = Items(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", course="Entree", Games=Games1)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", course="Entree", Games=Games1)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", course="Entree", Games=Games1)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", Games=Games1)

session.add(Items4)
session.commit()

Items5 = Items(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", course="Entree", Games=Games1)

session.add(Items5)
session.commit()


# Menu for Andala's
Games1 = Games(user_id=1, name="Andala\'s")

session.add(Games1)
session.commit()


Items1 = Items(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", course="Entree", Games=Games1)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", course="Entree", Games=Games1)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", course="Appetizer", Games=Games1)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", Games=Games1)

session.add(Items4)
session.commit()

Items2 = Items(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", course="Entree", Games=Games1)

session.add(Items2)
session.commit()


# Menu for Auntie Ann's
Games1 = Games(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(Games1)
session.commit()

Items9 = Items(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99", course="Entree", Games=Games1)

session.add(Items9)
session.commit()


Items1 = Items(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", course="Dessert", Games=Games1)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", course="Entree", Games=Games1)

session.add(Items2)
session.commit()

Items3 = Items(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50", course="Appetizer", Games=Games1)

session.add(Items3)
session.commit()

Items4 = Items(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", course="Entree", Games=Games1)

session.add(Items4)
session.commit()

Items2 = Items(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", Games=Games1)

session.add(Items2)
session.commit()

Items10 = Items(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", course="Dessert", Games=Games1)

session.add(Items10)
session.commit()


# Menu for Cocina Y Amor
Games1 = Games(user_id=1, name="Cocina Y Amor ")

session.add(Games1)
session.commit()


Items1 = Items(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", course="Entree", Games=Games1)

session.add(Items1)
session.commit()

Items2 = Items(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", course="Entree", Games=Games1)

session.add(Items2)
session.commit()


Games1 = Games(user_id=1, name="State Bird Provisions")
session.add(Games1)
session.commit()

Items1 = Items(user_id=1, name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", course="Appetizer", Games=Games1)

session.add(Items1)
session.commit()

Items1 = Items(user_id=1, name="Guanciale Chawanmushi",
                     description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$6.95", course="Dessert", Games=Games1)

session.add(Items1)
session.commit()


Items1 = Items(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", price="$4.25", course="Dessert", Games=Games1)

session.add(Items1)
session.commit()'''


print "added menu items!"