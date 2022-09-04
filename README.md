#Product-Identification-Assistant

The application allows users to capture a photo of any electronic product (could also include cars and electric appliances), and the app will return with the identified product’s brand, make and model, along with a comprehensive collection of tables filled with the application’s features sorted based on different categories – eg, hardware aspects etc. it would also include a component that compares that product’s previous prices across different websites and plots the data on a graph. it would also include a reviews component that shows the top most reviews for that product. Considering price, reviews and popularity of that platform of purchase, it concludes the best website to buy it from.

##Features:

- Easily figure out which product and what it is made of just by pointing your phone at it

- Dissimilar to google lens because lens just returns a bunch of search results while our
application’s goal is to give the information right away. raw facts.

- Eliminates the need of a salesperson at any store. One can youse their own phone to scan a
product and get a comprehensive outlook on it

- Shows you raw data, review and links to where to buy it from. Apart from that, also considers
multiple factors and compiles a graph that predicts already-bought user’s best choices.

##Logic:

- To make sure every device gets identified, a small and discreet code can be beamed out of
every device such that the application can pick that signal, verify that code with an existing
DB, and return the properties of that signature which are the results the user gets to see.

- Once post verification and pre service, the model will update the properties of that product to
the latest standard and then delivers the entire set.

##Limitations:

- Most products don’t have a signal that emits a code unique to the app

- Implementing the code signal would mean to write different programs for every category or
type of product in the market

- Another way of approaching this, in-order to eliminate the above two points, would mean to
directly compare the taken image to an already existing dataset. But here probability plays a huge role, and getting the right details for the right product Is crucial.
