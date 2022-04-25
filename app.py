from flask import Flask, render_template, request
import sqlite3 as sql
import pandas as pd
from tkinter import messagebox


app = Flask(__name__)
host = 'http://127.0.0.1:5000/'

conn = sql.connect('database.db')
cursor = conn.cursor()
ecursor = conn.cursor()
#Users Table
conn.execute('''CREATE TABLE IF NOT EXISTS Users (
                            email text PRIMARY KEY, 
                            password TEXT);''')
data = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Users.csv')
df = pd.DataFrame(data)
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO Users (email, password) 
                    VALUES (?,?);
                    ''',
                   (row.email,
                    row.password)
                   )
cursor = cursor.execute('''SELECT * FROM Users;''')
conn.commit()
resultUsers = cursor.fetchall()
for x in resultUsers:
  print(x)




#Buyers Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Buyers (
                            email text PRIMARY KEY, 
                            first_name text, 
                            last_name text, 
                            gender text, 
                            age INTEGER, 
                            home_address_id INTEGER, 
                            billing_address_id INTEGER,
                            FOREIGN KEY(billing_address_id) REFERENCES Address(address_ID) 
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
                            FOREIGN KEY(home_address_id) REFERENCES Address(address_ID) 
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE
                            FOREIGN KEY(email) REFERENCES Users(email) 
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE);''')
datab = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Buyers.csv')
dfb = pd.DataFrame(datab)
for row in dfb.itertuples():
    cursor.execute('''
                    INSERT INTO Buyers (email,first_name, last_name, gender, age, home_address_id, billing_address_id) 
                    VALUES (?,?,?,?,?,?,?);
                    ''',
                   (row.email,
                    row.first_name,
                    row.last_name,
                    row.gender,
                    row.age,
                    row.home_address_id,
                    row.billing_address_id)
                   )
cursor = cursor.execute('''SELECT * FROM Buyers;''')
conn.commit()
resultBuyers = cursor.fetchall()
for x in resultBuyers:
   print(x)



#Credit_Cards Table
cursor.execute('''CREATE TABLE Credit_Cards( 
                            credit_card_num text PRIMARY KEY , 
                            card_code INTEGER, 
                            expire_month INTEGER, 
                            expire_year INTEGER, 
                            card_type TEXT, 
                            Owner_email text,
                            FOREIGN KEY(Owner_email) REFERENCES Buyers(email) 
                            ON DELETE CASCADE 
                            ON UPDATE CASCADE);''')
datac = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Credit_Cards.csv')
dfc = pd.DataFrame(datac)
for row in dfc.itertuples():
    cursor.execute('''
                    INSERT INTO Credit_Cards ( credit_card_num, card_code, expire_month, expire_year, card_type, Owner_email)
                    VALUES (?,?,?,?,?,?);
                    ''',
                   (row.credit_card_num,
                    row.card_code,
                    row.expire_month,
                    row.expire_year,
                    row.card_type,
                    row.Owner_email)
                   )
cursor = cursor.execute('''SELECT * FROM Credit_Cards;''')
conn.commit()
resultCc = cursor.fetchall()
#for x in resultCc:
 #   print(x)



#Address Table
cursor.execute(''' CREATE TABLE Address(
                    address_ID text PRIMARY KEY,
                    zipcode INTEGER,
                    street_num INTEGER,
                    street_name text);''')
datad = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Address.csv')
dfd = pd.DataFrame(datad)
for row in dfd.itertuples():
    cursor.execute('''
                    INSERT INTO Address (address_ID, zipcode, street_num, street_name)
                    VALUES (?,?,?,?);
                    ''',
                   (row.address_id,
                    row.zipcode,
                    row.street_num,
                    row.street_name)
                   )
cursor = cursor.execute('''SELECT * FROM Address;''')
conn.commit()
resultAddy = cursor.fetchall()
#for x in resultAddy:
#   print(x)



#Zipcode_Info Table
cursor.execute('''CREATE TABLE Zipcode_Info(
                    zipcode INTEGER PRIMARY KEY,
                    city text NOT NULL,
                    state_id INTEGER NOT NULL, 
                    population INTEGER, 
                    density REAL,
                    county_name text,
                    timezone text); ''')
datae = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Zipcode_Info.csv')
dfe = pd.DataFrame(datae)
for row in dfe.itertuples():
    cursor.execute('''
                    INSERT INTO Zipcode_Info (zipcode ,city , state_id, population, density,county_name, timezone)
                    VALUES (?,?,?,?,?,?,?);
                    ''',
                   (row.zipcode,
                    row.city,
                    row.state_id,
                    row.population,
                    row.density,
                    row.county_name,
                    row.timezone)
                   )
cursor = cursor.execute('''SELECT * FROM Zipcode_Info;''')
conn.commit()
resultzip = cursor.fetchall()
#for x in resultzip:
 #   print(x)



#Sellers Table
cursor.execute('''CREATE TABLE Sellers (
                    email text PRIMARY KEY,
                    routing_number INTEGER,  --might not be integer
                    account_number INTEGER,
                    balance INTEGER,
                    FOREIGN KEY(email) REFERENCES Users(email) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE);''')
dataf = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Sellers.csv')
dff = pd.DataFrame(dataf)
for row in dff.itertuples():
    cursor.execute('''
                    INSERT INTO Sellers ( email, routing_number, account_number,balance )
                    VALUES (?,?,?,?);
                    ''',
                   (row.email,
                    row.routing_number,
                    row.account_number,
                    row.balance)
                   )
cursor = cursor.execute('''SELECT * FROM Sellers;''')
conn.commit()
resultsell = cursor.fetchall()
#for x in resultsell:
  #  print(x)



#Local_Vendors Table
cursor.execute('''CREATE TABLE Local_Vendors(
                    Email text PRIMARY KEY ,
                    Business_Name text,
                    Business_Address_ID INTEGER, 
                    Customer_Service_Number INTEGER,
                    FOREIGN KEY(Email) REFERENCES Sellers(email) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE);''')
datag = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Local_Vendors.csv')
dfg = pd.DataFrame(datag)
for row in dfg.itertuples():
    cursor.execute('''
                    INSERT INTO Local_Vendors ( Email, Business_Name, Business_Address_ID, Customer_Service_Number)
                    VALUES (?,?,?,?);
                    ''',
                   (row.Email,
                    row.Business_Name,
                    row.Business_Address_ID,
                    row.Customer_Service_Number)
                   )
cursor = cursor.execute('''SELECT * FROM Local_Vendors;''')
conn.commit()
resultlv = cursor.fetchall()
#for x in resultlv:
#   print(x)



#Categories Table
cursor.execute('''CREATE TABLE Categories(
                    parent_category text ,
                    category_name text PRIMARY KEY);''')
datah = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Categories.csv')
dfh = pd.DataFrame(datah)
for row in dfh.itertuples():
    cursor.execute('''
                    INSERT INTO Categories (parent_category, category_name)
                    VALUES (?,?);
                    ''',
                   (row.parent_category,
                    row.category_name)
                   )
cursor = cursor.execute('''SELECT * FROM Categories;''')
conn.commit()
resultcat = cursor.fetchall()
for x in resultcat:
    print(x)




#Products_Listings Table
cursor.execute('''CREATE TABLE Product_Listings(
                    Seller_Email text   ,
                    Listing_ID INTEGER  , 
                    Category text,
                    Title text,
                    Product_Name text,
                    Product_Description text,
                    Price REAL,
                    Quantity INTEGER,
                    Constraint PK_Product_Listings PRIMARY KEY (Seller_Email,Listing_ID),
                    FOREIGN KEY(Category) REFERENCES Categories(category_name) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE);''')
datai = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Product_Listing.csv')
dfi = pd.DataFrame(datai)
for row in dfi.itertuples():
    cursor.execute('''
                    INSERT INTO Product_Listings ( Seller_Email, Listing_ID, Category, Title, Product_Name, Product_Description, Price, Quantity)
                    VALUES (?,?,?,?,?,?,?,?);
                    ''',
                   (row.Seller_Email,
                    row.Listing_ID,
                    row.Category,
                    row.Title,
                    row.Product_Name,
                    row.Product_Description,
                    row.Price,
                    row.Quantity)
                   )
cursor = cursor.execute('''SELECT * FROM Product_Listings;''')
conn.commit()
resultpL = cursor.fetchall()
for x in resultpL:
   print(x)




# Orders Table
cursor.execute('''CREATE TABLE Orders(
                    Transaction_ID INTEGER PRIMARY KEY, 
                    Seller_Email text,
                    Listing_ID INTEGER,
                    Buyer_Email text,
                    Date text,
                    Quantity INTEGER,
                    Payment text);''')
dataj = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Orders.csv')
dfj = pd.DataFrame(dataj)
for row in dfj.itertuples():
    cursor.execute('''
                    INSERT INTO Orders (Transaction_ID, Seller_Email, Listing_ID, Buyer_Email, Date, Quantity, Payment)
                    VALUES (?,?,?,?,?,?,?);
                    ''',
                   (row.Transaction_ID,
                    row.Seller_Email,
                    row.Listing_ID,
                    row.Buyer_Email,
                    row.Date,
                    row.Quantity,
                    row.Payment)
                   )
cursor = cursor.execute('''SELECT * FROM Orders;''')
conn.commit()
resultO = cursor.fetchall()
#for x in resultO:
 #   print(x)


#Reviews Table
cursor.execute('''CREATE TABLE Reviews(
                    Buyer_Email text,
                    Seller_Email text ,
                    Listing_ID INTEGER,
                    Review_Desc text,
                    Constraint PK_Reviews PRIMARY KEY (Buyer_Email,Seller_Email,Listing_ID));''')
datak = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Reviews.csv')
dfk = pd.DataFrame(datak)
for row in dfk.itertuples():
    cursor.execute('''
                    INSERT INTO Reviews (Buyer_Email, Seller_Email, Listing_ID, Review_Desc)
                    VALUES (?,?,?,?);
                    ''',
                   (row.Buyer_Email,
                    row.Seller_Email,
                    row.Listing_ID,
                    row.Review_Desc)
                   )
cursor = cursor.execute('''SELECT * FROM Reviews;''')
conn.commit()
resultRev = cursor.fetchall()
#for x in resultRev:
 #   print(x)



#Rating Table
cursor.execute('''CREATE TABLE Rating(
                    Buyer_Email text,
                    Seller_Email text ,
                    Date text ,
                    Rating INTEGER,
                    Rating_Desc text,
                    Constraint PK_Rating PRIMARY KEY (Buyer_Email,Seller_Email,Date));''')
datal = pd.read_csv(r'C:\Users\i7\Desktop\CMPSC431W\Phase2\NittanyMarketDataset-Final\Ratings.csv')
dfl = pd.DataFrame(datal)
for row in dfl.itertuples():
    cursor.execute('''
                    INSERT INTO Rating ( Buyer_Email, Seller_Email, Date, Rating, Rating_Desc)
                    VALUES (?,?,?,?,?);
                    ''',
                   (row.Buyer_Email,
                    row.Seller_Email,
                    row.Date,
                    row.Rating,
                    row.Rating_Desc)
                   )
cursor = cursor.execute('''SELECT * FROM Rating;''')
conn.commit()
resultRat = cursor.fetchall()
#for x in resultRat:
#    print(x)


@app.route('/', methods=['GET'])
def index():
    cat = categorydropdown()
    return render_template('home.html', cat =cat)

@app.route('/home', methods=['GET'])
def home():
    cat = categorydropdown()
    return render_template('home.html', cat =cat)

# login page and sending result to infobuyer page
@app.route('/login', methods=['POST', 'GET'])
def login():  # put application's code here
    error = None
    connection = sql.connect('database.db')
    cat = categorydropdown()
    if request.method == 'POST':
        if (request.form['loginvalue'])== "seller":
            result = valid_login(request.form['email'], request.form['password'])
            if result:
                update_ecursor(request.form['email'])
                cursor =connection.execute('''SELECT b.email,b.first_name, b.last_name, b.gender, b.age, a.zipcode,a.street_num,a.street_name, z.city, z.state_id,SUBSTR(c.credit_card_num,14,17)
                                            FROM Buyers b, Address a, Zipcode_Info z, Credit_Cards c WHERE b.email=? AND a.address_ID = b.home_address_id and a.zipcode = z.zipcode and c.Owner_email = ?''',(request.form['email'],request.form['email']))
                result = cursor.fetchall()
                return render_template('checkingInfoBuyer.html', error=error, result=result, cat=cat)
            else:
                error = 'invalid login credential'
                messagebox.showerror("Error", "E-mail or Password is incorrect. Please check input.")
        else:
            result = valid_login(request.form['email'], request.form['password'])
            if result:
                update_ecursor(request.form['email'])
                cursor =connection.execute('''SELECT b.email,b.first_name, b.last_name, b.gender, b.age, a.zipcode,a.street_num,a.street_name, z.city, z.state_id,SUBSTR(c.credit_card_num,14,17)
                                            FROM Buyers b, Address a, Zipcode_Info z, Credit_Cards c WHERE b.email=? AND a.address_ID = b.home_address_id and a.zipcode = z.zipcode and c.Owner_email = ?''',(request.form['email'],request.form['email']))
                result = cursor.fetchall()
                return render_template('checkingInfoSeller.html', error=error, result=result, cat=cat)
            else:
                error = 'invalid login credential'
                messagebox.showerror("Error", "E-mail or Password is incorrect. Please check input.")
    return render_template('login.html', error=error, cat=cat)



#personal information page, update password
@app.route('/checkingInfoBuyer', methods=['POST', 'GET'])
def checkingInfoBuyer():
    connection = sql.connect('database.db')
    error = None
    cat = categorydropdown()
    if request.method == 'POST':
        if(request.form['oldpassword']==request.form['coldpassword']):
            cursor =connection.execute('UPDATE Users SET password=? WHERE email=?)',(request.form['newpass'],(ecursor)))
            cursor.fetchall()
        else:
            error = 'invalid password credential'
            messagebox.showerror("Error", "Password mismatched. Please check input.")
    return render_template('checkingInfoBuyer.html', error=error,cat=cat )

@app.route('/PublishProductListing', methods=['POST', 'GET'])
def PublishProductListing():
    error = None
    cat = categorydropdown()
    if request.method == 'POST':
        result = valid_listing(request.form['email'],request.form['listing_ID'],request.form['category'], request.form['title'], request.form['prod_name'], request.form['prod_desc'], request.form['price'], request.form['quantity'])
        if result:
            return render_template('PublishProductListing.html', error=error, result=result)
        else:
            error = 'invalid input '
    return render_template('PublishProductListing.html', cat =cat)

def valid_listing(email, listing_id, category, title, prod_name, prod_desc, price, quantity):
    connection = sql.connect('database.db')
    connection.execute('INSERT INTO Product_Listings (Seller_Email, Listing_ID, Category,Title, Product_Name, Product_Description, Price, Quantity) VALUES (?,?,?,?,?,?,?,?);', (email, listing_id,category, title, prod_name, prod_desc, price, quantity))
    connection.commit()
    cursor = connection.execute('SELECT * FROM Product_Listings;')
    return cursor.fetchall()

@app.route('/items/<prod_id>', methods=['POST','GET'])
def items(prod_id):
    error = None
    prod_id = prod_id
    connection = sql.connect('database.db')
    cat = categorydropdown()
    cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name,p.Category, p.Product_Description, p.Price
                                   FROM Product_Listings p WHERE p.Listing_ID=?''',(prod_id,))
    result = cursor.fetchall()
    for x in result:
        print(x)
    return render_template('items.html', error=error, result=result, cat=cat)


@app.route('/Clothing', methods=['POST', 'GET'])
def clothing():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                            FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        for x in result:
            print(x)
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing.html', prod=getallsubCategoryListing("clothing"))

@app.route('/Clothing/Tops/Bodysuits', methods=['POST', 'GET'])
def bodysuits():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                            FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        for x in result:
            print(x)
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Tops/Bodysuits.html', prod=getallsubCategoryListing("bodysuit"))

@app.route('/Clothing/Tops/Long Sleeves', methods=['POST', 'GET'])
def long_sleeve():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                            FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        for x in result:
            print(x)
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Tops/Long Sleeves.html', prod=getallsubCategoryListing("Long Sleeve"))

@app.route('/Clothing/Tops/T-Shirts', methods=['POST', 'GET'])
def tshirts():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                            FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        for x in result:
            print(x)
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Tops/T-Shirts.html', prod=getallsubCategoryListing("t-shirts"))

@app.route('/Clothing/Bottoms/Jeans', methods=['POST', 'GET'])
def jeans():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Bottoms/Jeans.html', prod=getallsubCategoryListing("jeans"))

@app.route('/Clothing/Bottoms/Pants', methods=['POST', 'GET'])
def pants():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Bottoms/Pants.html', prod=getallsubCategoryListing("pants"))

@app.route('/Clothing/Bottoms/Skirts', methods=['POST', 'GET'])
def skirts():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Bottoms/Skirts.html', prod=getallsubCategoryListing("skirts"))

@app.route('/Clothing/Sleepwear/Bath Robes', methods=['POST', 'GET'])
def bathrobes():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Sleepwear/Bath Robes.html', prod=getallsubCategoryListing("bath robes"))

@app.route('/Electrical Supplies', methods=['POST', 'GET'])
def es():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Electrical Supplies.html', prod=getallsubCategoryListing("electrical supplies"))

@app.route('/Electrical Supplies/Cell Phones', methods=['POST', 'GET'])
def cellphones():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Cell Phones.html', prod=getallsubCategoryListing("cell phones"))

@app.route('/Electrical Supplies/TV & Home Theater/75-Inch Tvs', methods=['POST', 'GET'])
def sevenfive():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/TV & Home Theater/75-Inch Tvs.html', prod=getallsubCategoryListing("75-Inch Tvs"))

@app.route('/Electrical Supplies/TV & Home Theater/65-Inch Tvs', methods=['POST', 'GET'])
def sixfive():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/TV & Home Theater/65-Inch Tvs.html', prod=getallsubCategoryListing("65-Inch Tvs"))

@app.route('/Electrical Supplies/TV & Home Theater/55-Inch Tvs', methods=['POST', 'GET'])
def fivefive():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/TV & Home Theater/55-Inch Tvs.html', prod=getallsubCategoryListing("55-Inch Tvs"))

@app.route('/Electrical Supplies/Wearable Technology/Apple Watch', methods=['POST', 'GET'])
def applewatch():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Wearable Technology/Apple Watch.html', prod=getallsubCategoryListing("apple watch"))

@app.route('/Electrical Supplies/Wearable Technology/Headphones', methods=['POST', 'GET'])
def headphones():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Wearable Technology/Headphones.html', prod=getallsubCategoryListing("headphones"))

@app.route('/Electrical Supplies/Wearable Technology/Wireless Headphones', methods=['POST', 'GET'])
def wheadphones():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Clothing/Wearable Technology/Wireless Headphones.html', prod=getallsubCategoryListing("Wireless headphones"))


@app.route('/Beauty Products', methods=['POST', 'GET'])
def bp():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                            FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Beauty Products.html', prod=getallsubCategoryListing("beauty products"))

@app.route('/Beauty Products/Makeup/Face', methods=['POST', 'GET'])
def face():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Beauty Products/Makeup/Face.html', prod=getallsubCategoryListing("face"))

@app.route('/Beauty Products/Makeup/Lip', methods=['POST', 'GET'])
def lip():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Beauty Products/Makeup/Lip.html', prod=getallsubCategoryListing("lip"))

@app.route('/Beauty Products/Makeup/Brushes & Applicators', methods=['POST', 'GET'])
def brushes():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Beauty Products/Makeup/Brushes & Applicators.html', prod=getallsubCategoryListing("brushes & applicators"))

@app.route('/Kitchen & Appliances', methods=['POST', 'GET'])
def ka():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                            FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances.html', prod=getallsubCategoryListing("kitchen & appliances"))

@app.route('/Kitchen & Appliances/Kitchen & Cooking Accessories/Cooking Accessories', methods=['POST', 'GET'])
def cookingacc():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen & Cooking Accessories/Cooking Accessories.html', prod=getallsubCategoryListing("Cooking Accessories"))

@app.route('/Kitchen & Appliances/Kitchen & Cooking Accessories/Kitchen Utensils', methods=['POST', 'GET'])
def kitchuten():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen & Cooking Accessories/Kitchen Utensils.html', prod=getallsubCategoryListing("Kitchen Utensils"))

@app.route('/Kitchen & Appliances/Kitchen & Cooking Accessories/Mixing & Measuring Tools', methods=['POST', 'GET'])
def mnmT():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen & Cooking Accessories/Mixing & Measuring Tools.html', prod=getallsubCategoryListing("Mixing & Measuring Tools"))

@app.route('/Kitchen & Appliances/Kitchen Cabinets/Base Cabinets', methods=['POST', 'GET'])
def base():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen Cabinets/Base Cabinets.html', prod=getallsubCategoryListing("Base Cabinets"))

@app.route('/Kitchen & Appliances/Kitchen Cabinets/High Cabinets', methods=['POST', 'GET'])
def high():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen Cabinets/High Cabinets.html', prod=getallsubCategoryListing("High Cabinets"))

@app.route('/Kitchen & Appliances/Kitchen Cabinets/Wall Cabinets', methods=['POST', 'GET'])
def wall():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen Cabinets/Wall Cabinets.html', prod=getallsubCategoryListing("Wall Cabinets"))

@app.route('/Kitchen & Appliances/Kitchen Faucets & Sinks/Kitchen Faucets', methods=['POST', 'GET'])
def faucet():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen Faucets & Sinks/Kitchen Faucets.html', prod=getallsubCategoryListing("Kitchen Faucets"))

@app.route('/Kitchen & Appliances/Kitchen Faucets & Sinks/Kitchen Sinks', methods=['POST', 'GET'])
def sink():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Kitchen & Appliances/Kitchen Faucets & Sinks/Kitchen Sinks.html', prod=getallsubCategoryListing("Kitchen Sinks"))


@app.route('/Toys & Video Games', methods=['POST', 'GET'])
def tvg():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Toys & Video Games.html', prod=getallsubCategoryListing("toys & video games"))

@app.route('/Toys & Video Games/Toys', methods=['POST', 'GET'])
def toys():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Toys & Video Games/Toys.html', prod=getallsubCategoryListing("Toys"))

@app.route('/Toys & Video Games/Video Games', methods=['POST', 'GET'])
def videog():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Toys & Video Games/Video Games.html', prod=getallsubCategoryListing("Video Games"))

@app.route('/Toys & Video Games/Outdoor Play', methods=['POST', 'GET'])
def oplay():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Toys & Video Games/Outdoor Play.html', prod=getallsubCategoryListing("Outdoor Play"))


@app.route('/Pharmacy, Health & Wellness', methods=['POST', 'GET'])
def phw():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness.html', prod=getallsubCategoryListing("pharmacy, health & wellness"))

@app.route('/Pharmacy, Health & Wellness/Health Care/Cough, Cold & Flu', methods=['POST', 'GET'])
def ccf():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness/Health Care/Cough, Cold & Flu.html', prod=getallsubCategoryListing("cough, cold & flu"))

@app.route('/Pharmacy, Health & Wellness/Health Care/Eye Care', methods=['POST', 'GET'])
def eye():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness/Health Care/Eye Care.html', prod=getallsubCategoryListing("eye care"))

@app.route('/Pharmacy, Health & Wellness/Health Care/Pain Relievers', methods=['POST', 'GET'])
def pain():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness/Health Care/Pain Relievers.html', prod=getallsubCategoryListing("pain relievers"))

@app.route('/Pharmacy, Health & Wellness/Wellness/Sleep Support', methods=['POST', 'GET'])
def sleep():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness/Health Care/Sleep Support.html', prod=getallsubCategoryListing("sleep support"))

@app.route('/Pharmacy, Health & Wellness/Wellness/Performance Nutrition', methods=['POST', 'GET'])
def peformnutri():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness/Health Care/Performance Nutrition.html', prod=getallsubCategoryListing("performance nutrition"))

@app.route('/Pharmacy, Health & Wellness/Wellness/Weight Loss', methods=['POST', 'GET'])
def weightloss():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pharmacy, Health & Wellness/Health Care/Weight Loss.html', prod=getallsubCategoryListing("weight loss"))



@app.route('/Pets', methods=['POST', 'GET'])
def p():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets.html', prod=getallsubCategoryListing("pets"))

@app.route('/Pets/Cat/Cat Dry Food', methods=['POST', 'GET'])
def catdry():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets/Cat/Cat Dry Food.html', prod=getallsubCategoryListing("cat dry food"))

@app.route('/Pets/Cat/Cat Wet Food', methods=['POST', 'GET'])
def catwet():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets/Cat/Cat Wet Food.html', prod=getallsubCategoryListing("cat wet food"))

@app.route('/Pets/Cat/Climbing Trees', methods=['POST', 'GET'])
def climb():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets/Cat/Climbing Trees.html', prod=getallsubCategoryListing("cat climbing trees"))

@app.route('/Pets/Dog/Dog Dry Food', methods=['POST', 'GET'])
def dogdry():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets/Dog /Dog Dry Food.html', prod=getallsubCategoryListing("dog dry food"))


@app.route('/Pets/Dog/Dog Wet Food', methods=['POST', 'GET'])
def dogwet():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets/Dog /Dog Wet Food.html', prod=getallsubCategoryListing("dog wet food"))

@app.route('/Pets/Dog/Dog Beds', methods=['POST', 'GET'])
def dogbed():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Pets/Dog /Dog Beds.html', prod=getallsubCategoryListing("dog beds"))



@app.route('/Sports & Outdoors', methods=['POST', 'GET'])
def so():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors.html', prod=getallsubCategoryListing("sports & outdoors"))

@app.route('/Sports & Outdoors/Sports/Baseball', methods=['POST', 'GET'])
def baseball():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Sports/Baseball.html', prod=getallsubCategoryListing("baseball"))

@app.route('/Sports & Outdoors/Sports/Basketball', methods=['POST', 'GET'])
def basketball():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Sports/Basketball.html', prod=getallsubCategoryListing("basketball"))

@app.route('/Sports & Outdoors/Sports/Tennis', methods=['POST', 'GET'])
def tennis():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Sports/Tennis.html', prod=getallsubCategoryListing("tennis"))

@app.route('/Sports & Outdoors/Bikes/Electric', methods=['POST', 'GET'])
def elec_b():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Bikes/Electric.html', prod=getallsubCategoryListing("electric"))

@app.route('/Sports & Outdoors/Bikes/Mountain', methods=['POST', 'GET'])
def mount_b():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Bikes/Mountain.html', prod=getallsubCategoryListing("mountain"))

@app.route('/Sports & Outdoors/Exercise & Fitness/Boxing & Mma', methods=['POST', 'GET'])
def bmma():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Exercise & Fitness/Boxing & Mma.html', prod=getallsubCategoryListing("boxing & mma"))

@app.route('/Sports & Outdoors/Exercise & Fitness/Exercise Machines', methods=['POST', 'GET'])
def exmach():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Exercise & Fitness/Exercise Machines.html', prod=getallsubCategoryListing("exercise machines"))

@app.route('/Sports & Outdoors/Exercise & Fitness/Yoga', methods=['POST', 'GET'])
def yoga():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Sports & Outdoors/Exercise & Fitness/Yoga.html', prod=getallsubCategoryListing("yoga"))


@app.route('/Patio & Garden', methods=['POST', 'GET'])
def pg():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden.html', prod=getallsubCategoryListing("patio & garden"))

@app.route('/Patio & Garden/Outdoor Decor/Outdoor Cushions', methods=['POST', 'GET'])
def outcush():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Outdoor Decor/Outdoor Cushions.html', prod=getallsubCategoryListing("outdoor cushions"))

@app.route('/Patio & Garden/Outdoor Decor/Outdoor Lighting', methods=['POST', 'GET'])
def outlight():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Outdoor Decor/Outdoor Lighting.html', prod=getallsubCategoryListing("outdoor lighting"))

@app.route('/Patio & Garden/Patio Furniture/Patio Conversation Sets', methods=['POST', 'GET'])
def patconsets():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Patio Furniture/Patio Conversation Sets.html', prod=getallsubCategoryListing("pati conversation sets"))

@app.route('/Patio & Garden/Patio Furniture/Patio Dining Sets', methods=['POST', 'GET'])
def patdinsets():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Patio Furniture/Patio Dining Sets.html', prod=getallsubCategoryListing("patio dining sets"))

@app.route('/Patio & Garden/Patio Furniture/Porch Swings', methods=['POST', 'GET'])
def porchswings():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Patio Furniture/Porch Swings.html', prod=getallsubCategoryListing("porch swings"))

@app.route('/Patio & Garden/Indoor & Live Plants/Annuals', methods=['POST', 'GET'])
def ann():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Indoor & Live Plants/Annuals.html', prod=getallsubCategoryListing("annuals"))

@app.route('/Patio & Garden/Indoor & Live Plants/Plant Gifts', methods=['POST', 'GET'])
def plantgifts():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Indoor & Live Plants/Plant Gifts.html', prod=getallsubCategoryListing("plant gifts"))

@app.route('/Patio & Garden/Indoor & Live Plants/Indoor Plants', methods=['POST', 'GET'])
def inplant():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                        FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Patio & Garden/Indoor & Live Plants/Indoor Plants.html', prod=getallsubCategoryListing("indoor plants"))


@app.route('/Grocery', methods=['POST', 'GET'])
def gr():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery.html', prod=getallsubCategoryListing("grocery"))

@app.route('/Grocery/Bakery & Bread/Rolls & Buns', methods=['POST', 'GET'])
def rnb():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Bakery & Bread/Rolls & Buns.html', prod=getallsubCategoryListing("rolls & buns"))

@app.route('/Grocery/Bakery & Bread/Cookies & Brownies', methods=['POST', 'GET'])
def cnb():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Bakery & Bread/Cookies & Brownies.html', prod=getallsubCategoryListing("cookies & brownies"))

@app.route('/Grocery/Bakery & Bread/Pies', methods=['POST', 'GET'])
def pies():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Bakery & Bread/Pies.html', prod=getallsubCategoryListing("pies"))

@app.route('/Grocery/Meat & Seafood/Seafood', methods=['POST', 'GET'])
def seafood():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Meat & Seafood/Seafood.html', prod=getallsubCategoryListing("seafood"))

@app.route('/Grocery/Meat & Seafood/Pork', methods=['POST', 'GET'])
def pork():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Meat & Seafood/Pork.html', prod=getallsubCategoryListing("pork"))

@app.route('/Grocery/Meat & Seafood/Beef & Lamb', methods=['POST', 'GET'])
def beeflamb():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Meat & Seafood/Beef & Lamb.html', prod=getallsubCategoryListing("beef & lamb"))

@app.route('/Grocery/Fresh Produce', methods=['POST', 'GET'])
def freshprod():
    error = None
    cat = categorydropdown()
    connection = sql.connect('database.db')
    if request.method == 'POST':
        cursor =connection.execute('''SELECT p.Seller_Email, p.Listing_ID, p.Product_Name, p.Product_Description, p.Price
                                                    FROM Products_Listings p WHERE p.Listing_ID=?''',(request.form['prod_id'],))
        result = cursor.fetchall()
        return render_template('items.html', error=error, result=result, cat=cat)
    return render_template('Grocery/Fresh Produce.html', prod=getallsubCategoryListing("fresh produce"))


def getallsubCategoryListing(y):

    connection = sql.connect('database.db')
    new =connection.execute('SELECT c.category_name From Categories c WHERE c.parent_category = ?', (y,))
    category = new.fetchall()
    for x in category:
        print(x)
    print(y)
    cursor =connection.execute('SELECT p.Listing_ID, p.Title, p.Product_Name FROM Product_Listings p WHERE lower(p.Category) = ?', (y,))
    prod = cursor.fetchall()
    return prod



def getCategory(x_category):
    error = None
    connection = sql.connect('database.db')
    cursor =connection.execute('SELECT * FROM Categories WHERE parent_category = ?', (x_category,))
    cat_name =  cursor.fetchall()
    return cat_name

def getsubCat(y_category):
    error = None
    connection = sql.connect('database.db')
    cursor =connection.execute('SELECT * FROM Categories WHERE parent_category = ?', (y_category,))
    cat_yname =  cursor.fetchall()
    return cat_yname


def categorydropdown():
    error = None
    connection = sql.connect('database.db')
    cursor =connection.execute('SELECT * FROM Categories WHERE parent_category = ?', ("Root",))
    cat =  cursor.fetchall()
    return cat

#cursor to email??? i guess
def update_ecursor(email):
    connection = sql.connect('database.db')
    ecursor = connection.execute('SELECT email FROM Buyers WHERE email=?',(email,))
    return ecursor

#check if login credential exist
def valid_login(email, password):
    connection = sql.connect('database.db')
    cursor =connection.execute('SELECT * FROM Users WHERE EXISTS(SELECT * FROM Users WHERE email=? AND password=?)',(email,password))
    return cursor.fetchall()

def valid_name(email,listing_id,category,title, prod_name, prod_Desc, price, quantity):
    connection = sql.connect('database.db')
    connection.execute('INSERT INTO Product_Listings (Seller_Email, Listing_ID,Category, Title, Product_Name, Product_Description, Price, Quantity) VALUES (?,?,?,?,?,?,?,?);', (email,listing_id,category,title, prod_name, prod_Desc, price, quantity))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()

if __name__ == "__main__":
    app.run()





