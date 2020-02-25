from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Data,DataSet #Import the classes from the other file

engine = create_engine('sqlite:////Users/isbader/Desktop/projects/nlp_arabic_tweets_processor/data_distribution_sys/aby_2.0/aby.db') #create the engine

Base.metadata.bind = engine #Bind the base class to the database engine
DBSession = sessionmaker(bind=engine) #Create a session 
session = DBSession() #change the name of the session 

# shm9999 = Data(name = 'shm', id = 12345)  #add an instanse of table data
# session.add(shm9999) # Add the data
# session.commit() # Commit the data

# session.query(Data).all() #query all of the data in the data table

# shm_first_data = Dataset(id = 43210 , tweet = 'this is a tweet' , time = 'This is the time' , label = 'positive' , data_id = shm9999) #Added the data and linked it using the forign key
# session.add(shm_first_data)
# session.commit()

first_result = session.query(Data).first()
print(first_result.name)
