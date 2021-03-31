import pickle

#saving the model in binary
with open("Hiring_model",'wb') as f:
    pickle.dump(reg,f)

#Loading the saved trained model
with open("Hiring_model",'rb') as f:
    md = pickle.load(f)
