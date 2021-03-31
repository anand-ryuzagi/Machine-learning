#Saving the Trained Model and loading again

from joblib import dump, load

#dumping the trained model
dump(reg, 'homeprice_model.joblib')

#lOading the trained model
model = load('homeprice_model.joblib')

#using that trained model and predicting the answers
model.predict([[12,10,10]])
